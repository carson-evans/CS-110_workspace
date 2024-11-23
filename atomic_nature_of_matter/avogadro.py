import math
import stdio

# Entry point.
def main():
    # Initialize constants
    ETA = 9.135e-4      # Viscosity of water in N*s/m^2
    RHO = 0.5e-6        # Radius of bead in meters
    T = 297             # Temperature in Kelvin
    R = 8.31457         # Universal gas constant in J/(mol*K)
    PIXEL_TO_METER = 0.175e-6  # Conversion factor from pixels to meters

    # Read displacements from standard input
    displacements = []
    while not stdio.isEmpty():
        displacement = stdio.readFloat()
        # Convert from pixels to meters
        displacement *= PIXEL_TO_METER
        displacements.append(displacement)

    n = len(displacements)
    if n == 0:
        stdio.writeln("No displacements read.")
        return

    # Calculate var as sum of squares of displacements
    var = sum(d ** 2 for d in displacements) / (2 * n)

    # Estimate Boltzmann's constant k
    k = (6 * math.pi * ETA * RHO * var) / T

    # Estimate Avogadro's constant NA
    NA = R / k

    # Write to standard output the Avogadro constant in scientific notation
    stdio.writef("%e\n", NA)

if __name__ == "__main__":
    main()
