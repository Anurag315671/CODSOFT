import random
import string

def generate_password(length):
    """Generates a random password of a specified length."""
    
    # Define the character set to use in the password (letters, digits, and symbols)
    characters = string.ascii_letters + string.digits + string.punctuation
    
    # Check if the length is a positive number
    if length <= 0:
        return "Error: Password length must be a positive number."
        
    # Generate the password by choosing random characters from the set
    password = ''.join(random.choice(characters) for _ in range(length))
    
    return password

def main():
    """Main function to run the password generator application."""
    print("--- Password Generator ---")
    
    while True:
        try:
            # Prompt the user for the desired password length
            length_input = input("Enter the desired length for the password: ")
            password_length = int(length_input)
            
            # Generate the password
            new_password = generate_password(password_length)
            
            # Display the generated password
            print("\nGenerated Password:", new_password)
            break # Exit the loop after successful generation
            
        except ValueError:
            # Handle cases where the input is not a number
            print("Invalid input. Please enter a valid number for the length.")
        except Exception as e:
            # Handle other potential errors
            print(f"An error occurred: {e}")
            break

# Run the main function when the script is executed
if __name__ == "__main__":
    main()

