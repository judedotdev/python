# This Program Encrypts a Message Using The Caesar Cipher
# The Program can also Decrypt Encrypted Messages
# Notice: right shift is a positive integer while
# left shift is a negative integer
# Encryption Phase with shift n:
#     En(x) = (x + n)mod 26
# Decryption Phase with shift n:
#     Dn(x) = (x - n)mod 26

alphabet = {
    "A": 0, "B": 1, "C": 2, "D": 3, "E": 4, "F": 5, "G": 6,
    "H": 7, "I": 8, "J": 9, "K": 10, "L": 11, "M": 12, "N": 13,
    "O": 14, "P": 15, "Q": 16, "R": 17, "S": 18, "T": 19, "U": 20,
    "V": 21, "W": 22, "X": 23, "Y": 24, "Z": 25
}


def getKey(val):
    for key, value in alphabet.items():
        if val == value:
            return key
    return "no key with input value"


def encryptMessage():
    print('\nYou Have Chosen To Encrypt A Message!')
    plainText = str(input("Enter Plain Text: "))
    plainText = plainText.replace(" ", "")
    shift = int(input("Enter Shift: "))
    cipherText = ''
    for letter in plainText:
        index = alphabet[letter.upper()]
        newIndex = (int(index) + int(shift)) % 26
        cipher = getKey(newIndex)
        cipherText += cipher
    print('Cipher Text:', cipherText)


def decryptMessage():
    print('\nYou Have Chosen To Decrypt An Encrypted Message!')
    cipherText = str(input("Enter Cipher Text: "))
    cipherText = cipherText.replace(" ", "")
    shift = int(input("Enter Shift: "))
    plainText = ''
    for letter in cipherText:
        index = alphabet[letter.upper()]
        newIndex = (int(index) - int(shift)) % 26
        plain = getKey(newIndex)
        plainText += plain
    print('Plain Text:', plainText)


# Main Program Starts Here
print("\nWELCOME TO THE CAESAR CIPHER PROGRAM")

print("\n\nChoose 1 to Encrypt a Message")
print("Choose 2 to Decrypt a Message")

option = str(input("Enter a Number From the Above Options: "))

supportedOptions = ['1', '2']

while option not in supportedOptions:
    print("\nChoose 1 to Encrypt a Message")
    print("Choose 2 to Decrypt a Message")
    option = str(input("Enter a Number From the Above Options: "))

if option == '1':
    encryptMessage()

if option == '2':
    decryptMessage()
