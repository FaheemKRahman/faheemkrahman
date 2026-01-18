import string
from collections import Counter


# Frequency of english letters

ENGLISH_FREQS= { 
    'E': 12.7, 'T': 9.1, 'A': 8.2, 'O': 7.5, 'I': 7.0, 'N': 6.7,
    'S': 6.3, 'H': 6.1, 'R': 6.0, 'D': 4.3, 'L': 4.0,
    'C': 2.8, 'U': 2.8, 'M': 2.4, 'W': 2.4, 'F': 2.2,
    'G': 2.0, 'Y': 2.0, 'P': 1.9, 'B': 1.5, 'V': 1.0,
    'K': 0.8, 'X': 0.2, 'J': 0.2, 'Q': 0.1, 'Z': 0.1
}


def encrypt(plaintext, shift):
    result = ""
    for char in plaintext.upper():
        if char in string.ascii_uppercase:
            shifted = (ord(char) - ord('A') + shift) % 26
            result += chr(ord('A')+ shifted)
        else:
            result += char
    return result


def decrypt(ciphertext, shift):
    return encrypt(ciphertext, -shift)



def frequency_analysis(text):
    text = ''.join(c for c in text if c in string.ascii_uppercase)
    if not text:
        return 0
    
    counts = Counter(text)
    score = 0

    for letter in ENGLISH_FREQS:
        observed = (counts.get(letter, 0)) / len(text) * 100
        expected = ENGLISH_FREQS[letter]
        score += abs(observed - expected)

    return score 

def break_caesar(ciphertext):
    best_shift = None
    best_score = float('inf')
    best_plaintext = ""

    for shift in range(26):
        decrypted = decrypt(ciphertext, shift)
        score = frequency_analysis(decrypted)

        if score < best_score:
            best_score = score 
            best_shift = shift
            best_plaintext = decrypted

    return best_shift, best_plaintext

def main():
    print("=== Caesar Cipher Tool ===")
    print("1) Encrypt")
    print("2) Decrypt")
    print("3) Break using frequency analysis")
    print("4) Exit")


    choice = input("\nChoose an option 1-4: ").strip()

    if choice == "1":
        text = input("Enter plaintext: ")
        shift = int(input("Enter the shift value: "))
        print("\nEncrypted text: ")
        print(encrypt(text, shift))

    elif choice == "2":
        text = input("Enter ciphertext: ")
        shift = int(input("Enter the shift value: "))
        print("\nDecrypted text: ")
        print(decrypt(text, shift))

    elif choice == "3":
        text = input("Enter ciphertext: ")
        shift, plaintext = break_caesar(text)
        print("\nCracked Result: ")
        print(f"Shift: {shift}")
        print(f"Plaintext: {plaintext}")

    elif choice == "4":
        print("Goodbye!")
        return
    
    else:
        print("Invalid choice!")

if __name__ == "__main__":
    main()








#if __name__ == "__main__":
   # message = "THIS IS A SECRET"
    #shift = 7

    ##encrypted = encrypt(message, shift)
    #print(f"Encrypted text is: {encrypted}")

    #cracked_shift, cracked_message = break_caesar(encrypted)
    #print(f"\nCracked shift is {cracked_shift}")
    #print(f"Cracked message is {cracked_message}")



