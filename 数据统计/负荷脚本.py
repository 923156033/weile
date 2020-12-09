#-*- codeing = utf-8 -*-
#@Time : 2020/11/28  14:01
#@Author : cyz
#@FIle : 负荷脚本.py
#@Software: PyCharm
import pandas as pd


#定义一个类，查询地区负荷，求出最大、最小、平均值、求和
#def set(area):
def chuli(diqu):
    data1=data[data['服务器名称'].str.contains(diqu)]
    print(data1['负荷'].max(),data1['负荷'].min(),int(data1['负荷'].mean()),data1['负荷'].sum())
print("---------求微乐反向代理地区最大值、最小值、平均值、总和-----------")
area=["通用","四川_甘肃_宁夏_云南","陕西","山西_内蒙","山东","辽宁","江西_福建","江苏_安徽_浙江_上海","吉林","湖南","湖北","黑龙江","河南","河北_北京_天津","贵州","广东_广西_海南","高防" ]
data = pd.read_csv(r"E:\GitHub\weile\数据统计\导出数据\地区导出数据 (4).csv",encoding='utf-8')
for i in area:
    chuli(i)
print("---------求微乐小程序大厅通用最大值、最小值、平均值、总和-----------")
data = pd.read_csv(r"E:\GitHub\weile\数据统计\导出数据\地区导出数据 (5).csv",encoding='utf-8')
for i in area:
    chuli(i)
print("---------求微乐APP大厅最大值、最小值、平均值、总和-----------")
area=["通用"]
data = pd.read_csv(r"E:\GitHub\weile\数据统计\导出数据\地区导出数据 (3).csv",encoding='utf-8')
for i in area:
    chuli(i)
print("---------求吉祥APP大厅最大值、最小值、平均值、总和-----------")
area=["大厅"]
data = pd.read_csv(r"E:\GitHub\weile\数据统计\导出数据\地区导出数据.csv",encoding='utf-8')
for i in area:
    chuli(i)
print("---------求吉祥小程序代理最大值、最小值、平均值、总和-----------")
area=["小程序[2-9]+--"]
data = pd.read_csv(r"E:\GitHub\weile\数据统计\导出数据\地区导出数据 (1).csv",encoding='utf-8')
for i in area:
    chuli(i)
print("---------求吉祥小程序大厅最大值、最小值、平均值、总和-----------")
area=["小程序"]
data = pd.read_csv(r"E:\GitHub\weile\数据统计\导出数据\地区导出数据 (2).csv",encoding='utf-8')
for i in area:
    chuli(i)