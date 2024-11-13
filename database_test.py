import mysql.connector

db = mysql.connector.connect(host="213.165.241.247",
                             user="lccs_user",
                             password="6OQBdH1TXlqD",
                             database="lccs_imogene")


mycursor = db.cursor()

mycursor.execute("SHOW DATABASES")

for x in mycursor:
  print(x)

mydb = mysql.connector.connect(
  host="213.165.241.247",
  user="lccs_user",
  password="6OQBdH1TXlqD",
  database="lccs_imogene"
)

mycursor = mydb.cursor()

#mycursor.execute("CREATE TABLE patient (id INT AUTO_INCREMENT PRIMARY KEY, fname VARCHAR(100), lname VARCHAR(100), dob date, age int(11),phone VARCHAR(55), doctor_id int(11))")
#mycursor.execute("CREATE TABLE doctor (id INT AUTO_INCREMENT PRIMARY KEY, fname VARCHAR(100), lname VARCHAR(100))")

choice = int(input("do you want to enter doc(1) or patient(2)?": ))
if choice == 1:
    DFname = input("enter doctors first name: ")
    DLname = input("enter last name: ")
else:
    PFname = input("enter patient first name: ")
    Plname = input("enter patient last name: ")
    dob = input("enter patients date of birth: ")
    age = input("enter patients age: ")
    phone = input("enter patients phone number: ")
    docId = input("enter your doctors id")
  sql = "INSERT INTO patient (PFname, Plname,dob,age,phone,docId) VALUES (%s, %s)"
  sql = "INSERT INTO patient (DFname, Dlname) VALUES (%s, %s)"
   mycursor.execute(sql)
  mydb.commit()
