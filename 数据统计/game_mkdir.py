#-*- codeing = utf-8 -*-
#@Time : 2021/1/2  13:44
#@Author : cyz
#@FIle : game_mkdir.py
#@Software: PyCharm
import os

#1、根据游戏目录下xml文件获取ServerName字段的变量名来创建根目录并把xml复制到相应的目录下

#2、从获取xml文件获取的到相应的程序名 （ShellFile），通过程序名查找相关exe、php、ini文件并复制到相应的目录下
#3、拷贝共有的文件到每个目录下
#4、压缩之前游戏目录做备份，并删除游戏目录


#定义一个类，查找xml文件
def find_xml_file(xml)
chdir='D:\\通用_麻将_朋友场'
items = os.listdir(chdir)
newlist = []
for names in items:
  if names.endswith(".xml"):
    newlist.append(names)
print (newlist)
