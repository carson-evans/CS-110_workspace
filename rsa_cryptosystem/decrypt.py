# decrypt.py
import rsa
import sys

def main():
    # Verify command-line arguments
    if len(sys.argv) != 3:
        sys.exit("Usage: python3 decrypt.py n d")

    try:
        n = int(sys.argv[1])
        d = int(sys.argv[2])
    except ValueError:
        sys.exit("n and d must be integers")

    # Determine the number of bits (width) needed to encode n
    width = rsa.bitLength(n)

    # Read the encrypted message from stdin
    encrypted_message = sys.stdin.read()

    # Remove any trailing newline or whitespace characters
    encrypted_message = encrypted_message.strip()

    # Decrypt each fixed-width binary segment in the message
    decrypted_message = ""
    for i in range(0, len(encrypted_message), width):
        # Extract substring of length width
        s = encrypted_message[i: i + width]

        # If the length of s is less than width, skip it
        if len(s) < width:
            continue

        # Convert binary string to int
        y = rsa.bin2dec(s)

        # Decrypt using RSA
        decrypted_value = rsa.decrypt(y, n, d)

        # Convert decrypted int to character
        decrypted_message += chr(decrypted_value)

    # Write the decrypted message to stdout
    print(decrypted_message)

if __name__ == "__main__":
    main()
