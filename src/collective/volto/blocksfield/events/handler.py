from zope.interface import alsoProvides
from collective.volto.blocksfield.field import BlocksField
from plone.dexterity.utils import iterSchemata
from zope.schema import getFields
from collective.volto.blocksfield.interfaces import IBlocksFieldEnabled


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
