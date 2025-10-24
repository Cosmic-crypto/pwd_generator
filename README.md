Password Manager & Generator

A simple and effective Python-based password manager that lets you generate, store, find, and delete passwords locally from the command line.

This tool provides both:

* A secure password generator, and

* A password manager that stores your passwords in a local text file.

Features
* Password Manager

* Add your own passwords or auto-generate new ones.

* Label each password with what it’s used for (e.g., "Email", "Bank Account", "Netflix").

* Search for saved passwords easily.

* Delete stored passwords securely (requires a master password).

* Optionally remember your password file name for future sessions.

* Password Generator

* Generate strong, random passwords of any length.

* Each password includes at least one digit.

* Uses uppercase, lowercase, digits, and special characters.

Requirements

* Python 3.7 or higher

* No external dependencies (only standard library modules)

Usage
1. Run the Script

In your terminal, run:

python password_manager.py


You’ll be prompted with:

```
Would you like to use the password generator or password manager?
(If no answer is given, password manager will be chosen by default):
```

2. Password Manager

If you choose password manager, you’ll be asked:

```
Would you like to add, find, or delete a password? (add/find/delete)
```
Add a Password

You can either:

* Save your own password, or

* Let the program generate one for you.

Each password is saved in a text file (default: password.txt) in this format:

```
<reason>: <password>
```

Example:
```
Email: kD8*Q4!aZ9xP
Bank: L@p1zS#qT5nK
```

Find a Password

```
Enter a keyword or reason (e.g., "email" or "bank") to search.
The program will show matching entries and ask for confirmation:


Found: Email: kD8*Q4!aZ9xP
Is this the one you want? (y/n):
```
You can also have it write everything out by typing !*all*!:
```
Enter a keyword or reason (e.g., "email" or "bank") to search.
The program will show matching entries and ask for confirmation:!*all*!

WARNING: THIS WILL PRINT ALL THE SAVED USERNAMES AND PASSWORDS
do you wish to continue (y/n):
y
...
```

Delete a Password

Search for the entry you want to delete, then verify using the master password:

```
Enter keyword or reason to delete: email
Enter master password:
```

Default master password:

shPd/mpM1MQ( (Can change to anything, I generated this with the program).

You can also delete everything you have by typing !*all*!
there are security features for this and this is fool proof

```
WARNING: THIS WILL COMPLETLEY DESTROY EVERYTHING
do you want to do this (y/n):
y
enter the password: shPd/mpM1MQ(
Enter the final confirmation by typing 'delete':
delete
Everything in your password collection has been deleted
```

3. Password Generator

If you choose password generator, you’ll be asked:

```
Enter desired password length:
```

Then the program generates and prints a strong password:

```
Generated password: !N7^aZ4g*kCq
```

File Management

Default password storage file: password.txt

Reference file (stores saved filename): file_saved

When you first run the program, you can save your filename permanently:

```
Do you want to save this filename for future use? (y/n)
```

Security Notes

All passwords are stored in plain text.
For stronger protection, consider encrypting the file using a Python library such as cryptography.

The deletion feature uses a static master password (shPd/mpM1MQ (this can be changed this just what i generated with the password generator).
You can change it directly in the script for your own use.

Example File Structure
```
project/
│
├── password_manager.py     # Main script
├── password.txt            # Stored passwords
└── file_saved              # Stores saved filename reference
```
Example Session
```
Would you like to use the password generator or password manager?
(If no answer is given, password manager will be chosen by default): password manager

Would you like to add, find, or delete a password? (add/find/delete): add
Would you like to save your own password or generate one? (own/generated): generated
Enter desired password length: 16
What is this password used for? Email
Generated password: P@w8#kH5!sZ1nD3$
Password saved successfully!
```

I am quite an intermediate python programmer and I would appreciate any feedback
Also please note this is for personal use and NOT for commercial use, use this carefully the passwords stored are NOT encrypted meaning if anyone accesses this then they will get all info stored there in plain text

Feel free to customize or extend this project.
