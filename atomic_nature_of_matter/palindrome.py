import stdio
import sys


# Entry point [DO NOT EDIT].
def main():
    s = sys.argv[1]
    stdio.writeln(_isPalindrome(s))


# Returns True if s is a palindrome, and False otherwise.
def _isPalindrome(s):
    """
    :param s:
    :return true or false if s is a palindrome:
    """

    n = len(s)

    # Base case
    if n == 0:
        return True
    else:
        # if first in s is the same as the last character
        if s[0] == s[-1] and (_isPalindrome(s[1: n - 1])) == True:
            return True
        else:
            return False

if __name__ == "__main__":
    main()
