#!/usr/bin/python

"""

	A class for Journal objects. With the main focus being manipulating
	their abstracts, links, titles, etc.

	Hopefully, this will be extended as a base class to other inheirited
	classes for specific websites (i.e. JsTor, Arxiv, PubMed, etc.) that
	can then hold more specific data about the objects

	For now, this will remain as being general enough to cover most journals	but will specifically be built for Arxiv titles.

"""
from datetime import datetime as dt


class Article:


	def __init__(self, title = u"Article Title", updated = dt.now().today(), published = dt.now().today(), ID = u"000000000", abstract = "Abstract: words, words, words", link = "https://www.google.com", authors = ["John H. Smith", "Jane M. Smith"], journal = "journ", topics = ["First topic", "Second Topic"]):
		self.title = title
		self.updated = updated
		self.published = published
		self.ID = ID
		self.abstract = abstract
		self.link = link
		self.authors = authors
		self.journal = journal
		self.topics = topics
		self.ObjList = [self.journal, self.ID, self.title, self.authors,self.abstract, str(self.updated), str(self.published), self.topics, self.link]

	def __repr__(self):
		RetString = ""
		for i in range(len(self.ObjList)):
			if type(self.ObjList[i]) == list:
				for j in range(len(self.ObjList[i])):
					RetString += self.ObjList[i][j]+" "
				RetString += "\n"
			else:
				RetString += self.ObjList[i] + "\n"
		return RetString

	def __str__(self):
		RetString = ""
		for i in range(len(self.ObjList)):
			if type(self.ObjList[i]) == list:
				for j in range(len(self.ObjList[i])):
					RetString += self.ObjList[i][j].encode('utf-8')+" "
				RetString += "\n"
			else:
				RetString += self.ObjList[i].encode('utf-8') + "\n"
		return RetString


if __name__ == "__main__":
	A = Article()
	print A
