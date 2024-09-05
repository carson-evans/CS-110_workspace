# Generates a random integer; repeatedly accepts user guesses from standard input; writes "Too
# low" or "Too high" to standard output, as appropriate, in response to each guess; and writes
# "You win!" to standard output and exits when the user"s guess is correct.

import stdio
import stdrandom

RANGE = 1000000
secret = stdrandom.uniformInt(1, RANGE + 1)
stdio.writef("I am thinking of a secret number between 1 and %d\n", RANGE)
guess = 0
while guess != secret:
    stdio.write("What is your guess? ")
    guess = stdio.readInt()
    if guess < secret:
        stdio.writeln("Too low")
    elif guess > secret:
        stdio.writeln("Too high")
    else:
        stdio.writeln("You win!")
