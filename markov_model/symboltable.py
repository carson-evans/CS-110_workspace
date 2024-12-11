# A data type to represent a symbol table of key-value pairs.

import stdio


class SymbolTable:
    # Constructs an empty symbol table.
    def __init__(self):
        self._st = {}  # dictionary of key-value pairs
        self._n = 0  # number of key-value pairs

    # Returns True if this symbol table is empty, and False otherwise.
    def isEmpty(self):
        return len(self) == 0

    # Returns the number of key-value pairs in this symbol table.
    def __len__(self):
        return self._n

    # Returns True if this symbol table contains key, and False otherwise.
    def __contains__(self, key):
        return self[key] != None

    # Returns the value associated with key in this symbol table.
    def __getitem__(self, key):
        if key == None:
            raise Exception("key is None")
        return self._st[key] if key in self._st else None

    # Inserts a key-value pair into this symbol table.
    def __setitem__(self, key, value):
        if key == None:
            raise Exception("key is None")
        if value == None:
            raise Exception("value is None")
        if key not in self:
            self._n += 1
        self._st[key] = value

    # Deletes key and the associated value from this symbol table.
    def __delitem__(self, key):
        if key == None:
            raise Exception("key is None")
        self._st.pop(key)

    # Returns the keys in this symbol table, as an iterable object.
    def keys(self):
        return self._st.keys()


# Unit tests the data type.
def _main():
    st = SymbolTable()
    stdio.writeln("Filling st with characters from the English alphabet ...")
    for i, c in enumerate("abcdefghijklmnopqrstuvwxyz"):
        st[c] = i + 1
    stdio.writeln(st)
    stdio.writeln("Deleting vowels from st ...")
    for c in "aeiou":
        del (st[c])
    for c in st.keys():
        stdio.writeln(c + ": " + str(st[c]))


if __name__ == "__main__":
    _main()
