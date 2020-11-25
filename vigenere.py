"""Author: Amzuloiu Andrei-Ciprian"""
import regex as re

"""Clean the message of any character that is not letter"""
def clean(message):
    clean_message = message.upper()
    clean_message = re.sub("[^A-Z]", '', clean_message)
    
    return clean_message

"""Process the key to the required size"""
def process_key(key, size):
    longKey = key.upper()

    while size > len(longKey):
        longKey += longKey

    longKey = longKey[:size]

    return longKey 

"""Encrypt the message using the given key"""
def encrypt(message, key):
    clean_message = clean(message)
    longKey = process_key(key, len(clean_message))
    result = ""
    
    for i_mes, i_key in zip(clean_message, longKey):
        result += chr(((ord(i_mes) + ord(i_key) - ord('A')) % ord('A')) % 26 + ord('A'))

    return result

"""Decrypt the message using the given key"""
def decrypt(message, key):
    clean_message = clean(message)
    longKey = process_key(key, len(clean_message))
    result = ""
    
    for i_mes, i_key in zip(clean_message, longKey):
        result += chr(((ord(i_mes) - ord(i_key) + ord('A') + 26) % ord('A')) % 26 + ord('A'))

    return result