import os
print('''--- Personal Notes Saver ---''')
input("Press Enter to access Menu:")
print("""1. Add a Note
2. View Notes
3. Delete All Notes
4. Exit""")
name=input("Enter your name:")
while True:
    choose=int(input("Enter a choice:"))
    if choose==1:
        content=input("Enter your content here:")
        print("Notes Saved...☑")
        with open(f"{name}.txt","a") as f:
            f.write((content) + "\n")
    elif choose==2:
        input("Press Enter to view notes:")
        with open(f"{name}.txt","a") as f:
            content = f.read()
            print(content)
    elif choose==3:
        c2=input("Enter 12 to confirm if you want to delete all notes:")
        if c2=="12":
            os.remove(f"{name}.txt")
            print("File remove succesfully")
        else:
            print("Invalid Input Recived Please Press 12 to confirm")
            
    elif choose==4:
        print("Exited Successfully.")
        print("Thankyou for using our program")
        break
    
    else:
        print("Invald Input recived please select from 1,2,3 or 4")
    
    
        

            

