# 2020 1113 
# Purpose: export Japan elc value to a summary
# source: https://www.enecho.meti.go.jp/statistics/electric_power/ep002/results.html
# pip install xlrd

# attention: natural gas consumption in ele = LNG + 天然ガス
# From 2013 - 2015, the format is different from recent years. I do not include them
# 

import pandas  as pd 
import numpy as np
from pandas import DataFrame
import datetime
import xlrd

starttime = datetime.datetime.now()
# unit： MCM


## 2016 

#文件路径
file_path = r'C:\Users\jiaxi\OneDrive\桌面\Japan\Japan Reports\Elc\Japan Elc 2016.xlsx'
# Jan
# 读取sheet的名字

# April
sheetName = 'H28.4'
table = pd.read_excel(file_path,sheet_name=sheetName)

data =  [["ELC", "2016", "04", table.iloc[11,3]/1000000*1360 + table.iloc[18,3]/1000]]
d201604 = pd.DataFrame(data,columns= ["sector", "year", "month", "value"])

# May
sheetName = 'H28.5'
table = pd.read_excel(file_path,sheet_name=sheetName)

data =  [["ELC", "2016", "05", table.iloc[11,3]/1000000*1360 + table.iloc[18,3]/1000]]
d201605 = pd.DataFrame(data,columns= ["sector", "year", "month", "value"])

# June
sheetName = 'H28.6'
table = pd.read_excel(file_path,sheet_name=sheetName)

data =  [["ELC", "2016", "06", table.iloc[11,3]/1000000*1360 + table.iloc[18,3]/1000]]
d201606 = pd.DataFrame(data,columns= ["sector", "year", "month", "value"])

# July
sheetName = 'H28.7'
table = pd.read_excel(file_path,sheet_name=sheetName)

data =  [["ELC", "2016", "07", table.iloc[11,3]/1000000*1360 + table.iloc[18,3]/1000]]
d201607 = pd.DataFrame(data,columns= ["sector", "year", "month", "value"])

# August
sheetName = 'H28.8'
table = pd.read_excel(file_path,sheet_name=sheetName)

data =  [["ELC", "2016", "08", table.iloc[11,3]/1000000*1360 + table.iloc[18,3]/1000]]
d201608 = pd.DataFrame(data,columns= ["sector", "year", "month", "value"])

# September
sheetName = 'H28.9'
table = pd.read_excel(file_path,sheet_name=sheetName)

data =  [["ELC", "2016", "09", table.iloc[11,3]/1000000*1360 + table.iloc[18,3]/1000]]
d201609 = pd.DataFrame(data,columns= ["sector", "year", "month", "value"])

# Octoer
sheetName = 'H28.10'
table = pd.read_excel(file_path,sheet_name=sheetName)

data =  [["ELC", "2016", "10", table.iloc[11,3]/1000000*1360 + table.iloc[18,3]/1000]]
d201610 = pd.DataFrame(data,columns= ["sector", "year", "month", "value"])

# November
sheetName = 'H28.11'
table = pd.read_excel(file_path,sheet_name=sheetName)

data =  [["ELC", "2016", "11", table.iloc[11,3]/1000000*1360 + table.iloc[18,3]/1000]]
d201611 = pd.DataFrame(data,columns= ["sector", "year", "month", "value"])

# December
sheetName = 'H28.12'
table = pd.read_excel(file_path,sheet_name=sheetName)

data =  [["ELC", "2016", "12", table.iloc[11,3]/1000000*1360 + table.iloc[18,3]/1000]]
d201612 = pd.DataFrame(data,columns= ["sector", "year", "month", "value"])

# Januray
sheetName = 'H29.1'
table = pd.read_excel(file_path,sheet_name=sheetName)

data =  [["ELC", "2017", "01", table.iloc[11,3]/1000000*1360 + table.iloc[18,3]/1000]]
d201701 = pd.DataFrame(data,columns= ["sector", "year", "month", "value"])

