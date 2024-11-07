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




