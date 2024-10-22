import stdio

...

total = 0

while not stdio.isEmpty():
    # read
    x = stdio.readInt()

    # control + z to exit

    # writes the sum of squares
    # of the even integers to standard output.

    total += x * x if x % 2 == 0 else 0

stdio.writeln (total)