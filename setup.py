#! /usr/bin/env python3.7

from setuptools import setup, find_packages

setup(name="arFinder",
      version="0.1.0",
      packages=find_packages(exclude=['*.tests', '*.tests.*',
                                      'tests.*', 'tests']),
      package_dir={'arFinder': 'arFinder'},
      url='https://github.com/jandersen7/arFinder',
      license='MIT License',
      author="John Andersen",
      author_email="johnandersen185@gmail.com",
      description="arFinder is a paper search and save for the arXiv",
      install_requires=["beautifulSoup4>=4.7.1", "requests>=2.21.0"],
      tests_require=["nose", "parameterized"],
      keywords=["arxiv", "academic", "papers", "search"]
      )
