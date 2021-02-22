#!/usr/bin/env python

from setuptools import setup, find_packages

# The version is updated automatically with bumpversion
# Do not update manually
__version = '4.0.0'

long_description = 'This device server is part of the ALBA Vacuum suite and ' \
                   'requires VacuumController and Fandango. It provides ' \
                   'communication with TPG300, TPG261 and MaxiGauge'



classifiers = [
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',
    'Topic :: Scientific/Engineering',
    'Topic :: Software Development :: Libraries',
    'License :: OSI Approved :: GNU Library or Lesser General Public License (LGPL)',
    'Programming Language :: Python :: 2.7',
]

entry_points = {
    'console_scripts': [
        'PfeifferGaugeController = PfeifferGaugeController.PfeifferGaugeController:main',
        ]
}

setup(
    name='PfeifferGaugeController',
    version=__version,
    include_package_data=True,
    packages=find_packages(),
    entry_points=entry_points,
    author='Sergi Rubio',
    author_email='srubio@cells.es',
    maintainer='srubio',
    maintainer_email='srubio@cells.es',
    url='https://git.cells.es/controls/PfeifferGaugeController',
    keywords='APP',
    license='LGPL',
    description='PfeifferGaugeController Tango Device Server',
    long_description=long_description,
    requires=['setuptools (>=1.1)'],
    install_requires=['pytango', 'fandango'],
    classifiers=classifiers
)
