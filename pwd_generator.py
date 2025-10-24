from string import ascii_letters, digits, punctuation
from secrets import choice

# File that stores the saved filename for long-term use
FILE_SAVE_REFERENCE = 'file_saved'


def password_gen(length):
    """
    Generates a random password of the given length containing at least one digit.
    """
    chars = ascii_letters + digits + punctuation
    password = [choice(chars) for _ in range(length)]

    # Ensure password has at least one digit
    if not any(c.isdigit() for c in password):
        pos = choice(range(len(password)))
        password[pos] = choice(digits)

    return "".join(password)


# Ask user for main mode (password manager or generator)
try:
    main_choice = input(
        "Would you like to use the password generator or password manager?\n"
        "(If no answer is given, password manager will be chosen by default): "
    ).strip().lower()
except Exception:
    main_choice = "password manager"
    print("Password manager has been chosen by default.")

# -------------------------
# PASSWORD MANAGER SECTION
# -------------------------
if main_choice in (
    "password manager",
    "password_manager",
    "pwd_manager",
    "pwd manager"
):
    mode = input(
        "Would you like to add, find, or delete a password? (add/find/delete): "
    ).strip().lower()

    # Try to load saved filename or ask user for one
    try:
        with open(FILE_SAVE_REFERENCE, "r") as file:
            saved_filename = file.read().strip()
        filename = saved_filename if saved_filename else input(
            "Enter a filename (default is 'password.txt'): "
        ).strip()
        if not filename:
            raise ValueError
    except Exception:
        filename = "password.txt"
        print("Using default filename: 'password.txt'")

        save_choice = input(
            "Do you want to save this filename for future use? (y/n): "
        ).strip().lower()
        if save_choice != 'n':
            while True:
                file_to_be_saved = input("Enter a name to save this file as: ").strip()
                if file_to_be_saved:
                    with open(FILE_SAVE_REFERENCE, 'w') as file:
                        file.write(file_to_be_saved)
                    break
                else:
                    print("Please enter a valid file name.")

    # -------------------------
    # ADD PASSWORD
    # -------------------------
    if mode == "add":
        password_type = input(
            "Would you like to save your own password or generate one? (own/generated): "
        ).strip().lower()

        # Generate a random password
        if password_type in ("generated", "generated password", "generated_password"):
            try:
                password_length = int(input("Enter desired password length: "))
            except ValueError:
                password_length = 12
                print("Invalid input. Using default length of 12.")

            password = password_gen(password_length)

            # Ask what the password is used for
            while True:
                password_reason = input("What is this password used for? ").strip()
                if password_reason:
                    break
                print("Please enter a valid reason.")

            # Ensure no duplicates
            try:
                with open(filename, "r") as file:
                    lines = file.readlines()
            except FileNotFoundError:
                lines = []

            for line in lines:
                if password in line:
                    print("Generated password already exists. Generating a new one...")
                    while True:
                        new_password = password_gen(password_length)
                        if new_password != password:
                            password = new_password
                            break

                if password_reason.lower() in line.lower():
                    print(f"A password for '{password_reason}' already exists.")
                    while True:
                        password_reason = input("Please enter another reason: ").strip()
                        if password_reason and password_reason.lower() not in line.lower():
                            break

            # Save password
            with open(filename, "a") as file:
                file.write(f"{password_reason}: {password}\n")

            print("Generated password:", password)
            print("Password saved successfully!")

        # Save user's own password
        elif password_type in ("own", "own password", "own_password"):
            while True:
                password = input("Enter your password: ").strip()
                if password:
                    break
                print("Password cannot be empty.")

            while True:
                password_reason = input("What is this password used for? ").strip()
                if password_reason:
                    break
                print("Please enter a valid reason.")

            # Avoid duplicates
            try:
                with open(filename, "r") as file:
                    lines = file.readlines()
            except FileNotFoundError:
                lines = []

            for line in lines:
                if password in line:
                    print("This password already exists.")
                    while True:
                        new_password = input("Enter a different password: ").strip()
                        if new_password and new_password != password:
                            password = new_password
                            break

                if password_reason.lower() in line.lower():
                    print(f"A password for '{password_reason}' already exists.")
                    while True:
                        password_reason = input("Please enter another reason: ").strip()
                        if password_reason:
                            break

            with open(filename, "a") as file:
                file.write(f"{password_reason}: {password}\n")

            print("Password saved successfully!")

        else:
            print("Invalid password type!")

    # -------------------------
    # FIND PASSWORD
    # -------------------------
    elif mode == "find":
        search = input("Enter what to find (keyword or reason): ").strip()
        found = False

        try:
            with open(filename, "r") as file:
                for line in file:
                    if search.lower() in line.lower():
                        found = True
                        print(f"\nFound: {line.strip()}")
                        confirmation = input("Is this the one you want? (y/n): ").strip().lower()
                        if confirmation == "y":
                            print("Bye!")
                            exit()
            if not found:
                print("Couldn't find that password.")
        except FileNotFoundError:
            print("No password collection found yet. Add one first!")

    # -------------------------
    # DELETE PASSWORD
    # -------------------------
    elif mode == "delete":
        search = input("Enter keyword or reason to delete: ").strip()
        master_password = 'shPd/mpM1MQ('  # Static master password for deletion

        try:
            with open(filename, "r") as file:
                lines = file.readlines()

            new_lines = []
            deleted = False

            for line in lines:
                if search.lower() in line.lower():
                    print(f"Found: {line.strip()}")
                    confirm = input("Delete this entry? (y/n): ").strip().lower()
                    if confirm == "y":
                        for attempt in range(3):
                            entered_pw = input("Enter master password: ").strip()
                            if entered_pw == master_password:
                                print("Password verified. Deleting entry...")
                                deleted = True
                                break
                            else:
                                print(f"Incorrect password. {2 - attempt} tries left.")

                        if not deleted:
                            print("Failed verification. Entry not deleted.")
                            new_lines.append(line)
                        continue
                new_lines.append(line)

            if deleted:
                with open(filename, "w") as file:
                    file.writelines(new_lines)
                print("Selected entry deleted successfully.")
            else:
                print("No entries deleted.")
        except FileNotFoundError:
            print("No password collection found yet. Add one first!")

    else:
        print("Invalid option. Please enter 'add', 'find', or 'delete'.")

# -------------------------
# PASSWORD GENERATOR SECTION
# -------------------------
elif main_choice in (
    "password generator",
    "password_generator",
    "pwd generator",
    "pwd_generator"
):
    try:
        pwd_len = int(input("Enter desired password length: "))
    except ValueError:
        pwd_len = 12
        print("Invalid input. Default length set to 12.")

    password = password_gen(pwd_len)
    print("Generated password:", password)

else:
    print("Invalid choice. Please select either 'password generator' or 'password manager'.")
