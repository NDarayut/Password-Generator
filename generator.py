import string 
import random


def generate_alphabet():
    # Generate alphabets from 'a-z and A-Z'
    alphabets = string.ascii_letters

    return alphabets

def generate_numbers():
    # Generate numbers from '0-9'
    numbers = string.digits

    return numbers

def generate_special_characters():
    # Generate special characters "!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"
    special_characters = string.punctuation

    return special_characters

def generate_password(length, include_letters = False, include_numbers = False,
                      include_symbols = False):
    
    # If user choose to include all 3 option
    if include_letters and include_numbers and include_symbols:
        number_of_letters = length // 3
        number_of_numbers = length // 3
        number_of_symbols = length - (number_of_letters + number_of_numbers)
    
    # If user choose to include only alphabets and numbers
    elif include_letters and include_numbers:
        number_of_letters = length // 2
        number_of_numbers = length - number_of_letters

    # If user choose to include only alphabets and special characters
    elif include_letters and include_symbols:
        number_of_letters = length // 2
        number_of_symbols = length - number_of_letters
    
    # If user choose to include only numbers and special characters
    elif include_numbers and include_symbols:
        number_of_numbers = length // 2
        number_of_symbols = length - number_of_numbers

    # If user choose to include only alphabets
    elif include_letters:
        number_of_letters = length
    
    # if user choose to include only numbers
    elif include_numbers:
        number_of_numbers = length

    # If user choose to include only special characters
    elif include_symbols:
        number_of_symbols = length

    # Generate an empty list of every option 
    letters = []
    numbers = []
    symbols = []

    # Add item to list if they are True
    if include_letters:
        letters += random.choices(generate_alphabet(), k = number_of_letters) # Only generate a specified number of item
    if include_numbers:
        numbers += random.choices(generate_numbers(), k = number_of_numbers)
    if include_symbols:
        symbols += random.choices(generate_special_characters(), k = number_of_symbols)

    # combine them into a bigger list
    password = letters + numbers + symbols

    # Shuffle all the items
    random.shuffle(password)

    # Join all item in the list into a string
    password = ''.join(password)

    return password
