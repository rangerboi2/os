def create_address_book():
    global address_book
    address_book = []
    print("Address book created successfully.")

def view_address_book():
    if not address_book:
        print("Address book is empty.")
        return
    print("\nAddress Book Records:")
    for idx, record in enumerate(address_book, start=1):
        print(f"{idx}. Name: {record['name']}, Phone: {record['phone']}, Email: {record['email']}")

def insert_record():
    name = input("Enter name: ").strip()
    phone = input("Enter phone number: ").strip()
    email = input("Enter email: ").strip()
    record = {'name': name, 'phone': phone, 'email': email}
    address_book.append(record)
    print("Record inserted successfully.")

def delete_record():
    if not address_book:
        print("Address book is empty.")
        return
    view_address_book()
    try:
        idx = int(input("Enter record number to delete: "))
        if 1 <= idx <= len(address_book):
            removed = address_book.pop(idx-1)
            print(f"Record '{removed['name']}' deleted successfully.")
        else:
            print("Invalid record number.")
    except ValueError:
        print("Invalid input. Please enter a number.")

def modify_record():
    if not address_book:
        print("Address book is empty.")
        return
    view_address_book()
    try:
        idx = int(input("Enter record number to modify: "))
        if 1 <= idx <= len(address_book):
            record = address_book[idx-1]
            print("Leave blank to keep current value.")
            name = input(f"Enter new name [{record['name']}]: ").strip()
            phone = input(f"Enter new phone [{record['phone']}]: ").strip()
            email = input(f"Enter new email [{record['email']}]: ").strip()
            if name:
                record['name'] = name
            if phone:
                record['phone'] = phone
            if email:
                record['email'] = email
            print("Record updated successfully.")
        else:
            print("Invalid record number.")
    except ValueError:
        print("Invalid input. Please enter a number.")

def main():
    global address_book
    address_book = []
    while True:
        print("\nAddress Book Menu")
        print("a) Create Address Book")
        print("b) View Address Book")
        print("c) Insert Record")
        print("d) Delete a Record")
        print("e) Modify a Record")
        print("f) Exit")
        choice = input("Choose an option: ").strip().lower()

        if choice == 'a':
            create_address_book()
        elif choice == 'b':
            view_address_book()
        elif choice == 'c':
            insert_record()
        elif choice == 'd':
            delete_record()
        elif choice == 'e':
            modify_record()
        elif choice == 'f':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
