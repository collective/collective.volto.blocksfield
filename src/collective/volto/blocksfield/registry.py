from collective.volto.blocksfield.field import BlocksField as BaseBlocksField

try:
    from plone.registry.field import PersistentField
except ImportError:

    class PersistentField(object):
        pass


class BlocksField(PersistentField, BaseBlocksField):
    pass
