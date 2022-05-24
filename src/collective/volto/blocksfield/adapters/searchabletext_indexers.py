# -*- coding: utf-8 -*-
from collective.dexteritytextindexer.converters import (
    DefaultDexterityTextIndexFieldConverter,
)
from collective.dexteritytextindexer.interfaces import (
    IDexterityTextIndexFieldConverter,
)
from collective.volto.blocksfield.interfaces import IBlocksField
from plone.dexterity.interfaces import IDexterityContent
from plone.restapi.interfaces import IBlockSearchableText
from z3c.form.interfaces import IWidget
from zope.component import adapter
from zope.component import queryMultiAdapter
from zope.interface import implementer


@implementer(IDexterityTextIndexFieldConverter)
@adapter(IDexterityContent, IBlocksField, IWidget)
class BlocksFieldConverter(DefaultDexterityTextIndexFieldConverter):
    def convert(self):
        value = self.field.get(self.context)
        if not isinstance(value, dict):
            return ""

        blocks = value.get("blocks", {})
        if not blocks:
            return ""

        blocks_text = []
        for block in blocks.values():
            searchableText = block.get("searchableText", "")
            if searchableText:
                blocks_text.append(searchableText)
            block_type = block.get("@type", "")
            adapter = queryMultiAdapter(
                (self.context, self.context.REQUEST),
                IBlockSearchableText,
                name=block_type,
            )

            if adapter is not None:
                text = adapter(block)
                if text:
                    blocks_text.append(text)
        return " ".join(blocks_text)
