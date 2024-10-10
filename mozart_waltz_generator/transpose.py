import stdarray
import stdio
import sys

...

# m x n floats from standard input representing
# the elements of an m x n matrix a
# set all elements to none

# and writes to standard output the transpose of a
# Recall that the transpose of an m x n matrix a
# is an n by m matrix b
# such that B sub ij = A sub ji
# where 0 <= i < n and 0 <= j < m

m = int(sys.argv[1])
n = int(sys.argv[2])

a = stdarray.create2D(m,n)

# read values into the matrix 'a'
# for each i ∈ [0, m)
for i in range(m):
    # for each j ∈ [0, n)
    for j in range(n):
        # set a[i][j] to a float read from stdin
        a[i][j] = stdio.readFloat()

# create an n x m list c with all elements set to none
c = stdarray.create2D(n,m)

# compute transpose of 'a' into 'c'
# for each i ∈ [0, n)
for i in range(n):
    # for each j ∈ [0, m)
    for j in range(m):
        # set c[i][j] to a[j][i]
        c[i][j] = a[j][i]

# for each i ∈ [0, n)
for i in range(n):
    # for each j ∈ [0, m)
    for j in range(m):
        # if j < m -1
        if j < m - 1:
            # write c[i][j] + " "
            stdio.write(str(c[i][j]) + " ")
        # else
        else:
            # write c[i][j] + "\n"
            stdio.writeln(c[i][j])