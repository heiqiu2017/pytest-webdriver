#encoding:utf-8
"""
    读info_conf.py配置文件
"""
import ConfigParser
import os
class Oper():

    def __init__(self):
        self.config = ConfigParser.ConfigParser()
        self.path = os.getcwd()+os.sep+"info.conf"
        print self.path
        self.config.read(self.path)

    def getConfig(self,section, key):
        # 指定section，option读取值

        return self.config.get(section, key)
    def insertConfig(self, section, option,data):
        # 更新指定section，option的值 & 写入指定section增加新option和值
        self.config.set(section, option, data)
        self.config.write(open(self.path, "w"))
    def addConfig(self, section):
        # 增加新的section
        self.config.add_section(section)
        # 写回配置文件
        self.config.write(open(self.path, "w"))
