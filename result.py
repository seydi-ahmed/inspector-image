from stegano import lsb

# Attempt to extract hidden message using LSB steganography
try:
    # Extract hidden message using LSB method
    hidden_message = lsb.reveal(image_path)
except Exception as e:
    hidden_message = f"Error while extracting hidden message: {e}"

hidden_message
