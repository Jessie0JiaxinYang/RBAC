# 2022 0118 Indonesia 
# Natural gas consumption
# Source: https://www.esdm.go.id/en/publication/handbook-of-energy-economic-statistics-of-indonesia-heesi
# pipe & LNG exports can only be found in table 6.3.3

# 2022 0120
# annual production, consumption by sector can be picked in balance table, in the beginning. 
# Bug: 2017 there is partial data, not whole year. Do not know how to fixx this...


import camelot
import pandas as pd
import tabula
from pandas.core.frame import DataFrame
import datetime


starttime = datetime.datetime.now()
'''
df = tabula.read_pdf("C:\\Users\\jiaxi\\OneDrive\\Desktop\\RBAC 2022\\Local\\Indonesia\\content-handbook-of-energy-and-economic-statistics-of-indonesia-2020.pdf", pages='71')
a = df[0]

df2 = tabula.read_pdf("C:\\Users\\jiaxi\\OneDrive\\Desktop\\RBAC 2022\\Local\\Indonesia\\content-handbook-of-energy-and-economic-statistics-of-indonesia-2020.pdf", pages='72')
b = df2[0]

df3 = tabula.read_pdf("C:\\Users\\jiaxi\\OneDrive\\Desktop\\RBAC 2022\\Local\\Indonesia\\content-handbook-of-energy-and-economic-statistics-of-indonesia-2020.pdf", pages='39')
c = df3[0]

df4 = tabula.read_pdf("C:\\Users\\jiaxi\\OneDrive\\Desktop\\RBAC 2022\\Local\\Indonesia\\content-handbook-of-energy-and-economic-statistics-of-indonesia-2020.pdf", pages='42')
d = df4[0]

df5 = tabula.read_pdf("C:\\Users\\jiaxi\\OneDrive\\Desktop\\RBAC 2022\\Local\\Indonesia\\content-handbook-of-energy-and-economic-statistics-of-indonesia-2020.pdf", pages='45')
e = df5[0]

df6 = tabula.read_pdf("C:\\Users\\jiaxi\\OneDrive\\Desktop\\RBAC 2022\\Local\\Indonesia\\content-handbook-of-energy-and-economic-statistics-of-indonesia-2020.pdf", pages='48')
f = df6[0]


df7 = tabula.read_pdf("C:\\Users\\jiaxi\\OneDrive\\Desktop\\RBAC 2022\\Local\\Indonesia\\content-handbook-of-energy-and-economic-statistics-of-indonesia-2020.pdf", pages='69')
g = df7[0]

df8 = tabula.read_pdf("C:\\Users\\jiaxi\\OneDrive\\Desktop\\RBAC 2022\\Local\\Indonesia\\content-handbook-of-energy-and-economic-statistics-of-indonesia-2020.pdf", pages='70')
h = df8[0]

df9 = tabula.read_pdf("C:\\Users\\jiaxi\\OneDrive\\Desktop\\RBAC 2022\\Local\\Indonesia\\content-handbook-of-energy-and-economic-statistics-of-indonesia-2020.pdf", pages='73')
i = df9[0]

df10 = tabula.read_pdf("C:\\Users\\jiaxi\\OneDrive\\Desktop\\RBAC 2022\\Local\\Indonesia\\content-handbook-of-energy-and-economic-statistics-of-indonesia-2020.pdf", pages='22')
j = df10[0]

'''

# 2020
df = tabula.read_pdf("C:\\Users\\jiaxi\\OneDrive\\Desktop\\RBAC 2022\\Local\\Indonesia\\content-handbook-of-energy-and-economic-statistics-of-indonesia-2020.pdf", pages='22')
a = df[0]
B = [["Local", "2020","", "Indonesia", "production", "",  "thousand BOE", a.iloc[1,11]], \
     ["Local", "2020","", "Indonesia", "consumption", "ELC",  "thousand BOE", a.iloc[11,11]], \
     ["Local", "2020","", "Indonesia", "consumption", "IND",  "thousand BOE", a.iloc[24,11]], \
     ["Local", "2020","", "Indonesia", "consumption", "TRN",  "thousand BOE", a.iloc[25,11]], \
     ["Local", "2020","", "Indonesia", "consumption", "RES",  "thousand BOE", a.iloc[26,11]], \
     ["Local", "2020","", "Indonesia", "consumption", "COM",  "thousand BOE", a.iloc[27,11]]]   
z20 = pd.DataFrame(B,columns=["source", "year", "period", "country", "sector", "sector2", "unit", "value"])

# 2019
df = tabula.read_pdf("C:\\Users\\jiaxi\\OneDrive\\Desktop\\RBAC 2022\\Local\\Indonesia\\content-handbook-of-energy-and-economic-statistics-of-indonesia-2019.pdf", pages='21')
a = df[0]
B = [["Local", "2019","", "Indonesia", "production", "",  "thousand BOE", a.iloc[11,11]], \
     ["Local", "2019","", "Indonesia", "consumption", "ELC",  "thousand BOE", a.iloc[21,11]], \
     ["Local", "2019","", "Indonesia", "consumption", "IND",  "thousand BOE", a.iloc[39,11]], \
     ["Local", "2019","", "Indonesia", "consumption", "TRN",  "thousand BOE", a.iloc[40,11]], \
     ["Local", "2019","", "Indonesia", "consumption", "RES",  "thousand BOE", a.iloc[41,11]], \
     ["Local", "2019","", "Indonesia", "consumption", "COM",  "thousand BOE", a.iloc[42,11]]]    
