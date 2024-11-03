# encrypt.py
import rsa
import stdio
import sys

# Entry point.
def main():
    """
    Main function to encrypt a message using RSA public key.
    Accepts public-key n (int) and e (int) as cla.
    Encrypts each character in the message and outputs fixed-width binary string.
    """

    # QA
    if len(sys.argv) != 3:
        return

    try:
        n = int(sys.argv[1])
        e = int(sys.argv[2])
    except ValueError:
        return

    # Determine the number of bits
    width = rsa.bitLength(n)

    # Read message to encrypt from stdin
    message = stdio.readString()

    # Encrypt each character
    for c in message:
        # Convert character to integer
        x = ord(c)

        # Encrypt the integer using RSA
        encrypted_value = rsa.encrypt(x, n, e)

        # Convert encrypted value to a fixed-width
        binary_string = rsa.dec2bin(encrypted_value, width)
        stdio.write(binary_string)

    stdio.writeln()

if __name__ == "__main__":
    main()
