#!/usr/bin/env python3

'''
    A class for Journal objects. With the main focus being manipulating
    their abstracts, links, titles, etc.

    Hopefully, this will be extended as a base class to other inheirited
    classes for specific websites (i.e. JsTor, Arxiv, PubMed, etc.) that
    can then hold more specific data about the objects

    For now, this will remain as being general enough to cover most journals	but will specifically be built for Arxiv titles.

'''
from __future__ import print_function
from datetime import datetime as dt
import requests


class Journal(object):
    '''
        The basic structure of journal objects

        Each journal subclass will have it's own method for putting together searchable
        urls that can find the appropriate articles for a given topic. The standard
        method will need to be overwritten for each class.
    '''

    def __init__(self):
        self.articles = []
        self.name = u""
        self.base_url = u""
        self.search_url = u""
        self.topics = []

    def __repr__(self):
        return u"{0}".format(self.name)

    def __str__(self):
        return u"{0} {1}".format(self.name, self.base_URL)

    def _getmain(self):
        req = requests.get(
            self.search_url,
            {'Journal Aggregation':
             'https://github.com/jandersen7/arFinder'})
        req.raise_for_status()
        return req.text

    def _read_topic(self, html):
        return html


class Article(object):
    '''
    The basic structure of article objects -- Journals have articles
    '''

    def __init__(self):
        self.title = u""
        self.updated = dt.today()
        self.published = dt.today()
        self.abstract = u""
        self.id = None
        self.link = u""
        self.authors = []
        self.topics = []

    def __repr__(self):
        return u"{0}".format(self.title)

    def __str__(self):
        return u"{0}".format(self.title)


if __name__ == "__main__":
    Arxiv = Journal()
    Arxiv.search_url = "http://export.arxiv.org/api/query?search_query=all:electron&start=0&max_results=10"
