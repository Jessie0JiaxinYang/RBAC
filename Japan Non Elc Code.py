
"""
Created on Thu Nov 12 13:58:15 2020

@author: jiaxi
"""

# Japan Non-Elc gas consumption

# Source: https://www.enecho.meti.go.jp/statistics/gas/ga001/results.html
# 2 month lag
# 2020 1112 update: the latest is August
# import and export Japan res, com, ind data
## + year
#  + month
# Note: 2013 - 2017 Mar has the same format. 


import pandas  as pd 
import numpy as np
from pandas import DataFrame
import datetime

starttime = datetime.datetime.now()

## 2013 

#文件路径
file_path = r'C:\\Users\\jiaxi\\OneDrive\\桌面\\Japan\\Japan Reports\\Non Elc\\2013 Summary Japan.xlsx'
# Jan
# 读取sheet的名字
sheetName = '総括表（数量）201301'
table = pd.read_excel(file_path,sheet_name=sheetName)

data =  [["res", "2013", "01", table.iloc[19,6]],\
         ["com", "2013", "01", table.iloc[16,6] + table.iloc[20,6]],\
         ["ind", "2013", "01", table.iloc[17,6] + table.iloc[21,6]],\
         ["oth", "2013", "01", table.iloc[18,6] + table.iloc[22,6]]]
d201301 = pd.DataFrame(data,columns= ["sector", "year", "month", "value"])

# Feb    
sheetName='総括表（数量）201302'
table = pd.read_excel(file_path,sheet_name=sheetName)

data = [["res", "2013", "02", table.iloc[19,6]],\
        ["com", "2013", "02", table.iloc[16,6] + table.iloc[20,6]],\
        ["ind", "2013", "02", table.iloc[17,6] + table.iloc[21,6]],\
        ["oth", "2013", "02", table.iloc[18,6] + table.iloc[22,6]]]
d201302 = pd.DataFrame(data,columns= ["sector", "year", "month", "value"])

# Mar    
sheetName = '総括表（数量）201303'
table=pd.read_excel(file_path,sheet_name=sheetName)

data = [["res", "2013", "03", table.iloc[19,6]],\
        ["com", "2013", "03", table.iloc[16,6] + table.iloc[20,6]],\
        ["ind", "2013", "03", table.iloc[17,6] + table.iloc[21,6]],\
        ["oth", "2013", "03", table.iloc[18,6] + table.iloc[22,6]]]
d201303 = pd.DataFrame(data,columns= ["sector", "year", "month", "value"])

# Apr    
sheetName = '総括表（数量）201304'
table=pd.read_excel(file_path,sheet_name=sheetName)

data = [["res", "2013", "04", table.iloc[19,6]],\
        ["com", "2013", "04", table.iloc[16,6] + table.iloc[20,6]],\
        ["ind", "2013", "04", table.iloc[17,6] + table.iloc[21,6]],\
        ["oth", "2013", "04", table.iloc[18,6] + table.iloc[22,6]]]
d201304 = pd.DataFrame(data,columns= ["sector", "year", "month", "value"])

# May    
sheetName = '総括表（数量）201305'
table=pd.read_excel(file_path,sheet_name=sheetName)

data = [["res", "2013", "05", table.iloc[19,6]],\
        ["com", "2013", "05", table.iloc[16,6] + table.iloc[20,6]],\
        ["ind", "2013", "05", table.iloc[17,6] + table.iloc[21,6]],\
        ["oth", "2013", "05", table.iloc[18,6] + table.iloc[22,6]]]
d201305 = pd.DataFrame(data,columns= ["sector", "year", "month", "value"])

# Jun    
sheetName = '総括表（数量）201306'
table=pd.read_excel(file_path,sheet_name=sheetName)

data = [["res", "2013", "06", table.iloc[19,6]],\
        ["com", "2013", "06", table.iloc[16,6] + table.iloc[20,6]],\
        ["ind", "2013", "06", table.iloc[17,6] + table.iloc[21,6]],\
        ["oth", "2013", "06", table.iloc[18,6] + table.iloc[22,6]]]
d201306 = pd.DataFrame(data,columns= ["sector", "year", "month", "value"])

# Jul    
sheetName = '総括表（数量）201307'
table=pd.read_excel(file_path,sheet_name=sheetName)

data = [["res", "2013", "07", table.iloc[19,6]],\
        ["com", "2013", "07", table.iloc[16,6] + table.iloc[20,6]],\
        ["ind", "2013", "07", table.iloc[17,6] + table.iloc[21,6]],\
        ["oth", "2013", "07", table.iloc[18,6] + table.iloc[22,6]]]
d201307 = pd.DataFrame(data,columns= ["sector", "year", "month", "value"])

# Aug    
sheetName = '総括表（数量）201308'
table=pd.read_excel(file_path,sheet_name=sheetName)

data = [["res", "2013", "08", table.iloc[19,6]],\
        ["com", "2013", "08", table.iloc[16,6] + table.iloc[20,6]],\
        ["ind", "2013", "08", table.iloc[17,6] + table.iloc[21,6]],\
        ["oth", "2013", "08", table.iloc[18,6] + table.iloc[22,6]]]
d201308 = pd.DataFrame(data,columns= ["sector", "year", "month", "value"])

# Sep    
sheetName = '総括表（数量）201309'
table=pd.read_excel(file_path,sheet_name=sheetName)

data = [["res", "2013", "09", table.iloc[19,6]],\
        ["com", "2013", "09", table.iloc[16,6] + table.iloc[20,6]],\
        ["ind", "2013", "09", table.iloc[17,6] + table.iloc[21,6]],\
        ["oth", "2013", "09", table.iloc[18,6] + table.iloc[22,6]]]
d201309 = pd.DataFrame(data,columns= ["sector", "year", "month", "value"])

# Oct    
sheetName = '総括表（数量）201310'
table=pd.read_excel(file_path,sheet_name=sheetName)

data = [["res", "2013", "10", table.iloc[19,6]],\
        ["com", "2013", "10", table.iloc[16,6] + table.iloc[20,6]],\
        ["ind", "2013", "10", table.iloc[17,6] + table.iloc[21,6]],\
        ["oth", "2013", "10", table.iloc[18,6] + table.iloc[22,6]]]
d201310 = pd.DataFrame(data,columns= ["sector", "year", "month", "value"])

# Nov    
sheetName = '総括表（数量）201311'
table=pd.read_excel(file_path,sheet_name=sheetName)

data = [["res", "2013", "11", table.iloc[19,6]],\
        ["com", "2013", "11", table.iloc[16,6] + table.iloc[20,6]],\
        ["ind", "2013", "11", table.iloc[17,6] + table.iloc[21,6]],\
        ["oth", "2013", "11", table.iloc[18,6] + table.iloc[22,6]]]
d201311 = pd.DataFrame(data,columns= ["sector", "year", "month", "value"])

# Dec    
sheetName = '総括表（数量）201312'
table=pd.read_excel(file_path,sheet_name=sheetName)

