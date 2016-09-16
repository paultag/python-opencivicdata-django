#!/usr/bin/env python
from setuptools import setup, find_packages

setup(name="person",
      version='0.8.2',
      author="Paul Tagliamonte",
      author_email='paultag@gmail.com',
      license="BSD",
      description="python person library",
      long_description="",
      url="",
      py_modules=['person'],
      packages=[],
      include_package_data=True,
      install_requires=[
          'Django>=1.9',
      ],
      platforms=["any"],
      classifiers=["Development Status :: 4 - Beta",
                   "Intended Audience :: Developers",
                   "License :: OSI Approved :: BSD License",
                   "Natural Language :: English",
                   "Operating System :: OS Independent",
                   "Programming Language :: Python :: 3.4",
                   "Programming Language :: Python :: 3.5",
                   ],
      )
