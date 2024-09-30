import stdio
import sys

...

k = int(sys.argv[1]) # the root to calculate (kth root)
c = float(sys.argv[2]) # The number to take the root of
epsilon = float(sys.argv[3]) # Precision

# Write to standard output the kth root of c, up to epsilon decimal places

t = c

# Repeat as long as |1 - c/t^k| > epsilon
while abs(1 - (c / (t ** k))) > epsilon:
    t = t - (t ** k - c) / (k * t ** (k - 1))
    # Set t to t - f(t) / f'(t), where f(t) = t^k - c
    # and f'(t) = kt^(k-1)

stdio.writeln(t) # Write t