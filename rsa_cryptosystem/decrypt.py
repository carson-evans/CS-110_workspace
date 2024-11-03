# decrypt.py
import rsa
import stdio
import sys
from rsa_cryptosystem.rsa import decrypt


# Entry point.
def main():
    """
    Main function to decrypt a message using RSA private key.
    Accepts private-key n (int) and d (int) as cla.
    Decrypts each fixed-width binary and outputs the original message.
    """

    # QA
    if len(sys.argv) != 3:
        return

    try:
        n = int(sys.argv[1])
        d = int(sys.argv[2])
    except ValueError:
        return

    # determine the num of bits (width) needed to encode n
    width = rsa.bitLength(n)

    # Read the encrypted message from stdin
    encrypted_message = stdio.readString()

    # Decrypt each fixed-width binary segment in message
    for i in range(0, len(encrypted_message), width):
        # Extract substring of length width
        s = encrypted_message[i: i + width]

        # Convert binary string to int
        y = rsa.bin2dec(s)

        # Decrypt using RSA
        decrypted_value = rsa.decrypt(y, n, d)

        # Convert decrypted int to chr
        stdio.write(chr(decrypted_value))

    stdio.writeln()


if __name__ == "__main__":
    main()
