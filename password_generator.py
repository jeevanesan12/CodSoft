import random
import string

def pass_worrd(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password=""
    for i in range(length):
        password=password+random.choice(characters)
    print("Generated Password:", password)


try:
    length = int(input("Enter the desired length of the password: "))
    if length <= 0:
        print("number should be a positive integer.")
        raise ValueError
        
    pass_worrd(length)
except ValueError:
    print("Invalid input enter a valid integer")