# Feburay
sheetName = 'H29.2'
table = pd.read_excel(file_path,sheet_name=sheetName)

data =  [["ELC", "2017", "02", table.iloc[11,3]/1000000*1360 + table.iloc[18,3]/1000]]
d201702 = pd.DataFrame(data,columns= ["sector", "year", "month", "value"])

# March
sheetName = 'H29.3'
table = pd.read_excel(file_path,sheet_name=sheetName)

data =  [["ELC", "2017", "03", table.iloc[11,3]/1000000*1360 + table.iloc[18,3]/1000]]
d201703 = pd.DataFrame(data,columns= ["sector", "year", "month", "value"])


## 2017 

#文件路径
file_path = r'C:\Users\jiaxi\OneDrive\桌面\Japan\Japan Reports\Elc\Japan Elc 2017.xlsx'
# Jan
# 读取sheet的名字

# April
sheetName = 'H29.4'
table = pd.read_excel(file_path,sheet_name=sheetName)

data =  [["ELC", "2017", "04", table.iloc[11,3]/1000000*1360 + table.iloc[18,3]/1000]]
d201704 = pd.DataFrame(data,columns= ["sector", "year", "month", "value"])

# May
sheetName = 'H29.5'
table = pd.read_excel(file_path,sheet_name=sheetName)

data =  [["ELC", "2017", "05", table.iloc[11,3]/1000000*1360 + table.iloc[18,3]/1000]]
d201705 = pd.DataFrame(data,columns= ["sector", "year", "month", "value"])

# June
sheetName = 'H29.6'
table = pd.read_excel(file_path,sheet_name=sheetName)

data =  [["ELC", "2017", "06", table.iloc[11,3]/1000000*1360 + table.iloc[18,3]/1000]]
d201706 = pd.DataFrame(data,columns= ["sector", "year", "month", "value"])

# July
sheetName = 'H29.7'
table = pd.read_excel(file_path,sheet_name=sheetName)

data =  [["ELC", "2017", "07", table.iloc[11,3]/1000000*1360 + table.iloc[18,3]/1000]]
d201707 = pd.DataFrame(data,columns= ["sector", "year", "month", "value"])

# August
sheetName = 'H29.8'
table = pd.read_excel(file_path,sheet_name=sheetName)

data =  [["ELC", "2017", "08", table.iloc[11,3]/1000000*1360 + table.iloc[18,3]/1000]]
d201708 = pd.DataFrame(data,columns= ["sector", "year", "month", "value"])

# September
sheetName = 'H29.9'
table = pd.read_excel(file_path,sheet_name=sheetName)

data =  [["ELC", "2017", "09", table.iloc[11,3]/1000000*1360 + table.iloc[18,3]/1000]]
d201709 = pd.DataFrame(data,columns= ["sector", "year", "month", "value"])

# Octoer
sheetName = 'H29.10'
table = pd.read_excel(file_path,sheet_name=sheetName)

data =  [["ELC", "2017", "10", table.iloc[11,3]/1000000*1360 + table.iloc[18,3]/1000]]
d201710 = pd.DataFrame(data,columns= ["sector", "year", "month", "value"])

# November
sheetName = 'H29.11'
table = pd.read_excel(file_path,sheet_name=sheetName)

data =  [["ELC", "2017", "11", table.iloc[11,3]/1000000*1360 + table.iloc[18,3]/1000]]
d201711 = pd.DataFrame(data,columns= ["sector", "year", "month", "value"])

# December
sheetName = 'H29.12'
table = pd.read_excel(file_path,sheet_name=sheetName)

data =  [["ELC", "2017", "12", table.iloc[11,3]/1000000*1360 + table.iloc[18,3]/1000]]
d201712 = pd.DataFrame(data,columns= ["sector", "year", "month", "value"])

# Januray
sheetName = 'H30.1'
table = pd.read_excel(file_path,sheet_name=sheetName)

