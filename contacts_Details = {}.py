contacts_Details = {}

while True:
    
    print("\n 1) Add Contact \n 2) View Contact List \n 3) Search Contact \n 4) Update Contact \n 5) Delete Contact \n 6) Exit ")
    choice = int(input("Enter the Choice: "))
    
    if choice == 1:
        print("Enter the name, phone number, email and address to add!!")
        name = input("Enter the name: ").strip().lower()
        phone_num = int(input("Enter the mobile number: "))
        
        email_Id = input("Enter the email id: ").strip()
        address = input("Enter the address: ").strip()
        contacts_Details[name] = phone_num,email_Id,address
        print(f"Contact created for {name}")
        
        
    elif choice == 2:
        if contacts_Details:
           for name,datas in contacts_Details.items():
               print(f"{name} :- {datas}")
        else:
            print("Contact Is Empty...")
            
            
    elif choice == 3:
        search_name = input("Enter the name To Search : ").lower()
        if search_name.lower() in contacts_Details:
            print(f"{search_name} :- {contacts_Details[search_name]}")
        else:
            print("No Contact Found!!")
        
    elif choice == 4:
        old_name = input("Enter the old_name To Update: ").lower()
        if old_name.lower() in contacts_Details:
             print("Enter the name, phone number, email and address to Update!!")
             name = input("Enter the name: ")
             phone_num = int(input("Enter the mobile number: "))
             email_Id = input("Enter the email id: ")
             address = input("Enter the address: ")
             contacts_Details[name] = phone_num,email_Id,address
             print(f"Contact Updated for {name}")
        else:
            print(f"Contact Not Found For {old_name}...")
            
    elif choice == 5:
        delete_contact = input("Enter the name to delete: ").lower()
        if delete_contact.lower() in contacts_Details:
            del contacts_Details[delete_contact]
            print(f"{delete_contact} has deleted")
        else:
            print(f"No Contact found for {delete_contact}")
            
    elif choice ==6:
        print("Exiting.....")
        break 
    else:
        print("Please Enter the Valid Choice From (1-6)!!!")
        continue
