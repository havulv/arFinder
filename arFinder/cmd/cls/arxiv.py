#!/usr/bin/env python3

'''
A class that looks through the arxiv to find journal articles
and other specifcations.

Inherits object properties from journal and article class

'''

from datetime import datetime as dt
from .journals import Journal, Article
from bs4 import BeautifulSoup as bs
import re


class ArXiv(Journal):
    '''
    A class for implementing a search of the arxiv that follows the specification
    set out by the arxiv API.

    Currently supports queries for specifc search_query but does not support
    boolean entries.

    '''

    def __init__(self):
        ''' Inherits journal members '''

        super(ArXiv, self).__init__()

        self.name = u"ArXiv.org"
        self.base_url = u"http://export.arxiv.org/api/query?"

    def _bldquery(self, title=None, author=None, abstract=None,
                  comment=None, journal_reference=None,
                  category=None, report_number=None,
                  id_number=None, all_=None):
        '''
            Builds the query to search the arxiv. The search params
            should be either a False boolean or a list of strings
        '''

        srch_str = "search_query="

        srch_dict = {
            'ti': title, 'au': author, 'abs': abstract, 'co': comment,
            'jr': journal_reference, 'cat': category, 'rn': report_number,
            'id': id_number, 'all': all_}

        for k, v in srch_dict.items():
            if isinstance(v, list):
                v_tmp = []
                for ind in range(len(v)):
                    if " " in v[ind]:
                        temp = v[ind].split(" ")
                    else:
                        temp = [v[ind]]
                    for i in temp:
                        v_tmp.append(i)
                v = v_tmp
                for value in v:
                    value = value.strip()
                    value.replace('(', '%28')
                    value.replace(')', '%29')
                    value.replace('\"', '%22')

        srch_dict = [[k, v] for k, v in filter(
            lambda x: isinstance(x[1], list), srch_dict.items())]
        srch_dict = [[k, v] for k, args in srch_dict for v in args]
        srch_str += "+AND+".join(map(":".join, srch_dict))

        self.search_url = self.base_url + srch_str
        return self.search_url

    def _clean(self, article, tag):
        ''' Clean the return values from the arxiv '''

        article.title = tag.find(re.compile('title')).string

        article.updated = dt.strptime(
            tag.find(re.compile(
                'updated')).string,
            "%Y-%m-%dT%H:%M:%SZ")
        article.published = dt.strptime(
            tag.find(re.compile(
                'published')).string,
            "%Y-%m-%dT%H:%M:%SZ")

        article.abstract = tag.find(re.compile('summary')).string

        article.id = tag.find(re.compile('id')).string.split('/')[-1]

        article.link = tag.find(title=re.compile('pdf'))['href']

        for tag in tag.findall_(re.compile("author")):
            article.authors.append(tag.find(re.compile("name")).string)
        try:
            article.topics = re.split(r'\.', tag.find(re.compile('category'))['term'])
        except TypeError:
            article.topic = [None]
            pass

    def _search(self):
        ''' Do the actual searching of the arxiv '''

        html = bs(self._getmain(), 'html.parser')
        for tag in html.findall_(re.compile("entry")):
            cur_art = Article()
            self.articles.append(cur_art)
            self._clean(self.articles[-1], tag)

    def find(self, title=None, author=None, abstract=None,
             comment=None, journal_reference=None, category=None,
             report_number=None, id_number=None, all_=None):
        '''
            The public method to actually find the articles
        '''

        self._bldquery(title, author, abstract, comment,
                       journal_reference, category,
                       report_number, id_number, all_)
        self._search()


if __name__ == "__main__":
    M = ArXiv()
    M.find(all_="electrons")
    print(M.articles)
