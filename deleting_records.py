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

deleteId = int(input("enter id you want to delete: "))
print(deleteId)
check = input("are you sure you want to delete this id [(y) for yes (n) for no]: ")
if check == "y":
    sql = "DELETE FROM patient WHERE id = %s"
    val = (deleteId,)
    mycursor.execute(sql,val)
    mydb.commit()
    print(mycursor.rowcount, "record(s) deleted")
else:
    print("ok")