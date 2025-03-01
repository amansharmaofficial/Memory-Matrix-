import cv2
import pickle

def decrypt_image():
    # Read the encrypted image
    img_path = input("Enter encrypted image path: ")
    img = cv2.imread(img_path)
    
    if img is None:
        print(f"Error: Could not read image at {img_path}")
        return
    
    # Load metadata
    try:
        with open('metadata.pickle', 'rb') as f:
            metadata = pickle.load(f)
    except FileNotFoundError:
        print("Error: metadata.pickle file not found. This file is required for decryption.")
        return
    
    # Get message length and stored password from metadata
    msg_length = metadata['msg_length']
    stored_password = metadata['password']
    
    # Ask for password
    password = input("Enter passcode for Decryption: ")
    
    # Create ASCII to character mapping
    c = {}
    for i in range(255):
        c[i] = chr(i)
    
    # Check password
    if password == stored_password:
        # Extract message
        message = ""
        n = 0
        m = 0
        z = 0
        
        for i in range(msg_length):
            message = message + c[img[n, m, z]]
            n = n + 1
            m = m + 1
            z = (z + 1) % 3
        
        print("Decrypted message:", message)
    else:
        print("YOU ARE NOT AUTHORIZED")

if __name__ == "__main__":
    decrypt_image()