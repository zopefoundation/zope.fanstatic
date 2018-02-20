Zope integration for fanstatic
******************************

This package provides Zope integration for fanstatic. This means it's
taking care of three things:

* provide access to the needed resources throughout the request/response cycle.

* provide the base URL for the resources to be rendered.

* clear the needed resources when an exception view is rendered.

This library fulfills these conditions for a Zope Toolkit/Grok setup.
