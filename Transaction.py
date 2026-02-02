import time as t
import mysql.connector


def withdrawl():
    con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="your password", #enter your password
    use_pure=True,
    database="your database" #enter your database name
    )
    cur = con.cursor()
    id=int(input("enter id no."))
    amount=float(input("enter amount"))
    debit=float(input("enter amount to be debit"))
    final_amount=amount-debit
    sql="INSERT INTO PASSBOOK (id,amount,debit)VALUES(%s,%s,%s)"
    values=(id,amount,debit)
    cur.execute(sql, values)
    con.commit()

    print("✅ Data successfully inserted into passbook table!")
    final_amount=amount-debit
    name=str(id)
    current_time=t.ctime()
    f = open(name + ".txt", "w")
    data=f.write(f'''
    Time: {current_time}

    id: {id}
    amount: {amount}
    debit: {debit}
    ---------------------5
    final amount:  {final_amount}''')
    f.close()
    cur.close()
    con.close() 
     
def deposit():
    con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="your password", #enter your password
    use_pure=True,
    database="your database"#enter your database name
    )
    cur = con.cursor()
    id=int(input("enter id no."))
    amount=float(input("enter amount"))
    credit=float(input("enter amount to be credit"))
    final_amount=amount+credit
    sql="INSERT INTO PASSBOOK (id,amount,credit)VALUES(%s,%s,%s)"
    values=(id,amount,credit)
    cur.execute(sql, values)
    con.commit()

    print("✅ Data successfully inserted into passbook table!")
    final_amount=amount+credit
    name=str(id)
    current_time=t.ctime()
    f = open(name + ".txt", "w")
    data=f.write(f'''
    Time: {current_time}

    id: {id}
    amount: {amount}
    credit: {credit}
    ---------------------5
    final amount:  {final_amount}''')
    f.close()
    cur.close()
    con.close()   

print("press1 for withdrawl, press2 for deposit")

choice=int(input("enter your choice:"))
if choice==1:
    withdrawl()
elif choice==2:
    deposit()
else:
    print("invalid choice")        