data = [["res", "2013", "12", table.iloc[19,6]],\
        ["com", "2013", "12", table.iloc[16,6] + table.iloc[20,6]],\
        ["ind", "2013", "12", table.iloc[17,6] + table.iloc[21,6]],\
        ["oth", "2013", "12", table.iloc[18,6] + table.iloc[22,6]]]
d201312 = pd.DataFrame(data,columns= ["sector", "year", "month", "value"])


## 2014 

#文件路径
file_path = r'C:\\Users\\jiaxi\\OneDrive\\桌面\\Japan\\Japan Reports\\Non Elc\\2014 Summary Japan.xlsx'
# Jan
# 读取sheet的名字
sheetName = '総括表（数量）201401'
table = pd.read_excel(file_path,sheet_name=sheetName)

data =  [["res", "2014", "01", table.iloc[19,6]],\
         ["com", "2014", "01", table.iloc[16,6] + table.iloc[20,6]],\
         ["ind", "2014", "01", table.iloc[17,6] + table.iloc[21,6]],\
         ["oth", "2014", "01", table.iloc[18,6] + table.iloc[22,6]]]
d201401 = pd.DataFrame(data,columns= ["sector", "year", "month", "value"])

# Feb    
sheetName='総括表（数量）201402'
table = pd.read_excel(file_path,sheet_name=sheetName)

data = [["res", "2014", "02", table.iloc[19,6]],\
        ["com", "2014", "02", table.iloc[16,6] + table.iloc[20,6]],\
        ["ind", "2014", "02", table.iloc[17,6] + table.iloc[21,6]],\
        ["oth", "2014", "02", table.iloc[18,6] + table.iloc[22,6]]]
d201402 = pd.DataFrame(data,columns= ["sector", "year", "month", "value"])

# Mar    
sheetName = '総括表（数量）201403'
table=pd.read_excel(file_path,sheet_name=sheetName)

data = [["res", "2014", "03", table.iloc[19,6]],\
        ["com", "2014", "03", table.iloc[16,6] + table.iloc[20,6]],\
        ["ind", "2014", "03", table.iloc[17,6] + table.iloc[21,6]],\
        ["oth", "2014", "03", table.iloc[18,6] + table.iloc[22,6]]]
d201403 = pd.DataFrame(data,columns= ["sector", "year", "month", "value"])

# Apr    
sheetName = '総括表（数量）201404'
table=pd.read_excel(file_path,sheet_name=sheetName)

data = [["res", "2014", "04", table.iloc[19,6]],\
        ["com", "2014", "04", table.iloc[16,6] + table.iloc[20,6]],\
        ["ind", "2014", "04", table.iloc[17,6] + table.iloc[21,6]],\
        ["oth", "2014", "04", table.iloc[18,6] + table.iloc[22,6]]]
d201404 = pd.DataFrame(data,columns= ["sector", "year", "month", "value"])

# May    
sheetName = '総括表（数量）201405'
table=pd.read_excel(file_path,sheet_name=sheetName)

data = [["res", "2014", "05", table.iloc[19,6]],\
        ["com", "2014", "05", table.iloc[16,6] + table.iloc[20,6]],\
        ["ind", "2014", "05", table.iloc[17,6] + table.iloc[21,6]],\
        ["oth", "2014", "05", table.iloc[18,6] + table.iloc[22,6]]]
d201405 = pd.DataFrame(data,columns= ["sector", "year", "month", "value"])

# Jun    
sheetName = '総括表（数量）201406'
table=pd.read_excel(file_path,sheet_name=sheetName)

data = [["res", "2014", "06", table.iloc[19,6]],\
        ["com", "2014", "06", table.iloc[16,6] + table.iloc[20,6]],\
        ["ind", "2014", "06", table.iloc[17,6] + table.iloc[21,6]],\
        ["oth", "2014", "06", table.iloc[18,6] + table.iloc[22,6]]]
d201406 = pd.DataFrame(data,columns= ["sector", "year", "month", "value"])

# Jul    
sheetName = '総括表（数量）201407'
table=pd.read_excel(file_path,sheet_name=sheetName)

data = [["res", "2014", "07", table.iloc[19,6]],\
        ["com", "2014", "07", table.iloc[16,6] + table.iloc[20,6]],\
        ["ind", "2014", "07", table.iloc[17,6] + table.iloc[21,6]],\
        ["oth", "2014", "07", table.iloc[18,6] + table.iloc[22,6]]]
d201407 = pd.DataFrame(data,columns= ["sector", "year", "month", "value"])

# Aug    
sheetName = '総括表（数量）201408'
table=pd.read_excel(file_path,sheet_name=sheetName)

data = [["res", "2014", "08", table.iloc[19,6]],\
        ["com", "2014", "08", table.iloc[16,6] + table.iloc[20,6]],\
        ["ind", "2014", "08", table.iloc[17,6] + table.iloc[21,6]],\
        ["oth", "2014", "08", table.iloc[18,6] + table.iloc[22,6]]]
d201408 = pd.DataFrame(data,columns= ["sector", "year", "month", "value"])

# Sep    
sheetName = '総括表（数量）201409'
table=pd.read_excel(file_path,sheet_name=sheetName)

data = [["res", "2014", "09", table.iloc[19,6]],\
        ["com", "2014", "09", table.iloc[16,6] + table.iloc[20,6]],\
        ["ind", "2014", "09", table.iloc[17,6] + table.iloc[21,6]],\
        ["oth", "2014", "09", table.iloc[18,6] + table.iloc[22,6]]]
d201409 = pd.DataFrame(data,columns= ["sector", "year", "month", "value"])

# Oct    
sheetName = '総括表（数量）201410'
table=pd.read_excel(file_path,sheet_name=sheetName)

data = [["res", "2014", "10", table.iloc[19,6]],\
        ["com", "2014", "10", table.iloc[16,6] + table.iloc[20,6]],\
        ["ind", "2014", "10", table.iloc[17,6] + table.iloc[21,6]],\
        ["oth", "2014", "10", table.iloc[18,6] + table.iloc[22,6]]]
d201410 = pd.DataFrame(data,columns= ["sector", "year", "month", "value"])

# Nov    
sheetName = '総括表（数量）201411'
table=pd.read_excel(file_path,sheet_name=sheetName)

data = [["res", "2014", "11", table.iloc[19,6]],\
        ["com", "2014", "11", table.iloc[16,6] + table.iloc[20,6]],\
        ["ind", "2014", "11", table.iloc[17,6] + table.iloc[21,6]],\
        ["oth", "2014", "11", table.iloc[18,6] + table.iloc[22,6]]]
d201411 = pd.DataFrame(data,columns= ["sector", "year", "month", "value"])

# Dec    
sheetName = '総括表（数量）201412'
table=pd.read_excel(file_path,sheet_name=sheetName)

data = [["res", "2014", "12", table.iloc[19,6]],\
        ["com", "2014", "12", table.iloc[16,6] + table.iloc[20,6]],\
        ["ind", "2014", "12", table.iloc[17,6] + table.iloc[21,6]],\
        ["oth", "2014", "12", table.iloc[18,6] + table.iloc[22,6]]]
