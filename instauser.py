print("Welcome to the User Account System!")
print("Please enter multiple usernames and passwords for the data collection.")

username1 = input("Enter your username1: ")
password1 = input("Enter your password1: ")
username2 = input("Enter your username2: ")
password2 = input("Enter your password2: ")
username3 = input("Enter your username3: ")
password3 = input("Enter your password3: ")

UserData ={username1: password1, username2: password2, username3: password3}
print("User data stored successfully!")
print("Username1:", username1)
print("Password1:", password1)
print("Username2:", username2)
print("Password2:", password2)
print("Username3:", username3)
print("Password3:", password3)

print()
yes = input("Do you want to create a new account? (yes/no): ")
if yes == "yes":
    input_username = input("Enter your username to log in: ")
    if input_username in UserData:
        print("User already exists.")
    else:
        print("you are allowed to create a new account as no such user exists.")
else:
    print("No new account created.")

yes = input("Do you want to check if the number of elements in a list is odd or even? (yes/no): ")
if yes == "yes":
    numbers = [1, 2, 3, 4, 5]
    if len(numbers) % 2 == 0:
        print("The number of elements in the list is even.")
    else:
        print("The number of elements in the list is odd.")


