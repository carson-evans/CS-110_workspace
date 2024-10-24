import stdio
import sys


# Entry point (DO NOT EDIT).
def main():
    s = sys.argv[1]
    stdio.writeln(_isPalindrome(s))


# Returns True if s is a palindrome and False otherwise.
def _isPalindrome(s):
    ...

    # set n to num of chars in s
    n = len(s)

    # for each i in [0, n/2]
        # return false if s[i] is different from s[n - i - 1]
    for i in range(0, n//2):
       if s[i] != s[n - i - 1]:
           return False

    # return true
    return True

if __name__ == "__main__":
    main()