d201412 = pd.DataFrame(data,columns= ["sector", "year", "month", "value"])

## 2015 

#文件路径
file_path = r'C:\\Users\\jiaxi\\OneDrive\\桌面\\Japan\\Japan Reports\\Non Elc\\2015 Summary Japan.xlsx'
# Jan
# 读取sheet的名字
sheetName = '総括表（数量）201501'
table = pd.read_excel(file_path,sheet_name=sheetName)

data =  [["res", "2015", "01", table.iloc[19,6]],\
         ["com", "2015", "01", table.iloc[16,6] + table.iloc[20,6]],\
         ["ind", "2015", "01", table.iloc[17,6] + table.iloc[21,6]],\
         ["oth", "2015", "01", table.iloc[18,6] + table.iloc[22,6]]]
d201501 = pd.DataFrame(data,columns= ["sector", "year", "month", "value"])

# Feb    
sheetName='総括表（数量）201502'
table = pd.read_excel(file_path,sheet_name=sheetName)

data = [["res", "2015", "02", table.iloc[19,6]],\
        ["com", "2015", "02", table.iloc[16,6] + table.iloc[20,6]],\
        ["ind", "2015", "02", table.iloc[17,6] + table.iloc[21,6]],\
        ["oth", "2015", "02", table.iloc[18,6] + table.iloc[22,6]]]
d201502 = pd.DataFrame(data,columns= ["sector", "year", "month", "value"])

# Mar    
sheetName = '総括表（数量）201503'
table=pd.read_excel(file_path,sheet_name=sheetName)

data = [["res", "2015", "03", table.iloc[19,6]],\
        ["com", "2015", "03", table.iloc[16,6] + table.iloc[20,6]],\
        ["ind", "2015", "03", table.iloc[17,6] + table.iloc[21,6]],\
        ["oth", "2015", "03", table.iloc[18,6] + table.iloc[22,6]]]
d201503 = pd.DataFrame(data,columns= ["sector", "year", "month", "value"])

# Apr    
sheetName = '総括表（数量）201504'
table=pd.read_excel(file_path,sheet_name=sheetName)

data = [["res", "2015", "04", table.iloc[19,6]],\
        ["com", "2015", "04", table.iloc[16,6] + table.iloc[20,6]],\
        ["ind", "2015", "04", table.iloc[17,6] + table.iloc[21,6]],\
        ["oth", "2015", "04", table.iloc[18,6] + table.iloc[22,6]]]
d201504 = pd.DataFrame(data,columns= ["sector", "year", "month", "value"])

# May    
sheetName = '総括表（数量）201505'
table=pd.read_excel(file_path,sheet_name=sheetName)

data = [["res", "2015", "05", table.iloc[19,6]],\
        ["com", "2015", "05", table.iloc[16,6] + table.iloc[20,6]],\
        ["ind", "2015", "05", table.iloc[17,6] + table.iloc[21,6]],\
        ["oth", "2015", "05", table.iloc[18,6] + table.iloc[22,6]]]
d201505 = pd.DataFrame(data,columns= ["sector", "year", "month", "value"])

# Jun    
sheetName = '総括表（数量）201506'
table=pd.read_excel(file_path,sheet_name=sheetName)

data = [["res", "2015", "06", table.iloc[19,6]],\
        ["com", "2015", "06", table.iloc[16,6] + table.iloc[20,6]],\
        ["ind", "2015", "06", table.iloc[17,6] + table.iloc[21,6]],\
        ["oth", "2015", "06", table.iloc[18,6] + table.iloc[22,6]]]
d201506 = pd.DataFrame(data,columns= ["sector", "year", "month", "value"])

# Jul    
sheetName = '総括表（数量）201507'
table=pd.read_excel(file_path,sheet_name=sheetName)

data = [["res", "2015", "07", table.iloc[19,6]],\
        ["com", "2015", "07", table.iloc[16,6] + table.iloc[20,6]],\
        ["ind", "2015", "07", table.iloc[17,6] + table.iloc[21,6]],\
        ["oth", "2015", "07", table.iloc[18,6] + table.iloc[22,6]]]
d201507 = pd.DataFrame(data,columns= ["sector", "year", "month", "value"])

# Aug    
sheetName = '総括表（数量）201508'
table=pd.read_excel(file_path,sheet_name=sheetName)

data = [["res", "2015", "08", table.iloc[19,6]],\
        ["com", "2015", "08", table.iloc[16,6] + table.iloc[20,6]],\
        ["ind", "2015", "08", table.iloc[17,6] + table.iloc[21,6]],\
        ["oth", "2015", "08", table.iloc[18,6] + table.iloc[22,6]]]
d201508 = pd.DataFrame(data,columns= ["sector", "year", "month", "value"])

# Sep    
sheetName = '総括表（数量）201509'
table=pd.read_excel(file_path,sheet_name=sheetName)

data = [["res", "2015", "09", table.iloc[19,6]],\
        ["com", "2015", "09", table.iloc[16,6] + table.iloc[20,6]],\
        ["ind", "2015", "09", table.iloc[17,6] + table.iloc[21,6]],\
        ["oth", "2015", "09", table.iloc[18,6] + table.iloc[22,6]]]
d201509 = pd.DataFrame(data,columns= ["sector", "year", "month", "value"])

# Oct    
sheetName = '総括表（数量）201510'
table=pd.read_excel(file_path,sheet_name=sheetName)

data = [["res", "2015", "10", table.iloc[19,6]],\
        ["com", "2015", "10", table.iloc[16,6] + table.iloc[20,6]],\
        ["ind", "2015", "10", table.iloc[17,6] + table.iloc[21,6]],\
        ["oth", "2015", "10", table.iloc[18,6] + table.iloc[22,6]]]
d201510 = pd.DataFrame(data,columns= ["sector", "year", "month", "value"])

# Nov    
sheetName = '総括表（数量）201511'
table=pd.read_excel(file_path,sheet_name=sheetName)

data = [["res", "2015", "11", table.iloc[19,6]],\
        ["com", "2015", "11", table.iloc[16,6] + table.iloc[20,6]],\
        ["ind", "2015", "11", table.iloc[17,6] + table.iloc[21,6]],\
        ["oth", "2015", "11", table.iloc[18,6] + table.iloc[22,6]]]
d201511 = pd.DataFrame(data,columns= ["sector", "year", "month", "value"])

# Dec    
sheetName = '総括表（数量）201512'
table=pd.read_excel(file_path,sheet_name=sheetName)

data = [["res", "2015", "12", table.iloc[19,6]],\
        ["com", "2015", "12", table.iloc[16,6] + table.iloc[20,6]],\
        ["ind", "2015", "12", table.iloc[17,6] + table.iloc[21,6]],\
        ["oth", "2015", "12", table.iloc[18,6] + table.iloc[22,6]]]
d201512 = pd.DataFrame(data,columns= ["sector", "year", "month", "value"])


## 2016 

