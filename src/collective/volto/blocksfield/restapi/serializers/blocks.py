# -*- coding: utf-8 -*-
from plone.dexterity.interfaces import IDexterityContent
from plone.restapi.interfaces import IBlockFieldSerializationTransformer
from plone.restapi.serializer.blocks import ResolveUIDSerializerBase
from plone.restapi.serializer.blocks import TextBlockSerializerBase
from zope.component import adapter
from zope.interface import implementer
from zope.publisher.interfaces.browser import IBrowserRequest


@implementer(IBlockFieldSerializationTransformer)
@adapter(IDexterityContent, IBrowserRequest)
class ResolveUIDSerializer(ResolveUIDSerializerBase):
    """ Base Serializer registered for all content-types """


@implementer(IBlockFieldSerializationTransformer)
@adapter(IDexterityContent, IBrowserRequest)
class TextBlockSerializer(TextBlockSerializerBase):
    """ TextBlock Serializer for all content-types """
