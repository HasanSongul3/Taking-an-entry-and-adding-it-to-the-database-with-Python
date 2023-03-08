import sqlite3 as sql

#Creating a database file
con = sql.connect("users.db")

#Creating table
cursor = con.cursor()
cursor.execute("""CREATE TABLE  IF NOT EXISTS peoples(name TEXT,lastname TEXT,age INTEGER)""")

#İnputs
name = input("Enter Your Name: ")
lastname = input("Enter Your Lastname: ")
age = int(input("Enter Your Age: "))

#Adding infos to database
cursor.execute(f"""INSERT INTO peoples VALUES(?,?,?)""",(name,lastname,age))

print(f"Welcome {name} {lastname}")

con.commit()
con.close()
