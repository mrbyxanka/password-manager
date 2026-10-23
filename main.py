import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
PASSWORD_FILE = BASE_DIR / "passwords.json"

try:
    print("searching for passwords.json in", BASE_DIR)
    with open(PASSWORD_FILE, "r", encoding="utf8") as file:
        passwords = json.load(file)
        print("passwords.json was found.")
except FileNotFoundError:
    print("file not found.\ncreating file in ", BASE_DIR)
    passwords = [
        {
            "title": "default pre-installed password",
            "password": "leave me a star on git-hub <3"
        }
    ]
    with open(PASSWORD_FILE, "w", encoding="utf8") as file:
        json.dump(passwords, file, indent=4, ensure_ascii=False)
except json.JSONDecodeError:
    print("file was found but program cant read it, if you were editing that file manualy -- you broke something.\n"
    "if you have important passwords there, make sure you copied it.\n" \
    "please delete that file manualy because the creator of the program doesnt want to be responsible for the accidental deletion of important passwords.\n" \
    "you can find it in", PASSWORD_FILE)

view_passwords_disp = "\nyour password: " if len(passwords) == 1 else "\nall your passwords: "
def only_int_choice(choice, text):
    try:
        choice = int(input(text))
        return choice
    except ValueError:
        print("\nPlease use integers\n")
        return None
def save():
    with open(PASSWORD_FILE, "w", encoding="utf8") as file:
        json.dump(passwords, file, indent=4, ensure_ascii=False)

def view_passwords():
    print("\n",view_passwords_disp)
    for i, password in enumerate(passwords, start=1):
        print(f"{i}. {password["title"]}: {password["password"]}")
    input("\nPress enter to continue: ")

def add_password():
    np_title = input("Enter a password name: ").capitalize().strip() #np stands for new password
    np_password = input("Enter a password its self: ").strip()
    if np_title and np_password != "":
        new_password = {
            "title": np_title,
            "password": np_password
        }
        passwords.append(new_password)
        save()
        print("Password was added.")
    else:
        print("Your password name or password its self cant be empty.")
    input("\nPress enter to continue: ")

def edit_password():
    ved_choice = 0
    ed_choice = 0
    print("\n",view_passwords_disp)
    for i, password in enumerate(passwords, start=1):
        print(f"{i}. {password["title"]}: {password["password"]}")
    ved_choice = only_int_choice(ved_choice, "What password you want to edit?: ")
    if isinstance(ved_choice, int):
        ved_choice -= 1
        if 0 <= ved_choice <= len(passwords) - 1:
            print("| 1. name | 2. password | 3. both |")
            ed_choice = only_int_choice(ed_choice, "\nWhat do you want to edit?: ") #ed stands for edit choice
        else:
            print("Unknown command.")
        if ed_choice == 1:
            new_name = input("Choose a new name for the password: ").capitalize().strip()
            if new_name != "":
                passwords[ved_choice]["title"] = new_name
                save()
                print("\nName was changed.")
            else:
                print("Name cant be empty.")
        elif ed_choice == 2:
            new_password = input("Choose a password: ").strip()
            if new_password != "":
                passwords[ved_choice]["password"] = new_password
                save()
                print("\nPassword was changed.")
            else:
                print("Password its self cant be empty.")
        elif ed_choice == 3:
            new_name = input("Choose a new name for the password: ").capitalize().strip()
            new_password = input("Choose a password: ").strip()
            if new_name and new_password != "":
                passwords[ved_choice]["title"] = new_name
                passwords[ved_choice]["password"] = new_password
                save()
                print("\nName and password were changed.")
            else:
                print("Name or password its self cant be empty.")
    else:
        print("Please use integers")
    input("\nPress enter to continue: ")

def delete_password():
    delete_choice = 0
    print("\n",view_passwords_disp)
    for i, password in enumerate(passwords, start=1):
        print(f"{i}. {password["title"]}: {password["password"]}")
    delete_choice -= 1
    delete_choice = only_int_choice(delete_choice, "Choose what password you want to delete: ")
    if isinstance(delete_choice, int):
        if 0 < delete_choice <= len(passwords) - 1:
            sure = input("Are you sure that you want to delete that password?\nyes/no: ").strip().lower()
            if sure == "yes" or sure == "y" or sure == "ye":
                del passwords[delete_choice]
                save()
                print("Password was deleted.")
            elif sure == "no" or sure == "n":
                print("afdafs")
            else:
                print("Unknown command")
        else:
            print("Unknown command.")
        input("Press enter to continue: ")
    else:
        print("Please use integers.")

posible_menu_choises = {
    1: view_passwords,
    2: add_password,
    3: edit_password,
    4: delete_password

}

while True:
    menu_choice = 0
    print(
    "__________________________________\n"
    "|------- COMMANDS MANAGER -------|\n"
    "|                                |\n" \
    "|1. View passwords               |\n" \
    "|2. Add password                 |\n" \
    "|3. Edit an existing password    |\n" \
    "|4. Delete a password            |\n" \
    "|5. Exit                         |\n"
    "|                                |\n" \
    "|--------------------------------|\n")
    menu_choice = only_int_choice(menu_choice, "Choose a command: ")
    if menu_choice in posible_menu_choises:
        posible_menu_choises[menu_choice]()
    elif menu_choice == 5:
        break
    else:
        print("that command doesnt exist.")