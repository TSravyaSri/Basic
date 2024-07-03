import random
import string
def generate_password(length=12, use_uppercase=True, use_numbers=True, use_symbols=True):
    # Define character sets
    characters = string.ascii_letters if use_uppercase else string.ascii_lowercase
    characters += string.digits if use_numbers else ''
    characters += string.punctuation if use_symbols else ''
    # Generate password
    password = ''.join(random.choice(characters) for _ in range(length))
    return password
if __name__ == "__main__":
    # Example usage: Generate a password with default settings
    password = generate_password()
    print(f"Generated Password: {password}")
