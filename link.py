import sqlite3

connection=sqlite3.connect('base.db')
cursor=connection.cursor()
#cursor.execute("UPDATE log_info SET Password='1234' WHERE Password='0000'")
cursor.execute("SELECT * FROM log_info")
log=cursor.fetchall()
print(log)
connection.commit()
connection.close()

