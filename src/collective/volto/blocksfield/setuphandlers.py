# -*- coding: utf-8 -*-
from Acquisition import aq_base
from collective.volto.blocksfield.field import BlocksField
from collective.volto.blocksfield.interfaces import IBlocksFieldEnabled
from plone import api
from plone.dexterity.utils import iterSchemata
from Products.CMFPlone.interfaces import INonInstallable
from zope.interface import alsoProvides
from zope.interface import implementer
from zope.schema import getFields

import logging


logger = logging.getLogger(__name__)


@implementer(INonInstallable)
class HiddenProfiles(object):
    def getNonInstallableProfiles(self):
        """Hide uninstall profile from site-creation and quickinstaller."""
        return [
            "collective.volto.blocksfield:uninstall",
        ]


def post_install(context):
    """Post install script"""
    # mark contents with blocksfield and reindex them
    catalog = api.portal.get_tool(name="portal_catalog")
    brains = list(catalog.getAllBrains())
    tot = len(brains)
    logger.info(f"Updating {tot} items.")
    reindexed = []
    i = 0
    for brain in brains:
        i += 1
        obj = brain.getObject()
        if i % 100 == 0:
            logger.info(f"Progress: {i}/{tot}")

        found = False
        for schema in iterSchemata(aq_base(obj)):
            for field in getFields(schema).values():
                if isinstance(field, BlocksField):
                    found = True
                    break

        if found:
            alsoProvides(obj, IBlocksFieldEnabled)
            obj.reindexObject(idxs=["block_types", "object_provides"])
            reindexed.append(brain.getURL())

    logger.info(f"Reindexed and marked {len(reindexed)} contents.")
    for x in reindexed:
        logger.info(f"- {x}")


def uninstall(context):
    """Uninstall script"""
    # Do something at the end of the uninstallation of this package.
