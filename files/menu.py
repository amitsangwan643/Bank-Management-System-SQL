import datetime as dt
import mysql.connector as sql
conn = sql.connect(host='localhost', user='root',
                   passwd='mysql', database='bank')
cur = conn.cursor()


conn.autocommit = True
c = 'n'
while c == 'n':

    print('\n1.CREATE BANK ACCOUNT', end="\n\n")

    print('2.TRANSACTION', end="\n\n")

    print('3.CUSTOMER DETAILS', end="\n\n")

    print('4.TRANSACTION DETAILS', end="\n\n")

    print('5.DELETE ACCOUNT', end="\n\n")

    print('6.QUIT', end="\n\n")

    n = int(input('Enter your CHOICE='))
    print()

    if n == 1:

        acc_no = int(input('Enter your ACCOUNT NUMBER='))
        print()
        acc_name = input('Enter your ACCOUNT NAME=')
        print()
        ph_no = int(input('Enter your PHONE NUMBER='))
        print()
        add = (input('Enter your place='))
        print()
        cr_amt = int(input('Enter your credit amount='))
        V_SQLInsert = "INSERT  INTO customer_details values (" + str(
            acc_no) + ",' " + acc_name + " ',"+str(ph_no) + ",' " + add + " '," + str(cr_amt) + " ) "
        cur.execute(V_SQLInsert)

        print('\nAccount Created Succesfully!!!!!')
        conn.commit()

    if n == 2:
        acct_no = int(input('Enter Your Account Number='))
        cur.execute(
            'select * from customer_details where acct_no='+str(acct_no))
        data = cur.fetchall()
        count = cur.rowcount
        conn.commit()
        if count == 0:

            print('\nAccount Number Invalid Sorry Try Again Later', end="\n\n")

        else:

            print('\n1.WITHDRAW AMOUNT', end="\n\n")

            print('2.ADD AMOUNT', end="\n\n")

            x = int(input('Enter your CHOICE='))
            print()
            if x == 1:
                amt = int(input('Enter withdrawl amount='))
                cr_amt = 0
                cur.execute('update customer_details set   cr_amt=cr_amt-' +
                            str(amt) + ' where acct_no=' + str(acct_no))
                V_SQLInsert = "INSERT  INTO transactions values ({} , '{}' , {} , {}) ".format(
                    acct_no, dt.datetime.now(), amt, cr_amt)
                cur.execute(V_SQLInsert)
                conn.commit()

                print('\nAccount Updated Successfully!!!!!')

            if x == 2:
                amt = int(input('Enter amount to be added='))
                cr_amt = 0
                cur.execute('update customer_details set  cr_amt=cr_amt+' +
                            str(amt) + ' where acct_no=' + str(acct_no))
                V_SQLInsert = "INSERT  INTO transactions values ({} , '{}' , {} , {}) ".format(
                    acct_no, dt.datetime.now(), cr_amt, amt)
                cur.execute(V_SQLInsert)
                conn.commit()

                print('\nAccount Updated Successfully!!!!!')

    if n == 3:
        acct_no = int(input('Enter your account number='))
        print()
        cur.execute(
            'select * from customer_details where acct_no='+str(acct_no))
        if cur.fetchone() is None:

            print('\nInvalid Account number')
        else:
            cur.execute(
                'select * from customer_details where acct_no='+str(acct_no))
            data = cur.fetchall()
            for row in data:
                print('ACCOUNT NO=', acct_no, end="\n\n")

                print('ACCOUNT NAME=', row[1], end="\n\n")

                print('PHONE NUMBER=', row[2], end="\n\n")

                print('ADDRESS=', row[3], end="\n\n")

                print('cr_amt=', row[4], end="\n\n")
    if n == 4:
        acct_no = int(input('Enter your account number='))
        print()
        cur.execute(
            'select * from customer_details where acct_no='+str(acct_no))
        if cur.fetchone() is None:

            print('\nInvalid Account number')
        else:
            cur.execute(
                'select * from transactions where acct_no='+str(acct_no))
            data = cur.fetchall()
            for row in data:
                print('ACCOUNT NO=', acct_no, end="\n\n")

                print('TIME=', row[1], end="\n\n")

                print('WITHDRAWAL AMOUNT=', row[2], end="\n\n")

                print('AMOUNT ADDED=', row[3], end="\n\n")

    if n == 5:
        print('DELETE YOUR ACCOUNT')
        acct_no = int(input('Enter your account number='))

        cur.execute('delete from customer_details where acct_no='+str(acct_no))
        print('ACCOUNT DELETED SUCCESFULLY')

    if n == 6:
        print('DO YO WANT TO EXIT(y/n)')
        c = input('enter your choice=')


else:
    print('THANK YOU PLEASE VISIT AGAIN')
    quit()
