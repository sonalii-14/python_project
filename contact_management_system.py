#-------------------------------------------------------------------------------
# Name:        module3
# Purpose:
#
# Author:      Sonali Singh
#
# Created:     23-05-2025
# Copyright:   (c) Sonali Singh 2025
# Licence:     <your licence>
#-------------------------------------------------------------------------------
# Contact Management System

contacts = []

def add_contact():
    print("\n--- Add Contact ---")
    name = input("Store Name: ")
    phone = input("Phone Number: ")
    email = input("Email: ")
    address = input("Address: ")
    contacts.append({
        "name": name,
        "phone": phone,
        "email": email,
        "address": address
    })
    print("Contact added successfully!")

def view_contacts():
    print("\n--- Contact List ---")
    if not contacts:
        print("No contacts available.")
    else:
        for i, contact in enumerate(contacts):
            print(f"{i + 1}. {contact['name']} - {contact['phone']}")

def search_contact():
    print("\n-- Search Contact --")
    keyword = input("Enter name or phone number to search: ")
    found = False
    for contact in contacts:
        if contact['name'] == keyword or contact['phone'] == keyword:
            print(f"\nName: {contact['name']}")
            print(f"Phone: {contact['phone']}")
            print(f"Email: {contact['email']}")
            print(f"Address: {contact['address']}")
            found = True
            break
    if not found:
        print("Contact not found.")

def update_contact():
    print("\n--- Update Contact ---")
    keyword = input("Enter name of contact to update: ")
    for contact in contacts:
        if contact['name'] == keyword:
            print("Leave blank to keep existing information.")
            new_name = input("New Store Name: ")
            new_phone = input("New Phone Number: ")
            new_email = input("New Email: ")
            new_address = input("New Address: ")

            if new_name:
                contact['name'] = new_name
            if new_phone:
                contact['phone'] = new_phone
            if new_email:
                contact['email'] = new_email
            if new_address:
                contact['address'] = new_address
            print("Contact updated successfully.")
            return
    print("Contact not found.")

def delete_contact():
    print("\n-- Delete Contact--")
    keyword = input("Enter name of contact to delete: ")
    for i, contact in enumerate(contacts):
        if contact['name'] == keyword:
            del contacts[i]
            print("Contact deleted successfully.")
            return
    print("Contact not found.")

def main_menu():
    while True:
        print("\n=== Contact Management System ===")
        print("1. Add Contact")
        print("2. View Contact List")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            add_contact()
        elif choice == "2":
            view_contacts()
        elif choice == "3":
            search_contact()
        elif choice == "4":
            update_contact()
        elif choice == "5":
            delete_contact()
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")
main_menu()
