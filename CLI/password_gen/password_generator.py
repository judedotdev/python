# A Program That Generates a Random Password
# That Contains 16 Characters, Uppercase
# Lowercase, Digits and Special Characters / Symbols

import random


# A function to shuffle the password to prevent it from cointaining consecutive letters or numbers
def shuffle(string):
    tempArray = list(string)
    random.shuffle(tempArray)
    return ''.join(tempArray)


# Function that generates the password with an option of saving to a text file
def generatePwd():
    symbol1 = chr(random.randint(33, 47))
    symbol2 = chr(random.randint(58, 64))
    symbol3 = chr(random.randint(91, 96))
    symbol4 = chr(random.randint(123, 126))

    password = symbol1 + symbol2 + symbol3 + symbol4

    for i in range(4):
        digit = chr(random.randint(48, 57))
        uppercase = chr(random.randint(65, 90))
        lowercase = chr(random.randint(97, 112))

        string = digit + uppercase + lowercase
        password += string

    password = shuffle(password)
    print('Password: ', password)
    print('Password Length: ', len(password))

    # Optionally save generated password to text file
    canSave = str(input('Save Password to text File? (yes/no): '))
    if canSave.lower() == 'yes':
        with open('pwd16char.txt', 'a') as outputfile:
            pwd = password + '\n'
            outputfile.write(pwd)
            print("Password Saved!!")


# Main program starts here
print("\nWELCOME TO THE CLI PASSWORD GENERATOR")

response = str(input('\nDo You Want To Generate a Password (yes/no) : '))
supportedOptions = ['yes', 'no']

while response not in supportedOptions:
    print("\nInvalid Response!!")
    response = str(input('\nDo You Want To Generate a Password (yes/no) : '))

while response.lower() == 'yes':
    generatePwd()
    response = str(
        input('\nDo You Want To Generate Another Password (yes/no) : '))
    while response not in supportedOptions:
        print("\nInvalid Response!!")
        response = str(
            input('\nDo You Want To Generate Another Password (yes/no) : '))
