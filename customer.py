#customer Details
from main import *
try:

    class Customer:
        def __init__(self, db, username, password, name, age, city, phone, account_number):
            self.db = db
            self.__username = username
            self.__password = password
            self.__name = name
            self.__age = age
            self.__city = city
            self.__phone = phone
            self.__account_number = account_number

        def createuser(self):
            self.temp = self.db.db_query(f"select status from customers where username = '{self.__username}' and phone = '{self.__phone}' and account_number = '{self.__account_number}';")
            if self.temp == [] or self.temp[0][0] == 1:
                if self.temp == []:
                    self.db.db_query(
                        f"insert into customers values ('{self.__username}','{self.__password}','{self.__name}','{self.__age}','{self.__city}','{self.__phone}','{self.__account_number}',0,1);")
                    self.db.mydb.commit()
                    print(f"Your Account Create Successfully {self.__username} .")
                elif self.temp[0][0] == 1:
                    print("This Record Already Exists")
                    mobj = Main()
                    mobj.main()
            else:
                self.db.db_query(f"insert into customers values ('{self.__username}','{self.__password}','{self.__name}','{self.__age}','{self.__city}','{self.__phone}','{self.__account_number}',0,1);")
                self.db.mydb.commit()
                print(f"Your Account Create Successfully {self.__username} .")
except Exception as e:
    print("Error:-",e,"\n")

