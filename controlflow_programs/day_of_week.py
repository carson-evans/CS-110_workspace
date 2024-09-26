import stdio
import sys

...

# Get year month and day from cli
m = int(sys.argv[1]) # Month
d = int(sys.argv[2]) # Day
y = int(sys.argv[3]) # Year

# Calculate
y0 = y - (14 - m) // 12
x0 = y0 + y0 // 4 - y0 // 100 + y0 // 400
m0 = m + 12 * ((14 - m) // 12) - 2
dow = (d + x0 + 31 * m0 // 12) % 7

# Print day of the week (0 for Sunday, 1 for Monday, and so on)
if dow == 0:
    stdio.writeln("Sunday")
if dow == 1:
    stdio.writeln("Monday")
if dow == 2:
    stdio.writeln("Tuesday")
if dow == 3:
    stdio.writeln("Wednesday")
if dow == 4:
    stdio.writeln("Thursday")
if dow == 5:
    stdio.writeln("Friday")
if dow == 6:
    stdio.writeln("Saturday")