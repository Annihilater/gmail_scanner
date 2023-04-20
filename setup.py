#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date  : 2023/4/18 23:27
# @Author: doi
# @email : me@coo.lol
# @File  : main.py
from setuptools import setup, find_packages

with open("README.md", "r") as f:
    long_description = f.read()

setup(
    name="gmail_scanner",
    version="1.0.4",
    license='MIT',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="coo",
    author_email="me@coo.lol",
    maintainer="coo",
    maintainer_email="me@coo.lol",
    description="gmail scanner",
    url='https://github.com/Annihilater/gmail_scanner',
    packages=find_packages(),
    include_package_data=False,
    platforms=["all"],
    zip_safe=False,

    install_requires=[
        'requests==2.28.2',
        'tqdm==4.65.0',
        'python-dotenv==1.0.0'
    ],
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]

)
