#!/usr/bin/env python3

"""
Usage: %(script_name)s [-v] <.marv file>

This program serves as an emulator for a register-based machine called Marvin (named after
the paranoid android character, Marvin, from The Hitchhiker's Guide to the Galaxy by 
Douglas Adams). The design of the machine was inspired by that of the Harvey Mudd 
Miniature Machine (HMMM) developed at Harvey Mudd College. The program accepts a .marv file 
as input, assembles and simulates the instructions within, and prints any output to stdout. 
Any input to the .marv program is via stdin. If the optional -v argument is specified, 
the emulator prints the assembled instructions to stdout before simulating them.
"""

import os, sys

# Maps opcodes to their binary 8-bit codes.
opcode2bin = {"halt": "00000000", "read": "00000001", "write": "00000010", "nop": "00000011",
              "set0": "00000100", "set1": "00000101", "setn": "00000110", "addn": "00000111",
              "copy": "00001000", "neg": "00001001", "add": "00001010", "sub": "00001011",
              "mul": "00001100", "div": "00001101", "mod": "00001110", "jumpn": "00001111",
              "jumpr": "00010000", "jeqzn": "00010001", "jnezn": "00010010", "jgen": "00010011",
              "jlen": "00010110", "jeqn": "00010100", "jnen": "00010101", "jgtn": "00010111",
              "jltn": "00011000", "calln": "00011001", "pushr": "00011010", "popr": "00011011",
              "loadn": "00011100", "storen": "00011101", "loadr": "00011110", "storer": "00011111"}

# Maps 8-bit binary codes to the opcodes they represent.
bin2opcode = {opcode2bin[opcode]: opcode for opcode in opcode2bin.keys()}

# Maps register names to their binary 4-bit codes.
reg2bin = {"r0": "0000", "r1": "0001", "r2": "0010", "r3": "0011", "r4": "0100", "r5": "0101",
           "r6": "0110", "r7": "0111", "r8": "1000", "r9": "1001", "r10": "1010", "r11": "1011",
           "r12": "1100", "r13": "1101", "r14": "1110", "r15": "1111"}