#文件路径
file_path = r'C:\\Users\\jiaxi\\OneDrive\\桌面\\Japan\\Japan Reports\\Non Elc\\2016 Summary Japan.xlsx'
# Jan
# 读取sheet的名字
sheetName = '総括表（数量）201601'
table = pd.read_excel(file_path,sheet_name=sheetName)

data =  [["res", "2016", "01", table.iloc[19,6]],\
         ["com", "2016", "01", table.iloc[16,6] + table.iloc[20,6]],\
         ["ind", "2016", "01", table.iloc[17,6] + table.iloc[21,6]],\
         ["oth", "2016", "01", table.iloc[18,6] + table.iloc[22,6]]]
d201601 = pd.DataFrame(data,columns= ["sector", "year", "month", "value"])

# Feb    
sheetName='総括表（数量）201602'
table = pd.read_excel(file_path,sheet_name=sheetName)

data = [["res", "2016", "02", table.iloc[19,6]],\
        ["com", "2016", "02", table.iloc[16,6] + table.iloc[20,6]],\
        ["ind", "2016", "02", table.iloc[17,6] + table.iloc[21,6]],\
        ["oth", "2016", "02", table.iloc[18,6] + table.iloc[22,6]]]
d201602 = pd.DataFrame(data,columns= ["sector", "year", "month", "value"])

# Mar    
sheetName = '総括表（数量）201603'
table=pd.read_excel(file_path,sheet_name=sheetName)

data = [["res", "2016", "03", table.iloc[19,6]],\
        ["com", "2016", "03", table.iloc[16,6] + table.iloc[20,6]],\
        ["ind", "2016", "03", table.iloc[17,6] + table.iloc[21,6]],\
        ["oth", "2016", "03", table.iloc[18,6] + table.iloc[22,6]]]
d201603 = pd.DataFrame(data,columns= ["sector", "year", "month", "value"])

# Apr    
sheetName = '総括表（数量）201604'
table=pd.read_excel(file_path,sheet_name=sheetName)

data = [["res", "2016", "04", table.iloc[19,6]],\
        ["com", "2016", "04", table.iloc[16,6] + table.iloc[20,6]],\
        ["ind", "2016", "04", table.iloc[17,6] + table.iloc[21,6]],\
        ["oth", "2016", "04", table.iloc[18,6] + table.iloc[22,6]]]
d201604 = pd.DataFrame(data,columns= ["sector", "year", "month", "value"])

# May    
sheetName = '総括表（数量）201605'
table=pd.read_excel(file_path,sheet_name=sheetName)

data = [["res", "2016", "05", table.iloc[19,6]],\
        ["com", "2016", "05", table.iloc[16,6] + table.iloc[20,6]],\
        ["ind", "2016", "05", table.iloc[17,6] + table.iloc[21,6]],\
        ["oth", "2016", "05", table.iloc[18,6] + table.iloc[22,6]]]
d201605 = pd.DataFrame(data,columns= ["sector", "year", "month", "value"])

# Jun    
sheetName = '総括表（数量）201606'
table=pd.read_excel(file_path,sheet_name=sheetName)

data = [["res", "2016", "06", table.iloc[19,6]],\
        ["com", "2016", "06", table.iloc[16,6] + table.iloc[20,6]],\
        ["ind", "2016", "06", table.iloc[17,6] + table.iloc[21,6]],\
        ["oth", "2016", "06", table.iloc[18,6] + table.iloc[22,6]]]
d201606 = pd.DataFrame(data,columns= ["sector", "year", "month", "value"])

# Jul    
sheetName = '総括表（数量）201607'
table=pd.read_excel(file_path,sheet_name=sheetName)

data = [["res", "2016", "07", table.iloc[19,6]],\
        ["com", "2016", "07", table.iloc[16,6] + table.iloc[20,6]],\
        ["ind", "2016", "07", table.iloc[17,6] + table.iloc[21,6]],\
        ["oth", "2016", "07", table.iloc[18,6] + table.iloc[22,6]]]
d201607 = pd.DataFrame(data,columns= ["sector", "year", "month", "value"])

# Aug    
sheetName = '総括表（数量）201608'
table=pd.read_excel(file_path,sheet_name=sheetName)

data = [["res", "2016", "08", table.iloc[19,6]],\
        ["com", "2016", "08", table.iloc[16,6] + table.iloc[20,6]],\
        ["ind", "2016", "08", table.iloc[17,6] + table.iloc[21,6]],\
        ["oth", "2016", "08", table.iloc[18,6] + table.iloc[22,6]]]
d201608 = pd.DataFrame(data,columns= ["sector", "year", "month", "value"])

# Sep    
sheetName = '総括表（数量）201609'
table=pd.read_excel(file_path,sheet_name=sheetName)

data = [["res", "2016", "09", table.iloc[19,6]],\
        ["com", "2016", "09", table.iloc[16,6] + table.iloc[20,6]],\
        ["ind", "2016", "09", table.iloc[17,6] + table.iloc[21,6]],\
        ["oth", "2016", "09", table.iloc[18,6] + table.iloc[22,6]]]
d201609 = pd.DataFrame(data,columns= ["sector", "year", "month", "value"])

# Oct    
sheetName = '総括表（数量）201610'
table=pd.read_excel(file_path,sheet_name=sheetName)

data = [["res", "2016", "10", table.iloc[19,6]],\
        ["com", "2016", "10", table.iloc[16,6] + table.iloc[20,6]],\
        ["ind", "2016", "10", table.iloc[17,6] + table.iloc[21,6]],\
        ["oth", "2016", "10", table.iloc[18,6] + table.iloc[22,6]]]
d201610 = pd.DataFrame(data,columns= ["sector", "year", "month", "value"])

# Nov    
sheetName = '総括表（数量）201611'
table=pd.read_excel(file_path,sheet_name=sheetName)

data = [["res", "2016", "11", table.iloc[19,6]],\
        ["com", "2016", "11", table.iloc[16,6] + table.iloc[20,6]],\
        ["ind", "2016", "11", table.iloc[17,6] + table.iloc[21,6]],\
        ["oth", "2016", "11", table.iloc[18,6] + table.iloc[22,6]]]
d201611 = pd.DataFrame(data,columns= ["sector", "year", "month", "value"])

# Dec    
sheetName = '総括表（数量）201612'
table=pd.read_excel(file_path,sheet_name=sheetName)

data = [["res", "2016", "12", table.iloc[19,6]],\
        ["com", "2016", "12", table.iloc[16,6] + table.iloc[20,6]],\
        ["ind", "2016", "12", table.iloc[17,6] + table.iloc[21,6]],\
        ["oth", "2016", "12", table.iloc[18,6] + table.iloc[22,6]]]
d201612 = pd.DataFrame(data,columns= ["sector", "year", "month", "value"])


## 2017 

#文件路径
file_path = r'C:\\Users\\jiaxi\\OneDrive\\桌面\\Japan\\Japan Reports\\Non Elc\\2017 Summary Japan.xlsx'
# Jan
# 读取sheet的名字
sheetName = '総括表（数量）201701'
table = pd.read_excel(file_path,sheet_name=sheetName)

