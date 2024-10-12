import stdarray
import stdrandom
import stdio

...

# A waltz:
# consists of two parts, the minuet and the trio
# each comprised of 16 measures

# The file data/mozart.wav provides an example of a waltz
# there are 176 possible minuet measures
# and 96 possible trio measures

# corresponding to each minuet and trio measure,
# there is an audio file under the data directory

# create a 2d list called minuetMeasures 11x16
minuetMeasures = stdarray.create2D(11, 16)

# populate with values read from stdin using readInt()
for i in range(11):
    for j in range(16):
        minuetMeasures[i][j] = stdio.readInt()

# create a 2d list called trioMeasures 6x16
trioMeasures = stdarray.create2D(6, 16)

# read trio measures from input
for i in range(6):
    for j in range(16):
        trioMeasures[i][j] = stdio.readInt()

# Generate 16 minuet measures
minuetSequence = []
for i in range(16):
    dice_roll = stdrandom.uniformInt(1, 6) + stdrandom.uniformInt(1, 6)
    measure = minuetMeasures[dice_roll - 1][i]
    minuetSequence.append(measure)

# generate 16 trio measures
trioSequence = []
for i in range(16):
    # Roll one die 1 to 6
    dice_roll = stdrandom.uniformInt(1, 6)
    # Use dice roll to pick a measure from the corresponding colum of trioMeasures
    measure = trioMeasures[dice_roll - 1][i]
    trioSequence.append(measure)

stdio.writeln(' '.join(map(str, minuetSequence + trioSequence)))