# Accepts floats from standard input; and writes their average to standard output.

import stdio

total = 0.0
count = 0
while not stdio.isEmpty():
    x = stdio.readFloat()
    total += x
    count += 1
average = total / count
stdio.writeln("Average is " + str(average))
