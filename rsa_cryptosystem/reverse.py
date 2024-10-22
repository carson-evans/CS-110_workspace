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
    ...


if __name__ == "__main__":
    main()