z19 = pd.DataFrame(B,columns=["source", "year", "period", "country", "sector", "sector2", "unit", "value"])

# 2018
df = tabula.read_pdf("C:\\Users\\jiaxi\\OneDrive\\Desktop\\RBAC 2022\\Local\\Indonesia\\content-handbook-of-energy-and-economic-statistics-of-indonesia-2018.pdf", pages='21')
a = df[1]
B = [["Local", "2018","", "Indonesia", "production", "",  "thousand BOE", a.iloc[0,11]], \
     ["Local", "2018","", "Indonesia", "consumption", "ELC",  "thousand BOE", a.iloc[10,11]], \
     ["Local", "2018","", "Indonesia", "consumption", "IND",  "thousand BOE", a.iloc[28,11]], \
     ["Local", "2018","", "Indonesia", "consumption", "TRN",  "thousand BOE", a.iloc[29,11]], \
     ["Local", "2018","", "Indonesia", "consumption", "RES",  "thousand BOE", a.iloc[30,11]], \
     ["Local", "2018","", "Indonesia", "consumption", "COM",  "thousand BOE", a.iloc[31,11]]]    
z18 = pd.DataFrame(B,columns=["source", "year", "period", "country", "sector", "sector2", "unit", "value"])

# 2017
df = tabula.read_pdf("C:\\Users\\jiaxi\\OneDrive\\Desktop\\RBAC 2022\\Local\\Indonesia\\content-handbook-of-energy-and-economic-statistics-of-indonesia-2017.pdf", pages='15')
a = df[0]
B = [["Local", "2017","", "Indonesia", "production", "",  "thousand BOE", a.iloc[5,7]], \
     ["Local", "2017","", "Indonesia", "consumption", "ELC",  "thousand BOE", a.iloc[14,7]], \
     ["Local", "2017","", "Indonesia", "consumption", "IND",  "thousand BOE", a.iloc[30,7]], \
     ["Local", "2017","", "Indonesia", "consumption", "TRN",  "thousand BOE", a.iloc[31,7]], \
     ["Local", "2017","", "Indonesia", "consumption", "RES",  "thousand BOE", a.iloc[32,7]], \
     ["Local", "2017","", "Indonesia", "consumption", "COM",  "thousand BOE", a.iloc[33,7]]]    
z17 = pd.DataFrame(B,columns=["source", "year", "period", "country", "sector", "sector2", "unit", "value"])

# 2016
df = tabula.read_pdf("C:\\Users\\jiaxi\\OneDrive\\Desktop\\RBAC 2022\\Local\\Indonesia\\content-handbook-of-energy-and-economic-statistics-of-indonesia-2017.pdf", pages='14')
a = df[0]
B = [["Local", "2016","", "Indonesia", "production", "",  "thousand BOE", a.iloc[5,7]], \
     ["Local", "2016","", "Indonesia", "consumption", "ELC",  "thousand BOE", a.iloc[14,7]], \
     ["Local", "2016","", "Indonesia", "consumption", "IND",  "thousand BOE", a.iloc[30,7]], \
     ["Local", "2016","", "Indonesia", "consumption", "TRN",  "thousand BOE", a.iloc[31,7]], \
     ["Local", "2016","", "Indonesia", "consumption", "RES",  "thousand BOE", a.iloc[32,7]], \
     ["Local", "2016","", "Indonesia", "consumption", "COM",  "thousand BOE", a.iloc[33,7]]]    
z16 = pd.DataFrame(B,columns=["source", "year", "period", "country", "sector", "sector2", "unit", "value"])

# 2015
df = tabula.read_pdf("C:\\Users\\jiaxi\\OneDrive\\Desktop\\RBAC 2022\\Local\\Indonesia\\content-handbook-of-energy-and-economic-statistics-of-indonesia-2015.pdf", pages='14')
a = df[0]
B = [["Local", "2015","", "Indonesia", "production", "",  "thousand BOE", a.iloc[5,7]], \
     ["Local", "2015","", "Indonesia", "consumption", "ELC",  "thousand BOE", "92921"], \
     ["Local", "2015","", "Indonesia", "consumption", "IND",  "thousand BOE", "92150"], \
     ["Local", "2015","", "Indonesia", "consumption", "TRN",  "thousand BOE", a.iloc[28,7]], \
     ["Local", "2015","", "Indonesia", "consumption", "RES",  "thousand BOE", a.iloc[29,7]], \
     ["Local", "2015","", "Indonesia", "consumption", "COM",  "thousand BOE", a.iloc[30,7]]]    
z15 = pd.DataFrame(B,columns=["source", "year", "period", "country", "sector", "sector2", "unit", "value"])

