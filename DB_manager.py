#!/usr/bin/python
from mysql.connector import MySQLConnection, Error
from sys import version_info
from enum import Enum

msgbox = None

if version_info[0] < 3:
	import tkinter,tk.messagebox
	msgbox = tk.messagebox()
else:
	from tkinter import messagebox
	msgbox = messagebox

class DatabaseUtility: 
	ConnectionStringArgs = {'host': '', 'database': '', 'user': '', 'password': ''}
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
			self.conn = MySQLConnection(**self.ConnectionStringArgs)
			self.cursor = self.conn.cursor()
		except Error as err:
			global msgbox
			raise Error("MySQL Error",str(err.msg))
			#msgbox.showerror("MySQL Error",str(err.msg))
			#print("Error Message : " + str(err.msg))

	def GetTable(self,tblName):
		return self.RunCommand("SELECT * FROM %s;" % tblName)

	def GetColumns(self,tblName):
		return self.RunCommand("SHOW COLUMNS FROM %s;" % tblName)

	def SelectCommand(self, cmd, SelectMode):
		#print ("RUNNING COMMAND: " + cmd)
		try:
			self.conn.close()
			if not self.conn.is_connected():
				self.conn._open_connection()
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
			print ('ERROR MESSAGE: ' + str(err.msg))
		finally:
			self.cursor.close()
			self.conn.close()
		
		return msg

		
	def InsertCommand(self, cmd, args=none):
		#print ("RUNNING COMMAND: " + cmd)
		try:
			self.conn.close()
			if not self.conn.is_connected():
				self.conn._open_connection()
			
			msg = None
			if SelectMode == self.CmdType.InsertOne:
				self.cursor.execute(cmd)
			elif SelectMode == self.CmdType.InsertMany:
				msg = self.cursor.executemany(cmd,args)
			else:
				msg = None
				raise ValueError("Invalid SelectMode")
				
			#return msg
		except Error as err:
			print ('ERROR MESSAGE: ' + str(err.msg))
		finally:
			self.cursor.close()
			self.conn.close()
		
		
		

	def __del__(self):
		self.conn.commit()
		self.cursor.close()
		self.conn.close()
