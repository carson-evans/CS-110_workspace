# Accepts dna (str) as command-line argument; and writes to standard output whether dna
# corresponds to a potential gene or not.

import stdio
import sys


# Entry point.
def main():
    dna = sys.argv[1]
    stdio.writeln(_isPotentialGene(dna))


# Returns True if dna corresponds to a potential gene, and False otherwise.
def _isPotentialGene(dna):
    ATG, TAA, TAG, TGA = "ATG", "TAA", "TAG", "TGA"
    if len(dna) % 3 != 0:
        return False
    if not dna.startswith(ATG):
        return False
    for i in range(len(dna) - 3):
        if i % 3 == 0:
            codon = dna[i:i + 3]
            if codon == TAA or codon == TAG or codon == TGA:
                return False
    return dna.endswith(TAA) or dna.endswith(TAG) or dna.endswith(TGA)


if __name__ == "__main__":
    main()
