# Importing Necessary Libraries
import datetime as dt
import mysql.connector as sql
from files.user_table import user_table_creation
from files.transaction_table import transaction_table_creation
from files.customer_detail_table import customer_table_creation

user_table_creation()           # To create user table if not exists already
customer_table_creation()       # To create customer details table if not exists already
transaction_table_creation()    # To create transaction table if not exists already

conn = sql.connect(host='localhost', user='root',
                   passwd='mysql', database='bank')
cur = conn.cursor()

print('========================= WELCOME TO BANK =========================')
print(dt.datetime.now())
print('1.REGISTER',end="\n\n")
print('2.LOGIN',end="\n\n")


n = int(input('enter your choice='))
print()

if n == 1:
    name = input('Enter a Username=')
    print()
    passwd = int(input('Enter a 4 DIGIT Password='))
    print()
    V_SQLInsert = "INSERT  INTO user_table (passwrd,username) values (" + str(
        passwd) + ",' " + name + " ') "
    cur.execute(V_SQLInsert)
    conn.commit()
    print()
    print('USER created succesfully')
    import files.menu

if n == 2:
    name = input('Enter your Username=')
    print()
    passwd = int(input('Enter your 4 DIGIT Password='))
    V_Sql_Sel = "select * from user_table where passwrd='" + \
        str(passwd)+"' and username=  ' " + name + " ' "
    cur.execute(V_Sql_Sel)
    if cur.fetchone() is None:
        print()
        print('Invalid username or password')
    else:
        print()
        import files.menu
