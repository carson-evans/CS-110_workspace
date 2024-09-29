import stdio
import sys

...

# verify that 1729 is an interesting number
# because it is the smallest number expressible as the sum
# of two cubes in two different ways

n = int(sys.argv[1])

# output all integers less than or equal to n
# that can be expressed as the sum of two cubes in two ways

# Find all distinct positive ints 'a', 'b', 'c', and 'd'
# such that
# a^3 + b^3 = c^3 + d^3 ≤ n

# Calculate upper limit for 'a' and 'b' to keep computation within 'n'
max_a = 1
while max_a ** 3 < n:
    max_a += 1

a = 1
while a <= max_a:
    b = a
    while b <= max_a:
        s = a ** 3 + b ** 3
        if s > n:
            b += 1
            continue
        c = a # Start from 'a' to avoid redundancy
        while c <= max_a:
            d = c
            while d <= max_a:
                if (a == c and b == d) or (a == d and b == c):
                    d += 1
                    continue # Skip identical and symmetrical pairs
                t = c ** 3 + d ** 3
                if t > n:
                    d += 1
                    continue
                if s == t:
                    stdio.writeln(f"{s} = {a}^3 + {b}^3 = {c}^3 + {d}^3")
                d += 1
            c += 1
        b += 1
    a += 1
