import DBConnect;
from interface import implements, Interface

class DBInsert(Interface):
    def insert(self,req,val=None):
        pass
    
class MysqlInsert(implements(DBInsert)):
    def insert(self,req,val=None):
        tempDB=MySqlConnection().connect();
        mycursor = tempDB.cursor(prepared=True);
        if val!=None:
            mycursor.execute(sql, val);
        else :
            mycursor.execute(sql);
        tempDB.connect().commit();
        

