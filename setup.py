# -*- coding: utf-8 -*-

# Learn more: https://github.com/kennethreitz/setup.py
import codecs

from setuptools import setup, find_packages

with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()


def long_description():
    with codecs.open('README.rst', encoding='utf8') as f:
        return f.read()


setup(
    name='pyfuncpiper',
    version='0.1.9',
    long_description=long_description(),
    author='Dzhamal Abdulbasirov',
    author_email='dzamal26abdulbasirov@gmail.com',
    license=license,
    url='https://github.com/Dzhamal265/piper',
    packages=find_packages(exclude=('tests', 'docs'))
)
