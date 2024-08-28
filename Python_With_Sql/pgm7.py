import mysql.connector as ms #module aliasing

#using the created database
mydb = ms.connect(host="localhost",user="root",password="Krishna@123",database="HOSPITAL")

#object - cursor
mycur = mydb.cursor()

print("WELCOME")
#id, name, which role, what is their salary

#taking inputs
id = input("Enter your id: ")
