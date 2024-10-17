# -*- coding: utf-8 -*-
from plone.schema.jsonfield import IJSONField
from zope.interface import Interface


class IBlocksField(IJSONField):
    """A text field that stores a set of blocks."""


class IBlocksFieldEnabled(Interface):
    """Marker interface"""
