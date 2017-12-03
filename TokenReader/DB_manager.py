#!/usr/bin/python
from mysql.connector import MySQLConnection, Error
from sys import version_info
from enum import Enum

'''
msgbox = None

if version_info[0] < 3:
	import tkinter,tk.messagebox
	msgbox = tk.messagebox()
else:
	from tkinter import messagebox
	msgbox = messagebox
'''


class DatabaseUtility:
    ConnectionStringArgs={}
    class CmdType(Enum):
        SelectOne = 1
        SelectAll = 2
        InsertOne = 3
        InsertMany = 4

    def setMySQLConnection(self, host, database, user, password, port='3306'):
        self.ConnectionStringArgs['host'] = host
        self.ConnectionStringArgs['database'] = database
        self.ConnectionStringArgs['user'] = user
        self.ConnectionStringArgs['password'] = password
        self.ConnectionStringArgs['port'] = int(port)

    def __init__(self, host, database, user, password,port):
        self.setMySQLConnection(host, database, user, password, port)
        try:
            # self.conn.config(**self.ConnectionStringArgs)
            self.conn = MySQLConnection(**self.ConnectionStringArgs)
            self.cursor = self.conn.cursor()
        except Error as err:
            raise Error("Error Message : " + str(err.msg))

    def GetTable(self, tblName, withColumnName=True):
        result = self.RunCommand("SELECT * FROM %s;" % tblName)
        if withColumnName == True:
            return result
        else:
            return result[0]

    def GetTableColumn(self, tblName, ColumnName, withColumnName=True):
        qur = "SELECT {0} FROM {1}".format(ColumnName, tblName)
        result = self.RunCommand(qur)
        if withColumnName == True:
            return result
        else:
            return result[0]

    def GetColumns(self, tblName):
        return self.RunCommand("SHOW COLUMNS FROM %s;" % tblName)

    def GetCursor(self):
        return self.conn.cursor()

    def RunCommand(self, cmd):
        try:
            if not self.conn.is_connected():
                self.conn._open_connection()
                self.cursor = self.conn.cursor()

            self.cursor.execute(cmd)
            rows = self.cursor.fetchall()
            if len(rows) == 1:
                rows = rows[0]

            columnName = self.cursor.column_names
        except Error as err:
            raise Error('ERROR MESSAGE: ' + str(err.msg))
        finally:
            self.cursor.close()
            self.conn.close()

        return rows, columnName

    def SelectCommand(self, cmdText):
        try:
            if not self.conn.is_connected():
                self.conn._open_connection()
                self.cursor = self.conn.cursor()

            self.cursor.execute(cmdText)
            rows = self.cursor.fetchall()
            if len(rows) == 1:
                rows = rows[0]

        except Error as err:
            raise Error('ERROR MESSAGE: ' + str(err.msg))
        finally:
            self.cursor.close()
            self.conn.close()

        return rows

    def InsertCommand(self, cmd, args=None, InsertMode=None):
        try:
            if not self.conn.is_connected():
                self.conn._open_connection()
                self.cursor = self.conn.cursor()

            msg = None
            if InsertMode == self.CmdType.InsertOne:
                self.cursor.execute(cmd, args)
            elif InsertMode == self.CmdType.InsertMany:
                msg = self.cursor.executemany(cmd, args)
            else:
                self.cursor.execute(cmd)

            self.conn.commit()
            # return msg
        except Error as err:
            raise Error('ERROR MESSAGE: ' + str(err.msg))
        finally:
            self.cursor.close()
            self.conn.close()

    def ExecuteStoredProcedure(self, ProcedureName, in_args=None):
        try:
            if not self.conn.is_connected():
                self.conn._open_connection()
                self.cursor = self.conn.cursor()

            Out_args = self.cursor.callproc(ProcedureName, in_args)

            self.conn.commit()
        except Error as err:
            raise Error('ERROR MESSAGE: ' + str(err.msg))
        finally:
            self.cursor.close()
            self.conn.close()
        return Out_args

    def __del__(self):
        self.cursor.close()
        self.conn.close()
