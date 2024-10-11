import stdarray
import stdio
import sys

...

# accept n as cli
n = int(sys.argv[1])

# create a list 'a' of size n + 1 with all set to none
a = stdarray.create1D(n + 1)

# for each i  ∈ [0, n]
for i in range(n + 1):
    # set a[i] to a list of size i + 1 with all set to 1
    a[i] = stdarray.create1D(i + 1, 1)

# for each i  ∈ [0, n]
for i in range(n + 1):
    # for each j  ∈ [1, i]
    for j in range (1, i):
        a[i][j] = a[i - 1][j - 1] + a[i -1][j]

# for each i ∈ [0, n]
for i in range(0, n + 1):
    # For each j ∈ [0, i]
    for j in range(0, i + 1):
        # f j < i, write a[i][j] with a space after;
        if j == i:
            stdio.writeln(a[i][j])
        # otherwise, write a[i][j] with a newline after
        else:
            stdio.write(str(a[i][j]) + " ")
    # Print a new line after each row