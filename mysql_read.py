print ('Mysql')

import mysql.connector

dbconnection = mysql.connector.connect(
        host='localhost', 
        user= 'root'
        password='password'
        database='pythondb'

)

mycursor = dbconnection.cursor()
mycursor.execute('SELECT * FROM PERSONS')
alleregels = mycursor.fetchall()

print(alleregels)