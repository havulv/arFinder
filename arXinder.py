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

"""



import sys
from .journals.arxiv import arXiv


def cmds():
    try:
        for i in sys.argv:
            search = arXiv()
            search.find(All=sys.argv[i])
            for j in search.articles:
                print (j)
    except IndexError:
        sys.exit(0)


if __name__ == "__main__":
    print (sys.path)
    cmds()

