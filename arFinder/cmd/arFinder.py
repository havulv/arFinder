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

from .cls.arxiv import ArXiv
import argparse
import cmd
import sys


class ArCmd(cmd.Cmd):
    intro = 'Welcome to the arXiv paper search and save. Type help or ? to list commands.\n'
    prompt = ' R|F|R :: '

    def __init__(self):
        cmd.Cmd.__init__(self)
        self.jrnl = ArXiv()

    def do_search(self, args):
        '''
            Search for a specific article based on title, all, author,
            abstract, comment, journal_reference, category, report_number
            id_number, or report_number
        '''

        args = args.split(" ")
        arg_dict = {k: [v] for k, v in zip(args[::2], args[1:][::2])}
        self.jrnl.find(**arg_dict)
        print(self.jrnl.name)
        for article in self.jrnl.articles:
            print("{:<4} {:^30} {:>13}".format(
                article.id, article.title, article.published))
            print(article.abstract + "\n")

    def do_topiclist(self, args):
        '''
            Print out the topics contined in the journal
            Currently deprecated.
        '''
        for topic in self.jrnl.topics:
            print(topic)

    def do_exit(self, args):
        sys.exit()


def main(args):

    if args.command:
        try:
            client = ArCmd()
            client.cmdloop()
        except Exception:
            if args.debug:
                import pdb
                pdb.set_trace()
            else:
                raise

    elif any(map(
            lambda x: False if x is None else x,
            vars(args).values())):
        search_args = vars(args)
        for cmd_arg in ['debug', 'command']:
            search_args.pop(cmd_arg)
        search = ArXiv()
        search.find(**search_args)
        for i, article in enumerate(search.articles, start=1):
            print(f"{i}. {article}")

    else:
        print("No arguments entered.")


def parse_args(args):
    parser = argparse.ArgumentParser(
        description=("Search the arxiv for papers on a certain topic."))
    parser.add_argument(
        "-ti", "--title", nargs=1, type=str,
        help=("Search the arxiv for a keyword in the title of the article"))
    parser.add_argument(
        "-a", "--all", nargs=1, type=str, dest='all_',
        help=("Search all possible search parameters for the argument"))
    parser.add_argument(
        "-au", "--author", nargs=1, type=str,
        help=("Search the arxiv for a specific author"))
    parser.add_argument(
        "-abs", "--abstract", nargs=1, type=str,
        help=("Search the arxiv for a keyword in the abstract of the article"))
    parser.add_argument(
        "-co", "--comment", nargs=1, type=str,
        help=("Search the arxiv for a keyword in the comments of the article"))
    parser.add_argument(
        "-jr", "--journal-reference", nargs=1, type=str,
        help=("Search the arxiv for a specifc journal reference"))
    parser.add_argument(
        "-cat", "--category", nargs=1, type=str,
        help=("Search the arxiv for a specific article category"))
    # TODO add a subparser for category instances
    parser.add_argument(
        "-rn", "--report-number", nargs=1, type=int,
        help=("Search the arxiv for a specific report number"))
    parser.add_argument(
        "-id", "--id-number", nargs=1, type=int,
        help=("Search the arxiv for a specific id number"))
    parser.add_argument(
        "-d", "--debug", action="store_true", default=False,
        help=("Turn on debug mode."))
    parser.add_argument(
        '-c', '--command', action='store_true',
        help=("Start the command line interface for searching and saving"))
    return parser.parse_args(args)


if __name__ == "__main__":
    main(parse_args(sys.argv[1:]))
