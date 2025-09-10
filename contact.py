contacts=[]
def add_contact():
    name = input("enter name :")
    phone = input("enter phone number :")
    email = input("enter email :")
    address = input("enter address :")
    contact = {
        "name": name,
        "phone": phone,
        "email": email,
        "address": address
    }
    contacts.append(contact)
    print("contact added successfully")
def view_contacts():
    if not contacts:
        print("no contacts available")
        return
    print(" "*10,"contact list"," "*10)
    for i, contact in enumerate(contacts,start=1):
        print(f"{i}. {contact['name']} - {contact['phone']}")
    print()
def search_contact():
    search_term = input("enter name or phone number to search :")
    found = False
    for contact in contacts:
        if contact["name"] == search_term or contact["phone"] == search_term:
            print("\n--- contact Found ---")
            print(f"name: {contact['name']}")
            print(f"phone: {contact['phone']}")
            print(f"email: {contact['email']}")
            print(f"address: {contact['address']}\n")
            found = True
    if not found:
        print("noo matching contact found")
def update_contact():
    search_term = input("enter name or phone number of the contact to update :")
    for contact in contacts:
        if contact["name"] == search_term or contact["phone"] == search_term:
            print("leave field blank to keep existing value")
            name = input(f"new name ({contact['name']}): ") or contact['name']
            phone = input(f"new phone ({contact['phone']}): ") or contact['phone']
            email = input(f"new email ({contact['email']}): ") or contact['email']
            address = input(f"new address ({contact['address']}): ") or contact['address']
            
            contact.update({"name": name, "phone": phone, "email": email, "address": address})
            print("contact updated successfully!")
            return
    print("contact not found")
def delete_contact():
    search_term = input("enter name or phone number of the contact to delete :")
    for contact in contacts:
        if contact["name"] == search_term or contact["phone"] == search_term:
            contacts.remove(contact)
            print("contact deleted successfully")
            return
    print("contact not found")
def menu():
    while True:
        print("your contact lnformation :")
        print("1. add ocntact")
        print("2. view contact cist")
        print("3. search contact")
        print("4. update contact")
        print("5. delete contact")
        print("6. exit")
        choice = input("Enter your choice (1/2/3/4/5/6): ")
        if choice == "6":
            print("exit")
            break
        elif choice == "1":
            add_contact()
        elif choice == "2":
            view_contacts()
        elif choice == "3":
            search_contact()
        elif choice == "4":
            update_contact()
        elif choice == "5":
            delete_contact()
        else:
            print("Invalid choice Please enter again ")
menu()
