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
    sys.stdout.write("Sunday\n")
if dow == 1:
    sys.stdout.write("Monday\n")
if dow == 2:
    sys.stdout.write("Tuesday\n")
if dow == 3:
    sys.stdout.write("Wednesday\n")
if dow == 4:
    sys.stdout.write("Thursday\n")
if dow == 5:
    sys.stdout.write("Friday\n")
if dow == 6:
    sys.stdout.write("Saturday\n")