# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in erpnext_sales/__init__.py
from erpnext_sales import __version__ as version

setup(
	name='erpnext_sales',
	version=version,
	description='Sales application',
	author='shubhangi raut',
	author_email='shubhngirut@gmail.com',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
