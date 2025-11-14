import string
import secrets

def generate_password(length, use_letters, use_digits, use_symbols):
    character_set = ""

    if use_letters:
        character_set += string.ascii_letters
    if use_digits:
        character_set += string.digits
    if use_symbols:
        character_set += string.punctuation

    if not character_set:
        return "Error: No character types selected!"

    password = ''.join(secrets.choice(character_set) for _ in range(length))
    return password


# ------- Main Program -------
print("=== RANDOM PASSWORD GENERATOR ===")

while True:
    try:
        length = int(input("Enter password length: "))
        if length <= 0:
            print("Length must be positive!")
            continue
        break
    except ValueError:
        print("Invalid input! Enter a number.")

# Character types
use_letters = input("Include letters (y/n)? ").lower() == 'y'
use_digits = input("Include digits (y/n)? ").lower() == 'y'
use_symbols = input("Include symbols (y/n)? ").lower() == 'y'

password = generate_password(length, use_letters, use_digits, use_symbols)

print("\nGenerated Password:", password)
