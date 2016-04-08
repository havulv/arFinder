#!/usr/bin/python


"""
 Looking into getting papers that are "interesting" from the arxiv
 At a base I want to look for things that have to do with a list of topics
 The results of the search are recorded into a file
 	That file contains the title, link, and relevant classifications

First Steps:
    [] create a robust object that will handle any journal object
        [] the arxiv object should be a class inheriting the journals data members and functions




 TO DO:
[]	Add other journals to choose from
[]	Implement the listing into an application with vim-like bindings
    []      q for quit
    []      Enter to save download the pdf
    []      Arrow keys or j & k to go up and down respectvely
[]      The application should have all of the titles listed on the left and then the highlighted one would be on the center
            I.E.
            -----------------
            | 1 |           |
            | 2 |           |
            | 3 |     3     |
            | 4 |           |
            | 5 |           |
            | 6 |           |
            -----------------
[]	Save the files into Zotero or EndNote, through the Arxiv metadata
[]	Implement Error Handling across all files

	MAYBE:
[]		-Have the user cycle through the new articles (Either with Tkinter or maybe as a pdf? Questionable.)
[]		-At a key press, the user can save it to the file
[]		-Or can reject it and not save it (Consider saving the rejected titles/ids [Would need to start recording Arxiv ids] to another file and when scanning for new articles these would not be picked up again.)
[]			+Include a master quit out key
[X]		-Implement the Arxiv items as a class. Might be easier to pass around objects.
[]			+If this is the case then I might want to implement the class in C++ (4 speed)

"""



import time
import urllib
import datetime as dt
import sys
import feedparser
from Journal import Journal

def search():

	with open("Arxivlog.txt") as fil:
		strdate = fil.readlines()[0][0:19]
	pastdate = dt.datetime.strptime(strdate, "%Y-%m-%d %H:%M:%S")

	with open("topics.txt") as topic:
		lines = topic.readlines()

	for topic in lines:
		time.sleep(3)
		url = 'http://export.arxiv.org/api/query?search_query=%28abs:{0}+OR+ti:{0}%29&start=0&max_results=150&sortBy=lastUpdatedDate&sortOrder=descending'.format(topic)
		d = feedparser.parse(url)

		for entry in d['entries']:

			artupdate = dt.datetime.strptime(entry['updated'], '%Y-%m-%dT%H:%M:%SZ')
			artpubdate = dt.datetime.strptime(entry['published'], '%Y-%m-%dT%H:%M:%SZ')
			Artic = Journal.Article(title = entry[u'title'],updated = artupdate,published = artpubdate,ID = entry['id'][-12:],abstract = entry['summary'],authors = [entry['authors'][i]['name'] for i in range(len(entry['authors']))], journal = "Arxiv", topics = [entry['tags'][0]['term']], link = entry['links'][1]['href'] )
			if artupdate >= pastdate:
				flag = False
				with open("ArxivDoc.txt", 'r+w') as fil:
					for line in fil.readlines():
						if ("{0}".format((Artic.title).encode('utf-8')) in line):
							flag = True
							break
					if flag == False:
						fil.seek(0,2)
						fil.write("%s\n" % (Artic))
						fil.flush()
			else:
				break
	return


def DispTopic():
	with open("topics.txt") as topic:
		line = topic.readlines()
		for i in range(len(line)):
			print line[i].rstrip()

def delTopic(top):
	with open("topics.txt", 'r+w') as topic:
		line = topic.readlines()
		topic.seek(0)
		for i in range(len(line)):
			if top != line[i].rstrip():
				topic.write(line[i])
		topic.truncate()

def AddTopic(top):
	flag = False
	with open("topics.txt", 'r+w') as topic:
		line = topic.readlines()
		for i in range(len(line)):
			if top == line[i].rstrip():
				flag = True
	if flag == False:
		with open("topics.txt", 'a') as topic:
			topic.write(top)




def log():
	with open("Arxivlog.txt", 'w') as fil:
		fil.write(str(dt.datetime.now().today()))


def Help():
	hListDescrip = ["Searches Arxiv and retrieves the mathematics related articles with specified topics", "removes a topic from topics.txt", "adds a topic to topics.txt", "Displays the topics"]
	hList = ['-s', '-rm', '-a', '-d']
	print 'Usage: ./ArxivGet.py [-s][-rm][-a topic][-d]'

	for i in range(len(hList)):
		print "{0:^10}{1:>}".format(hList[i], hListDescrip[i])

#DispTopic()
#print
#delTopic("functional")
#DispTopic()
#print
#AddTopic("functional")
#DispTopic()

#search()

if __name__ == "__main__":
	try:
		sys.argv[1]
	except IndexError:
		Help()
		sys.exit(0)

	if sys.argv[1] == '-a':
		try:
			topic = sys.argv[2]
		except IndexError:
			raise Exception('You must specify the topic to add.')
		AddTopic(topic)

	elif sys.argv[1] == '-rm':
		DispTopic()

		topic = raw_input("\nEnter the topic you would like removed:\n")
		delTopic(topic)

	elif sys.argv[1] == '-s':
		search()
		log()

	elif sys.argv[1] == '-d':
		DispTopic()

	else:
		Help()



