#! /usr/bin/env python3.6

from .cmd import arFinder
import sys

if __name__ == "__main__":
    arFinder.main(arFinder.parse_args(sys.argv[1:]))
