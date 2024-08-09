from plone.dexterity.interfaces import IDexterityContent
from plone.restapi.indexers import SlateTextIndexer as SlateTextIndexerBase
from plone.restapi.interfaces import IBlockSearchableText
from zope.component import adapter
from zope.interface import implementer
from zope.publisher.interfaces.browser import IBrowserRequest


@implementer(IBlockSearchableText)
@adapter(IDexterityContent, IBrowserRequest)
class SlateTextIndexer(SlateTextIndexerBase):
    """Searchable Text indexer for Slate blocks."""

    def __call__(self, block):
        block = block or {}
        # BBB compatibility with slate blocks that used the "plaintext" field
        return block.get("plaintext", "")
