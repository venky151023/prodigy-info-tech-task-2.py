from PIL import Image
import numpy as np

def encrypt_image(input_path, output_path, key):
    # Load image
    img = Image.open(input_path)
    arr = np.array(img)
    
    # Apply XOR operation with key
    encrypted_arr = arr ^ key
    
    # Save encrypted image
    encrypted_img = Image.fromarray(encrypted_arr.astype('uint8'))
    encrypted_img.save(output_path)
    print("Image encrypted successfully!")

def decrypt_image(input_path, output_path, key):
    # Load encrypted image
    img = Image.open(input_path)
    arr = np.array(img)
    
    # Reverse XOR with same key
    decrypted_arr = arr ^ key
    
    # Save decrypted image
    decrypted_img = Image.fromarray(decrypted_arr.astype('uint8'))
    decrypted_img.save(output_path)
    print("Image decrypted successfully!")


# Example usage
key = 123  # Secret key for XOR
encrypt_image("input.jpg", "encrypted.png", key)
decrypt_image("encrypted.png", "decrypted.png", key)
