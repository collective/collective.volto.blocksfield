# -*- coding: utf-8 -*-
from plone.app.contenttypes.testing import PLONE_APP_CONTENTTYPES_FIXTURE
from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PloneSandboxLayer

import collective.volto.blocksfield


class CollectiveVoltoBlocksfieldLayer(PloneSandboxLayer):

    defaultBases = (PLONE_APP_CONTENTTYPES_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load any other ZCML that is required for your tests.
        # The z3c.autoinclude feature is disabled in the Plone fixture base
        # layer.
        import plone.restapi

        self.loadZCML(package=plone.restapi)
        self.loadZCML(package=collective.volto.blocksfield)

    def setUpPloneSite(self, portal):
        applyProfile(portal, "plone.restapi:default")


COLLECTIVE_VOLTO_BLOCKSFIELD_FIXTURE = CollectiveVoltoBlocksfieldLayer()


COLLECTIVE_VOLTO_BLOCKSFIELD_INTEGRATION_TESTING = IntegrationTesting(
    bases=(COLLECTIVE_VOLTO_BLOCKSFIELD_FIXTURE,),
    name="CollectiveVoltoBlocksfieldLayer:IntegrationTesting",
)


COLLECTIVE_VOLTO_BLOCKSFIELD_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(COLLECTIVE_VOLTO_BLOCKSFIELD_FIXTURE,),
    name="CollectiveVoltoBlocksfieldLayer:FunctionalTesting",
)