data =  [["res", "2017", "01", table.iloc[19,6]],\
         ["com", "2017", "01", table.iloc[16,6] + table.iloc[20,6]],\
         ["ind", "2017", "01", table.iloc[17,6] + table.iloc[21,6]],\
         ["oth", "2017", "01", table.iloc[18,6] + table.iloc[22,6]]]
d201701 = pd.DataFrame(data,columns= ["sector", "year", "month", "value"])

# Feb    
sheetName='総括表（数量）201702'
table = pd.read_excel(file_path,sheet_name=sheetName)

data = [["res", "2017", "02", table.iloc[19,6]],\
        ["com", "2017", "02", table.iloc[16,6] + table.iloc[20,6]],\
        ["ind", "2017", "02", table.iloc[17,6] + table.iloc[21,6]],\
        ["oth", "2017", "02", table.iloc[18,6] + table.iloc[22,6]]]
d201702 = pd.DataFrame(data,columns= ["sector", "year", "month", "value"])

# Mar    
sheetName = '総括表（数量）201703'
table=pd.read_excel(file_path,sheet_name=sheetName)

data = [["res", "2017", "03", table.iloc[19,6]],\
        ["com", "2017", "03", table.iloc[16,6] + table.iloc[20,6]],\
        ["ind", "2017", "03", table.iloc[17,6] + table.iloc[21,6]],\
        ["oth", "2017", "03", table.iloc[18,6] + table.iloc[22,6]]]
d201703 = pd.DataFrame(data,columns= ["sector", "year", "month", "value"])

# Apr    
sheetName = '総括表（数量）201704'
table=pd.read_excel(file_path,sheet_name=sheetName)

data = [["res", "2017", "04", table.iloc[19,6]],\
        ["com", "2017", "04", table.iloc[20,6]],\
        ["ind", "2017", "04", table.iloc[21,6]],\
        ["oth", "2017", "04", table.iloc[22,6]]]
d201704 = pd.DataFrame(data,columns= ["sector", "year", "month", "value"])

# May    
sheetName = '総括表（数量）201705'
table=pd.read_excel(file_path,sheet_name=sheetName)

data = [["res", "2017", "05", table.iloc[19,6]],\
        ["com", "2017", "05", table.iloc[20,6]],\
        ["ind", "2017", "05", table.iloc[21,6]],\
        ["oth", "2017", "05", table.iloc[22,6]]]
d201705 = pd.DataFrame(data,columns= ["sector", "year", "month", "value"])

# Jun    
sheetName = '総括表（数量）201706'
table=pd.read_excel(file_path,sheet_name=sheetName)

data = [["res", "2017", "06", table.iloc[19,6]],\
        ["com", "2017", "06", table.iloc[20,6]],\
        ["ind", "2017", "06", table.iloc[21,6]],\
        ["oth", "2017", "06", table.iloc[22,6]]]
d201706 = pd.DataFrame(data,columns= ["sector", "year", "month", "value"])

# Jul    
sheetName = '総括表（数量）201707'
table=pd.read_excel(file_path,sheet_name=sheetName)

data = [["res", "2017", "07", table.iloc[19,6]],\
        ["com", "2017", "07", table.iloc[20,6]],\
        ["ind", "2017", "07", table.iloc[21,6]],\
        ["oth", "2017", "07", table.iloc[22,6]]]
d201707 = pd.DataFrame(data,columns= ["sector", "year", "month", "value"])

# Aug    
sheetName = '総括表（数量）201708'
table=pd.read_excel(file_path,sheet_name=sheetName)

data = [["res", "2017", "08", table.iloc[19,6]],\
        ["com", "2017", "08", table.iloc[20,6]],\
        ["ind", "2017", "08", table.iloc[21,6]],\
        ["oth", "2017", "08", table.iloc[22,6]]]
d201708 = pd.DataFrame(data,columns= ["sector", "year", "month", "value"])

# Sep    
sheetName = '総括表（数量）201709'
table=pd.read_excel(file_path,sheet_name=sheetName)

data = [["res", "2017", "09", table.iloc[19,6]],\
        ["com", "2017", "09", table.iloc[20,6]],\
        ["ind", "2017", "09", table.iloc[21,6]],\
        ["oth", "2017", "09", table.iloc[22,6]]]
d201709 = pd.DataFrame(data,columns= ["sector", "year", "month", "value"])

# Oct    
sheetName = '総括表（数量）201710'
table=pd.read_excel(file_path,sheet_name=sheetName)

data = [["res", "2017", "10", table.iloc[19,6]],\
        ["com", "2017", "10", table.iloc[20,6]],\
        ["ind", "2017", "10", table.iloc[21,6]],\
        ["oth", "2017", "10", table.iloc[22,6]]]
d201710 = pd.DataFrame(data,columns= ["sector", "year", "month", "value"])

# Nov    
sheetName = '総括表（数量）201711'
table=pd.read_excel(file_path,sheet_name=sheetName)

data = [["res", "2017", "11", table.iloc[19,6]],\
        ["com", "2017", "11", table.iloc[20,6]],\
        ["ind", "2017", "11", table.iloc[21,6]],\
        ["oth", "2017", "11", table.iloc[22,6]]]
d201711 = pd.DataFrame(data,columns= ["sector", "year", "month", "value"])

# Dec    
sheetName = '総括表（数量）201712'
table=pd.read_excel(file_path,sheet_name=sheetName)

data = [["res", "2017", "12", table.iloc[19,6]],\
        ["com", "2017", "12", table.iloc[20,6]],\
        ["ind", "2017", "12", table.iloc[21,6]],\
        ["oth", "2017", "12", table.iloc[22,6]]]
d201712 = pd.DataFrame(data,columns= ["sector", "year", "month", "value"])


## 2018 

#文件路径
file_path = r'C:\\Users\\jiaxi\\OneDrive\\桌面\\Japan\\Japan Reports\\Non Elc\\2018 Summary Japan.xlsx'
# Jan
# 读取sheet的名字
sheetName = '総括表（数量）201801'
table = pd.read_excel(file_path,sheet_name=sheetName)

data =  [["res", "2018", "01", table.iloc[19,6]],\
         ["com", "2018", "01", table.iloc[20,6]],\
         ["ind", "2018", "01", table.iloc[21,6]],\
         ["oth", "2018", "01", table.iloc[22,6]]]
d201801 = pd.DataFrame(data,columns= ["sector", "year", "month", "value"])

# Feb    
sheetName='総括表（数量）201802'
table = pd.read_excel(file_path,sheet_name=sheetName)

data = [["res", "2018", "02", table.iloc[19,6]],\
        ["com", "2018", "02", table.iloc[20,6]],\
        ["ind", "2018", "02", table.iloc[21,6]],\
        ["oth", "2018", "02", table.iloc[22,6]]]
d201802 = pd.DataFrame(data,columns= ["sector", "year", "month", "value"])

# Mar    
sheetName = '総括表（数量）201803'
table=pd.read_excel(file_path,sheet_name=sheetName)

