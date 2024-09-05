# Accepts minLen (int) as command-line argument, and words from standard input; and for the words
# that have at least minLen characters, writes to standard output the total word count, the number
# of distinct words, and the most frequent word.

from symboltable import SymbolTable
import stdio
import sys


# Entry point.
def main():
    minLen = int(sys.argv[1])
    distinct, words = 0, 0
    st = SymbolTable()
    while not stdio.isEmpty():
        word = stdio.readString()
        if len(word) < minLen:
            continue
        words += 1
        if word in st:
            st[word] += 1
        else:
            st[word] = 1
            distinct += 1
    maxFreq = 0
    maxFreqWord = ""
    for word in st.keys():
        if st[word] > maxFreq:
            maxFreq = st[word]
            maxFreqWord = word
    stdio.writeln("Word count: " + str(words))
    stdio.writeln("Distinct word count: " + str(distinct))
    stdio.writef("Most frequent word: %s (%d repetitions)\n", maxFreqWord, maxFreq)


if __name__ == "__main__":
    main()
