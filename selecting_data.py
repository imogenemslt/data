import mysql.connector

mydb = mysql.connector.connect(
  host="213.165.241.247",
  user="lccs_user",
  password="6OQBdH1TXlqD",
  database="lccs_imogene"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM doctor")

myresults = mycursor.fetchall()

for i in myresults:
    print(i)
    
mycursor.execute("SELECT * FROM patient WHERE doctor_id = 2")
myresult = mycursor.fetchall()
for i in myresult:
    print(i)