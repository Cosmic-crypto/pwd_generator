import secrets
import string

mode = input("Would you like to add to your password collection or find a password in your collection? (add/find/delete)\n").strip().lower() # To see if the user wants to add, find, or delete their passwords

try:
    filename = input("Enter a filename:\n") # so the user can set their own file instead of being a default 'password.txt'
except:
    print("filename is not provided") # inform the user that filename is not provided

    while True: # puts user into a loop of asking the user for a filename
        try:
            filename = input("enter a filename:\n") # asks user for filename
            break # breaks if code continues without going to the except
        except: # if went into except:
            print("filename not provided") # print file not provided

if mode == "add": # checks what they want to do
    try:
        password_length = int(input("Enter the desired password length: ")) # asks user how long the password should be
    except ValueError: # checks if the password type was wrong
        password_length = 12 # sets it to a default 12
        print("Invalid input. Using default length of 12.") # notifies the user that it is 12

    characters = string.ascii_letters + string.digits + string.punctuation # defining everything that can be in the password
    password = ''.join(secrets.choice(characters) for _ in range(password_length)) # password generation code

    print("Generated password:", password) # shows the user the password

    password_reason = input("What is this password used for? ").strip() # password reason so the user can later check what the password is for

    with open(filename, "a") as file: # opens a file by the name given by the user
        file.write(f"{password_reason}: {password}\n") # writes the password and the reason

    print("Password saved successfully!") # notifies user password has been saved

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
        password_ = 'shPd/mpM1MQ('

        for line in lines: # goes through all lines
            if search.lower() in line.lower(): # checks if the search term is in the line (case-insensitive)
                print(f"Found: {line.strip()}") # shows what it found
                choice = input("Delete this? (y/n): ").strip().lower() # asks user for confirmation
                if choice == "y":
                    for i in range(3):
                        password_user = input("Enter the password") # if user says yes
                        if password_user == password_:
                            deleted = True # mark as deleted
                            continue # skip adding this line to new_lines (this removes it)
                        else:
                            print(f"no try again you have {i-3} tries left")
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
