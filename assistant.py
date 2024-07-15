def main():
    # greetings to user + list of supported commands
    print("Welcome to the assistant bot!")
    print(format_info())
    
    # waits for user's commands forever, untill terminal command is occurred
    contacts = {}
    while True:
        user_input = input("Enter a command: ")

        try:
            command, *args = parse_input(user_input)

            if command in ["close", "exit"]:
                print("Good bye!")
                break

            elif command == "hello":
                print("How can I help you?")
            elif command == "add":
                print(add_contact(args, contacts))
            elif command == "change":
                print(change_contact(args, contacts))
            elif command == "phone":
                print(find_number_by_name(args, contacts))
            elif command == "all":
                print(output_all_contacts(contacts))
            elif command == "info":
                print(format_info())
            else:
                print("Invalid command.")
        except:
            print("Failed parse your command. Make sure you enter it right. Run \'info\' command if you have a quistion about how to use it")


def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."


def output_all_contacts(contacts):
    if len(contacts) > 0:
        return f"Here's all added contacts:\n{contacts}."
    else:
        return "No contacts added so far."


def find_number_by_name(args, contacts):
    name = args[0]
    phone = contacts.get(name)

    if phone is not None:
        return f"Phone number of {name}: {phone}."
    else:
        return f"There is not phone number saved for {name}."
    

def change_contact(args, contacts):
    name, phone = args

    contact_was_added_before = contacts.get(name) is not None

    if contact_was_added_before:
        contacts[name] = phone
        return "Contact changed."
    else:
        return f"There was no contact created for {name}. Make sure you added it before and you spell it right."


def format_info():
    return "Supported list of comands:\n"\
    "hello -> just says hi!\n"\
    "add \'name\' \'phone\' -> saves phone number by name\n"\
    "change \'name\' \'phone\' -> edits phone number by name\n"\
    "phone \'name\' -> outputs saved phone number for this name\n"\
    "all -> output all saved contacts\n"\
    "close -> finish assistant\n"\
    "exit -> finish assistant\n"\
    "info -> information about supported commands\n"\
    "\n"\
    "Make sure you follows format of commands, and avoid spaces in phone number, it's not supported"

if __name__ == "__main__":
    # run program
    main()