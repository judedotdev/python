import random
prefix = '0703'

print('THIS PROGRAM GENERATES 5 RANDOM MTN PHONE NUMBERS\n')

for i in range(5):
    randomSuffix = random.randint(1000000, 9999999)
    randomPhoneNumber = prefix + str(randomSuffix)
    print(randomPhoneNumber)