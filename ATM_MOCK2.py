print("Welcome Dear User")
allowed_users=['chukwuka',"jacobs","david"]
allowed_passwords=["chukwukapwd","jacobspwd","davidpwd"]
name=input("Enter your name:\n")
name_position= allowed_users.index(name)
if (name in allowed_users):
    user_id=input("Enter your password:\n")
   
else:
    print("System does not recognize name. Try again, please!")

if (user_id in allowed_passwords[name_position]):
     print("Welcome",name.capitalize())
else:
    print("Wrong Password. try again, please.")
from datetime import date
today=date.today()
print("Today is:",today)
import time
print("And the time is",time.strftime("%H:%M:%S:%B"))
