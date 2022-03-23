import mysql.connector as sql
conn = sql.connect(host='localhost', user='root',
                   passwd='mysql')


def transaction_table_creation():
    try:
        cur = conn.cursor()
        cur.execute("create database if not exists bank;")
        cur.execute("use bank;")
        cur.execute(
            'create table transactions(acct_no int(11),date datetime ,withdrawal_amt bigint(20),amount_added bigint(20) )')
        conn.close()

    except Exception as error:
        print("Error while creating user table and occurred error is : ", error)

    finally:
        conn.close()
