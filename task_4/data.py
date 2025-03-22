CONTACTS_FILE = "contacts.txt"

def load_contacts():
    contacts = {}
    try:
        with open(CONTACTS_FILE, "r", encoding="utf-8") as file:
            for line in file:
                name, phone = line.strip().split(",")
                contacts[name] = phone
    except FileNotFoundError:
        pass
    return contacts

def save_contacts(contacts):
    with open(CONTACTS_FILE, "w", encoding="utf-8") as file:
        for name, phone in contacts.items():
            file.write(f"{name},{phone}\n")