#!/usr/bin/python

from datetime import datetime as tme

from .journals import journal, article
from bs4 import BeautifulSoup as bs
import lxml
import re

class arXiv(journal):

    # In accordance with the ArXiv API
    def __init__(self):
        super(arXiv, self).__init__()

        self.name = u"ArXiv.org"
        self.base_url = u"http://export.arxiv.org/api/query?"

    def _bldquery(self, ti=None, au=None, ABS=None, co=None,
                jr=None, cat=None, rn=None, ID=None, All=None):
        srch_str = "search_query="

        srchDict = {'ti':ti,'au':au,'abs':ABS,'co':co,'jr':jr,'cat':cat,'rn':rn,'id':ID,'all':All}

        for i in srchDict:
            if bool(srchDict[i]):
                if '(' in srchDict[i] or ')' in srchDict[i]:
                    srchDict[i].replace('(', '%28')
                    srchDict[i].replace(')', '%29')
                if '\"' in srchDict[i]:
                    srchDict[i].replace('\"', '%22')
                if ' ' in srchDict[i]:
                    srchDict[i].replace(' ', '+')
                srch_str += i+":"+srchDict[i]+"&"

        if srch_str[-1] == "&":
            srch_str = srch_str[0:len(srch_str)-1]

        self.search_url = self.base_url+srch_str


    def _clean(self, article, tag):
        article.title = tag.find(re.compile('title')).string
        article.updated = tme.strptime(tag.find(re.compile('updated'
                                            )).string, "%Y-%m-%dT%H:%M:%SZ")
        article.published = tme.strptime(tag.find(re.compile('published'
                                            )).string, "%Y-%m-%dT%H:%M:%SZ")
        article.abstract = tag.find(re.compile('summary')).string
        article.id = tag.find(re.compile('id')).string
        article.link = tag.find(title=re.compile('pdf'))['href']
        for tag in tag.find_all(re.compile("author")):
            article.authors.append(tag.find(re.compile("name")).string)
        try:
            article.topics = re.split('\.', tag.find(re.compile('category'))['term'])
        except TypeError:
            article.topic = [None]
            pass


    def _search(self):
        html = bs(self._getmain(), 'lxml')
        for tag in html.find_all(re.compile("entry")):
            curArt = article()
            self.articles.append(curArt)
            self._clean(self.articles[-1], tag)

    def find(self, ti=None, au=None, ABS=None, co=None, jr=None, cat=None, rn=None, ID=None, All=None):
        self._bldquery(ti,au,ABS,co,jr,cat,rn,ID,All)
        self._search()

if __name__ == "__main__":
    M = arXiv()
    M.find(All="electrons")
    print (M.articles)


