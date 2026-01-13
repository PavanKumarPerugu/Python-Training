import string

def password_strength_check():
    print("\nPlease choose a password of at least 8 characters long\n"
          "which should contain a Capital letter,\n"
          "a number and a special character")

    password = input("\nPlease choose a strong password: ")

    if len(password) < 8:
        return "Your password must be at least 8 characters long!"

    if not any(p.isupper() for p in password):
        return "Your password does not contain a capital letter!"

    if not any(p.isalpha() for p in password):
        return "Your password does not contain an alphabet!"

    if not any(p.isdigit() for p in password):
        return "Your password does not contain a digit!"

    if not any(p in string.punctuation for p in password):
        return "Your password does not contain a special character!"

    return "Your password is strong!!"

result = password_strength_check()
print(result)
