import pymysql

dbConn = pymysql.connect(
  user='admin', 
  passwd='your admin password',
  host='your RDS server endpoint',
  port=3306, 
  database='sys')
  
dbCursor = dbConn.cursor()

dbCursor.execute("SHOW DATABASES")

for dbname in dbCursor:
  print(dbname)

dbCursor.close()
dbConn.close()
