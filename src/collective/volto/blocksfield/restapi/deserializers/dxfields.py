# -*- coding: utf-8 -*-
from collective.volto.blocksfield.interfaces import IBlocksField
from plone.dexterity.interfaces import IDexterityContent
from plone.restapi.deserializer.dxfields import DefaultFieldDeserializer
from plone.restapi.interfaces import IBlockFieldDeserializationTransformer
from plone.restapi.interfaces import IFieldDeserializer
from zope.component import adapter
from zope.component import subscribers
from zope.interface import implementer
from zope.publisher.interfaces.browser import IBrowserRequest


@implementer(IFieldDeserializer)
@adapter(IBlocksField, IDexterityContent, IBrowserRequest)
class BlocksFieldDeserializer(DefaultFieldDeserializer):
    def __call__(self, value):
        value = super(BlocksFieldDeserializer, self).__call__(value)
        blocks = value.get("blocks", {})
        if blocks:
            for id, block_value in blocks.items():
                block_type = block_value.get("@type", "")
                handlers = []
                for h in subscribers(
                    (self.context, self.request),
                    IBlockFieldDeserializationTransformer,
                ):
                    if h.block_type == block_type or h.block_type is None:
                        handlers.append(h)
                for handler in sorted(handlers, key=lambda h: h.order):
                    if not getattr(handler, "disabled", False):
                        block_value = handler(block_value)

                blocks[id] = block_value
        return value
