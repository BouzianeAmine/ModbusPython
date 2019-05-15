from interface import implements, Interface
#import mysql.connector as mysql
HOST="localhost"
USER="root"
PASS="admin"
DBNAME="amine"

class DBConnect(Interface):
    def connect(self):
        pass
    
class MySqlConnection(implements(DBConnect)):
    def connect(self):
        # return mysql.connect(host=HOST,user=USER,passwd=PASS,database=DBNAME)
        print("Mysql")
class SQLServerConnection(implements(DBConnect)):
    def connect(self):
        #return sqlServer package
        print("SQL Server")
        
print(MySqlConnection().connect())
