# keygen.py
import rsa
import stdio
import sys

# Entry point.
def main():
    """
    Main function to generate RSA public and private keys.
    Accepts two command line arguments representing lower and upper bounds
    for prime number selection.
    Outputs the keys to standard output
    """

    # QA
    if len(sys.argv) != 3:
        return

    # Parse lo and hi
    try:
        lo = int(sys.argv[1])
        hi = int(sys.argv[2])
    except ValueError:
        return

    # Generate
    # Returns n (modulus), e (public exponent), and d (private exponent)
    n, e, d = rsa.keygen(lo, hi)

    # print n e d
    stdio.writeln(f"{n} {e} {d}")


if __name__ == "__main__":
    main()
