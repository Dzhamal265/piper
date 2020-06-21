# -*- coding: utf-8 -*-

# Learn more: https://github.com/kennethreitz/setup.py

from setuptools import setup, find_packages

with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='pyfuncpiper',
    version='0.1.6',
    description='Functional programming helper library',
    author='Dzhamal Abdulbasirov',
    author_email='dzamal26abdulbasirov@gmail.com',
    license=license,
    url='https://github.com/Dzhamal265/piper',
    packages=find_packages(exclude=('tests', 'docs'))
)
