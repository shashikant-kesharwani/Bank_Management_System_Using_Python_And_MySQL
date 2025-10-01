import mysql.connector as sql
try:
    class Database:
        def __init__(self):
            self.mydb = sql.connect(
                host="localhost",
                user='root',
                passwd='2002',
                database='bank'
            )
            self.cursor = self.mydb.cursor()
            self.createcustomertable()
        def createcustomertable(self):
            self.cursor.execute('''
            create table if not exists customers(
            username varchar(30) not null,
            password varchar(20) not null,
            name varchar(30) not null, 
            age integer not null,
            city varchar(30) not null, 
            phone bigint not null,
            account_number integer primary key not null,
            balance bigint,
            status boolean)
            ''')
            self.mydb.commit()

        def db_query(self,query):
            self.cursor.execute(query)
            result = self.cursor.fetchall()
            return result
except Exception as e:
    print(f"Error :- {e} \n ")

