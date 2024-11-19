import mysql.connector

mydb = mysql.connector.connect(
  host="213.165.241.247",
  user="lccs_user",
  password="6OQBdH1TXlqD",
  database="lccs_imogene"
)
mycursor = mydb.cursor()



mycursor.execute("SELECT * FROM patient")
myresults = mycursor.fetchall()
for i in myresults:
    print(i)




changeId = int(input("enter patient id: "))
lname = input("enter new name: ")
sql = "UPDATE patient SET lname = %s WHERE id = %s"
val = (lname,changeId)
mycursor.execute(sql,val)
mydb.commit()
print(mycursor.rowcount, "record(s) affected")


mycursor.execute("SELECT * FROM patient")
myresults = mycursor.fetchall()
for i in myresults:
    print(i)

