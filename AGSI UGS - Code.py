# -*- coding: utf-8 -*-
"""
Created on Thu Nov 19 17:06:52 2020

@author: jiaxi
"""
# Source: https://agsi.gie.eu/#/historical/
# How to dowland all countries once? In "Download" window on the right of "Data selection", select all countries. 
# After downlading from AGSI, first convert from .xls to xlsx, using "save as"
#


import pandas  as pd 
import numpy as np
from pandas import DataFrame
import datetime

starttime = datetime.datetime.now()

## 2013 

#文件路径
file_path = r'C:\Users\jiaxi\OneDrive\桌面\RBAC\LNG Infrastructure\Underground Storage\Europe\2020 1119 AGSI UGS\Raw Data\2020 1119.xlsx'

# Austria
sheetName = 'Austria'
Austria = pd.read_excel(file_path,sheet_name=sheetName)
Austria.insert(Austria.shape[1], "country", "Austria")

# Belgium
sheetName = 'Belgium'
Belgium = pd.read_excel(file_path,sheet_name=sheetName)
Belgium.insert(Belgium.shape[1], "country", "Belgium")

# Bulgaria
sheetName = 'Bulgaria'
Bulgaria = pd.read_excel(file_path,sheet_name=sheetName)
Bulgaria.insert(Bulgaria.shape[1], "country", "Bulgaria")

# Croatia
sheetName = 'Croatia'
Croatia = pd.read_excel(file_path,sheet_name=sheetName)
Croatia.insert(Croatia.shape[1], "country", "Croatia")

# Czech Republic
sheetName = 'CzechRepublic'
Czech_Republic = pd.read_excel(file_path,sheet_name=sheetName)
Czech_Republic.insert(Czech_Republic.shape[1], "country", "Czech Republic")

# Denmark
sheetName = 'Denmark'
Denmark = pd.read_excel(file_path,sheet_name=sheetName)
Denmark.insert(Denmark.shape[1], "country", "Denmark")

# France
sheetName = 'France'
France = pd.read_excel(file_path,sheet_name=sheetName)
France.insert(France.shape[1], "country", "France")

# Germany
sheetName = 'Germany'
Germany = pd.read_excel(file_path,sheet_name=sheetName)
Germany.insert(Germany.shape[1], "country", "Germany")

# Hungary
sheetName = 'Hungary'
Hungary = pd.read_excel(file_path,sheet_name=sheetName)
Hungary.insert(Hungary.shape[1], "country", "Hungary")

# Ireland
sheetName = 'Ireland'
Ireland = pd.read_excel(file_path,sheet_name=sheetName)
Ireland.insert(Ireland.shape[1], "country", "Ireland")

# Italy
sheetName = 'Italy'
Italy = pd.read_excel(file_path,sheet_name=sheetName)
Italy.insert(Italy.shape[1], "country", "Italy")

# Latvia
sheetName = 'Latvia'
Latvia = pd.read_excel(file_path,sheet_name=sheetName)
Latvia.insert(Latvia.shape[1], "country", "Latvia")

# Netherlands
sheetName = 'Netherlands'
Netherlands = pd.read_excel(file_path,sheet_name=sheetName)
Netherlands.insert(Netherlands.shape[1], "country", "Netherlands")

# Poland
sheetName = 'Poland'
Poland = pd.read_excel(file_path,sheet_name=sheetName)
Poland.insert(Poland.shape[1], "country", "Poland")

# Portugal
sheetName = 'Portugal'
Portugal = pd.read_excel(file_path,sheet_name=sheetName)
Portugal.insert(Portugal.shape[1], "country", "Portugal")

# Romania
sheetName = 'Romania'
Romania = pd.read_excel(file_path,sheet_name=sheetName)
Romania.insert(Romania.shape[1], "country", "Romania")

# Slovakia
sheetName = 'Slovakia'
Slovakia = pd.read_excel(file_path,sheet_name=sheetName)
Slovakia.insert(Slovakia.shape[1], "country", "Slovakia")

# Spain
sheetName = 'Spain'
Spain = pd.read_excel(file_path,sheet_name=sheetName)
Spain.insert(Spain.shape[1], "country", "Spain")

# Sweden
sheetName = 'Sweden'
Sweden = pd.read_excel(file_path,sheet_name=sheetName)
Sweden.insert(Sweden.shape[1], "country", "Sweden")

# United Kingdom
sheetName = 'UnitedKingdom'
United_Kingdom = pd.read_excel(file_path,sheet_name=sheetName)
United_Kingdom.insert(United_Kingdom.shape[1], "country", "United Kingdom")

# Serbia
sheetName = 'Serbia'
Serbia = pd.read_excel(file_path,sheet_name=sheetName)
Serbia.insert(Serbia.shape[1], "country", "Serbia")

# Ukraine
sheetName = 'Ukraine'
Ukraine = pd.read_excel(file_path,sheet_name=sheetName)
Ukraine.insert(Ukraine.shape[1], "country", "Ukraine")

########

# total 22 countries
Output1 = [Austria, Belgium, Bulgaria, Croatia, Czech_Republic, Denmark, France, Germany, \
           Hungary, Ireland, Italy, Latvia, Netherlands, Poland, Portugal, Romania, Slovakia, \
           Spain, Sweden, United_Kingdom, Serbia, Ukraine]
Output2 = pd.concat(Output1)

Output2.to_csv("C:\\Users\\jiaxi\\OneDrive\\桌面\\RBAC\\LNG Infrastructure\\Underground Storage\\Europe\\2020 1119 AGSI UGS\\Summary.csv",index=None)

##############

endtime = datetime.datetime.now()
print ("duration：", endtime - starttime)

print("Congradutions! Finished :)")