data =  [["ELC", "2018", "01", table.iloc[11,3]/1000000*1360 + table.iloc[18,3]/1000]]
d201801 = pd.DataFrame(data,columns= ["sector", "year", "month", "value"])

# Feburay
sheetName = 'H30.2'
table = pd.read_excel(file_path,sheet_name=sheetName)

data =  [["ELC", "2018", "02", table.iloc[11,3]/1000000*1360 + table.iloc[18,3]/1000]]
d201802 = pd.DataFrame(data,columns= ["sector", "year", "month", "value"])

# March
sheetName = 'H30.3'
table = pd.read_excel(file_path,sheet_name=sheetName)

data =  [["ELC", "2018", "03", table.iloc[11,3]/1000000*1360 + table.iloc[18,3]/1000]]
d201803 = pd.DataFrame(data,columns= ["sector", "year", "month", "value"])


## 2018 

#文件路径
file_path = r'C:\Users\jiaxi\OneDrive\桌面\Japan\Japan Reports\Elc\Japan Elc 2018.xlsx'
# Jan
# 读取sheet的名字

# April
sheetName = '2018.4'
table = pd.read_excel(file_path,sheet_name=sheetName)

data =  [["ELC", "2018", "04", table.iloc[11,3]/1000000*1360 + table.iloc[18,3]/1000]]
d201804 = pd.DataFrame(data,columns= ["sector", "year", "month", "value"])

# May
sheetName = '2018.5'
table = pd.read_excel(file_path,sheet_name=sheetName)

data =  [["ELC", "2018", "05", table.iloc[11,3]/1000000*1360 + table.iloc[18,3]/1000]]
d201805 = pd.DataFrame(data,columns= ["sector", "year", "month", "value"])

# June
sheetName = '2018.6'
table = pd.read_excel(file_path,sheet_name=sheetName)

data =  [["ELC", "2018", "06", table.iloc[11,3]/1000000*1360 + table.iloc[18,3]/1000]]
d201806 = pd.DataFrame(data,columns= ["sector", "year", "month", "value"])

# July
sheetName = '2018.7'
table = pd.read_excel(file_path,sheet_name=sheetName)

data =  [["ELC", "2018", "07", table.iloc[11,3]/1000000*1360 + table.iloc[18,3]/1000]]
d201807 = pd.DataFrame(data,columns= ["sector", "year", "month", "value"])

# August
sheetName = '2018.8'
table = pd.read_excel(file_path,sheet_name=sheetName)

data =  [["ELC", "2018", "08", table.iloc[11,3]/1000000*1360 + table.iloc[18,3]/1000]]
d201808 = pd.DataFrame(data,columns= ["sector", "year", "month", "value"])

# September
sheetName = '2018.9'
table = pd.read_excel(file_path,sheet_name=sheetName)

data =  [["ELC", "2018", "09", table.iloc[11,3]/1000000*1360 + table.iloc[18,3]/1000]]
d201809 = pd.DataFrame(data,columns= ["sector", "year", "month", "value"])

# Octoer
sheetName = '2018.10'
table = pd.read_excel(file_path,sheet_name=sheetName)

data =  [["ELC", "2018", "10", table.iloc[11,3]/1000000*1360 + table.iloc[18,3]/1000]]
d201810 = pd.DataFrame(data,columns= ["sector", "year", "month", "value"])

# November
sheetName = '2018.11'
table = pd.read_excel(file_path,sheet_name=sheetName)

data =  [["ELC", "2018", "11", table.iloc[11,3]/1000000*1360 + table.iloc[18,3]/1000]]
d201811 = pd.DataFrame(data,columns= ["sector", "year", "month", "value"])

# December
sheetName = '2018.12'
table = pd.read_excel(file_path,sheet_name=sheetName)

data =  [["ELC", "2018", "12", table.iloc[11,3]/1000000*1360 + table.iloc[18,3]/1000]]
d201812 = pd.DataFrame(data,columns= ["sector", "year", "month", "value"])

# Januray
sheetName = '2019.1'
table = pd.read_excel(file_path,sheet_name=sheetName)

