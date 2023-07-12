#CodeRunner.in
import random
import string

def generate_password(min_length,numbers=True,special_characters=True):
    letters=string.ascii_letters
    digits=string.digits
    special=string.punctuation

    characters=letters
    if numbers:
        characters+=digits
    if special_characters:
        characters+=special
    
    pwd=""
    requirement_fulfilled=False
    has_number=False
    has_special=False

    while not requirement_fulfilled or len(pwd)<min_length:
        new_char=random.choice(characters)
        pwd+=new_char

        if new_char in digits:
            has_number=True
        if new_char in special:
            has_special=True 
        
        requirement_fulfilled=True
        if numbers:
            requirement_fulfilled=has_number
        if special_characters:
            requirement_fulfilled=has_special

    return pwd


min_length=int(input("Enter the minimum length: "))
include_number=input("Do you want to have numbers (y/n)? ").lower()=="y"
include_special=input("Do you want to have special characters (y/n)? ").lower()=="y"

pwd=generate_password(min_length,include_number,include_special)
print("\n The generated password is: ",pwd)

