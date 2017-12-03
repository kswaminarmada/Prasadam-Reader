#!/usr/bin/python
import os
from configparser import ConfigParser
import zx


class MyConfigs:
    cfg = ConfigParser()
    ConfigFileName = 'MyConfig.ini'
    dbconfig = {'host': 'localhost', 'database': '',
                            'user': 'root', 'password': '123', 'port': '3306'}
    MySetting = {'VisibleCols':'1,2,3','DepartmentGroup':'1,2,3','Location':''}
    DepartmentGroup = {'GroupName':'Query'}
    encryptedconfig = ['dbConnection:password']

    def __init__(self):
        if not os.path.isfile(self.ConfigFileName):
            open(self.ConfigFileName, 'w+').close()
       
        with open(self.ConfigFileName, 'r') as fp:
            self.cfg.readfp(fp, self.ConfigFileName)
            fp.close()
        
        if not self.cfg.has_section("dbConnection"):
            self.WriteConfig("dbConnection",self.dbconfig)
        
        if not self.cfg.has_section("MySetting"):
            self.WriteConfig("MySetting",self.MySetting)
        
        if not self.cfg.has_section("DepartmentGroup"):
            self.WriteConfig("DepartmentGroup",self.DepartmentGroup)

    def WriteConfig(self, MySection, Configs={}):
        with open(self.ConfigFileName, 'w+') as fp:
            self.cfg.readfp(fp, self.ConfigFileName)
            if not self.cfg.has_section(MySection):
                self.cfg.add_section(MySection)
                for opt, value in Configs.items():
                    for itm in self.encryptedconfig:
                        sec, key = itm.split(':')

                    if MySection == sec and opt == key:
                        zx.SetKey(value)
                        value = "My" + opt

                    self.cfg.set(MySection, opt, value)
            else:
                if self.cfg.has_section(MySection):
                    for opt, value in Configs.items():
                        for itm in self.encryptedconfig:
                            sec, key = itm.split(':')

                        if MySection == sec and opt == key:
                            zx.SetKey(value)
                            value = "My" + opt

                        self.cfg.set(MySection, opt, value)
            self.cfg.write(fp)

    def Get_db_config(self, section='dbConnection'):
        """ Read database configuration file and return a dictionary object
        :param filename: name of the configuration file
        :param section: section of database configuration
        :return: a dictionary of database parameters
        """
        # create parser and read ini configuration file
        self.cfg.read(self.ConfigFileName)

        # get section, default to mysql
        db = {}
        if self.cfg.has_section(section):
            items = self.cfg.items(section)
            for item in items:
                for itm in self.encryptedconfig:
                        sec, key = itm.split(':')
                
                if section == sec and item[0] == key:
                    db[item[0]] = zx.GetKey()
                else:
                    db[item[0]] = item[1]
        else:
            raise Exception('{0} not found in the {1} file'.format(section,self.ConfigFileName))
    
        return db

    def Get_MySetting(self,MySection='MySetting',option=None):
        self.cfg.read(self.ConfigFileName)
        db=None
        # get section, default to mysql
        if option == None:
            db = {}
            if self.cfg.has_section(MySection):
                items = self.cfg.items(MySection)
                for item in items:
                    for itm in self.encryptedconfig:
                            sec, key = itm.split(':')
                    
                    if MySection == sec and item[0] == key:
                        db[item[0]] = zx.GetKey()
                    else:
                        db[item[0]] = item[1]
            else:
                raise Exception('{0} not found in the {1} file'.format(MySection,self.ConfigFileName))
        else:
            
            if self.cfg.has_section(MySection):
                if self.cfg.has_option(MySection,option):
                    db = self.cfg.get(MySection, option)
                
        return db

'''
if __name__ == '__main__':
    cfg = MyConfigs()
    cfg.WriteConfig('dbConnection',MyConfigs.dbconfig)
    cfg.Get_db_config()
'''