data = [["res", "2018", "03", table.iloc[19,6]],\
        ["com", "2018", "03", table.iloc[20,6]],\
        ["ind", "2018", "03", table.iloc[21,6]],\
        ["oth", "2018", "03", table.iloc[22,6]]]
d201803 = pd.DataFrame(data,columns= ["sector", "year", "month", "value"])

# Apr    
sheetName = '総括表（数量）201804'
table=pd.read_excel(file_path,sheet_name=sheetName)

data = [["res", "2018", "04", table.iloc[19,6]],\
        ["com", "2018", "04", table.iloc[20,6]],\
        ["ind", "2018", "04", table.iloc[21,6]],\
        ["oth", "2018", "04", table.iloc[22,6]]]
d201804 = pd.DataFrame(data,columns= ["sector", "year", "month", "value"])

# May    
sheetName = '総括表（数量）201805'
table=pd.read_excel(file_path,sheet_name=sheetName)

data = [["res", "2018", "05", table.iloc[19,6]],\
        ["com", "2018", "05", table.iloc[20,6]],\
        ["ind", "2018", "05", table.iloc[21,6]],\
        ["oth", "2018", "05", table.iloc[22,6]]]
d201805 = pd.DataFrame(data,columns= ["sector", "year", "month", "value"])

# Jun    
sheetName = '総括表（数量）201806'
table=pd.read_excel(file_path,sheet_name=sheetName)

data = [["res", "2018", "06", table.iloc[19,6]],\
        ["com", "2018", "06", table.iloc[20,6]],\
        ["ind", "2018", "06", table.iloc[21,6]],\
        ["oth", "2018", "06", table.iloc[22,6]]]
d201806 = pd.DataFrame(data,columns= ["sector", "year", "month", "value"])

# Jul    
sheetName = '総括表（数量）201807'
table=pd.read_excel(file_path,sheet_name=sheetName)

data = [["res", "2018", "07", table.iloc[19,6]],\
        ["com", "2018", "07", table.iloc[20,6]],\
        ["ind", "2018", "07", table.iloc[21,6]],\
        ["oth", "2018", "07", table.iloc[22,6]]]
d201807 = pd.DataFrame(data,columns= ["sector", "year", "month", "value"])

# Aug    
sheetName = '総括表（数量）201808'
table=pd.read_excel(file_path,sheet_name=sheetName)

data = [["res", "2018", "08", table.iloc[19,6]],\
        ["com", "2018", "08", table.iloc[20,6]],\
        ["ind", "2018", "08", table.iloc[21,6]],\
        ["oth", "2018", "08", table.iloc[22,6]]]
d201808 = pd.DataFrame(data,columns= ["sector", "year", "month", "value"])

# Sep    
sheetName = '総括表（数量）201809'
table=pd.read_excel(file_path,sheet_name=sheetName)

data = [["res", "2018", "09", table.iloc[19,6]],\
        ["com", "2018", "09", table.iloc[20,6]],\
        ["ind", "2018", "09", table.iloc[21,6]],\
        ["oth", "2018", "09", table.iloc[22,6]]]
d201809 = pd.DataFrame(data,columns= ["sector", "year", "month", "value"])

# Oct    
sheetName = '総括表（数量）201810'
table=pd.read_excel(file_path,sheet_name=sheetName)

data = [["res", "2018", "10", table.iloc[19,6]],\
        ["com", "2018", "10", table.iloc[20,6]],\
        ["ind", "2018", "10", table.iloc[21,6]],\
        ["oth", "2018", "10", table.iloc[22,6]]]
d201810 = pd.DataFrame(data,columns= ["sector", "year", "month", "value"])

# Nov    
sheetName = '総括表（数量）201811'
table=pd.read_excel(file_path,sheet_name=sheetName)

data = [["res", "2018", "11", table.iloc[19,6]],\
        ["com", "2018", "11", table.iloc[20,6]],\
        ["ind", "2018", "11", table.iloc[21,6]],\
        ["oth", "2018", "11", table.iloc[22,6]]]
d201811 = pd.DataFrame(data,columns= ["sector", "year", "month", "value"])

# Dec    
sheetName = '総括表（数量）201812'
table=pd.read_excel(file_path,sheet_name=sheetName)

data = [["res", "2018", "12", table.iloc[19,6]],\
        ["com", "2018", "12", table.iloc[20,6]],\
        ["ind", "2018", "12", table.iloc[21,6]],\
        ["oth", "2018", "12", table.iloc[22,6]]]
d201812 = pd.DataFrame(data,columns= ["sector", "year", "month", "value"])


## 2019 

#文件路径
file_path = r'C:\\Users\\jiaxi\\OneDrive\\桌面\\Japan\\Japan Reports\\Non Elc\\201901 Japan.xlsx'
# Jan
# 读取sheet的名字
sheetName = '総括表（数量）201901'
table = pd.read_excel(file_path,sheet_name=sheetName)

data =  [["res", "2019", "01", table.iloc[19,6]],\
         ["com", "2019", "01", table.iloc[20,6]],\
         ["ind", "2019", "01", table.iloc[21,6]],\
         ["oth", "2019", "01", table.iloc[22,6]]]
d201901 = pd.DataFrame(data,columns= ["sector", "year", "month", "value"])

# Feb    
file_path = r'C:\\Users\\jiaxi\\OneDrive\\桌面\\Japan\\Japan Reports\\Non Elc\\201902 Japan.xlsx'
sheetName='総括表（数量）201902'
table = pd.read_excel(file_path,sheet_name=sheetName)

data = [["res", "2019", "02", table.iloc[19,6]],\
        ["com", "2019", "02", table.iloc[20,6]],\
        ["ind", "2019", "02", table.iloc[21,6]],\
        ["oth", "2019", "02", table.iloc[22,6]]]
d201902 = pd.DataFrame(data,columns= ["sector", "year", "month", "value"])

# Mar    
file_path = r'C:\\Users\\jiaxi\\OneDrive\\桌面\\Japan\\Japan Reports\\Non Elc\\201903 Japan.xlsx'

sheetName = '総括表（数量）201903'
table=pd.read_excel(file_path,sheet_name=sheetName)

data = [["res", "2019", "03", table.iloc[19,6]],\
        ["com", "2019", "03", table.iloc[20,6]],\
        ["ind", "2019", "03", table.iloc[21,6]],\
        ["oth", "2019", "03", table.iloc[22,6]]]
d201903 = pd.DataFrame(data,columns= ["sector", "year", "month", "value"])

# Apr    
file_path = r'C:\\Users\\jiaxi\\OneDrive\\桌面\\Japan\\Japan Reports\\Non Elc\\201904 Japan.xlsx'
sheetName = '総括表（数量）201904'
table=pd.read_excel(file_path,sheet_name=sheetName)

data = [["res", "2019", "04", table.iloc[19,6]],\
        ["com", "2019", "04", table.iloc[20,6]],\
        ["ind", "2019", "04", table.iloc[21,6]],\
        ["oth", "2019", "04", table.iloc[22,6]]]
d201904 = pd.DataFrame(data,columns= ["sector", "year", "month", "value"])

