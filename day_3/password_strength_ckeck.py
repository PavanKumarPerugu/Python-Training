import string

def password_strength_check():
    print("\nPlease choose a password of atleat 8 characters long \nwhich should contain a Capital letter, \na number and special character in it")
    password = input("\nPlease choose a strong password: ")
    if not len(password)<8:
        if any(p.isupper() for p in password):
            if any(p.isalpha() for p in password):
                if any(p.isdigit() for p in password):
                    if any(p in string.punctuation for p in password):
                        return f"Your password is strong!!"
                    else:
                        return f"Your password does not contain a special character in it!! Choose another!!"
                else:
                    return f"Your password does not contain a digit in it!! Choose another!!"
            else:
                return f"Your password does not contain an alphabet in it!! Choose another!!"
        else:
            return f"Your password does not contain a capital letter in it!! Choose another!!"
    else:
        return f"Your password does not contain 8 digits in it!! It's weak!! Choose another!!"
    
result = password_strength_check()
print(result)