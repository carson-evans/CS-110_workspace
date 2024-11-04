# rsa.py
import stdio
import stdrandom
import sys

# Generates and returns the public/private keys as a tuple (n, e, d). Prime numbers p and q
# needed to generate the keys are picked from the interval [lo, hi).
def keygen(lo, hi):
    # Get two distinct prime numbers p and q from [lo, hi)
    primes = _primes(lo, hi)
    p = _choice(primes)
    q = _choice([x for x in primes if x != p])

    # Calculate n and the totient m
    n = p * q
    m = (p - 1) * (q - 1)

    # Choose e such that 1 < e < m and gcd(e, m) = 1
    e = stdrandom.uniformInt(2, m - 1)
    while True:
        # Compute gcd of e and m
        a, b = e, m
        while b != 0:
            a, b = b, a % b
        if a == 1:
            break
        e = stdrandom.uniformInt(2, m - 1)

    # Compute d, the modular inverse of e modulo m using the Extended Euclidean Algorithm
    old_r, r = m, e
    old_s, s = 0, 1

    while r != 0:
        quotient = old_r // r
        old_r, r = r, old_r - quotient * r
        old_s, s = s, old_s - quotient * s

    # Ensure d is positive
    d = old_s % m

    return n, e, d


# Encrypts x (int) using the public key (n, e) and returns the encrypted value.
def encrypt(x, n, e):
    return pow(x, e, n)


# Decrypts y (int) using the private key (n, d) and returns the decrypted value.
def decrypt(y, n, d):
    return pow(y, d, n)


# Returns the least number of bits needed to represent n.
def bitLength(n):
    return len(bin(n)) - 2


# Returns the binary representation of n expressed in decimal, having the given width, and padded
# with leading zeros.
def dec2bin(n, width):
    return format(n, "0%db" % (width))


# Returns the decimal representation of n expressed in binary.
def bin2dec(n):
    return int(n, 2)


# Returns a list of primes from the interval [lo, hi).
def _primes(lo, hi):
    sieve = [True] * hi
    sieve[0] = sieve[1] = False
    for i in range(2, hi):
        if sieve[i]:
            for j in range(i * i, hi, i):
                sieve[j] = False
    return [x for x in range(lo, hi) if sieve[x]]


# Returns a list containing a random sample (without replacement) of k items from the list a.
def _sample(a, k):
    if k > len(a):
        raise ValueError

    if k == len(a):
        return a[:]

    # Create a copy of list to avoid modifying original
    a_copy = a[:]
    sample = []

    # Select k unique items from a_copy
    for _ in range(k):
        index = stdrandom.uniformInt(0, len(a_copy) - 1)
        sample.append(a_copy.pop(index))

    return sample


# Returns a random item from the list a.
def _choice(a):
    return a[stdrandom.uniformInt(0, len(a) - 1)]


# Unit tests the library [DO NOT EDIT].
def _main():
    c = sys.argv[1]
    x = ord(c)
    n, e, d = keygen(25, 100)
    encrypted = encrypt(x, n, e)
    stdio.writef("encrypt(%c) = %d\n", c, encrypted)
    decrypted = decrypt(encrypted, n, d)
    stdio.writef("decrypt(%d) = %c\n", encrypted, chr(decrypted))
    width = bitLength(x)
    stdio.writef("bitLength(%d) = %d\n", x, width)
    xBinary = dec2bin(x, width)
    stdio.writef("dec2bin(%d) = %s\n", x, xBinary)
    stdio.writef("bin2dec(%s) = %d\n", xBinary, bin2dec(xBinary))


if __name__ == "__main__":
    _main()
