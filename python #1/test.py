print('Let me Test what is happing in my computer!')
print('And Linux Will help me in it!')
print("And I Will DO that!")

# Importing random module for genrate password_characters randomly
import random as rd

# password characters list
password_characters = "abcdefghijklmnopqrstuvwxyz!@#$%^&*()?><_ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()?><_"
# password which will be done
password = ""

# giving loop for it for password range
rangePass = int(input("Enter the range of the password: "))

# Loop to create password
for i in range(rangePass):
    password += rd.choice(password_characters)

# finally printing our genrated password
print(password)