data =  [["ELC", "2019", "01", table.iloc[11,3]/1000000*1360 + table.iloc[18,3]/1000]]
d201901 = pd.DataFrame(data,columns= ["sector", "year", "month", "value"])

# Feburay
sheetName = '2019.2'
table = pd.read_excel(file_path,sheet_name=sheetName)

data =  [["ELC", "2019", "02", table.iloc[11,3]/1000000*1360 + table.iloc[18,3]/1000]]
d201902 = pd.DataFrame(data,columns= ["sector", "year", "month", "value"])

# March
sheetName = '2019.3'
table = pd.read_excel(file_path,sheet_name=sheetName)

data =  [["ELC", "2019", "03", table.iloc[11,3]/1000000*1360 + table.iloc[18,3]/1000]]
d201903 = pd.DataFrame(data,columns= ["sector", "year", "month", "value"])


## 2019 

#文件路径
file_path = r'C:\Users\jiaxi\OneDrive\桌面\Japan\Japan Reports\Elc\Japan Elc 2019.xlsx'
# Jan
# 读取sheet的名字

# April
sheetName = '2019.4'
table = pd.read_excel(file_path,sheet_name=sheetName)

data =  [["ELC", "2019", "04", table.iloc[11,3]/1000000*1360 + table.iloc[18,3]/1000]]
d201904 = pd.DataFrame(data,columns= ["sector", "year", "month", "value"])

# May
sheetName = '2019.5'
table = pd.read_excel(file_path,sheet_name=sheetName)

data =  [["ELC", "2019", "05", table.iloc[11,3]/1000000*1360 + table.iloc[18,3]/1000]]
d201905 = pd.DataFrame(data,columns= ["sector", "year", "month", "value"])

# June
sheetName = '2019.6'
table = pd.read_excel(file_path,sheet_name=sheetName)

data =  [["ELC", "2019", "06", table.iloc[11,3]/1000000*1360 + table.iloc[18,3]/1000]]
d201906 = pd.DataFrame(data,columns= ["sector", "year", "month", "value"])

# July
sheetName = '2019.7'
table = pd.read_excel(file_path,sheet_name=sheetName)

data =  [["ELC", "2019", "07", table.iloc[11,3]/1000000*1360 + table.iloc[18,3]/1000]]
d201907 = pd.DataFrame(data,columns= ["sector", "year", "month", "value"])

# August
sheetName = '2019.8'
table = pd.read_excel(file_path,sheet_name=sheetName)

data =  [["ELC", "2019", "08", table.iloc[11,3]/1000000*1360 + table.iloc[18,3]/1000]]
d201908 = pd.DataFrame(data,columns= ["sector", "year", "month", "value"])

# September
sheetName = '2019.9'
table = pd.read_excel(file_path,sheet_name=sheetName)

data =  [["ELC", "2019", "09", table.iloc[11,3]/1000000*1360 + table.iloc[18,3]/1000]]
d201909 = pd.DataFrame(data,columns= ["sector", "year", "month", "value"])

# Octoer
sheetName = '2019.10'
table = pd.read_excel(file_path,sheet_name=sheetName)

data =  [["ELC", "2019", "10", table.iloc[11,3]/1000000*1360 + table.iloc[18,3]/1000]]
d201910 = pd.DataFrame(data,columns= ["sector", "year", "month", "value"])

# November
sheetName = '2019.11'
table = pd.read_excel(file_path,sheet_name=sheetName)

data =  [["ELC", "2019", "11", table.iloc[11,3]/1000000*1360 + table.iloc[18,3]/1000]]
d201911 = pd.DataFrame(data,columns= ["sector", "year", "month", "value"])

# December
sheetName = '2019.12'
table = pd.read_excel(file_path,sheet_name=sheetName)

data =  [["ELC", "2019", "12", table.iloc[11,3]/1000000*1360 + table.iloc[18,3]/1000]]
d201912 = pd.DataFrame(data,columns= ["sector", "year", "month", "value"])

