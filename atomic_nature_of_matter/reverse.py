import stdio
import sys


# Entry point [DO NOT EDIT].
def main():
    s = sys.argv[1]
    stdio.writeln(_reverse(s))


# Returns the reverse of the string s.
def _reverse(s):
    """
    :param s:
    :return reversed string:
    """

    n = len(s)

    # Base case
    if n == 0:
        return ""

    return s[n - 1] + _reverse(s[: n - 1])


if __name__ == "__main__":
    main()
