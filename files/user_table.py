# Importing necessary libraries
import mysql.connector as sql

conn = sql.connect(host="localhost", user="root", passwd="mysql")


def user_table_creation():
    try:
        cur = conn.cursor()
        cur.execute("create database if not exists bank;")
        cur.execute("use bank;")
        cur.execute(
            "create table user_table(username varchar(25) primary key,passwrd varchar(25) not null )"
        )

    except Exception as error:
        print("Error while creating user table and occurred error is : ",
              error)

    finally:
        conn.close()
