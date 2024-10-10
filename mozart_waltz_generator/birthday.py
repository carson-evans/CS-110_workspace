import stdarray
import stdio
import stdrandom
import sys

...

# Suppose people empty an empty room until a pair of people
# Share a birthday

# On average, how many people will have to enter
# Before there is a match?

# Run trials experiments to estimate
# Each run involves sampling until a pair shares

days_per_year = 365
trials = int(sys.argv[1])
count = 0

for t in range (0, trials):
    # Set birthdaysSeen to a list the size of days_per_year
    # With all elements set to false using stdarray.createID()
    # Repeat forever
        # Increment count by 1
        # Set birthday to a random int from [0, days_per_year)
        # If birthday was seen before, break
        # else, record that we are seeing it now
# Write count / trials using integer division