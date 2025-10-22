import secrets
import string

try:
    main_choice = input("Would you like to generate a password or password manager (if no answer is given program will assume that you chose password manager)\n").strip().lower() # asks user if they want to use the generator or password manager
except: # if main_choice was not provided
    main_choice = "password manager" # password manager will be chosen by default
    print("Password manager has been chosen") # notifies the user that password manager was chosen

chars = string.ascii_letters + string.digits + string.punctuation # defining everything that can be in the password

if main_choice in ("password manager", "password_manager", "pwd_manager", "pwd manger"): # checks if user wants password generator
    mode = input("Would you like to add to your password collection or find a password in your collection? (add/find/delete)\n").strip().lower() # To see if the user wants to add, find, or delete their passwords

    try:
        filename = input("Enter a filename (if password not provided then it will be set to a file called password.txt):\n") # so the user can set their own file instead of being a default 'password.txt'
    except: # if file name wasn't provided
        filename = "password.txt" # filename is now 'password.txt'
        print("filename is user will be 'password.txt'")

    if mode == "add": # checks what they want to do
        password_type = input("would you like to save your own password or a randomly generated password:\n").strip().lower() # asks user if they want to save their own password or a randomly generated password
        if password_type in ("generated password", "generated_password"): # checks if the user has told to generate a password
            try:
                password_length = int(input("Enter the desired password length: ")) # asks user how long the password should be
            except ValueError: # checks if the password type was wrong
                password_length = 12 # sets it to a default 12
                print("Invalid input. Using default length of 12.") # notifies the user that it is 12

            password = ''.join(secrets.choice(chars) for _ in range(password_length)) # password generation code

            print("Generated password:", password) # shows the user the password

            password_reason = input("What is this password used for? ").strip() # password reason so the user can later check what the password is for

            with open(filename, "a") as file: # opens a file by the name given by the user
                file.write(f"{password_reason}: {password}\n") # writes the password and the reason

            print("Password saved successfully!") # notifies user password has been saved
        elif password_type in ("own_password", "own password"):
            while True: # puts user into loops
                password = input("Enter your password") # asks user for password
                if password: # if password is a truthy value
                    break #then it breaks the loop
                else: # else
                    print("Password not given") # it says password isn't given and carrys on
        else:
            print("Invalid password type!")

    elif mode == "find": # checks if the user wanted to find instead
        search = input("Enter what password to find:\n").strip() # asks the user what password they want to find
        found = False # sets found to false so we can track if anything was found

        try:
            with open(filename, "r") as file: # opens the file in read mode
                for line in file: # goes through every line in the file
                    if search.lower() in line.lower():  # case-insensitive search
                        print(f"\nFound: {line.strip()}") # prints what was found
                        confirmation = input("Is this the one you want? (y/n): ").strip().lower() # asks the user if they are happy with the result
                        if confirmation == "y": # checks if they are happy
                            print("Bye!") # says bye and exits
                            exit() # exits program
                        else:
                            continue # keeps searching
            if not found: # if nothing was found
                print("Couldn't find that password.") # notifies the user that it wasn't found
        except FileNotFoundError:
            print("No password collection found yet. Add one first!") # safety feature just telling the user what is wrong

    elif mode == "delete": # checks if the user wants to delete a password
        search = input("Enter what to delete:\n").strip() # asks the user what they want to delete
        try:
            with open(filename, "r") as file: # opens the file in read mode
                lines = file.readlines() # reads all the lines from the file

            new_lines = [] # list to store all lines except the ones we delete
            deleted = False # variable to track if something was deleted
            password_ = 'shPd/mpM1MQ(' # sets the master password for deletion

            for line in lines: # goes through all lines
                if search.lower() in line.lower(): # checks if the search term is in the line (case-insensitive)
                    print(f"Found: {line.strip()}") # shows what it found
                    choice = input("Delete this? (y/n): ").strip().lower() # asks user for confirmation
                    if choice == "y": # if user says yes to deletion
                        for i in range(3): # gives the user 3 tries
                            password_user = input("Enter the password: ").strip() # asks user to enter the master password
                            if password_user == password_: # if the password is correct
                                deleted = True # mark as deleted
                                print("Password verified. Deleting entry...") # inform user
                                break # break out of password loop
                            else: # if password is incorrect
                                print(f"Wrong password. Try again. You have {2 - i} tries left.") # shows remaining tries

                        if not deleted: # if password was never correct after 3 tries
                            print("Too many failed attempts. Entry not deleted.") # warns user
                            new_lines.append(line) # keep the line since deletion failed
                            continue # move on to next line
                        else:
                            continue # skip adding this line (delete it)
                new_lines.append(line) # adds the line if not deleted

            if deleted: # checks if anything was deleted
                with open(filename, "w") as file: # opens file in write mode to overwrite it
                    file.writelines(new_lines) # writes back only the remaining lines
                print("Selected entry deleted successfully.") # notifies user deletion is done
            else:
                print("No entries deleted.") # tells user nothing was deleted
        except FileNotFoundError:
            print("No password collection found yet. Add one first!") # tells user the file doesn't exist yet

    else:
        print("Invalid option. Please enter either 'add', 'find', or 'delete'.") # informs user of invalid mode
elif main_choice in ("password_generator", "password generator", "pwd generator", "pwd_generator"): # checks if user wanted password generator instead
    try:
        pwd_len = int(input("Enter an the password length")) # asks user the password length
    except: # if the the password lenght wasn't provided or was wrong type
        pwd_len = 12 # program writes it as 12
        print("password length is 12") # notifies user that password length is 12
    
    pwd = "".join(secrets.choice(chars) for _ in range(pwd_len))

    print("Password is:", pwd)
