class ContactManager:
    def __init__(self):
        self.contacts = []                                  # Initializing an empty list to store contacts

    def add_contact(self, name: str, country_code: str, phone: str, email: str, address: str) -> None:
        # Validate phone number
        full_phone = country_code + phone                # Combining country code with phone number
        if not self.validate_phone(phone):
            print("Invalid phone number. Please enter a valid phone number.")
            return
        
        # Adding a new contact to the list
        contact = {
            'name': name,
            'country_code': country_code,
            'phone': phone,
            'email': email,
            'address': address
        }
        self.contacts.append(contact)
        print(f"Contact '{name}' added.")

    def validate_phone(self, phone: str) -> bool:
        # Checking if phone number is valid (only digits)
        return phone.isdigit() and len(phone) > 0

    def view_contacts(self) -> None:
        # Viewing all contacts of the list
        if not self.contacts:
            print("No contacts found.")
            return
        print("\nContacts:")
        for contact in self.contacts:
            self.print_contact_box(contact)

    def print_contact_box(self, contact: dict) -> None:
        # Printing a contact in a box-like format
        box_width = 60
        print( "-" * (box_width) )
        print(f"| Name: {contact['name']:<30}                 |")
        print(f"| Country Code: {contact['country_code']:<30} |")
        print(f"| Phone: {contact['phone']:<30}               |")
        print(f"| Email: {contact['email']:<30}               |")
        print(f"| Address: {contact['address']:<30}           |")
        print("-" * (box_width))

    def search_contact(self, search_term: str) -> None:
        # Search for contacts by name or phone number
        results = [contact for contact in self.contacts if search_term.lower() in contact['name'].lower() or search_term in contact['phone']]
        if not results:
            print("No contacts found.")
        else:
            print("\nSearch Results:")
            for contact in results:
                self.print_contact_box(contact)

    def update_contact(self, name: str, country_code: str = None, phone: str = None, email: str = None, address: str = None) -> None:
        # Update an existing contact's details
        for contact in self.contacts:
            if contact['name'] == name:
                if country_code is not None:
                    contact['country_code'] = country_code
                if phone is not None:
                    if not self.validate_phone(phone):
                        print("Invalid phone number. Please enter a valid phone number.")
                        return
                    contact['phone'] = phone
                if email is not None:
                    contact['email'] = email
                if address is not None:
                    contact['address'] = address
                print(f"Contact '{name}' updated.")
                return
        print("Contact not found.")

    def delete_contact(self, name: str) -> None:
        # Delete a contact from the list
        for i, contact in enumerate(self.contacts):
            if contact['name'] == name:
                del self.contacts[i]
                print(f"Contact '{name}' deleted.")
                return
        print("Contact not found.")

# Main function to interact with the user

def print_main_menu() -> None:
    print("Welcome to Contact Manager")
    box_width = 30
    print( "-" * (box_width) )
    print("|   Contact Manager Menu     |")
    print("+" + "-" * (box_width - 2) + "+")
    print("| 1. Add Contact             |")
    print("| 2. View Contacts           |")
    print("| 3. Search Contact          |")
    print("| 4. Update Contact          |")
    print("| 5. Delete Contact          |")
    print("| 6. Exit                    |")
    print( "-" * (box_width))

def main() -> None:
    manager = ContactManager()  

    while True:
        print_main_menu()                                                   # Print the main menu
        choice = input("Choose an option: ")

        if choice == '1':
            name = input("Enter name: ")                                    # Add a new contact
            country_code = input("Enter country code (e.g., +1, +44): ")
            phone = input("Enter phone number (10 digits): ")
            email = input("Enter email: ")
            address = input("Enter address: ")
            manager.add_contact(name, country_code, phone, email, address) 
        elif choice == '2':
            manager.view_contacts()                                          # View all contacts
        elif choice == '3':
            search_term = input("Enter name or phone number to search: ")
            manager.search_contact(search_term)                              # Search for a contact
        elif choice == '4':
            name = input("Enter the name of the contact to update: ")
            country_code = input("Enter new country code (leave blank to keep current): ")
            phone = input("Enter new phone number (leave blank to keep current): ")
            email = input("Enter new email (leave blank to keep current): ")
            address = input("Enter new address (leave blank to keep current): ")
            manager.update_contact(name, country_code if country_code else None, phone if phone else None, email if email else None, address if address else None)  # Update a contact
        elif choice == '5':
            name = input("Enter the name of the contact to delete: ")
            manager.delete_contact(name)                                         # Delete a contact
        elif choice == '6':
            print("Exiting...")
            break                                                                 # Exit the program
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()                                                                       # Start the program