# Januray
sheetName = '2020.1'
table = pd.read_excel(file_path,sheet_name=sheetName)

data =  [["ELC", "2020", "01", table.iloc[11,3]/1000000*1360 + table.iloc[18,3]/1000]]
d202001 = pd.DataFrame(data,columns= ["sector", "year", "month", "value"])

# Feburay
sheetName = '2020.2'
table = pd.read_excel(file_path,sheet_name=sheetName)

data =  [["ELC", "2020", "02", table.iloc[11,3]/1000000*1360 + table.iloc[18,3]/1000]]
d202002 = pd.DataFrame(data,columns= ["sector", "year", "month", "value"])

# March
sheetName = '2020.3'
table = pd.read_excel(file_path,sheet_name=sheetName)

data =  [["ELC", "2020", "03", table.iloc[11,3]/1000000*1360 + table.iloc[18,3]/1000]]
d202003 = pd.DataFrame(data,columns= ["sector", "year", "month", "value"])


## 2020 

#文件路径
file_path = r'C:\Users\jiaxi\OneDrive\桌面\Japan\Japan Reports\Elc\Japan Elc 2020 Incomplete.xlsx'
# Jan
# 读取sheet的名字

# April
sheetName = '2020.4'
table = pd.read_excel(file_path,sheet_name=sheetName)

data =  [["ELC", "2020", "04", table.iloc[11,3]/1000000*1360 + table.iloc[18,3]/1000]]
d202004 = pd.DataFrame(data,columns= ["sector", "year", "month", "value"])

# May
sheetName = '2020.5'
table = pd.read_excel(file_path,sheet_name=sheetName)

data =  [["ELC", "2020", "05", table.iloc[11,3]/1000000*1360 + table.iloc[18,3]/1000]]
d202005 = pd.DataFrame(data,columns= ["sector", "year", "month", "value"])

# June
sheetName = '2020.6'
table = pd.read_excel(file_path,sheet_name=sheetName)

data =  [["ELC", "2020", "06", table.iloc[11,3]/1000000*1360 + table.iloc[18,3]/1000]]
d202006 = pd.DataFrame(data,columns= ["sector", "year", "month", "value"])

# July
sheetName = '2020.7'
table = pd.read_excel(file_path,sheet_name=sheetName)

