import string

print("===================================")
print("     PASSWORD STRENGTH CHECKER")
print("===================================")

password = input("Enter your password: ")

score = 0
suggestions = []

# 1. Check password length
if len(password) >= 8:
    score += 1
else:
    suggestions.append("Use at least 8 characters.")

# 2. Check uppercase letter
if any(char.isupper() for char in password):
    score += 1
else:
    suggestions.append("Add at least one uppercase letter (A-Z).")

# 3. Check lowercase letter
if any(char.islower() for char in password):
    score += 1
else:
    suggestions.append("Add at least one lowercase letter (a-z).")

# 4. Check number
if any(char.isdigit() for char in password):
    score += 1
else:
    suggestions.append("Add at least one number (0-9).")

# 5. Check special character
if any(char in string.punctuation for char in password):
    score += 1
else:
    suggestions.append("Add at least one special character (!, @, #, $, etc.).")

# Display result
print("\n-----------------------------------")

if score == 5:
    print("Password Strength: STRONG")
elif score >= 3:
    print("Password Strength: MEDIUM")
else:
    print("Password Strength: WEAK")

print(f"Score: {score}/5")

# Display suggestions for weak/medium passwords
if suggestions:
    print("\nHow to improve your password:")
    for suggestion in suggestions:
        print("- " + suggestion)
else:
    print("\nYour password meets all the strength requirements!")

print("-----------------------------------")