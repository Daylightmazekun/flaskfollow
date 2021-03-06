# Fix for older setuptools
import re
import os

try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup, find_packages

def fpath(name):
    return os.path.join(os.path.dirname(__file__), name)


def read(fname):
    return open(fpath(fname)).read()

def desc():
    return read("README.md")


def grep(attrname):
    pattern = r"{0}\W*=\W*'([^']+)'".format(attrname)
    strval, = refindall(pattern, file_text)
    return strval

setup(
    name = "flask_learnjanpanese",
    version = grep('__version__'),
    # url='https://github.com....'
    licence = 'MIT',
    author = grep('__author__'),
    author_email = grep('__email__'),
    # description = 'xxxxxxxx'
    long_description = desc(),
    packages = find_packages(),
    include_package_data = True,
    zip_safe = False,
    platforms = 'any',
    install_requires = ['Flask>=0.12', 'click', 'flask_wtf']

)

 