data =  [["ELC", "2020", "07", table.iloc[11,3]/1000000*1360 + table.iloc[18,3]/1000]]
d202007 = pd.DataFrame(data,columns= ["sector", "year", "month", "value"])
'''
# August
sheetName = '2020.8'
table = pd.read_excel(file_path,sheet_name=sheetName)

data =  [["ELC", "2020", "08", table.iloc[11,3]/1000000*1360 + table.iloc[18,3]/1000]]
d202008 = pd.DataFrame(data,columns= ["sector", "year", "month", "value"])

# September
sheetName = '2020.9'
table = pd.read_excel(file_path,sheet_name=sheetName)

data =  [["ELC", "2020", "09", table.iloc[11,3]/1000000*1360 + table.iloc[18,3]/1000]]
d202009 = pd.DataFrame(data,columns= ["sector", "year", "month", "value"])

# Octoer
sheetName = '2020.10'
table = pd.read_excel(file_path,sheet_name=sheetName)

data =  [["ELC", "2020", "10", table.iloc[11,3]/1000000*1360 + table.iloc[18,3]/1000]]
d202010 = pd.DataFrame(data,columns= ["sector", "year", "month", "value"])

# November
sheetName = '2020.11'
table = pd.read_excel(file_path,sheet_name=sheetName)

data =  [["ELC", "2020", "11", table.iloc[11,3]/1000000*1360 + table.iloc[18,3]/1000]]
d202011 = pd.DataFrame(data,columns= ["sector", "year", "month", "value"])

#文件路径
file_path = r'C:\Users\jiaxi\OneDrive\Desktop\RBAC 2021\Balance\balance\Japan\4-2020.xlsx'
# Jan
# 读取sheet的名字

# Dec
sheetName = '2020.12'
table = pd.read_excel(file_path,sheet_name=sheetName)

data =  [["ELC", "2020", "12", table.iloc[11,3]/1000000*1360 + table.iloc[18,3]/1000]]
d202012 = pd.DataFrame(data,columns= ["sector", "year", "month", "value"])


# Januray
sheetName = '2021.1'
table = pd.read_excel(file_path,sheet_name=sheetName)
data =  [["ELC", "2021", "01", table.iloc[11,3]/1000000*1360 + table.iloc[18,3]/1000]]
d202101 = pd.DataFrame(data,columns= ["sector", "year", "month", "value"])
# Feburay
sheetName = '2021.2'
table = pd.read_excel(file_path,sheet_name=sheetName)
data =  [["ELC", "2021", "02", table.iloc[11,3]/1000000*1360 + table.iloc[18,3]/1000]]
d202102 = pd.DataFrame(data,columns= ["sector", "year", "month", "value"])
# March
sheetName = '2021.3'
table = pd.read_excel(file_path,sheet_name=sheetName)
data =  [["ELC", "2021", "03", table.iloc[11,3]/1000000*1360 + table.iloc[18,3]/1000]]
d202103 = pd.DataFrame(data,columns= ["sector", "year", "month", "value"])


#文件路径
file_path = r'C:\Users\jiaxi\OneDrive\Desktop\RBAC 2021\Balance\balance\Japan\4-2021.xlsx'
# Jan
# 读取sheet的名字

# April
sheetName = '2021.4'
table = pd.read_excel(file_path,sheet_name=sheetName)
data =  [["ELC", "2021", "04", table.iloc[11,3]/1000000*1360 + table.iloc[18,3]/1000]]
d202104 = pd.DataFrame(data,columns= ["sector", "year", "month", "value"])


# May
sheetName = '2021.5'
table = pd.read_excel(file_path,sheet_name=sheetName)

data =  [["ELC", "2021", "05", table.iloc[11,3]/1000000*1360 + table.iloc[18,3]/1000]]
d202105 = pd.DataFrame(data,columns= ["sector", "year", "month", "value"])

# June
sheetName = '2021.6'
table = pd.read_excel(file_path,sheet_name=sheetName)

data =  [["ELC", "2021", "06", table.iloc[11,3]/1000000*1360 + table.iloc[18,3]/1000]]
d202106 = pd.DataFrame(data,columns= ["sector", "year", "month", "value"])

, d201306, d201307, d201308, d201309, d201310, d201311, d201312, \
           d201401, d201402, d201403, d201404, d201405, d201406, d201407, d201408, d201409, d201410, d201411, d201412, \
           d201501, d201502, d201503, d201504, d201505, d201506, d201507, d201508, d201509, d201510, d201511, d201512, \
           d201601, d201602, d201603, 
 '''
          
Output1 = [d201604, d201605, d201606, d201607, d201608, d201609, d201610, d201611, d201612, \
           d201701, d201702, d201703, d201704, d201705, d201706, d201707, d201708, d201709, d201710, d201711, d201712, \
           d201801, d201802, d201803, d201804, d201805, d201806, d201807, d201808, d201809, d201810, d201811, d201812, \
           d201901, d201902, d201903, d201904, d201905, d201906, d201907, d201908, d201909, d201910, d201911, d201912, \
           d202001, d202002, d202003, d202004, d202005, d202006, d202007]
    d202012, d202101, d202102,d202103,d202104,d202105,d202106
#, d202008 , d202009, d202010, d202011, d202012        ]

Output2 = pd.concat(Output1)
Output2.to_csv('C:\\Users\\jiaxi\\OneDrive\\桌面\\Japan\\Japan Reports\\Summary-Elc.csv',index=None)


endtime = datetime.datetime.now()
print ("duration：", endtime - starttime)

print("Congradutions! Finished :)")
