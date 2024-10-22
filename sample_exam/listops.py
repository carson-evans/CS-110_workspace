def any (a ):
    ...
    # returns True if any value in the list a is True, and False otherwise

def all (a ):
    ...
    # returns True if all values in the list a are True, and False otherwise

def exactly (a , k ):
    ...
    # returns True if exactly k values in the list a are True, and False otherwise

def count (a ):
    ...
    # returns the number of True values in the list a

# Unit tests the library .
def _main ():

    import stdio
    a = [ False , False , True , False , True , True , True ]
    stdio . writeln ( any (a ))
    stdio . writeln ( all (a ))
    stdio . writeln ( exactly (a , 3))
    stdio . writeln ( count (a ))

if __name__ == " __main__ ":
    _main()