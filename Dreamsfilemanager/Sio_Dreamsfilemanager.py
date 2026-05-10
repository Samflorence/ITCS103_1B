import os

while True:
    print("-------[ Dreams File Manager ]-------\n")
    print("1. Read inspiring message")
    print("2. Add a new inspiring message")
    print("3. Rewrite the entire file")
    print("4. Exit")
    
    num = (input("Enter your choice: "))

    if num == "1":
        file = open("message.txt", "r")
        content = file.read()
        file.close()
        print("---[ Inspiring message ]---")
        print(content)
        input("Press Enter to continue: ")
        os.system("clear")
        continue

    if num == "2":
        file = open("message.txt", "a")
        file.write("\n"+input("Enter your new aspiring line:\n"))
        file.close()
        print("Your new aspiring line has successfully added")
        input("Press Enter to continue: ")
        os.system("clear")
        continue

    if num == "3":
        print("Warning: This will overwite the file")
        choose = input("Type yes to continue:").lower()
        if choose == "yes":
            file = open("message.txt", "w")
            file.write(input("write your new set of inspiring message:\n"))
            file.close()
            print("Successfully overwritten")
            input("Press Enter to continue: ")
            os.system("clear")
            continue
        if choose == "no":
            break
        else:
            input("Please choose between (YES/NO:) ").lower()
            continue

    if num == "4":
        break

    else:
        print("Please try again")
