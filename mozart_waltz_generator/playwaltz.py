import stdaudio
import stdio
import sys

...

# Play

# stdin = 32 measures
# stdaud = the waltz

# set measures to a list of ints
# representing measures of a waltz
# read from stdin using stdio.readAllInts()

measures = stdio.readAllInts()

# exit the program with message
# "A waltz must contain exactly 32 measures"
# if measures does not contain 32 values
# use sys.exit()

if len(measures) != 32:
    sys.exit("A waltz must contain exactly 32 measures")

# Exit the program with the message "a minuet measure must
# be from [1, 176]" if any of the first 16 values of measures
# is not from the interval [1, 176] using sys.exit()

for i in range(16):
    if not(1 <= measures[i] <= 176):
        sys.exit("A minuet measure must be from [1, 176]")

# Exit the program with the message “A trio measure must
# be from [1, 96]” if the any of the last 16 values of
# measures is not from the interval [1, 96]
# (use sys.exit())

for i in range(16, 32):
    if not(1 <= measures[i] <= 96):
        sys.exit("A trio measure must be from [1, 96]")

# Play the minuet measures
for i in range(16):
    filename = 'data/T' + str(measures[i]) + '.wav'
    #Play
    stdaudio.playFile(filename)

# play trio measures
for i in range(16, 32):
    filename = 'data/M' + str(measures[i]) + '.wav'
    # Play
    stdaudio.playFile(filename)

# wait for all to finish before exiting
stdaudio.wait()