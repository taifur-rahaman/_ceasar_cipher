
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def shifting(shifted_index):
    if shifted_index > len(alphabet):
        shifted_index = abs(shifted_index - len(alphabet))


def encrypt(text, shift):
    encrypted_char = []
    for char in text:
        shifted_index = alphabet.index(char) + shift
        shifting(shifted_index)
        encrypted_char.append(alphabet[shifted_index])
    return ''.join(encrypted_char)


def decrypt(text, shift):
    decrypted_char = []
    for char in text:
        shifted_index = alphabet.index(char) - shift
        shifting(shifted_index)
        decrypted_char.append(alphabet[shifted_index])
    return ''.join(decrypted_char)


while True:
    choice = int(input(
        "What would you like to do?\n1. Encrypt\n2. Decrypt\n0. Quit\nEnter your choice: "))

    if choice == 1:
        text = input("Enter the text to encrypt: ").lower()
        shift = int(input("Enter the shift: "))
        encrypted_text = encrypt(text, shift)
        print(f"Your encrypted text is '{encrypted_text}'")

    elif choice == 2:
        text = input("Enter the text to decrypt: ").lower()
        shift = int(input("Enter the shift: "))
        decrypted_text = decrypt(text, shift)
        print(f"Your decrypted text is '{decrypted_text}'")

    elif choice == 0:
        print("Thank you for Using Ceasar Chipher")
        exit()

    else:
        print("INVALID choice. Please try again")
        continue
