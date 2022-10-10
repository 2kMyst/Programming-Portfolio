# Asking user for a name
name = input("Hi, what's your name? ")
if name == "":
    print("Hello, Stranger!")
else:
    print("Hello, ",name)

    BAD_PASSWORDS = ['password', 'letmein', 'sesame', 'hello', 'justinbieber']

# Creating a password
password = input("Choose a password. ")
confirmpassword = input("Type the same password to confirm. ")
if len(password) <8:
    print("Password is too short.")
elif len(password) >12:
    print("Password is too long.")
elif password == confirmpassword:
    print("Password Set")
else:
    print("Passwords do not match")

#7 times tables
num = input("Select a number. ")
num = int(num)
if num > 12:
    print("Number is too large.")
else:
    for count in range (1, 13):
        print(num, "x", count, "=", num * count)

if num < 0:
    for count in range (0, -12):
        print(num, "x", count, "=", num * count)
