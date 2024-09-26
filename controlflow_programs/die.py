import stdio
import stdrandom

...

roll = stdrandom.uniformInt(1, 6)

if roll == 1:
    stdio.writeln("     ")
    stdio.writeln("  *  ")
    stdio.writeln("     ")

if roll == 2:
    stdio.writeln("*    ")
    stdio.writeln("     ")
    stdio.writeln("    *")

if roll == 3:
    stdio.writeln("*    ")
    stdio.writeln("  *  ")
    stdio.writeln("    *")

if roll == 4:
    stdio.writeln("*   *")
    stdio.writeln("     ")
    stdio.writeln("*   *")

if roll == 5:
    stdio.writeln("*   *")
    stdio.writeln("  *  ")
    stdio.writeln("*   *")

if roll == 6:
    stdio.writeln("*   *")
    stdio.writeln("*   *")
    stdio.writeln("*   *")