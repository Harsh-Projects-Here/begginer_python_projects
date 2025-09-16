import datetime
diary = {
    }
print("⬇My Personal Diary⬇")
input("Press Enter if you want us to create your own personal diary:")
pin = input("Do you want a pin in your diary or not (yes / no)")
if pin.lower() == "yes":
    lock = input("Enter your pin:")
    if len(lock)==4:
        print("Pin Created Successfully")
    login = input("Enter your password to login:")
    if login == lock:
        print("Login Successfully")
        ax = ('''--- Menu ---
1. Add New Entry
2. View All Entries
3. Remove an Entry
4. Exit''')
        while True:
            print(ax)
            choose = int(input("Enter your choice:"))
            if choose == 1:
                print("You chose to enter a new diary entry.")
                date = input("Press Enter if you want to begin your entry:")
                content = input("Write Content Here:")
                x = datetime.datetime.now()
                csk = (x.strftime("Date -%d/%m/%Y Time-%H:%M:%S"))
                diary.update({csk: content})
                print("Diary Updated Successfully")
            elif choose == 2:
                input("Press Enter to see all entries.")
                for date, content in diary.items():
                    print(f'''⭕ {date}
☑️Content- {content}''')
            elif choose == 3:
                print("Remove any entry")
                print("Your Entries⬇")
                print(diary)
                c = input("Which entry do you want to remove? Fill exact date from your entries:")
                if c in diary:
                    diary.update({c: "Removed"})
                    print(f"{c} removed from your entries successfully")
                else:
                    print(f"Item {c} isn't found in your entries. Please fill valid date and time from your entries shown below.")
                    print(diary)
            elif choose == 4:
                print("Exited Successfully. Thanks for using our program.")
                break

                
    else:
        print("Wrong Password. Fill the exact pin you have set up before.")
    
elif pin.lower() == "no":
    print("Your personal Diary with no password generated Successfully")
    input("Press enter to begin:")
    ax = ('''--- Menu ---
1. Add New Entry
2. View All Entries
3. Remove an Entry
4. Exit''')
    while True:
        print(ax)
        choose = int(input("Enter your choice:"))
        if choose == 1:
            print("You chose to enter a new diary entry.")
            date = input("Press Enter if you want to begin your entry:")
            content = input("Write Content Here:")
            x = datetime.datetime.now()
            csk = (x.strftime("Date -%d/%m/%Y Time-%H:%M"))
            diary.update({csk: content})
            print("Diary Updated Successfully")
        elif choose == 2:
            input("Press Enter to see all entries.")
            for date, content in diary.items():
                print(f'''⭕ {date}
Content-{content}''')
        elif choose == 3:
            print("Remove any entry")
            print("Your Entries⬇")
            print(diary)
            c = input("Which entry do you want to remove? Fill exact date from your entries:")
            if c in diary:
                diary.update({c: "Removed"})
                print(f"{c} removed from your entries successfully")
            else:
                print(f"Item {c} isn't found in your entries. Please fill valid date and time from your entries shown below.")
                print(diary)
        elif choose == 4:
            print("Exited Successfully. Thanks for using our program.")
            break

                
    else:
        print("Wrong Password. Fill the exact pin you have set up before.")
else:
    print("Invalid Input received! Please fill only yes or no ")
