# -*- coding: utf-8 -*-
from __future__ import with_statement
from setuptools import setup

def get_version():
    return "0"

def get_long_description():
    return "0"

setup(
    name='stylize',
    version=get_version(),
    description="English style checker",
    long_description=get_long_description(),
    keywords='stylize',
    author='Ceasar Bautista',
    author_email='cbautista2010@gmail.com',
    url='https://github.com/Ceasar/stylize',
    license='MIT license',
    py_modules=['stylize'],
    namespace_packages=[],
    include_package_data=True,
    zip_safe=False,
    entry_points={
        'console_scripts': [
            'stylize = stylize:_main',
        ],
    },
    classifiers=[
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
