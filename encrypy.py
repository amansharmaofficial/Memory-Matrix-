import cv2
import os
import pickle

def encrypt_image():
    # Read the image
    img_path = input("Enter image path: ")
    img = cv2.imread(img_path)
    
    if img is None:
        print(f"Error: Could not read image at {img_path}")
        return
    
    # Get message and password
    msg = input("Enter secret message: ")
    password = input("Enter a passcode: ")
    
    # Create character to ASCII mapping
    d = {}
    for i in range(255):
        d[chr(i)] = i
    
    # Embed message in image
    n = 0
    m = 0
    z = 0
    
    for i in range(len(msg)):
        img[n, m, z] = d[msg[i]]
        n = n + 1
        m = m + 1
        z = (z + 1) % 3
    
    # Save metadata (message length and password) for decryption
    metadata = {
        'msg_length': len(msg),
        'password': password
    }
    
    # Save encrypted image
    encrypted_path = "encryptedImage.jpg"
    cv2.imwrite(encrypted_path, img)
    
    # Save metadata file
    with open('metadata.pickle', 'wb') as f:
        pickle.dump(metadata, f)
    
    print(f"Encryption successful. Image saved as {encrypted_path}")
    print("Remember to keep metadata.pickle file for decryption")
    
    # Open the image (Windows specific)
    os.system("start encryptedImage.jpg")

if __name__ == "__main__":
    encrypt_image()