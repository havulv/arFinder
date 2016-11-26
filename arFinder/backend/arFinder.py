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
import argparse

import cmd, readline

import sys
from journals.arxiv import arXiv

class ArCmd(cmd.Cmd):
    intro = 'Welcome to the arXiv paper search and save. Type help or ? to list commands.\n'
    prompt = ' R|F|R :: '

    def __init__(self):
        cmd.Cmd.__init__(self)
        jrnl = ArXiv()

    def do_search(self, args):
        self.jrnl.find(**parse(args))



    def do_help(self, args):


def parse(args):
    args = args.split(" ")
    return dict(zip(args[::2], args[1:][::2]))

def main():
    args = parse_args()

    if not any([ val if key != "debug" else False for
                                key, val in args.items()]):
        try:
            client = ArCmd()
            client.cmdloop()
        except Exception:
            if "debug" in args:
                import pdb
                pdb.set_trace()
            else:
                raise
    else:
        search = arXiv()
        search.find(**args)
        print(search.articles)

def parse_args():
    parser = argparse.ArgumentParser(
        description=("Search the arxiv for papers on a certain topic."))
    parser.add_argument(
        "-ti", "--title", nargs=1, type=str, help=("Search the arxiv "
            "for a keyword in the title of the article"))
    parser.add_argument(
        "-a", "--All", nargs=1, type=str, help=("Search all possible"
            "search parameters for the argument"))
    parser.add_argument(
        "-au", "--author", nargs=1, type=str, help=("Search the arxiv "
            "for a specific author"))
    parser.add_argument(
        "-abs", "--abstract", nargs=1, type=str, help=("Search the "
            "arxiv for a keyword in the abstract of the article"))
    parser.add_argument(
        "-co", "--comment", nargs=1, type=str, help=("Search the arxiv"
            " for a keyword in the comments of the article"))
    parser.add_argument(
        "-jr", "--journal-reference", nargs=1, type=str, help=("Search"
            "the arxiv for a specifc journal reference"))
    parser.add_argument(
        "-cat", "--category", nargs=1, type=str, help=("Search the "
            "arxiv for a specific article category"))
        #TODO add a subparser for category instances
    parser.add_argument(
        "-rn", "--report-number", nargs=1, type=int, help=("Search the"
            "arxiv for a specific report number"))
    parser.add_argument(
        "-id", "--id-number", nargs=1, type=int, help=("Search the "
            "arxiv for a specific id number"))
    parser.add_argument(
        "-d",  "--debug", action="store_true", default=False, help=(
        "Turn on debug mode."))
    opts = parser.parse_args()
    return dict(vars(opts))

if __name__ == "__main__":
    main()

