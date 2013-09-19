

# stylize

stylize is a style checker for English.

# Motivation

Remembering rules for style is needlessly difficult. It is much easier to simply program them and then fix them as they arise until they become effortless.

# Installation

1. Clone this repo somewhere
2. `python setup.py install` (this may need sudo privileges to install systemwide)

TODO: set up on pip

## syntastic

stylize can be configured to work with syntastic via:

```
ln -s `pwd`/auxillary/md/ ~/.vim/bundle/syntastic/syntax_checkers/md
```

# Example usage

```
stylize README.md
README.md:9:53: X's Y -> Y of X
```