# May    
file_path = r'C:\\Users\\jiaxi\\OneDrive\\桌面\\Japan\\Japan Reports\\Non Elc\\201905 Japan.xlsx'
sheetName = '総括表（数量）201905'
table=pd.read_excel(file_path,sheet_name=sheetName)

data = [["res", "2019", "05", table.iloc[19,6]],\
        ["com", "2019", "05", table.iloc[20,6]],\
        ["ind", "2019", "05", table.iloc[21,6]],\
        ["oth", "2019", "05", table.iloc[22,6]]]
d201905 = pd.DataFrame(data,columns= ["sector", "year", "month", "value"])

# Jun
file_path = r'C:\\Users\\jiaxi\\OneDrive\\桌面\\Japan\\Japan Reports\\Non Elc\\201906 Japan.xlsx'    
sheetName = '総括表（数量）201906'
table=pd.read_excel(file_path,sheet_name=sheetName)

data = [["res", "2019", "06", table.iloc[19,6]],\
        ["com", "2019", "06", table.iloc[20,6]],\
        ["ind", "2019", "06", table.iloc[21,6]],\
        ["oth", "2019", "06", table.iloc[22,6]]]
d201906 = pd.DataFrame(data,columns= ["sector", "year", "month", "value"])

# Jul    
file_path = r'C:\\Users\\jiaxi\\OneDrive\\桌面\\Japan\\Japan Reports\\Non Elc\\201907 Japan.xlsx'
sheetName = '総括表（数量）201907'
table=pd.read_excel(file_path,sheet_name=sheetName)

data = [["res", "2019", "07", table.iloc[19,6]],\
        ["com", "2019", "07", table.iloc[20,6]],\
        ["ind", "2019", "07", table.iloc[21,6]],\
        ["oth", "2019", "07", table.iloc[22,6]]]
d201907 = pd.DataFrame(data,columns= ["sector", "year", "month", "value"])

# Aug    
file_path = r'C:\\Users\\jiaxi\\OneDrive\\桌面\\Japan\\Japan Reports\\Non Elc\\201908 Japan.xlsx'
sheetName = '総括表（数量）201908'
table=pd.read_excel(file_path,sheet_name=sheetName)

data = [["res", "2019", "08", table.iloc[19,6]],\
        ["com", "2019", "08", table.iloc[20,6]],\
        ["ind", "2019", "08", table.iloc[21,6]],\
        ["oth", "2019", "08", table.iloc[22,6]]]
d201908 = pd.DataFrame(data,columns= ["sector", "year", "month", "value"])

# Sep    
file_path = r'C:\\Users\\jiaxi\\OneDrive\\桌面\\Japan\\Japan Reports\\Non Elc\\201909 Japan.xlsx'
sheetName = '総括表（数量）201909'
table=pd.read_excel(file_path,sheet_name=sheetName)

data = [["res", "2019", "09", table.iloc[19,6]],\
        ["com", "2019", "09", table.iloc[20,6]],\
        ["ind", "2019", "09", table.iloc[21,6]],\
        ["oth", "2019", "09", table.iloc[22,6]]]
d201909 = pd.DataFrame(data,columns= ["sector", "year", "month", "value"])

# Oct    
file_path = r'C:\\Users\\jiaxi\\OneDrive\\桌面\\Japan\\Japan Reports\\Non Elc\\201910 Japan.xlsx'
sheetName = '総括表（数量）201910'
table=pd.read_excel(file_path,sheet_name=sheetName)

data = [["res", "2019", "10", table.iloc[19,6]],\
        ["com", "2019", "10", table.iloc[20,6]],\
        ["ind", "2019", "10", table.iloc[21,6]],\
        ["oth", "2019", "10", table.iloc[22,6]]]
d201910 = pd.DataFrame(data,columns= ["sector", "year", "month", "value"])

# Nov    
file_path = r'C:\\Users\\jiaxi\\OneDrive\\桌面\\Japan\\Japan Reports\\Non Elc\\201911 Japan.xlsx'
sheetName = '総括表（数量）201911'
table=pd.read_excel(file_path,sheet_name=sheetName)

data = [["res", "2019", "11", table.iloc[19,6]],\
        ["com", "2019", "11", table.iloc[20,6]],\
        ["ind", "2019", "11", table.iloc[21,6]],\
        ["oth", "2019", "11", table.iloc[22,6]]]
d201911 = pd.DataFrame(data,columns= ["sector", "year", "month", "value"])

# Dec    
file_path = r'C:\\Users\\jiaxi\\OneDrive\\桌面\\Japan\\Japan Reports\\Non Elc\\201912 Japan.xlsx'
sheetName = '総括表（数量）201912'
table=pd.read_excel(file_path,sheet_name=sheetName)

data = [["res", "2019", "12", table.iloc[19,6]],\
        ["com", "2019", "12", table.iloc[20,6]],\
        ["ind", "2019", "12", table.iloc[21,6]],\
        ["oth", "2019", "12", table.iloc[22,6]]]
d201912 = pd.DataFrame(data,columns= ["sector", "year", "month", "value"])

## 2020 

#文件路径
file_path = r'C:\\Users\\jiaxi\\OneDrive\\桌面\\Japan\\Japan Reports\\Non Elc\\202001 Japan.xlsx'
# Jan
# 读取sheet的名字
sheetName = '総括表（数量）202001'
table = pd.read_excel(file_path,sheet_name=sheetName)

data =  [["res", "2020", "01", table.iloc[19,6]],\
         ["com", "2020", "01", table.iloc[20,6]],\
         ["ind", "2020", "01", table.iloc[21,6]],\
         ["oth", "2020", "01", table.iloc[22,6]]]
d202001 = pd.DataFrame(data,columns= ["sector", "year", "month", "value"])

# Feb    
file_path = r'C:\\Users\\jiaxi\\OneDrive\\桌面\\Japan\\Japan Reports\\Non Elc\\202002 Japan.xlsx'
sheetName='総括表（数量）202002'
table = pd.read_excel(file_path,sheet_name=sheetName)

data = [["res", "2020", "02", table.iloc[19,6]],\
        ["com", "2020", "02", table.iloc[20,6]],\
        ["ind", "2020", "02", table.iloc[21,6]],\
        ["oth", "2020", "02", table.iloc[22,6]]]
d202002 = pd.DataFrame(data,columns= ["sector", "year", "month", "value"])

# Mar    
file_path = r'C:\\Users\\jiaxi\\OneDrive\\桌面\\Japan\\Japan Reports\\Non Elc\\202003 Japan.xlsx'

sheetName = '総括表（数量）202003'
table=pd.read_excel(file_path,sheet_name=sheetName)

data = [["res", "2020", "03", table.iloc[19,6]],\
        ["com", "2020", "03", table.iloc[20,6]],\
        ["ind", "2020", "03", table.iloc[21,6]],\
        ["oth", "2020", "03", table.iloc[22,6]]]
d202003 = pd.DataFrame(data,columns= ["sector", "year", "month", "value"])

