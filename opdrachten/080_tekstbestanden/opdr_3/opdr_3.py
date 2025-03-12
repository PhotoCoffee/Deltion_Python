# Opdracht 3 Tekst opslaan
# Naam student:
# Groep:

def encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            shift_amount = shift % 26
            new_char = chr((ord(char) - ord('a') + shift_amount) % 26 + ord('a')) if char.islower() else chr((ord(char) - ord('A') + shift_amount) % 26 + ord('A'))
            encrypted_text += new_char
        else:
            encrypted_text += char
    return encrypted_text

def decrypt(text, shift):
    return encrypt(text, -shift)

if __name__ == "__main__":
    text_to_encrypt = input("Geef de tekst die wilt encrypten: ")
    shift = 5
    encrypted_text = encrypt(text_to_encrypt, shift)
    print(f"Encrypted text: {encrypted_text}")
    decrypted_text = decrypt(encrypted_text, shift)
    print(f"Decrypted text: {decrypted_text}")