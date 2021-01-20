# -*- coding: utf-8 -*-
from collective.volto.blocksfield.interfaces import IBlocksField
from plone.schema.jsonfield import JSONField
from zope.interface import implementer
from zope.schema.interfaces import IFromUnicode

import json

BLOCKS_FIELD_SCHEMA = json.dumps(
    {
        "type": "object",
        "properties": {
            "blocks": {"type": "object", "properties": {}},
            "blocks_layout": {
                "items": {"type": "array", "items": {"type": "string"}}
            },
        },
    }
)


DEFAULT_VALUE = {"blocks": {}, "blocks_layout": {"items": []}}


@implementer(IBlocksField, IFromUnicode)
class BlocksField(JSONField):
    """ """

    def __init__(self, **kw):
        if "schema" not in kw:
            kw["schema"] = BLOCKS_FIELD_SCHEMA
        if "default" not in kw:
            kw["default"] = DEFAULT_VALUE
        super(BlocksField, self).__init__(**kw)
