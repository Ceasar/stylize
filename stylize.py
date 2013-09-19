import re
import sys


class Error(object):
    def __init__(self, filename, line, character, message):
        self.filename = filename
        self.line = line
        self.character = character
        self.message = message

    def __str__(self):
        return "%s:%s:%s: %s" % (self.filename,
                                self.line,
                                self.character,
                                self.message)


def rule_so_that(sentence, tokens):
    if "so" in tokens and not "that" in tokens:
        return tokens.index("so"), "X is so Y -> X is so Y that Z"


def rule_possesive(sentence, tokens):
    if "\'s" in sentence:
        return sentence.index("\'s"), "X's Y -> Y of X"
    elif "s\'" in sentence:
        return sentence.index("s\'"), "Xs' Y -> Y of Xs"

RULES = [
    rule_so_that,
    rule_possesive,
]

REGEXES = []

with open("regexes/comma.txt") as f:
    lines = iter(f)
    pattern = next(lines)
    repl = next(lines)
    REGEXES.append((pattern, repl))


def find_errors(filename):
    with open(sys.argv[1]) as f:
        for i, line in enumerate(f):
            i = i + 1
            tokens = line.split()
            for rule in RULES:
                rv = rule(line, tokens)
                if rv is not None:
                    c, e = rv
                    yield Error(filename, i, c, e)
                    break
            for pattern, repl in REGEXES:
                if re.match(pattern, line):
                    yield Error(filename, i, 0, re.sub(pattern, repl, line))


def _main():
    errors = find_errors(sys.argv[1])
    for error in errors:
        print error

if __name__ == "__main__":
    _main()
