print("Welcome Dear User")
allowed_users=['chukwuka',"jacobs","david"]
allowed_passwords=["chukwukapwd","jacobspwd","davidpwd"]
name=input("Enter your name:\n")
if (name in allowed_users):
    print("Welcome",name.capitalize())
    user_id=("Enter your password:\n")

else:
    print('Try again')
from datetime import date
today=date.today()
print("Today is:",today)
import time
print("And the time is",time.strftime("%H:%M:%S"))
print("")
username=int(input("What do you want to do?"))