# prodigy-info-tech-task-2.py
Pixel Manipulation for Image Encryption 🔒🖼️
📌 Overview

This project demonstrates image encryption and decryption usingpixel manipulation techniques.
The goal is to secure images by altering pixel values through mathematical operations (e.g., XOR, addition, subtraction, swapping).

Users can:

Encrypt an image with a secret key.

Decrypt the encrypted image using the same key to restore the original.

🚀 Features

Simple XOR-based pixel manipulation.

Fully reversible encryption and decryption.

Works with common image formats (JPG, PNG, BMP).

Extendable with different operations like:

Swapping pixel values

Adding/subtracting constants

Random scrambling

🛠️ Requirements

Install dependencies using pip:

pip install pillow numpy

📂 Project Structure
📦 image-encryption
 ┣ 📜 encrypt.py      # Main encryption & decryption code
 ┣ 📜 README.md       # Project documentation
 ┣ 📜 sample.jpg      # Sample input image
 ┣ 📜 encrypted.png   # Encrypted image (output)
 ┗ 📜 decrypted.png   # Decrypted image (output)

💻 Usage
1. Encryption
from encrypt import encrypt_image

key = 123  # Secret key
encrypt_image("sample.jpg", "encrypted.png", key)

2. Decryption
from encrypt import decrypt_image

key = 123  # Same key used in encryption
decrypt_image("encrypted.png", "decrypted.png", key)

🔑 How It Works

Each pixel in an image is represented by values (0–255).

A secret key is applied using XOR or other operations.

To decrypt, apply the same key to restore the original.

Example:

Original Pixel:  150
Key:             123
Encrypted Pixel: 150 ^ 123 = 233
Decrypted Pixel: 233 ^ 123 = 150

⚡ Future Improvements

Add pixel shuffling for stronger encryption.

Build a GUI (Tkinter / PyQt) for user-friendly interaction.

Support batch encryption for multiple images.

Allow users to choose different encryption algorithms.

📷 Example

Input → Encrypted → Decrypted
