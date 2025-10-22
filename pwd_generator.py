import secrets
import string

mode = input("Would you like to add to your password collection or find a password in your collection? (add/find)\n").strip().lower() # To see if the user wants to add or see they're passwords

try:
    filename = input("Enter a filename:\n") # so the user can set their own file instead of being a default 'password.txt'
except:
    print("filename is not provided") # inform the user that filename is not provided

    while True: # puts user into a loop of aksking the user for a filename
        try:
            filename = input("enter a filename:\n") # asks user for filename
            break # breaks if code continues without going to the except
        except: # if went into except:
            print("filename not provided") # print file not provided

if mode == "add": #checks what they want to do
    try:
        password_length = int(input("Enter the desired password length: "))
    except ValueError: # checks if the password type was wrong
        password_length = 12 # sets it to a default 12
        print("Invalid input. Using default length of 12.") # notifies the user that it is 12

    characters = string.ascii_letters + string.digits + string.punctuation # deining everything that can be in the password
    password = ''.join(secrets.choice(characters) for _ in range(password_length)) # password generation code

    print("Generated password:", password) # Shows the user the password

    password_reason = input("What is this password used for? ").strip() # password reason so the user can later check what the password is for

    with open(filename, "a") as file: # opens a file by the name of 'password.txt' (can be modified)
        file.write(f"{password_reason}: {password}\n") # writes the password and the reason

    print("Password saved successfully!") # notifies user password has been saved

elif mode == "find": # checks if the user wanted to find instead
    search = input("Enter what password to find:\n").strip()
    found = False

    try:
        with open(filename, "r") as file: # opens a file by the name of 'password.txt' (can be modified) to find the thing they want
            for line in file:
                if search.lower() in line.lower():  # case-insensitive search
                    print(f"\nFound: {line.strip()}")
                    confirmation = input("Is this the one you want? (y/n): ").strip().lower() # asks the user if they are happy with the result
                    if confirmation == "y": # checks if they are happy
                        print("Bye!")
                        exit()
                    else:
                        continue
        if not found:
            print("Couldn't find that password.")
    except FileNotFoundError:
        print("No password collection found yet. Add one first!") # safety feature just telling the user what is wrong
else:
    print("Invalid option. Please enter either 'add' or 'find'.")
