
from customer import *
import random
from bank import *
from bank import Bank

# User Registration SignUp and SignIn
db=Database()
try:
    def SignUp():
        try:
            username = input("Create Username: ").strip()
            temp = db.db_query(f"select username from customers where username = '{username}';")
            if temp:
                print("Username Already Exists !!!")
                SignUp()
            else:
                print("Username is Available Please Proceed ->")
                password = input("Enter Your Password: ").strip()
                name = input("Enter Your Name: ").strip()
                age = int(input("Enter Your Age: "))
                city = input("Enter Your City: ").strip()
                phone= int(input("Enter the Phone Number: "))
                while True:
                    account_number = random.randint(10000000,99999999)
                    temp = db.db_query(f"select account_number from customers where account_number = '{account_number}';")
                    if temp:
                        continue
                    else:
                        break
                if len(str(phone)) == 10:
                    cobj = Customer(db,username,password,name,age,city,phone,account_number)
                    cobj.createuser()
                    bobj = Bank(username,account_number)
                    bobj.create_transaction_table()

                else:
                    print("Phone Number is not correct. Please Enter 10 digit Phone Number\n")
                    pass
        except Exception as e:
            print("Error Occur In SignUp:-",e,"\n")
    def SignIn():
        try:
            print("\n SignIn By ->\n 1.UserName and Password \n 2.UserName and AccountNumber :")
            ch = int(input(""))
            if ch==1:
                username = input("Enter Username: ").strip()
                password = input("Enter the Password: ").strip()
                temp = db.db_query(f"select username from customers where username = '{username}' and password = '{password}';")
                status_check = db.db_query(f"select status from customers where username = '{username}' and password = '{password}';")
                if temp:
                    if status_check[0][0] == 1:
                        print(f"SignIn successfully !!\n")
                        return username
                    else:
                        print("This Account Deactive.\n")
                else:
                    print("Username and Password are Wrong, Try Again !\n")
                    SignIn()
            elif ch==2:
                username = input("Enter Username: ").strip()
                account_number = input("Enter the Account Number: ").strip()
                temp = db.db_query(f"select username from customers where username = '{username}' and account_number = '{account_number}';")
                status_check = db.db_query(f"select status from customers where username = '{username}' and account_number = '{account_number}';")
                if temp:
                    if status_check[0][0] == 1:
                        print(f"SignIn successfully !!\n")
                        return username
                    else:
                        print("This Account Deactive.\n")
                else:
                    print("Username and Account Number are Wrong, Try Again !\n")
                    SignIn()
            else:
                print("Please Enter Valid Input From Options!!\n")
                SignIn()
        except Exception as e:
            print("Error Occur in SingIn :- ",e)

    def Deactive_account():
        Customer_name = input("Enter The Customer Name: ").strip()
        Customer_account_number = int(input("Enter The Customer Account Number: "))
        temp = db.db_query(f"select balance from customers where username = '{Customer_name}' and account_number = '{Customer_account_number}';")

        if temp[0][0] == 0:
            db.db_query(f"update customers set status = 0 where account_number = '{Customer_account_number}';")
            db.mydb.commit()
            print("Account Successfully Deactived !!\n")

        else:
            print("First Of All Withdraw All Money.\n")

except Exception as e:
    print("Error:-",e,"\n")