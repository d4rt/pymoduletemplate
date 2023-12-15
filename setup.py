# -*- coding: utf-8 -*-

# Learn more: https://github.com/kennethreitz/setup.py

from setuptools import setup, find_packages


with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='sample',
    version='0.1.0',
    description='Module Template',
    long_description=readme,
    long_description_type='text/markdown',
    author='Duncan Turnbull',
    author_email='duncan@v7labs.com',
    url='https://github.com/d4rt/pymoduletemplate',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)

