# encrypt.py
import rsa
import sys

def main():
    # Verify command-line arguments
    if len(sys.argv) != 3:
        sys.exit("Usage: python3 encrypt.py n e")

    try:
        n = int(sys.argv[1])
        e = int(sys.argv[2])
    except ValueError:
        sys.exit("n and e must be integers")

    # Determine the number of bits
    width = rsa.bitLength(n)

    # Read message to encrypt from stdin
    message = sys.stdin.read()

    # Encrypt each character
    encrypted_message = ""
    for c in message:
        # Convert character to integer
        x = ord(c)

        # Encrypt the integer using RSA
        encrypted_value = rsa.encrypt(x, n, e)

        # Convert encrypted value to a fixed-width binary string
        binary_string = rsa.dec2bin(encrypted_value, width)
        encrypted_message += binary_string

    # Write the encrypted message to stdout without adding a newline
    sys.stdout.write(encrypted_message)

if __name__ == "__main__":
    main()
