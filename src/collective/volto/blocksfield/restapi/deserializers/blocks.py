# -*- coding: utf-8 -*-
from plone.dexterity.interfaces import IDexterityContent
from plone.restapi.deserializer.blocks import HTMLBlockDeserializerBase
from plone.restapi.deserializer.blocks import ImageBlockDeserializerBase
from plone.restapi.deserializer.blocks import ResolveUIDDeserializerBase
from plone.restapi.deserializer.blocks import TextBlockDeserializerBase
from plone.restapi.interfaces import IBlockFieldDeserializationTransformer
from zope.component import adapter
from zope.interface import implementer
from zope.publisher.interfaces.browser import IBrowserRequest


@adapter(IDexterityContent, IBrowserRequest)
@implementer(IBlockFieldDeserializationTransformer)
class ResolveUIDDeserializer(ResolveUIDDeserializerBase):
    """ Deserializer for content-types """


@adapter(IDexterityContent, IBrowserRequest)
@implementer(IBlockFieldDeserializationTransformer)
class TextBlockDeserializer(TextBlockDeserializerBase):
    """ Deserializer for content-types """


@adapter(IDexterityContent, IBrowserRequest)
@implementer(IBlockFieldDeserializationTransformer)
class HTMLBlockDeserializer(HTMLBlockDeserializerBase):
    """ Deserializer for content-types """


@adapter(IDexterityContent, IBrowserRequest)
@implementer(IBlockFieldDeserializationTransformer)
class ImageBlockDeserializer(ImageBlockDeserializerBase):
    """ Deserializer for content-types """
