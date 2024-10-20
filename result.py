from stegano import lsb

image_path = "image.jpeg"

# Attempt to extract hidden message using LSB steganography
try:
    # Extract hidden message using LSB method
    hidden_message = lsb.reveal(image_path)
    if hidden_message:
        print(f"Hidden message: {hidden_message}")
    else:
        print("No hidden message found.")
except Exception as e:
    print(f"Error while extracting hidden message: {e}")
