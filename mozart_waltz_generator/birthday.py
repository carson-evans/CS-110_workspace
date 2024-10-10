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

for t in range (trials):
    # Set birthdaysSeen to a list the size of days_per_year
    # With all elements set to false using stdarray.createID()
    birthdaysSeen = stdarray.create1D(days_per_year, False)

    # Repeat forever
    while True:

        # Increment count by 1
        count += 1

        # Set birthday to a random int from [0, days_per_year)
        birthday = stdrandom.uniformInt(0, days_per_year)

        # If birthday was seen before, break
        if birthdaysSeen[birthday]:
            break

        # else, record that we are seeing it now
        else:
            birthdaysSeen[birthday] = True

# Write count / trials using integer division
average_count = count // trials
stdio.write(average_count)