# -*- coding: utf-8 -*-
from collective.volto.blocksfield.field import IBlocksField
from plone.restapi.types.adapters import JSONFieldSchemaProvider
from plone.restapi.types.interfaces import IJsonSchemaProvider
from zope.component import adapter
from zope.interface import implementer
from zope.interface import Interface


@adapter(IBlocksField, Interface, Interface)
@implementer(IJsonSchemaProvider)
class BlocksFieldSchemaProvider(JSONFieldSchemaProvider):
    """
    Set custom widget and factory name for Volto
    """

    def get_widget(self):
        return "blocks"

    def get_factory(self):
        return "BlocksField"
