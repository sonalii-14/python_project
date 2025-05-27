#-------------------------------------------------------------------------------
# Name:        module2
# Purpose:
#
# Author:      Sonali Singh
#
# Created:     22-05-2025
# Copyright:   (c) Sonali Singh 2025
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def lowercase_letters():
    return "abcdefghijklmnopqrstuvwxyz"

def uppercase_letters():
    return "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def digit():
    return "0123456789"

def special_characters():
    return "!@#$%^&*()-_=+[{]}|;:'\",<.>/?"

def all_characters():
    lowercase = lowercase_letters()
    uppercase = uppercase_letters()
    digits = digit()
    special_chars = special_characters()

    all_chars = lowercase + uppercase + digits + special_chars
    return all_chars

def generate_random_index(position, length):
    return (32767 * position + 12345) % length

def generate_password(length):
    characters = all_characters()
    password = ""

    for i in range(length):
        index = generate_random_index(i, len(characters))
        password += characters[index]

    return password

def valid_length():
    while True:
        user_input = input("Enter the desired length of the password: ")
        if user_input.isdigit():
            length = int(user_input)
            if length > 0:
                return length
            else:
                print("Please enter a positive number greater than zero.")
        else:
            print("Invalid input. Please enter a numeric value.")

def main():
    print("Welcome to the Password Generator!")
    password_length = valid_length()
    print("\nGenerating password...\n")
    generated_password = generate_password(password_length)
    print(f"Generated password: {generated_password}")

main()