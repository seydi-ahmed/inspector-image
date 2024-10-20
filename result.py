import sys
from stegano import lsb

# Vérifie les arguments fournis
if len(sys.argv) < 3:
    print("Usage: python3 result.py -steg <image_path>")
    sys.exit(1)

# Vérifie le type d'argument fourni
option = sys.argv[1]
image_path = sys.argv[2]

if option == "-steg":
    # Attempt with different bit depths
    for bits in range(1, 9):  # Try from 1 to 8 bits
        try:
            hidden_message = lsb.reveal(image_path, shift=bits)
            if hidden_message:
                print(f"Hidden message found with {bits} bit(s):")
                print(hidden_message)
                break
        except Exception as e:
            print(f"Failed to extract with {bits} bit(s): {e}")

else:
    print("Invalid option. Use -steg to extract hidden messages.")