# 2014
df = tabula.read_pdf("C:\\Users\\jiaxi\\OneDrive\\Desktop\\RBAC 2022\\Local\\Indonesia\\content-handbook-of-energy-and-economic-statistics-of-indonesia-2014.pdf", pages='15')
a = df[0]
B = [["Local", "2014","", "Indonesia", "production", "",  "thousand BOE", a.iloc[5,7]], \
     ["Local", "2014","", "Indonesia", "consumption", "ELC",  "thousand BOE", a.iloc[13,7]], \
     ["Local", "2014","", "Indonesia", "consumption", "IND",  "thousand BOE", a.iloc[27,7]], \
     ["Local", "2014","", "Indonesia", "consumption", "TRN",  "thousand BOE", a.iloc[28,7]], \
     ["Local", "2014","", "Indonesia", "consumption", "RES",  "thousand BOE", a.iloc[29,7]], \
     ["Local", "2014","", "Indonesia", "consumption", "COM",  "thousand BOE", a.iloc[30,7]]]    
z14 = pd.DataFrame(B,columns=["source", "year", "period", "country", "sector", "sector2", "unit", "value"])

# 2013
df = tabula.read_pdf("C:\\Users\\jiaxi\\OneDrive\\Desktop\\RBAC 2022\\Local\\Indonesia\\content-handbook-of-energy-and-economic-statistics-of-indonesia-2013.pdf", pages='26')
a = df[0]
B = [["Local", "2013","", "Indonesia", "production", "",  "thousand BOE", a.iloc[5,7]], \
     ["Local", "2013","", "Indonesia", "consumption", "ELC",  "thousand BOE", a.iloc[13,7]], \
     ["Local", "2013","", "Indonesia", "consumption", "IND",  "thousand BOE", a.iloc[25,7]], \
     ["Local", "2013","", "Indonesia", "consumption", "TRN",  "thousand BOE", a.iloc[26,7]], \
     ["Local", "2013","", "Indonesia", "consumption", "RES",  "thousand BOE", a.iloc[27,7]], \
     ["Local", "2013","", "Indonesia", "consumption", "COM",  "thousand BOE", a.iloc[28,7]]]    
z13 = pd.DataFrame(B,columns=["source", "year", "period", "country", "sector", "sector2", "unit", "value"])

# 2012
df = tabula.read_pdf("C:\\Users\\jiaxi\\OneDrive\\Desktop\\RBAC 2022\\Local\\Indonesia\\content-handbook-of-energy-and-economic-statistics-of-indonesia-2012.pdf", pages='25')
a = df[3]
B = [["Local", "2012","", "Indonesia", "production", "",  "thousand BOE", a.iloc[1,8]], \
     ["Local", "2012","", "Indonesia", "consumption", "ELC",  "thousand BOE", a.iloc[9,8]], \
     ["Local", "2012","", "Indonesia", "consumption", "IND",  "thousand BOE", a.iloc[19,8]], \
     ["Local", "2012","", "Indonesia", "consumption", "TRN",  "thousand BOE", a.iloc[20,8]], \
     ["Local", "2012","", "Indonesia", "consumption", "RES",  "thousand BOE", a.iloc[21,8]], \
     ["Local", "2012","", "Indonesia", "consumption", "COM",  "thousand BOE", a.iloc[22,8]]]    
z12 = pd.DataFrame(B,columns=["source", "year", "period", "country", "sector", "sector2", "unit", "value"])

# 2011
df = tabula.read_pdf("C:\\Users\\jiaxi\\OneDrive\\Desktop\\RBAC 2022\\Local\\Indonesia\\content-handbook-of-energy-and-economic-statistics-of-indonesia-2011.pdf", pages='24')
a = df[0]
B = [["Local", "2011","", "Indonesia", "production", "",  "thousand BOE", a.iloc[5,0]], \
     ["Local", "2011","", "Indonesia", "consumption", "ELC",  "thousand BOE", a.iloc[13,0]], \
     ["Local", "2011","", "Indonesia", "consumption", "IND",  "thousand BOE", a.iloc[23,0]], \
     ["Local", "2011","", "Indonesia", "consumption", "TRN",  "thousand BOE", a.iloc[24,0]], \
     ["Local", "2011","", "Indonesia", "consumption", "RES",  "thousand BOE", a.iloc[25,0]], \
     ["Local", "2011","", "Indonesia", "consumption", "COM",  "thousand BOE", a.iloc[26,0]]]    
z11 = pd.DataFrame(B,columns=["source", "year", "period", "country", "sector", "sector2", "unit", "value"])


b = a.iloc[5,7]
Output1 = [z20, z19, z18, z17, z16, z15, z14, z13, z12, z11]

Output2 = pd.concat(Output1)

Output2.to_csv("C:\\Users\\jiaxi\\OneDrive\\Desktop\\RBAC 2022\\Local\\Indonesia\\Consumption by sector output.csv",index=None)



endtime = datetime.datetime.now()
print (endtime - starttime)

print("Congradulations! Final Finished :)")


