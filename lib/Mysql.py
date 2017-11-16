# -*- coding: utf-8 -*-
'''
Created on 2015年6月14日

@author: Administrator
'''
import MySQLdb
class Mysql(object):
    def __init__(self, host, port, user, pwd, db, charset):
        self._db = MySQLdb.connect(host=host, user=user, passwd=pwd, db=db, charset=charset)
        self._cursor = self._db.cursor()
    def query(self, sql):
        try:
            count = self._cursor.execute(sql)
            if count > 0:
                result = self._cursor.fetchall()
                return result
            return None
        except Exception, ex:
            self._db.rollback()
            self._logger.error(str(ex))
        return None
    def queryOne(self, sql):
        try:
            count = self._cursor.execute(sql)
            if count > 0:
                results = self._cursor.fetchone()
                return results
            return None
        except Exception, ex:
            self._db.rollback()
            self._logger.error(str(ex))
        return None
        pass
    
    def insert(self, sql):
        try:
            self._cursor.execute(sql)
            self._db.commit()
            return True
        except Exception, ex:
            self._db.rollback()
            print str(ex)
            return False    
    def close(self):
        self._db.close()
    def commit(self):
        self._db.commit()
def main():
    tableNames = []
    allColumns = []
    allColumnSupper = []
    mysql = Mysql("127.0.0.1", 3306, "root", "root", "logic", "utf8")
    tables = mysql.query("show tables")
    for t in tables:
        tableName = t[0]
        tableNames.append(tableName)
        columns = mysql.query("show COLUMNS from %s"%(t[0]))
        for c in columns:
            if c[0] != "":
                column = str(c[0]);
                print column
                allColumns.append(column)
                allColumnSupper.append((tableName+"_"+column).upper())
#         print columns
    print tableNames
    print allColumns
    print allColumnSupper

    pass
if __name__ == '__main__':
    main()
