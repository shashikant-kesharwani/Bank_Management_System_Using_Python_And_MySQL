from register import *
from bank import *
# print Welcome
try:
    class Main:
        def main(self):
            try:
                print("*** Welcome to Local Gramin Bank ***")
                while True:
                    self.register = int(input("1. SignUp\n"
                                         "2. SignIn\n3. Deactive Customer\n4. Exit Program\n"))
                    if self.register >= 1 or self.register <=4:
                        if self.register == 1:
                            SignUp()
                        elif self.register == 2:
                            self.username = SignIn()
                            if self.username:
                                self.facility(self.username)
                            else:
                                continue
                        elif self.register == 3:
                            Deactive_account()
                        elif self.register == 4:
                            print("Thanku For Visiting !!!")
                            exit()
                        else:
                            print("Please Enter Valid Input From Options!!\n")
                    else:
                        print("Please Enter Valid Input From Options!!\n")
            except ValueError:
                print("Invalid Input Try Again With Number !!\n")
                return mobj.main()
        def facility(self,username):
            try:
                self.username=username
                self.account_number = db.db_query(f"select account_number from customers where username='{self.username}';")
                while True:
                    self.choice = int(input("1. Balance Enquiry\n"
                                       "2. Cash Deposit\n"
                                       "3. Cash Withdraw\n"
                                       "4. Money Transfer\n"
                                       "5. Sign Out\n"
                                       ))
                    self.bobj = Bank(self.username, self.account_number[0][0])
                    if self.choice >= 1 and self.choice <= 5:
                        if self.choice == 1:
                            self.bobj.balance_enquiry()
                        elif self.choice == 2:
                            self.amount = int(input("Enter the Amount: "))
                            self.bobj.deposite(self.amount)
                        elif self.choice == 3:
                            self.amount = int(input("Enter the Amount: "))
                            self.bobj.withdraw(self.amount)
                        elif self.choice == 4:
                            while True:
                                self.receiver_name = input("Enter The Receiver Name: ").strip()
                                self.receiver_account_number = int(input("Enter The Account Number: "))
                                self.temp = db.db_query(f"select account_number from customers where username='{self.receiver_name}' and account_number = '{self.receiver_account_number}';")
                                if self.temp:
                                    self.amount = int(input("Enter the Amount: "))
                                    self.bobj.transfer_money(self.amount,self.receiver_name,self.receiver_account_number )
                                    break
                                else:
                                    print("Not Present This Person , Plz Check Reciever Name and Account Number Is Correct.")
                                    print("Please Try Again!!!\n")
                                    self.back = input("Do You Want To Back -> yes/no:").strip().lower()

                                    if self.back == "yes":
                                        break
                                    else:
                                        continue

                        elif self.choice == 5:
                            print("Sign Out Successfully !!!\n")
                            self.main()

            except Exception as e:
                print("Error :- ",e,"\n")
except Exception as e:
    print(f"Error:- {e}\n")

if __name__ == "__main__":
    try:
        db = Database()
        mobj = Main()
        mobj.main()
    except Exception as e:
        print("Error Occur in Main:- ",e,"\n")
