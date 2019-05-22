# arFinder

An article search and save for the arXiv.

## Installation

```
    pip install arFinder
```

## Usage

Currently supports search by title (-ti), author (-au), abstract (-abs), comment (-co), journal reference (-jr), subject category (-cat), report number (-rn), identification number (-id), or all of the previous (-all). Below are some sample usages:


For finding anything regarding `functional analysis`
```
  >python -m arFinder.py -all "functional analysis"
```


For initiating the command loop:
```
  >python -m arFinder
```

### Command Loop

The command loop has three commands: `exit`, `search`, and `topiclist` (and obviously `help`).

`search` searches for a specific topic within the arXiv.
`topiclist` displays a list of searchable topics.
`exit` exits the command loop.


To Do
-----

* Upgrade to argparse for taking in commands
* Create a better logging system
* Implement a GUI
* Implement command loop for searching and reading files
