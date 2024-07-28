import re

def check_password_strength(password):
    length_regex = re.compile(r'.{8,}') # Minimum 8 characters long
    uppercase_regex = re.compile(r'[A-Z]') # At least one uppercase letter
    lowercase_regex = re.compile(r'[a-z]') # At least one lowercase letter
    digit_regex = re.compile(r'\d') # At least one digit
    special_char_regex = re.compile(r'[@$!%*?&]') # At least one special character

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

