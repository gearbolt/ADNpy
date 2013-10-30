#!/usr/bin/env python
#from distutils.core import setup
from setuptools import setup, find_packages
from adnpy import __version__

setup(name="adnpy",
      version=__version__,
      description="App.net API library for python",
      license="MIT",
      author="Alex Kessinger",
      author_email="alex@app.net",
      url="http://github.com/appdotnet/adnpy",
      packages=find_packages(exclude=['tests']),
      install_requires=[
        'python-dateutil==1.5',
        'requests==2.0.1',
      ],
      keywords="app.net api library",
      zip_safe=True)
