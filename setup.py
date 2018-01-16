import os
from setuptools import setup, find_packages


def read(*rnames):
    return open(os.path.join(os.path.dirname(__file__), *rnames)).read()


long_description = (
    read('CHANGES.txt')
    + '\n' +
    'Download\n'
    '********\n'
    )

setup(
    name='zope.fanstatic',
    version='0.13dev',
    description="Fanstatic integration for Zope.",
    long_description=long_description,
    classifiers=['Framework :: Zope3'],
    keywords='',
    author='Zope Foundation and Contributors',
    author_email='zope-dev@zope.org',
    url='http://pypi.python.org/pypi/zope.fanstatic',
    license='ZPL 2.1',
    packages=find_packages('src'),
    namespace_packages=['zope'],
    package_dir={'': 'src'},
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'fanstatic >= 0.11',
        'setuptools',
        'zope.component',
        'zope.errorview [browser]',
        'zope.event',
        'zope.interface',
        'zope.publisher',
        'zope.traversing',
        ],
    extras_require={
        'test': [
            'zope.annotation',
            'zope.app.appsetup',
            'zope.app.publication',
            'zope.app.wsgi[test]',
            'zope.browserpage',
            'zope.container',
            'zope.principalregistry',
            'zope.security',
            'zope.securitypolicy',
            'zope.site'
            ],
    },
)
