import os

from setuptools import find_packages
from setuptools import setup


def read(*rnames):
    return open(os.path.join(os.path.dirname(__file__), *rnames)).read()


long_description = (
    read('src/zope/fanstatic/README.txt')
    + '\n' +
    read('CHANGES.txt')
    + '\n' +
    'Download\n'
    '********\n'
)


setup(
    name='zope.fanstatic',
    version='4.0.dev0',
    description="Fanstatic integration for Zope.",
    long_description=long_description,
    keywords='',
    author='Zope Foundation and Contributors',
    author_email='zope-dev@zope.dev',
    url='https://github.com/zopefoundation/zope.fanstatic',
    license='ZPL 2.1',
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Zope Public License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: Implementation',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Framework :: Zope :: 3',
        'Framework :: Zope :: 3',
    ],
    packages=find_packages('src'),
    namespace_packages=['zope'],
    package_dir={'': 'src'},
    include_package_data=True,
    zip_safe=False,
    python_requires='>=3.7',
    install_requires=[
        'fanstatic >= 1.0.0',
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
            'zope.site',
            'zope.testbrowser',
        ],
    },
)
