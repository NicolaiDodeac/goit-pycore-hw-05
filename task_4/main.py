from processing import *
from data import *

def main():
    contacts = load_contacts()

    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ").strip()
        command, args = parse_input(user_input)

        if command in ["close", "exit"]:
            save_contacts(contacts)
            print("Good bye!")
            break

        elif command == "hello":
            print("How can I help you?")

        elif command == "add":
            print(add_contact(args, contacts))
            
        elif command == "change":
            print(change_contact(args, contacts))

        elif command == "phone":
            print(show_phone(args, contacts))

        elif command == "all":
            print(show_all(contacts))

        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()

#! Different approach I've also tried

# elif command == "add":
#     add_input = input("Enter name and phone number (e.g., Nick 0954021386): ")
#     _, args = parse_input(f"add {add_input}")
#     if len(args) != 2:                
#         print("Error: Please provide command: Name Phone-number)")
#     else:
#         print(add_contact(args, contacts))

# elif command == "change":
#     change_input = input("Enter name and new phone number to update to  (e.g., Nick 0954021386): ")
#     _, args = parse_input(f"add {change_input}")
#     if len(args) != 2:                
#         print("Error: Please provide command: Name to change Phone-number")
#     else:
#         print(change_contact(args, contacts))

