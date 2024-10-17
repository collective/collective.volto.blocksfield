from plone.dexterity.interfaces import IDexterityContent
from plone.restapi.indexers import SlateTextIndexer as SlateTextIndexerBase
from plone.restapi.interfaces import IBlockSearchableText
from zope.component import adapter
from zope.interface import implementer
from zope.publisher.interfaces.browser import IBrowserRequest
from collective.volto.blocksfield.interfaces import IBlocksFieldEnabled
from Acquisition import aq_base
from plone.dexterity.interfaces import IDexterityContent
from plone.indexer.decorator import indexer
from plone.restapi.blocks import visit_blocks
from plone.dexterity.utils import iterSchemata
from zope.schema import getFields
from collective.volto.blocksfield.field import BlocksField


@implementer(IBlockSearchableText)
@adapter(IDexterityContent, IBrowserRequest)
class SlateTextIndexer(SlateTextIndexerBase):
    """Searchable Text indexer for Slate blocks."""

    def __call__(self, block):
        block = block or {}
        # BBB compatibility with slate blocks that used the "plaintext" field
        return block.get("plaintext", "")


@indexer(IBlocksFieldEnabled)
def block_types_indexer(obj):
    """Indexer for all block types included in a content."""
    obj = aq_base(obj)
    block_types = set()
    # first set standard blocks
    for block in visit_blocks(obj, getattr(obj, "blocks", {})):
        block_type = block.get("@type")
        if block_type:
            block_types.add(block_type)

    # then search for block fields
    for schema in iterSchemata(obj):
        for field in getFields(schema).values():
            if not isinstance(field, BlocksField):
                continue
            value = field.get(obj)
            if not value:
                continue
            for block in visit_blocks(obj, value.get("blocks", {})):
                block_type = block.get("@type")
                if block_type:
                    block_types.add(block_type)
    return block_types
