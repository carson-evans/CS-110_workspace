# An iterable data type to iterate over the words in a sentence.

import stdio
import sys


class Words:
    # Constructs a Words object from the given sentence.
    def __init__(self, sentence):
        self._sentence = sentence  # the sentence

    # Returns a string representation of this object.
    def __str__(self):
        s = ""
        for v in self:
            s += str(v) + " "
        return s.strip()

    # Returns an iterator to iterate over the words in a sentence.
    def __iter__(self):
        return Words.WordsIterator(self._sentence)

    # An iterator that iterates over the words in a sentence.
    class WordsIterator:
        # Constructs a WordsIterator object given the sentence.
        def __init__(self, sentence):
            self._words = sentence.split()  # words in the sentence
            self._current = 0  # index of the current word

        # Returns the next word in the sentence if there is one, and raises StopIteration otherwise.
        def __next__(self):
            if self._current == len(self._words):
                raise StopIteration
            word = self._words[self._current]
            self._current += 1
            return word


# Unit tests the data type.
def _main():
    sentence = sys.argv[1]
    words = Words(sentence)
    stdio.writeln(words)


if __name__ == "__main__":
    _main()