# Apr    
file_path = r'C:\\Users\\jiaxi\\OneDrive\\桌面\\Japan\\Japan Reports\\Non Elc\\202004 Japan.xlsx'
sheetName = '総括表（数量）202004'
table=pd.read_excel(file_path,sheet_name=sheetName)

data = [["res", "2020", "04", table.iloc[19,6]],\
        ["com", "2020", "04", table.iloc[20,6]],\
        ["ind", "2020", "04", table.iloc[21,6]],\
        ["oth", "2020", "04", table.iloc[22,6]]]
d202004 = pd.DataFrame(data,columns= ["sector", "year", "month", "value"])

# May    
file_path = r'C:\\Users\\jiaxi\\OneDrive\\桌面\\Japan\\Japan Reports\\Non Elc\\202005 Japan.xlsx'
sheetName = '総括表（数量）202005'
table=pd.read_excel(file_path,sheet_name=sheetName)

data = [["res", "2020", "05", table.iloc[19,6]],\
        ["com", "2020", "05", table.iloc[20,6]],\
        ["ind", "2020", "05", table.iloc[21,6]],\
        ["oth", "2020", "05", table.iloc[22,6]]]
d202005 = pd.DataFrame(data,columns= ["sector", "year", "month", "value"])

# Jun
file_path = r'C:\\Users\\jiaxi\\OneDrive\\桌面\\Japan\\Japan Reports\\Non Elc\\202006 Japan.xlsx'    
sheetName = '総括表（数量）202006'
table=pd.read_excel(file_path,sheet_name=sheetName)

data = [["res", "2020", "06", table.iloc[19,6]],\
        ["com", "2020", "06", table.iloc[20,6]],\
        ["ind", "2020", "06", table.iloc[21,6]],\
        ["oth", "2020", "06", table.iloc[22,6]]]
d202006 = pd.DataFrame(data,columns= ["sector", "year", "month", "value"])

# Jul    
file_path = r'C:\\Users\\jiaxi\\OneDrive\\桌面\\Japan\\Japan Reports\\Non Elc\\202007 Japan.xlsx'
sheetName = '総括表（数量）202007'
table=pd.read_excel(file_path,sheet_name=sheetName)

data = [["res", "2020", "07", table.iloc[19,6]],\
        ["com", "2020", "07", table.iloc[20,6]],\
        ["ind", "2020", "07", table.iloc[21,6]],\
        ["oth", "2020", "07", table.iloc[22,6]]]
d202007 = pd.DataFrame(data,columns= ["sector", "year", "month", "value"])

# Aug    
file_path = r'C:\\Users\\jiaxi\\OneDrive\\桌面\\Japan\\Japan Reports\\Non Elc\\202008 Japan.xlsx'
sheetName = '総括表（数量）202008'
table=pd.read_excel(file_path,sheet_name=sheetName)

data = [["res", "2020", "08", table.iloc[19,6]],\
        ["com", "2020", "08", table.iloc[20,6]],\
        ["ind", "2020", "08", table.iloc[21,6]],\
        ["oth", "2020", "08", table.iloc[22,6]]]
d202008 = pd.DataFrame(data,columns= ["sector", "year", "month", "value"])

'''
# Sep    
file_path = r'C:\\Users\\jiaxi\\OneDrive\\桌面\\Japan\\Japan Reports\\Non Elc\\202009 Japan.xlsx'
sheetName = '総括表（数量）202009'
table=pd.read_excel(file_path,sheet_name=sheetName)

data = [["res", "2020", "09", table.iloc[19,6]],\
        ["com", "2020", "09", table.iloc[20,6]],\
        ["ind", "2020", "09", table.iloc[21,6]],\
        ["oth", "2020", "09", table.iloc[22,6]]]
d202009 = pd.DataFrame(data,columns= ["sector", "year", "month", "value"])

# Oct    
file_path = r’C:\\Users\\jiaxi\\OneDrive\\桌面\\Japan\\Japan Reports\\Non Elc\\202010 Japan.xlsx'
sheetName = '総括表（数量）202010'
table=pd.read_excel(file_path,sheet_name=sheetName)

data = [["res", "2020", "10", table.iloc[19,6]],\
        ["com", "2020", "10", table.iloc[20,6]],\
        ["ind", "2020", "10", table.iloc[21,6]],\
        ["oth", "2020", "10", table.iloc[22,6]]]
d202010 = pd.DataFrame(data,columns= ["sector", "year", "month", "value"])

# Nov    
file_path = r'C:\\Users\\jiaxi\\OneDrive\\桌面\\Japan\\Japan Reports\\Non Elc\\202011 Japan.xlsx'
sheetName = '総括表（数量）202011'
table=pd.read_excel(file_path,sheet_name=sheetName)

data = [["res", "2020", "11", table.iloc[19,6]],\
        ["com", "2020", "11", table.iloc[20,6]],\
        ["ind", "2020", "11", table.iloc[21,6]],\
        ["oth", "2020", "11", table.iloc[22,6]]]
d202011 = pd.DataFrame(data,columns= ["sector", "year", "month", "value"])

# Dec    
file_path = r'C:\\Users\\jiaxi\\OneDrive\\桌面\\Japan\\Japan Reports\\Non Elc\\202012 Japan.xlsx'
sheetName = '総括表（数量）202012'
table=pd.read_excel(file_path,sheet_name=sheetName)

data = [["res", "2020", "12", table.iloc[19,6]],\
        ["com", "2020", "12", table.iloc[20,6]],\
        ["ind", "2020", "12", table.iloc[21,6]],\
        ["oth", "2020", "12", table.iloc[22,6]]]
d202012 = pd.DataFrame(data,columns= ["sector", "year", "month", "value"])
'''

###############3

Output1 = [d201301, d201302, d201303, d201304, d201305, d201306, d201307, d201308, d201309, d201310, d201311, d201312, \
           d201401, d201402, d201403, d201404, d201405, d201406, d201407, d201408, d201409, d201410, d201411, d201412, \
           d201501, d201502, d201503, d201504, d201505, d201506, d201507, d201508, d201509, d201510, d201511, d201512, \
           d201601, d201602, d201603, d201604, d201605, d201606, d201607, d201608, d201609, d201610, d201611, d201612, \
           d201701, d201702, d201703, d201704, d201705, d201706, d201707, d201708, d201709, d201710, d201711, d201712, \
           d201801, d201802, d201803, d201804, d201805, d201806, d201807, d201808, d201809, d201810, d201811, d201812, \
           d201901, d201902, d201903, d201904, d201905, d201906, d201907, d201908, d201909, d201910, d201911, d201912, \
           d202001, d202002, d202003, d202004, d202005, d202006, d202007, d202008 ]
#, d202009, d202010, d202011, d202012        ]

Output2 = pd.concat(Output1)
Output2.to_csv('C:\\Users\\jiaxi\\OneDrive\\桌面\\Japan\\Japan Reports\\Summary.csv',index=None)


endtime = datetime.datetime.now()
print ("duration：", endtime - starttime)

print("Congradutions! Finished :)")
