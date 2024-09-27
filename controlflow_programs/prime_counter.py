import stdio
import sys

...

n = int(sys.argv[1])
count = 0

for i in range(2, n+1):
    is_prime = True
    for j in range(2, int(i**0.5) + 1):
        if i % j == 0:
            is_prime = False
            break
    if is_prime:
        count += 1

sys.stdout.write(f"{count}\n")