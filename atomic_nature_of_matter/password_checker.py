import stdio
import sys


# Entry point [DO NOT EDIT].
def main():
    pwd = sys.argv[1]
    stdio.writeln(_isValid(pwd))


# Returns True if pwd is a valid password, and False otherwise.
def _isValid(pwd):
    """
    :param pwd:
    :return bool:
    """

    check1, check2, check3, check4, check5 = False, False, False, False, False

    if len(pwd) >= 8:
        check1 = True

    for c in pwd: # For each char c in pwd
        if c.isdigit(): # if c is a digit, set check2 to true
            check2 = True
        elif c.isupper(): # else if c is upper case, set check3 to true
            check3 = True
        elif c.islower(): # else if c is lower case, set check4 to true
            check4 = True
        elif not c.isalnum(): # else if c is not alphanumeric set check5 to true
            check5 = True

    # Return the logical and of check1, check2, check3, check4, and check5
    if check1 and check2 and check3 and check4 and check5 == True:
        return True
    else:
        return False

if __name__ == "__main__":
    main()
