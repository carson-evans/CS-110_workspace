import stdio


# Entry point (DO NOT EDIT).
def main():
    a = stdio.readAllStrings()
    _reverse(a)
    for v in a:
        stdio.writef("%s ", v)
    stdio.writeln()


# Reverses a in place, ie, without creating a new list.
def _reverse(a):
    n = len(a)
    # for each i in [0, n/2]
        # exchange a[i] with a[n-i-1] using temp variable
    for i in range(0, n // 2):
        temp = a[i]
        a[i] = a[n - i - 1]
        a[n - i - 1] = temp

if __name__ == "__main__":
    main()
