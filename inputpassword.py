import re

def check_password_strength(password):
    # Minimum 8 characters long
    length_regex = re.compile(r'.{8,}')
    # At least one uppercase letter
    uppercase_regex = re.compile(r'[A-Z]')
    # At least one lowercase letter
    lowercase_regex = re.compile(r'[a-z]')
    # At least one digit
    digit_regex = re.compile(r'\d')
    # At least one special character
    special_char_regex = re.compile(r'[@$!%*?&]')

    if (length_regex.search(password) and uppercase_regex.search(password) and lowercase_regex.search(password) and digit_regex.search(password) and special_char_regex.search(password)):
        return True
    else:
        return False

def get_input():
    password = input("Set Your Password: ")
    if check_password_strength(password):
        print("Strong")
        confirm = input ("Re-enter Your Password: ")
        if confirm == password:
            print("Password Set Successfully!")
        else:
            print("Passwords do NOT match!")
            get_input()    
    else:
        print("Weak Password, Retry")
        get_input()

def main():
    get_input()  

if __name__ == "__main__":
    main()          

