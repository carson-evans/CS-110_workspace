import stdio

...

# Read all strings from stdin into a list 'a' use stdio.readAllStrings()

a = stdio.readAllStrings()
# set n to the size of a

n = len(a)

# for each i ∈ [0, n/2)
for i in range (0, n // 2):
    # Exchange a[i] with a[n - i - 1]
    a[i], a[n - i -1] = a[n - i - 1], a[i]

# for each i ∈ [0, n)
for i in range (n):
    if i < n - 1:
        stdio.write(a[i])
        stdio.write(" ")
    else:
        stdio.writeln(a[i])
