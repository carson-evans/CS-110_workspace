import stdio
import sys

...

n1 = int(sys.argv[1]) # player 1's number of pennies
n2 = int(sys.argv[2]) # player 2's number of pennies
p = float(sys.argv[3]) # prob that player 1 wins each toss
q = 1 - p # prob that player 2 wins each toss

p1 = (1 - (p / q) ** n2) / (1 - (p / q) ** (n1 + n2))
p2 = (1 - (p / q) ** n1) / (1 - (p / q) ** (n1 + n2))

print(f"{p1} {p2}")