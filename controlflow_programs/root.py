import stdio
import sys

...

k = int(sys.argv[1]) # the root to calculate (kth root)
c = float(sys.argv[2]) # The number to take the root of
epsilon = float(sys.argv[3]) # Precision

# Write to standard output the kth root of c, up to epsilon decimal places

# Handle case where c is zero
if c == 0:
    stdio.writeln(0.0)
    sys.exit()

# Initialize a guess
guess = 1.0

# Iterate until close enough
while abs(guess ** k - c) > epsilon:
    guess = ((k-1) * guess + c / (guess**(k-1))) / k

# Print approx
stdio.writeln(guess)