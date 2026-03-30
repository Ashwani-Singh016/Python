# checking strong password
password = "Secure2P@ss"

if len(password) < 6:
    strength = "Weak"
elif len(password) <= 10:
    strength ="medium"
else:
    strength = "Strong"

print("Password strength is : ", strength)