def main(argv):
    verbose = False
    inFile = None

    # Process command-line inputs and exit if they are not as expected.
    if len(argv) == 2:
        inFile = argv[1]
    elif len(argv) == 3:
        if argv[1] != "-v":
            sys.exit("Error: unkown argument %s\n" % (argv[1]) + \
                     __doc__ % {"script_name": argv[0].split("/")[-1]})
        verbose = argv[1] == "-v"
        inFile = argv[2]
    else:
        sys.exit(__doc__ % {"script_name": argv[0].split("/")[-1]})
    if not inFile.endswith(".marv") or not os.path.exists(inFile):
        sys.exit("Error: invalid file '%s'\n" % (inFile) + \
                 __doc__ % {"script_name": argv[0].split("/")[-1]})

    fh = open(inFile, "r")
    lines = fh.readlines()
    expectedID = 0
    tuples = []
    for i, line in enumerate(lines):
        lineno = i + 1
        line = line.strip()
        # Ignore if line is empty or is a comment.
        if line == "" or line.startswith("#"):
            continue

        # Remove inlined comment if any.
        if "#" in line:
            line = line[:line.rfind("#")].strip()

        # Exit with error if number of tokens in line is less than 2, or if the instruction ID is
        # invalid, or if the instruction is invalid.
        toks = line.split()
        if len(toks) < 2:
            sys.exit("Error %s@%d: not enough tokens" % (inFile, lineno))
        if not isNum(toks[0]) or int(toks[0]) != expectedID:
            sys.exit("Error %s@%d: invalid instruction ID '%s'" % (inFile, lineno, toks[0]))
        if toks[1] not in opcode2bin:
            sys.exit("Error %s@%d: invalid instruction '%s'" % (inFile, lineno, toks[1]))
        expectedID += 1

        # Validate the instruction arguments.
        ID, opcode, args = int(toks[0]), toks[1], toks[2:]
        if opcode in {"halt", "nop"}:
            if len(args) != 0:
                sys.exit("Error %s@%d: '%s' expects 0 arguments" % (inFile, lineno, opcode))
            tuples.append((lineno, ID, opcode))
        elif opcode in {"jumpr", "read", "set0", "set1", "write"}:
            if len(args) != 1:
                sys.exit("Error %s@%d: '%s' expects 1 argument, rX" % (inFile, lineno, opcode))
            if not validReg(toks[2]):
                sys.exit("Error %s@%d: invalid register '%s'" % (inFile, lineno, toks[2]))
            tuples.append((lineno, ID, opcode, toks[2]))
        elif opcode in {"jumpn"}:
            if len(args) != 1:
                sys.exit("Error %s@%d: '%s' expects 1 argument, N" % (inFile, lineno, opcode))
            if not isNum(toks[2]):
                sys.exit("Error %s@%d: invalid number '%s'" % (inFile, lineno, toks[2]))
            tuples.append((lineno, ID, opcode, int(toks[2])))
        elif opcode in {"copy", "loadr", "neg", "popr", "pushr", "storer"}:
            if len(args) != 2:
                sys.exit("Error %s@%d: '%s' expects 2 arguments, rX rY" % (inFile, lineno, toks[1]))
            if not validReg(toks[2]):
                sys.exit("Error %s@%d: invalid register '%s'" % (inFile, lineno, toks[2]))
            if not validReg(toks[3]):
                sys.exit("Error %s@%d: invalid register '%s'" % (inFile, lineno, toks[3]))
            tuples.append((lineno, ID, opcode, toks[2], toks[3]))
        elif opcode in {"addn", "calln", "jeqzn", "jnezn", "loadn", "setn", "storen"}:
            if len(args) != 2:
                sys.exit("Error %s@%d: '%s' expects 2 arguments, rX N" % (inFile, lineno, toks[1]))
            if not validReg(toks[2]):
                sys.exit("Error %s@%d: invalid register '%s'" % (inFile, lineno, toks[2]))
            if not isNum(toks[3]):
                sys.exit("Error %s@%d: invalid number '%s'" % (inFile, lineno, toks[3]))
            tuples.append((lineno, ID, opcode, toks[2], int(toks[3])))
        elif opcode in {"add", "div", "mod", "mul", "sub"}:
            if len(args) != 3:
                sys.exit("Error %s@%d: '%s' expects 3 arguments, rX rY rZ" \
                         % (inFile, lineno, toks[1]))
            if not validReg(toks[2]):
                sys.exit("Error %s@%d: invalid register '%s'" % (inFile, lineno, toks[2]))
            if not validReg(toks[3]):
                sys.exit("Error %s@%d: invalid register '%s'" % (inFile, lineno, toks[3]))
            if not validReg(toks[4]):
                sys.exit("Error %s@%d: invalid register '%s'" % (inFile, lineno, toks[4]))
            tuples.append((lineno, ID, opcode, toks[2], toks[3], toks[4]))
        elif opcode in {"jeqn", "jgen", "jgtn", "jlen", "jltn", "jnen"}:
            if len(args) != 3:
                sys.exit("Error %s@%d: '%s' expects 3 arguments, rX rY N" \
                         % (inFile, lineno, toks[1]))
            if not validReg(toks[2]):
                sys.exit("Error %s@%d: invalid register '%s'" % (inFile, lineno, toks[2]))
            if not validReg(toks[3]):
                sys.exit("Error %s@%d: invalid register '%s'" % (inFile, lineno, toks[3]))
            if not isNum(toks[4]):
                sys.exit("Error %s@%d: invalid number '%s'" % (inFile, lineno, toks[4]))
            tuples.append((lineno, ID, opcode, toks[2], toks[3], int(toks[4])))

    # Additional validation of instruction arguments.
    for tuple in tuples:
        lineno, ID, opcode, args = tuple[0], tuple[1], tuple[2], tuple[3:]
        if opcode in {"jumpn"} and args[0] >= len(tuples):
            sys.exit("Error %s@%d: invalid instruction address '%s'" % (inFile, lineno, args[0]))
        elif opcode in {"addn", "setn"} and not validNum(args[1]):
            sys.exit("Error %s@%d: invalid number '%s'" % (inFile, lineno, args[1]))
        elif opcode in {"loadn", "storen"} and not validAddr(args[1]):
            sys.exit("Error %s@%d: invalid address '%s'" % (inFile, lineno, args[1]))
        elif opcode in {"calln", "jeqzn", "jnezn"} and args[1] >= len(tuples):
            sys.exit("Error %s@%d: invalid instruction address '%s'" % (inFile, lineno, args[1]))
        elif opcode in {"jeqn", "jgen", "jgtn", "jlen", "jltn", "jnen"} and args[2] >= len(tuples):
            sys.exit("Error %s@%d: invalid instruction address '%s'" % (inFile, lineno, args[2]))

    # Assemble the instructions into machine codes.
    machineCodes = assemble(tuples, verbose)

    # Simulate the machine codes.
    if len(machineCodes) > 0:
        simulate(machineCodes)


