from collective.volto.blocksfield.field import BlocksField
from collective.volto.blocksfield.interfaces import IBlocksFieldEnabled
from plone.dexterity.utils import iterSchemata
from zope.interface import alsoProvides
from zope.schema import getFields


def markObject(obj, event):
    """
    Mark object with a marker interface
    """
    found = False
    for schema in iterSchemata(obj):
        for field in getFields(schema).values():
            if isinstance(field, BlocksField):
                found = True
                break
    if found:
        alsoProvides(obj, IBlocksFieldEnabled)
