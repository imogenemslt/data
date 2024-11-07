import csv
heading = ["make","model","reg"]
file = open("mygarage.csv","a",newline = "")
db = csv.writer(file)
db.writerow(heading)
file.close()
data1 = input("what make is the vhical")
db.writerow(data1)
data2 = input("what model is the vhical")
db.writerow(data2)
data3 = input("what reg is the vihical")
db.writerow(data3)



import csv
# heading = ["make","model","reg"]
# file = open("mygarage.csv","a",newline = "")
# db = csv.writer(file)
# db.writerow(heading)
# file.close()
# data = []
# data1 = input("what make is the vehicle: ")
# data.append(data1)
# data2 = input("what model is the vehicle: ")
# data.append(data2)
# data3 = input("what reg is the vehicle: ")
# data.append(data3)
# file = open("mygarage.csv","a",newline = "")
# db = csv.writer(file)
# db.writerow(data)
# file.close()
# 
#

file = open("mygarage.csv","r")
data = list(csv.reader(file))
file.close()
print("make\t model\t\t reg\t")
print("-----------------------------------------")
for i in data[1:]:
    print(data[1],data[2],data[3])
