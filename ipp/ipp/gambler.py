# Accepts stake (int), goal (int), and trials (int) as command-line arguments; runs trials
# experiments (dollar bets) that start with stake dollars and terminate on 0 dollars or goal; and
# writes the percentage of wins and the average number of bets per experiment to standard output.

import stdio
import sys
import stdrandom

stake = int(sys.argv[1])
goal = int(sys.argv[2])
trials = int(sys.argv[3])
bets = 0
wins = 0
for t in range(trials):
    cash = stake
    while cash > 0 and cash < goal:
        bets += 1
        cash += 1 if stdrandom.bernoulli() else -1
    wins += 1 if cash == goal else 0
stdio.writeln(str(100 * wins // trials) + "% wins")
stdio.writeln("Avg # bets: " + str(bets // trials))
