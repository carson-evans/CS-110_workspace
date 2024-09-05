# Accepts a name as command-line argument; and writes a message containing that name to standard
# output.

import stdio
import sys

stdio.write("Hi, ")
stdio.write(sys.argv[1])
stdio.writeln(". How are you?")
