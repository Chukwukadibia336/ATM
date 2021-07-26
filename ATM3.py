# A MOCK ATM MACHINE
print("Welcome Dear User")
allowed_users=['chukwuka',"jacobs","david"]
allowed_passwords=["chukwukapwd","jacobspwd","davidpwd"]
name=input("Enter your name:\n")
balance=0
if (name in allowed_users):
    name_position= allowed_users.index(name)
    user_id=input("Enter your password:\n")
    if(user_id == allowed_passwords[name_position]):
        print("Welcome",name.capitalize())
        from datetime import date
        today=date.today()
        print("Today is:",today)
        import time
        print("And the time is",time.strftime("%H:%M:%S\n\n"))
        print("1: How much will you like to withdraw?\n2: How much will you like to deposit?\n3: Complaints ")
        option=int(input("Enter choice here:\n"))
        if(option==1):
            amount=int(input("How much would you like to withdraw\n"))
            print("Take your cash")
        elif(option==2):
            deposit=int(input("How much would you like to deposit?\n"))
            print("Your current balance is:",balance+deposit)
        elif(option==3):
            complaint=input("What issue will you like to report?\n")
            print("Thank you for contacting us")   
        else:
            print("Invalid Selection!")     
    else:
        print("Wrong Password. try again, please.")
else:
    print("System does not recognize name. Try again, please!")


