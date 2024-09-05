# Accepts x (float) as command-line argument; and writes to standard output the square root of
# x, reporting an error if x is not specified, is not a float, or is negative.

import math
import stdio
import sys


# Entry point.
def main():
    try:
        x = float(sys.argv[1])
        result = _sqrt(x)
        stdio.writeln(result)
    except IndexError:
        stdio.writeln("x not specified")
    except ValueError:
        stdio.writeln("x must be a float")
    except Exception as e:
        stdio.writeln(e)
    finally:
        stdio.writeln("Done!")


# Returns the square root of x. Raises an Exception if x is negative.
def _sqrt(x):
    if x < 0:
        raise Exception("x must be non-negative")
    return math.sqrt(x)


if __name__ == "__main__":
    main()
