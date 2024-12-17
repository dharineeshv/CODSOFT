contacts_Details = {}

while True:
    
    print("\n 1) Add Contact \n 2) View Contact List \n 3) Search Contact \n 4) Update Contact \n 5) Delete Contact \n 6) Exit ")
    choice = int(input("Enter the Choice: "))
    
    if choice == 1:
        print("Enter the name, phone number, email and address to add!!")
        name = input("Enter the name: ")
        phone_num = int(input("Enter the mobile number: "))
        email_Id = input("Enter the email id: ")
        address = input("Enter the address: ")
        contacts_Details[name] = phone_num,email_Id,address
        print(f"Contact created for {name}")
        
        
    elif choice == 2:
        for name,datas in contacts_Details.items():
            print(f"{name} :- {datas}")
            
            
    elif choice == 3:
        search_name = input("Enter the name To Search : ")
        if search_name.lower() in contacts_Details:
            print(f"{search_name} :- {contacts_Details[search_name]}")
        else:
            print("No Contact Found!!")
    
    
    elif choice == 5:
        delete_contact = input("Enter the name to delete: ")
        if delete_contact.lower() in contacts_Details:
            del contacts_Details[delete_contact]
            print(f"{delete_contact} has deleted")
        else:
            print(f"No Contact found for {delete_contact}")
            
            
    elif choice == 4:
        name = input("Enter the name: ")
        if name.lower() in contacts_Details:
            print("\n1) Update Name \n 2) Update Phone Number \n 3) Update Email \n 4) Update Address")
            choices = int(input("Enter the choice: "))
            if choice == 1:
                old_name = input("Enter the old name: ")
                if old_name.lower() in contacts_Details:
                    new_name = input("Enter The New Name: ")
                    print(f"{new_name} has created")
                    contacts_details.pop()
                    
        
        
        