def check_password_strength(password):
    if len(password) < 8:
        return "Weak: Password must be at least 8 characters long"

    has_upper = False
    has_lower = False
    has_digit = False
    has_special = False

    for char in password:
        if char.isupper():
            has_upper = True
        elif char.islower():
            has_lower = True
        elif char.isdigit():
            has_digit = True
        else:
            has_special = True

    if has_upper and has_lower and has_digit and has_special:
        return "Strong password!!"
    else:
        return "Medium: Add uppercase, digit, or special character"

password = input("Enter your password: ")
result = check_password_strength(password)
print(result)
