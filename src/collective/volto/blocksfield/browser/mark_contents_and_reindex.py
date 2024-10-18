from Products.Five import BrowserView
from plone import api
from collective.volto.blocksfield.field import BlocksField
from plone.dexterity.utils import iterSchemata
from zope.schema import getFields
from collective.volto.blocksfield.interfaces import IBlocksFieldEnabled
from Acquisition import aq_base
from zope.interface import alsoProvides
from plone.protect.interfaces import IDisableCSRFProtection

import logging

logger = logging.getLogger(__name__)


class View(BrowserView):

    def __call__(self):
        alsoProvides(self.request, IDisableCSRFProtection)
        self.update_contents()
        api.portal.show_message(message="Contents reindexed")
        return self.request.response.redirect(self.context.portal_url())

    def update_contents(self):
        catalog = api.portal.get_tool(name="portal_catalog")
        brains = catalog()
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