# Assembles the instructions in tuples and returns a list containing the corresponding machine
# codes. Prints the assembled instructions to stdout if verbose is True.
def assemble(tuples, verbose):
    machineCodes, verboseOutput = [], []
    for tuple in tuples:
        ID, opcode, args = tuple[1], tuple[2], tuple[3:]
        bArg1, bArg2, bArg3 = "", "", ""
        aArg1, aArg2, aArg3 = "", "", ""

        if opcode in {"halt", "nop"}:
            bArg1, bArg2, bArg3 = "00000000", "00000000", "00000000"
        elif opcode in {"jumpr", "read", "set0", "set1", "write"}:
            bArg1, bArg2, bArg3 = "00000000", "00000000", "0000" + reg2bin[args[0]]
            aArg1 = args[0]
        elif opcode in {"jumpn"}:
            s = format(args[0], "016b")
            bArg1, bArg2, bArg3 = "00000000", s[:8], s[8:]
            aArg1 = args[0]
        elif opcode in {"copy", "loadr", "neg", "popr", "pushr", "storer"}:
            bArg1, bArg2, bArg3 = "00000000", "00000000", reg2bin[args[0]] + reg2bin[args[1]]
            aArg1, aArg2 = args[0], args[1]
        elif opcode in {"addn", "setn"}:
            bArg1 = "0000" + reg2bin[args[0]]
            s = format(args[1], "016b").replace("-", "1")  # msb(s) is 1 if args[1] < 0
            bArg2, bArg3 = s[:8], s[8:]
            aArg1, aArg2 = args[0], args[1]
        elif opcode in {"calln", "jeqzn", "jnezn", "loadn", "storen"}:
            bArg1 = "0000" + reg2bin[args[0]]
            s = format(args[1], "016b")
            bArg2, bArg3 = s[:8], s[8:]
            aArg1, aArg2 = args[0], args[1]
        elif opcode in {"add", "div", "mod", "mul", "sub"}:
            bArg1, bArg2, bArg3 = \
                "00000000", "0000" + reg2bin[args[0]], reg2bin[args[1]] + reg2bin[args[2]]
            aArg1, aArg2, aArg3 = args[0], args[1], args[2]
        elif opcode in {"jeqn", "jgen", "jgtn", "jlen", "jltn", "jnen"}:
            bArg1 = reg2bin[args[0]] + reg2bin[args[1]]
            s = format(args[2], "016b")
            bArg2, bArg3 = s[:8], s[8:]
            aArg1, aArg2, aArg3 = args[0], args[1], args[2]

        op = opcode2bin[opcode]
        code = int(op, 2) << 24 | int(bArg1, 2) << 16 | int(bArg2, 2) << 8 | int(bArg3, 2)
        machineCodes.append(code)

        binCode = "%5s: %s %s %s %s" % (ID, opcode2bin[opcode], bArg1, bArg2, bArg3)
        asmCode = "%5s: %-6s %s %s %s" % (ID, opcode, aArg1, aArg2, aArg3)
        verboseOutput.append("%-50s        %s" % (binCode, asmCode))

    if verbose:
        for s in verboseOutput:
            print(s)
        print()

    return machineCodes


