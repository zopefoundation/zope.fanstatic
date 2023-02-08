##############################################################################
#
# Copyright (c) 2011 Zope Foundation and Contributors.
# All Rights Reserved.
#
# This software is subject to the provisions of the Zope Public License,
# Version 2.1 (ZPL).  A copy of the ZPL should accompany this distribution.
# THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL EXPRESS OR IMPLIED
# WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND FITNESS
# FOR A PARTICULAR PURPOSE.
#
##############################################################################
import doctest
import unittest

import fanstatic
from zope.component import getGlobalSiteManager
from zope.interface import Interface
from zope.publisher.interfaces.browser import IBrowserRequest

import zope.fanstatic.tests
from zope.fanstatic.testing import ZopeFanstaticBrowserLayer
from zope.fanstatic.tests.view import foo
from zope.fanstatic.zcml import create_factory


class TestLayer(ZopeFanstaticBrowserLayer):

    def testSetUp(self):
        super(TestLayer, self).testSetUp()
        # Because it is difficult to dynamically register a
        # entry_point in tests, we do the setup by hand:
        registry = fanstatic.get_library_registry()
        registry.add(foo)
        resource_factory = create_factory(foo)
        getGlobalSiteManager().registerAdapter(
            resource_factory, (IBrowserRequest,), Interface, foo.name)

    def testTearDown(self):
        super(TestLayer, self).testTearDown()
        registry = fanstatic.get_library_registry()
        registry.clear()


layer = TestLayer(zope.fanstatic.tests)


class NoInjectorTestLayer(TestLayer):

    def setup_middleware(self, app):
        return app


no_injector_layer = NoInjectorTestLayer(
    zope.fanstatic.tests, allowTearDown=True)


def test_suite():
    readme = doctest.DocFileSuite(
        '../README.txt',
        optionflags=doctest.NORMALIZE_WHITESPACE | doctest.ELLIPSIS)
    readme.layer = layer
    return unittest.TestSuite([readme])
