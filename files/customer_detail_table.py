import mysql.connector as sql
conn = sql.connect(host='localhost', user='root',
                   passwd='mysql')


def customer_table_creation():
    try:
        cur = conn.cursor()
        cur.execute("create database if not exists bank;")
        cur.execute("use bank;")
        cur.execute('create table customer_details(acct_no int primary key,acct_name varchar(25) ,phone_no bigint(25) check(phone_no>11),address varchar(25),cr_amt float )')

    except Exception as error:
        print("Error while creating user table and occurred error is : ", error)

    finally:
        conn.close()
