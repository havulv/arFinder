#!/usr/bin/env python3


"""
 Looking into getting papers that are "interesting" from the arxiv
 At a base I want to look for things that have to do with a list of topics
 The results of the search are recorded into a file
 	That file contains the title, link, and relevant classifications


Next:
    [] Implement pyqt
        ((( from PyQt5 import QtWidgets )))

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

def none(dct):
    """ Handle None types for parameters of journal.find """
    for i,v in dct.items():
        if v != None:
            return False
    return True


def cmds(lookup=sys.argv):
    """
    Simple implementation of searching a journal for a specific query (only as it applies to the Arxiv currently)
    -ti = title
    -au = author
    -abs = abstract
    -co = comment
    -jr = journal reference
    -cat = subject category
    -rn = report number
    -id = identification number
    -all = all of the above
        (All of these parameters are strings)

    Please see the specific class entry on the return value of the journal
    """

    try: #Can be implemented with a help message [fix this]
        search = arXiv()
        SrchPrm = query(lookup)

        if none(SrchPrm):
            raise ValueError("You must input some value -- TODO: implement \
                                                                help message")

        search.find(ti=SrchPrm['-ti'], au=SrchPrm['-au'], ABS=SrchPrm['-abs'],
                    co=SrchPrm['-co'] , jr=SrchPrm['-jr'], cat=SrchPrm['-cat'],
                    rn=SrchPrm['-rn'], ID=SrchPrm['-id'], All=SrchPrm['-all'])
        return(search.articles)

    except IndexError as e:
        return("An error occurred %s, please implement logging and unit testing." % e)

def query(args):
    """
    Parse command line arguments for search query (only as it applies to arxiv)
    """

    params = {'-ti': None, '-au': None, '-abs': None, '-co': None, '-jr': None,
                            '-cat': None, '-rn': None, '-id': None,'-all': None }

    for i in range(len(args)):
        if args[i] in  params.keys():
            if args[i+1] not in params.keys():
                params[args[i]] = args[i+1]

    return params


if __name__ == "__main__":
    sample = cmds()
    for i in sample:
        print(i)
    print(sample)

