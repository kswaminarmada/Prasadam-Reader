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
	ConnectionStringArgs = {'host': '', 'database': '', 'user': '', 'password': '', 'port': 3306}
	class CmdType(Enum):
		SelectOne = 1
		SelectAll = 2
		InsertOne = 3
		InsertMany = 4
	
	def setMySQLConnection(self,host,database,user,pwd):
		self.ConnectionStringArgs['host'] = host
		self.ConnectionStringArgs['database'] = database
		self.ConnectionStringArgs['user'] = user
		self.ConnectionStringArgs['password'] = pwd

	def __init__(self,host, database,user,pwd):
		self.setMySQLConnection(host,database,user,pwd)
		try:
			#self.conn.config(**self.ConnectionStringArgs)
			self.conn = MySQLConnection(**self.ConnectionStringArgs)
			self.cursor = self.conn.cursor()
		except Error as err:
			raise Error("Error Message : "+ str(err.msg))
			
	def GetTable(self,tblName):
		return self.RunCommand("SELECT * FROM %s;" % tblName)

	def GetColumns(self,tblName):
		return self.RunCommand("SHOW COLUMNS FROM %s;" % tblName)

	def RunCommand(self, cmd):
		try:
			if not self.conn.is_connected():
				self.conn._open_connection()
				self.cursor = self.conn.cursor()
			
			self.cursor.execute(cmd)
			
			msg = None
			
			try:
				msg = self.cursor.fetchall()
			except:
				msg = self.cursor.fetchone()
				
			#return msg
		except Error as err:
			print ('ERROR MESSAGE: ' + str(err.msg))
		finally:
			self.cursor.close()
			self.conn.close()
		
		return msg
	
	def SelectCommand(self, cmd, SelectMode):
		try:
			if not self.conn.is_connected():
				self.conn._open_connection()
				self.cursor = self.conn.cursor()
			
			self.cursor.execute(cmd)
			
			msg = None
			if SelectMode == self.CmdType.SelectAll:
				msg = self.cursor.fetchall()
			elif SelectMode == self.CmdType.SelectOne:
				msg = self.cursor.fetchone()
			else:
				msg = None
				raise ValueError("Invalid SelectMode")
				
			#return msg
		except Error as err:
			raise Error('ERROR MESSAGE: ' + str(err.msg))
		finally:
			self.cursor.close()
			self.conn.close()
		
		return msg
		
	def InsertCommand(self, cmd, args=None):
		#print ("RUNNING COMMAND: " + cmd)
		try:
			if not self.conn.is_connected():
				self.conn._open_connection()
				self.cursor = self.conn.cursor()

			msg = None
			if SelectMode == self.CmdType.InsertOne:
				self.cursor.execute(cmd,args)
			elif SelectMode == self.CmdType.InsertMany:
				msg = self.cursor.executemany(cmd,args)
			else:
				self.cursor.execute(cmd)
			
			self.conn.commit()	
			#return msg
		except Error as err:
			raise Error('ERROR MESSAGE: ' + str(err.msg))
		finally:
			self.cursor.close()
			self.conn.close()
		
	def ExecuteStoredProcedure(self,ProcedureName,in_args=None):
		try:
			if not self.conn.is_connected():
				self.conn._open_connection()
				self.cursor = self.conn.cursor()
			
			Out_args = self.cursor.callproc(ProcedureName,in_args)
			
			self.conn.commit()
		except Error as err:
			raise Error('ERROR MESSAGE: ' + str(err.msg))
		finally:
			self.cursor.close()
			self.conn.close()	
		return Out_args

	def __del__(self):
		self.conn.commit()
		self.cursor.close()
		self.conn.close()
