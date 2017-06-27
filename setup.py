#!/usr/bin/python
import sys

from setuptools import setup, find_packages

SUP_VER = ['3.5', '3.6']

if sys.version_info < (3, 5):
    version = '.'.join([str(x) for x in sys.version_info[:3]])
    print('Python version ' + ' is not supported. '
          'Supported versions are ' + ','.join(SUP_VER))
    sys.exit(1)

setup(name="arFinder",
      version="0.1.0",
      packages=find_packages(),
      package_dir={'arFinder': 'arFinder'},
      url='https://github.com/jandersen7/arFinder',
      license='MIT License',
      author="John Andersen",
      author_email="johnandersen185@gmail.com",
      description="arFinder is a paper search and save for the arXiv",
      install_requires=["beautifulSoup4", "requests"],
      tests_require=["unittest"],
      keywords=["arxiv", "academic", "papers", "search"]
      )
