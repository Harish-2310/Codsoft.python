#Random Password Generator 
import string
import random

length = int(input("Enter password length: ")) 

print('''Choose character set for password from these:
      1. Digits
      2. Letters
      3.Special characters
      4.Exit''')

characterList = ""
while(True):
  Choice = int(input("Pick a number "))
  if(Choice == 1):
    characterList += string.digits
  elif(Choice == 2):
    characterList += string.ascii_letters 
  elif(Choice == 3):
    characterList += string.punctuation
  elif(Choice == 4):
    break
  else:
    print("Please Pick a valid option!")

password = []

for i in range(length):
  randomchar = random.choice(characterList)
  password.append(randomchar)
print("The random password is "+"".join(password))