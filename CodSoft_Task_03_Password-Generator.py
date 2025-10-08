import random
import string

def generate_password(length):
    """Generates a random password of a specified length."""
    characters = string.ascii_letters + string.digits + string.punctuation
      
    if length <= 0:
        return "Error: Password length must be a positive number."
    
    password = ''.join(random.choice(characters) for _ in range(length))
    return password
def main():
    """Main function to run the password generator application."""
    print("--- Password Generator ---")
    while True:
        try:
            length_input = input("Enter the desired length for the password: ")
            password_length = int(length_input)
            new_password = generate_password(password_length)
            print("\nGenerated Password:", new_password)
            break 
            
        except ValueError:
            print("Invalid input. Please enter a valid number for the length.")
        except Exception as e:
            print(f"An error occurred: {e}")
            break

if __name__ == "__main__":
    main()

