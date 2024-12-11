from symboltable import SymbolTable
import stdio
import stdrandom
import sys


class MarkovModel(object):
    # Creates a Markov model of order k from the given text.
    def __init__(self, text, k):
        ...

    # Returns the order this Markov model.
    def order(self):
        ...

    # Returns the number of occurrences of kgram in this Markov model; and 0 if kgram is
    # nonexistent. Raises an error if kgram is not of length k.
    def kgram_freq(self, kgram):
        ...

    # Returns number of times character c follows kgram in this Markov model; and 0 if kgram is
    # nonexistent or if it is not followed by c. Raises an error if kgram is not of length k.
    def char_freq(self, kgram, c):
        ...

    # Returns a random character following kgram in this Markov model. Raises an error if kgram is
    # not of length k or if kgram is nonexistent.
    def rand(self, kgram):
        ...

    # Generates and returns a string of length n from this Markov model, the first k characters of
    # which is kgram.
    def gen(self, kgram, n):
        ...

    # Replaces unknown characters (~) in corrupted with most probable characters from this Markov
    # model, and returns that string.
    def replace_unknown(self, corrupted):
        original = ""
        for i in range(len(corrupted)):
            if corrupted[i] == "~":
                ...
            else:
                original += corrupted[i]
        return original


# Given a list a, _argmax returns the index of the maximum value in a.
def _argmax(a):
    return a.index(max(a))


# Unit tests the data type [DO NOT EDIT].
def _main():
    model = MarkovModel("gagggagaggcgagaaa", 2)
    stdio.writeln("model       = MarkoveModel(\"gagggagaggcgagaaa\", k = 2)")
    stdio.writef("freq(ag)    = %d\n", model.kgram_freq("ag"))
    stdio.writef("freq(cg)    = %d\n", model.kgram_freq("cg"))
    stdio.writef("freq(gc)    = %d\n", model.kgram_freq("gc"))
    stdio.writef("freq(xx)    = %d\n", model.kgram_freq("xx"))
    stdio.writef("freq(aa, a) = %d\n", model.char_freq("aa", "a"))
    stdio.writef("freq(ga, g) = %d\n", model.char_freq("ga", "g"))
    stdio.writef("freq(gg, c) = %d\n", model.char_freq("gg", "c"))
    stdio.writef("freq(xx, x) = %d\n", model.char_freq("xx", "x"))
    stdio.writef("freq(gg, x) = %d\n", model.char_freq("gg", "x"))


if __name__ == "__main__":
    _main()
