import pandas as pd
import numpy as np
from cryptography.fernet import Fernet

class UserProfile:
    def __init__(self, keyboard_file="processed_data/keyboard_data_clean.csv", 
                 mouse_file="processed_data/mouse_data_clean.csv"):
        self.keyboard_file = keyboard_file
        self.mouse_file = mouse_file
        self.key = Fernet.generate_key()
        self.cipher = Fernet(self.key)

    def encrypt_data(self, data):
        return self.cipher.encrypt(data.encode())

    def decrypt_data(self, encrypted_data):
        return self.cipher.decrypt(encrypted_data).decode()
