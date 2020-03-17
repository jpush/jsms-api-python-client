#!/usr/bin/env python
# coding=utf-8

from setuptools import setup
import jsms

with open('README.md',encoding='utf-8') as f:
    readme = f.read()

setup(
    name = 'jsms',
    version = jsms.__version__,
    keywords = 'jiguang jsms python-sdk',
    description = "JSMS\'s officially supported Python client library",
    long_description = readme,
    author = 'jpush',
    author_email = 'support@jpush.cn',
    url = 'https://github.com/jpush/jsms-api-python-client',
    license = 'MIT',
    py_modules = [ 'jsms' ],
    install_requires = [ 'requests' ],
    include_package_data = True,
    zip_safe = False
)
