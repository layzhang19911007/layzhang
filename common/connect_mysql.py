import pymysql
dbinfo = {
    "host":"49.235.92.12",
    "port":3309,
    "username":"root",
    "password":"123456",
    "cursorclass":pymysql.cursors.DictCursor
}
class DbConnect():
    """连接数据库"""
    def __init__(self,database,dbinfo):
        self.db = pymysql.connect(database=database,**dbinfo)
        self.dbcur = self.db.cursor()
    def select(self,sql):
        self.dbcur.execute(sql)
        result = self.dbcur.fetchall() #获取数据库查询的数据
        return result
    def updatedb(self,sql):
        try:
            self.dbcur.execute(sql)
            self.db.commit()
        except:
            self.db.rollback()
    def close(self):
        self.dbcur.close()
        self.db.close()
if __name__ == "__main__":
    db = DbConnect("apps",dbinfo)
    sql1 = "SELECT * from apiapp_goods;"
    r = db.select(sql1)
    print(len(r))
    sql2 = "UPDATE  apiapp_goods set goodsname = 'layzhang' where id = 12;"
    db.updatedb(sql2)
    db.close()