# Simulate the assembled instructions in machineCodes.
def simulate(machineCodes):
    reg = [0] * 16  # registers
    mem = [0] * 65536  # main memory
    pc = 0  # program counter
    ir = 0  # instruction register

    # Initialize the frame and stack pointers to 8192 (the base address of the stack).
    reg[14], reg[15] = 8192, 8192

    # Load the machine codes into memory starting at location 0.
    for i, v in enumerate(machineCodes):
        mem[i] = v

    while True:
        # Fetch the next instruction to simulate.
        try:
            ir = machineCodes[pc]
        except IndexError as e:
            sys.exit("Error: attempted to execute mem['%d']; halting the machine" % (pc))

        # Extract the opcode.
        code = format(ir, "032b")
        op = format(int(code[0:8], 2), "08b")
        opcode = bin2opcode[op]

        # Simulation the instruction given by opcode.

        # halt
        if opcode == "halt":
            break
        # read
        elif opcode == "read":
            arg1 = int(code[28:], 2)
            x = None
            while True:
                try:
                    x = int(input())
                    break
                except ValueError as e:
                    print("Illegal input: number must be in [-32768, 32767]")
            reg[arg1] = x
            pc += 1
        # write
        elif opcode == "write":
            arg1 = int(code[28:], 2)
            print(reg[arg1])
            pc += 1
        # nop
        elif opcode == "nop":
            pc += 1
            continue
        # set0
        elif opcode == "set0":
            arg1 = int(code[28:], 2)
            reg[arg1] = 0
            pc += 1
        # set1
        elif opcode == "set1":
            arg1 = int(code[28:], 2)
            reg[arg1] = 1
            pc += 1
        # jumpr
        elif opcode == "jumpr":
            arg1 = int(code[28:], 2)
            pc = reg[arg1]
        # jumpn
        elif opcode == "jumpn":
            arg1 = int(code[16:], 2)
            pc = arg1
        # copy
        elif opcode == "copy":
            arg1 = int(code[24:28], 2)
            arg2 = int(code[28:], 2)
            reg[arg1] = reg[arg2]
            pc += 1
        # loadr
        elif opcode == "loadr":
            arg1 = int(code[24:28], 2)
            arg2 = int(code[28:], 2)
            reg[arg1] = mem[reg[arg2]]
            pc += 1
        # neg
        elif opcode == "neg":
            arg1 = int(code[24:28], 2)
            arg2 = int(code[28:], 2)
            reg[arg1] = -reg[arg2]
            pc += 1
        # popr
        elif opcode == "popr":
            arg1 = int(code[24:28], 2)
            arg2 = int(code[28:], 2)
            reg[arg2] -= 1
            reg[arg1] = mem[reg[arg2]]
            pc += 1
        # pushr
        elif opcode == "pushr":
            arg1 = int(code[24:28], 2)
            arg2 = int(code[28:], 2)
            mem[reg[arg2]] = reg[arg1]
            reg[arg2] += 1
            pc += 1
        # storer
        elif opcode == "storer":
            arg1 = int(code[24:28], 2)
            arg2 = int(code[28:], 2)
            mem[reg[arg2]] = reg[arg1]
            pc += 1
        # addn
        elif opcode == "addn":
            arg1 = int(code[12:16], 2)
            arg2, arg2sign = code[16:], 1
            if arg2.startswith("1"):
                arg2 = "0" + arg2[1:]
                arg2sign = -1
            arg2 = arg2sign * int(arg2, 2)
            reg[arg1] += arg2
            pc += 1
        # calln
        elif opcode == "calln":
            arg1 = int(code[12:16], 2)
            arg2 = int(code[16:], 2)
            reg[arg1] = pc + 1
            pc = arg2
        # jeqzn
        elif opcode == "jeqzn":
            arg1 = int(code[12:16], 2)
            arg2 = int(code[16:], 2)
            pc = arg2 if reg[arg1] == 0 else pc + 1
        # jnezn
        elif opcode == "jnezn":
            arg1 = int(code[12:16], 2)
            arg2 = int(code[16:], 2)
            pc = arg2 if reg[arg1] != 0 else pc + 1
        # loadn
        elif opcode == "loadn":
            arg1 = int(code[12:16], 2)
            arg2 = int(code[16:], 2)
            reg[arg1] = mem[arg2]
            pc += 1
        # setn
        elif opcode == "setn":
            arg1 = int(code[12:16], 2)
            arg2, arg2sign = code[16:], 1
            if arg2.startswith("1"):
                arg2 = "0" + arg2[1:]
                arg2sign = -1
            arg2 = arg2sign * int(arg2, 2)
            reg[arg1] = arg2
            pc += 1
        # storen
        elif opcode == "storen":
            arg1 = int(code[12:16], 2)
            arg2 = int(code[16:], 2)
            mem[arg2] = reg[arg1]
            pc += 1
        # add
        elif opcode == "add":
            arg1 = int(code[20:24], 2)
            arg2 = int(code[24:28], 2)
            arg3 = int(code[28:], 2)
            reg[arg1] = reg[arg2] + reg[arg3]
            pc += 1
        # div
        elif opcode == "div":
            arg1 = int(code[20:24], 2)
            arg2 = int(code[24:28], 2)
            arg3 = int(code[28:], 2)
            reg[arg1] = reg[arg2] // reg[arg3]
            pc += 1
        # mod
        elif opcode == "mod":
            arg1 = int(code[20:24], 2)
            arg2 = int(code[24:28], 2)
            arg3 = int(code[28:], 2)
            reg[arg1] = reg[arg2] % reg[arg3]
            pc += 1
        # mul
        elif opcode == "mul":
            arg1 = int(code[20:24], 2)
            arg2 = int(code[24:28], 2)
            arg3 = int(code[28:], 2)
            reg[arg1] = reg[arg2] * reg[arg3]
            pc += 1
        # sub
        elif opcode == "sub":
            arg1 = int(code[20:24], 2)
            arg2 = int(code[24:28], 2)
            arg3 = int(code[28:], 2)
            reg[arg1] = reg[arg2] - reg[arg3]
            pc += 1
        # jeqn
        elif opcode == "jeqn":
            arg1 = int(code[8:12], 2)
            arg2 = int(code[12:16], 2)
            arg3 = int(code[16:], 2)
            pc = arg3 if reg[arg1] == reg[arg2] else pc + 1
        # jgen
        elif opcode == "jgen":
            arg1 = int(code[8:12], 2)
            arg2 = int(code[12:16], 2)
            arg3 = int(code[16:], 2)
            pc = arg3 if reg[arg1] >= reg[arg2] else pc + 1
        # jgtn
        elif opcode == "jgtn":
            arg1 = int(code[8:12], 2)
            arg2 = int(code[12:16], 2)
            arg3 = int(code[16:], 2)
            pc = arg3 if reg[arg1] > reg[arg2] else pc + 1
        # jlen
        elif opcode == "jlen":
            arg1 = int(code[8:12], 2)
            arg2 = int(code[12:16], 2)
            arg3 = int(code[16:], 2)
            pc = arg3 if reg[arg1] <= reg[arg2] else pc + 1
        # jltn
        elif opcode == "jltn":
            arg1 = int(code[8:12], 2)
            arg2 = int(code[12:16], 2)
            arg3 = int(code[16:], 2)
            pc = arg3 if reg[arg1] < reg[arg2] else pc + 1
        # jnen
        elif opcode == "jnen":
            arg1 = int(code[8:12], 2)
            arg2 = int(code[12:16], 2)
            arg3 = int(code[16:], 2)
            pc = arg3 if reg[arg1] != reg[arg2] else pc + 1


# Returns True if s encodes an integer, and False otherwise.
def isNum(s):
    ans = True
    try:
        x = int(s)
    except ValueError as e:
        ans = False
    return ans


# Return True if n is a valid signed 16-bit integer, and False otherwise.
def validNum(n):
    return -2 ** 15 <= n <= 2 ** 15 - 1


# Return True if s is "r" followed by a number from the interval [0, 15], and False otherwise.
def validReg(s):
    return s in {"r" + str(i) for i in range(16)}


# Return True if n is a valid unsigned 16-bit integer, and False otherwise.
def validAddr(n):
    return 0 <= n <= 2 ** 16 - 1


if __name__ == "__main__":
    main(sys.argv)
