from datetime import datetime
from database import *
from datetime import *
from register import *

db = Database()
try:
    class Bank:
        def __init__(self,username,account_number):
            self.__username=username
            self.__account_number=account_number


        def create_transaction_table(self):
            db.db_query(f"create table if not exists {self.__account_number}_transaction ("
                     f"timedate varchar(30),"
                     f"account_number integer,"
                     f"remarks text,"
                     f"amount integer);")

        def balance_enquiry(self):
            self.balance = db.db_query(f"select balance from customers where username = '{self.__username}' and account_number = '{self.__account_number}'; ")
            print("Your Total Balance : ",self.balance[0][0]," Rupees.\n")
        def deposite(self,amount):
            self.amount=amount
            self.__temp = db.db_query(f"select balance from customers where username = '{self.__username}' and account_number = '{self.__account_number}';")
            self.__temp = self.__temp[0][0] + self.amount
            db.db_query(f"update customers set balance = '{self.__temp}' where account_number = '{self.__account_number}';")
            db.db_query(f"insert into {self.__account_number}_transaction values('{datetime.now()}','{self.__account_number}','Amount Deposite','{self.amount}');")
            db.mydb.commit()
            print(f"{self.amount} Rupees Successfully Deposite.\n" )
            self.balance_enquiry()

        def withdraw(self,amount):
            self.amount=amount
            self.__temp = db.db_query(f"select balance from customers where username = '{self.__username}' and account_number = '{self.__account_number}';")
            if self.__temp[0][0] >= self.amount:
                self.__temp = self.__temp[0][0] - self.amount
                db.db_query(f"update customers set balance = '{self.__temp}' where account_number = '{self.__account_number}';")
                db.db_query(f"insert into {self.__account_number}_transaction values('{datetime.now()}','{self.__account_number}','Amount Withdraw','{self.amount}');")
                db.mydb.commit()
                print(f"{self.amount} Rupees Successfully Withdraw.\n")
                self.balance_enquiry()
            else:
                print("Money Not Efficient In Your Account!!!")
                print("Transaction Fail !!\n")


        def transfer_money(self,amount,reciever_name,recierver_account_number):
            self.amount = amount
            self.__reciever_name = reciever_name
            self.__reciever_account_number = recierver_account_number
            self.__temp = db.db_query(f"select balance from customers where username = '{self.__username}' and account_number = '{self.__account_number}';")
            if self.__temp[0][0] >= self.amount:
                self.__temp = self.__temp[0][0] - self.amount
                db.db_query(f"update customers set balance = '{self.__temp}' where account_number = '{self.__account_number}';")
                db.db_query(f"insert into {self.__account_number}_transaction values('{datetime.now()}','{self.__account_number}','Amount Transfer In {self.__reciever_account_number}',{self.amount});")

                self.__temp1 = db.db_query(f"select balance from customers where username = '{self.__reciever_name }' and account_number = '{self.__reciever_account_number}';")
                self.__temp1 = self.__temp1[0][0] + self.amount
                db.db_query(f"update customers set balance = '{self.__temp1}' where account_number = '{self.__reciever_account_number}';")
                db.db_query(f"insert into {self.__reciever_account_number}_transaction values('{datetime.now()}','{self.__reciever_account_number}','Amount Recieved From {self.__account_number}',{self.amount});")
                db.mydb.commit()
                print(f"{self.amount} Rupees Successfully Send.\n")
                self.balance_enquiry()
            else:
                print("Money Not Efficient In Your Account!!!")
                print("Transaction Fail !!\n")
except Exception as e:
    print("Error:- ",e,"\n")