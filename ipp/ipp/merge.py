# This library implements merge sort.

import stdarray
import stdio
import sys


# Sorts the specified array according to the natural ordering of its objects, or according to
# the order induced by key, if one is specified.
def sort(a, key=lambda x: x):
    aux = stdarray.create1D(len(a), None)
    _sort(a, aux, 0, len(a) - 1, key)


# Sorts the specified array from index lo to index hi according to the natural ordering of its
# elements, or according to the order induced by key, if one is specified.
def _sort(a, aux, lo, hi, key):
    if hi <= lo:
        return
    mid = lo + (hi - lo) // 2
    _sort(a, aux, lo, mid, key)
    _sort(a, aux, mid + 1, hi, key)
    _merge(a, aux, lo, mid, hi, key)


# Merges the two halves(index lo to index mid and index mid + 1 to index hi) in the specified
# array according to the natural ordering of its elements, or according to the order induced by
# key, if one is specified.
def _merge(a, aux, lo, mid, hi, key):
    for k in range(lo, hi + 1):
        aux[k] = a[k]
    i, j = lo, mid + 1
    for k in range(lo, hi + 1):
        if i > mid:
            a[k] = aux[j]
            j += 1
        elif j > hi:
            a[k] = aux[i]
            i += 1
        elif key(aux[j]) < key(aux[i]):
            a[k] = aux[j]
            j += 1
        else:
            a[k] = aux[i]
            i += 1


# Unit tests the library.
def _main():
    a = stdio.readAllStrings()
    if sys.argv[1] == "String":
        sort(a)
    elif sys.argv[1] == "string":
        sort(a, key=lambda x: x.lower())
    else:
        raise Exception("Illegal command-line argument")
    for s in a:
        stdio.write(s + " ")
    stdio.writeln()


if __name__ == "__main__":
    _main()
