#  Price grab from LNG Daily report
# starting on 2021 0618

# pip install tabula-py

import camelot
import pandas as pd
import tabula
from pandas.core.frame import DataFrame
import datetime


starttime = datetime.datetime.now()

# tables = camelot.read_pdf("C:\\Users\\jiaxi\\OneDrive\\Desktop\\RBAC 2021\\Price\\LNG Daily\\LNG_20210610.pdf", pages = '4')
# tableB2010 = tables[0].df


''' test
df = tabula.read_pdf("C:\\Users\\jiaxi\\OneDrive\\Desktop\\RBAC 2021\\Price\\LNG Daily\\LNG_20210610.pdf", pages='1')
a = df[0]
'''

# 21Jul
df = tabula.read_pdf("C:\\Users\\jiaxi\\OneDrive\\Desktop\\RBAC 2021\\Price\\LNG Daily\\LNG_20210615.pdf", pages='1')
a = df[0]

df = tabula.read_pdf("C:\\Users\\jiaxi\\OneDrive\\Desktop\\RBAC 2021\\Price\\LNG Daily\\LNG_20210615.pdf", pages='4')
a2 = df[0]
a2 = a2.iloc[68,0]
a2 = a2.split()
            
B = [["JKM", "2021/07/01", "12.125"], \
     ["JKM Singapore","2021/07/01", a.iloc[7,2]], \
     ["JKM London","2021/07/01", a.iloc[11,2]], \
     ["MED","2021/07/01", a.iloc[15,2]], \
     ["NWE","2021/07/01", a.iloc[20,2]], \
     ["MEM","2021/07/01", a.iloc[25,2]], \
     ["WIM","2021/07/01", a.iloc[32,2]], \
     ["WIM Singpore","2021/07/01", a.iloc[39,2]], \
     ["GCM","2021/07/01", a.iloc[44,2]], \
     ["TTF","2021/07/01",  a2[2]], \
     ["FOB Australia","2021/06/15", a.iloc[49,2]], \
     ["FOB Middle East","2021/06/15", a.iloc[50,2]], \
     ["FOB Brazil Marker","2021/06/15", a.iloc[51,2]], \
     ["FOB Singaporee","2021/06/15", a.iloc[52,2]], \
     ["FOB Murmansk","2021/06/15", a.iloc[53,2]]]
     
z21Jul = pd.DataFrame(B,columns=["Marker","month","$/MMBtu"])



# 21Jun
df = tabula.read_pdf("C:\\Users\\jiaxi\\OneDrive\\Desktop\\RBAC 2021\\Price\\LNG Daily\\LNG_20210514.pdf", pages='1')
a = df[0]

df = tabula.read_pdf("C:\\Users\\jiaxi\\OneDrive\\Desktop\\RBAC 2021\\Price\\LNG Daily\\LNG_20210514.pdf", pages='4')
a2 = df[0]
a2 = a2.iloc[70,0]
a2 = a2.split()

B = [["JKM", "2021/06/01", "10.200"], \
     ["JKM Singapore","2021/06/01", a.iloc[7,2]], \
     ["JKM London","2021/06/01", a.iloc[11,2]], \
     ["MED","2021/06/01", a.iloc[15,2]], \
     ["NWE","2021/06/01", a.iloc[21,2]], \
     ["MEM","2021/06/01", a.iloc[26,2]], \
     ["WIM","2021/06/01", a.iloc[33,2]], \
     ["WIM Singpore","2021/06/01", a.iloc[40,2]], \
     ["GCM","2021/06/01", a.iloc[45,2]], \
     ["TTF","2021/06/01",  a2[2]], \
     ["FOB Australia","2021/05/15", a.iloc[54,2]], \
     ["FOB Middle East","2021/05/15", a.iloc[55,2]], \
     ["FOB Brazil Marker","2021/05/15", a.iloc[56,2]], \
     ["FOB Singaporee","2021/05/15", a.iloc[57,2]], \
     ["FOB Murmansk","2021/05/15", a.iloc[58,2]]]
     
z21Jun = pd.DataFrame(B,columns=["Marker","month","$/MMBtu"])

# 21May
df = tabula.read_pdf("C:\\Users\\jiaxi\\OneDrive\\Desktop\\RBAC 2021\\Price\\LNG Daily\\LNG_20210415.pdf", pages='1')
a = df[1]
a1 = df[0]

df = tabula.read_pdf("C:\\Users\\jiaxi\\OneDrive\\Desktop\\RBAC 2021\\Price\\LNG Daily\\LNG_20210415.pdf", pages='4')
a2 = df[0]
a2 = a2.iloc[55,0]
a2 = a2.split()

B = [["JKM", "2021/05/01", "7.563"], \
     ["JKM Singapore","2021/05/01", a.iloc[7,3]], \
     ["JKM London","2021/05/01", a.iloc[12,3]], \
     ["MED","2021/05/01", a.iloc[17,3]], \
     ["NWE","2021/05/01", a.iloc[22,3]], \
     ["MEM","2021/05/01", a.iloc[27,3]], \
     ["WIM","2021/05/01", a.iloc[33,3]], \
     ["GCM","2021/05/01", a.iloc[40,3]], \
     ["TTF","2021/05/01",  a2[2]], \
     ["FOB Australia","2021/04/15", "7.100"], \
     ["FOB Middle East","2021/04/15", "7.050"], \
     ["FOB Brazil Marker","2021/04/15", a1.iloc[0,9]], \
     ["FOB Singaporee","2021/04/15", a1.iloc[1,9]], \
     ["FOB Murmansk","2021/04/15", a1.iloc[2,9]]]
     
z21May = pd.DataFrame(B,columns=["Marker","month","$/MMBtu"])


# 21Apr
df = tabula.read_pdf("C:\\Users\\jiaxi\\OneDrive\\Desktop\\RBAC 2021\\Price\\LNG Daily\\LNG_20210315.pdf", pages='1')
a = df[1]
a1 = df[0]

df = tabula.read_pdf("C:\\Users\\jiaxi\\OneDrive\\Desktop\\RBAC 2021\\Price\\LNG Daily\\LNG_20210315.pdf", pages='4')
a2 = df[0]
a2 = a2.iloc[56,0]
a2 = a2.split()

B = [["JKM", "2021/04/01", "6.713"], \
     ["JKM Singapore","2021/04/01", a.iloc[7,3]], \
     ["JKM London","2021/04/01", a.iloc[12,3]], \
     ["MED","2021/04/01", a.iloc[17,3]], \
     ["NWE","2021/04/01", a.iloc[22,3]], \
     ["MEM","2021/04/01", a.iloc[27,3]], \
     ["WIM","2021/04/01", a.iloc[33,3]], \
     ["GCM","2021/04/01", a.iloc[41,3]], \
     ["TTF","2021/04/01",  a2[2]], \
     ["FOB Australia","2021/03/15", "6.320"], \
     ["FOB Middle East","2021/03/15", "6.300"], \
     ["FOB Brazil Marker","2021/03/15", a1.iloc[0,9]], \
     ["FOB Singaporee","2021/03/15", a1.iloc[1,9]], \
     ["FOB Murmansk","2021/03/15", a1.iloc[2,9]]]
     
z21Apr = pd.DataFrame(B,columns=["Marker","month","$/MMBtu"])

# 21Mar
df = tabula.read_pdf("C:\\Users\\jiaxi\\OneDrive\\Desktop\\RBAC 2021\\Price\\LNG Daily\\LNG_20210215.pdf", pages='1')
a = df[0]
a1 = df[1]

df = tabula.read_pdf("C:\\Users\\jiaxi\\OneDrive\\Desktop\\RBAC 2021\\Price\\LNG Daily\\LNG_20210215.pdf", pages='4')
a2 = df[0]


B = [["JKM", "2021/03/01", "6.900"], \
     ["JKM Singapore","2021/03/01", a.iloc[9,3]], \
     ["JKM London","2021/03/01", a.iloc[14,3]], \
     ["MED","2021/03/01", a.iloc[19,3]], \
     ["NWE","2021/03/01", a.iloc[24,3]], \
     ["MEM","2021/03/01", a.iloc[30,3]], \
     ["WIM","2021/03/01", a.iloc[36,3]], \
     ["GCM","2021/03/01", a.iloc[43,3]], \
     ["TTF","2021/03/01", a2.iloc[56,1]], \
     ["FOB Australia","2021/02/15", "6.390"], \
     ["FOB Middle East","2021/02/15", "5.950"], \
     ["FOB Brazil Marker","2021/02/15", a1.iloc[0,9]], \
     ["FOB Singaporee","2021/02/15", a1.iloc[1,9]], \
     ["FOB Murmansk","2021/02/15", a1.iloc[2,9]]]

z21Mar = pd.DataFrame(B,columns=["Marker","month","$/MMBtu"])


# 21Feb
df = tabula.read_pdf("C:\\Users\\jiaxi\\OneDrive\\Desktop\\RBAC 2021\\Price\\LNG Daily\\LNG_20210115.pdf", pages='1')
a = df[1]
a1 = df[0]

df = tabula.read_pdf("C:\\Users\\jiaxi\\OneDrive\\Desktop\\RBAC 2021\\Price\\LNG Daily\\LNG_20210115.pdf", pages='4')
a2 = df[0]

B = [["JKM", "2021/02/01", "6.900"], \
["JKM Singapore","2021/02/01", a.iloc[7,3]], \
["JKM London","2021/02/01", a.iloc[13,3]], \
["MED","2021/02/01", a.iloc[18,3]], \
["NWE","2021/02/01", a.iloc[23,3]], \
["MEM","2021/02/01", a.iloc[28,3]], \
["WIM","2021/02/01", a.iloc[34,3]], \
["GCM","2021/02/01", a.iloc[41,3]], \
["TTF","2021/02/01", a2.iloc[58,1]], \
["FOB Australia","2021/01/15", "25.180"], \
["FOB Middle East","2021/01/15", "14.950"], \
["FOB Brazil Marker","2021/01/15", a1.iloc[0,9]], \
["FOB Singaporee","2021/01/15", a1.iloc[1,9]], \
["FOB Murmansk","2021/01/15", a1.iloc[2,9]]]

z21Feb = pd.DataFrame(B,columns=["Marker","month","$/MMBtu"])

# 21Jan
df = tabula.read_pdf("C:\\Users\\jiaxi\\OneDrive\\Desktop\\RBAC 2021\\Price\\LNG Daily\\LNG_20201215.pdf", pages='1')
a = df[0]
a1 = df[1]

df = tabula.read_pdf("C:\\Users\\jiaxi\\OneDrive\\Desktop\\RBAC 2021\\Price\\LNG Daily\\LNG_20201215.pdf", pages='4')
a2 = df[0]
a2 = a2.iloc[56,0]
a2 = a2.split()

B = [["JKM", "2021/01/01", "12.404"], \
["JKM Singapore","2021/01/01", a.iloc[7,3]], \
["JKM London","2021/01/01", a.iloc[12,3]], \
["MED","2021/01/01", a.iloc[17,3]], \
["NWE","2021/01/01", a.iloc[22,3]], \
["MEM","2021/01/01", a.iloc[27,3]], \
["WIM","2021/01/01", "11.8"], \
["GCM","2021/01/01", "8.414"], \
["TTF","2021/01/01", a2[2]], \
["FOB Australia","2020/12/15", "11.130"], \
["FOB Middle East","2020/12/15", "11.200"], \
["FOB Brazil Marker","2020/12/15", a1.iloc[0,9]], \
["FOB Singaporee","2020/12/15", a1.iloc[1,9]], \
["FOB Murmansk","2020/12/15", a1.iloc[2,9]]]

z21Jan = pd.DataFrame(B,columns=["Marker","month","$/MMBtu"])

# 20Dec
df = tabula.read_pdf("C:\\Users\\jiaxi\\OneDrive\\Desktop\\RBAC 2021\\Price\\LNG Daily\\LNG_20201113.pdf", pages='1')
a = df[0]
a1 = df[1]

df = tabula.read_pdf("C:\\Users\\jiaxi\\OneDrive\\Desktop\\RBAC 2021\\Price\\LNG Daily\\LNG_20201113.pdf", pages='3')
a2 = df[0]

B = [["JKM", "2020/12/01", "6.8"], \
["JKM Singapore","2020/12/01", a.iloc[9,3]], \
["JKM London","2020/12/01", a.iloc[14,3]], \
["MED","2020/12/01", a.iloc[19,3]], \
["NWE","2020/12/01", a.iloc[24,3]], \
["MEM","2020/12/01", a.iloc[29,3]], \
["WIM","2020/12/01", a.iloc[35,3]], \
["GCM","2020/12/01", a.iloc[43,3]], \
["TTF","2020/12/01", a2.iloc[53,2]], \
["FOB Australia","2020/11/15", "5.97"], \
["FOB Middle East","2020/11/15", "6.000"], \
["FOB Brazil Marker","2020/11/15", a1.iloc[0,9]], \
["FOB Singaporee","2020/11/15", a1.iloc[1,9]], \
["FOB Murmansk","2020/11/15", a1.iloc[2,9]]]

z20Dec = pd.DataFrame(B,columns=["Marker","month","$/MMBtu"])


# 20Nov
df = tabula.read_pdf("C:\\Users\\jiaxi\\OneDrive\\Desktop\\RBAC 2021\\Price\\LNG Daily\\LNG_20201015.pdf", pages='1')
a = df[0]
a1 = df[1]

df = tabula.read_pdf("C:\\Users\\jiaxi\\OneDrive\\Desktop\\RBAC 2021\\Price\\LNG Daily\\LNG_20201015.pdf", pages='3')
a2 = df[0]

B = [["JKM", "2020/11/01", "5.638"], \
["JKM Singapore","2020/11/01", a.iloc[7,3]], \
["JKM London","2020/11/01", a.iloc[13,3]], \
["MED","2020/11/01", a.iloc[18,3]], \
["NWE","2020/11/01", a.iloc[23,3]], \
["MEM","2020/11/01", a.iloc[29,3]], \
["WIM","2020/11/01", "5.450"], \
["GCM","2020/11/01", "4.125"], \
["TTF","2020/11/01", a2.iloc[53,2]], \
["FOB Australia","2020/10/15", "5.050"], \
["FOB Middle East","2020/10/15", "5.250"], \
["FOB Brazil Marker","2020/10/15", a1.iloc[0,9]], \
["FOB Singaporee","2020/10/15", a1.iloc[1,9]], \
["FOB Murmansk","2020/10/15", a1.iloc[2,9]]]

z20Nov = pd.DataFrame(B,columns=["Marker","month","$/MMBtu"])


# 20Oct
df = tabula.read_pdf("C:\\Users\\jiaxi\\OneDrive\\Desktop\\RBAC 2021\\Price\\LNG Daily\\LNG_20200915.pdf", pages='1')
a1 = df[0]

df = tabula.read_pdf("C:\\Users\\jiaxi\\OneDrive\\Desktop\\RBAC 2021\\Price\\LNG Daily\\LNG_20200915.pdf", pages='3')
a2 = df[0]


B = [["JKM", "2020/10/01", "4.550"], \
["JKM Singapore","2020/10/01", "4.308"], \
["JKM London","2020/10/01","4.300"], \
["MED","2020/10/01", "3.96"], \
["NWE","2020/10/01", "3.96"], \
["MEM","2020/10/01", "4.425"], \
["WIM","2020/10/01", "4.425"], \
["GCM","2020/10/01", "4.125"], \
["TTF","2020/10/01", a2.iloc[53,2]], \
["FOB Australia","2020/09/15", "4.080"], \
["FOB Middle East","2020/09/15", "4.250"], \
["FOB Brazil Marker","2020/09/15", a1.iloc[0,9]], \
["FOB Singaporee","2020/09/15", a1.iloc[1,9]], \
["FOB Murmansk","2020/09/15", a1.iloc[2,9]]]

z20Oct = pd.DataFrame(B,columns=["Marker","month","$/MMBtu"])

# 20Sep
df = tabula.read_pdf("C:\\Users\\jiaxi\\OneDrive\\Desktop\\RBAC 2021\\Price\\LNG Daily\\LNG_20200814.pdf", pages='1')
a = df[1]
a1 = df[0]

df = tabula.read_pdf("C:\\Users\\jiaxi\\OneDrive\\Desktop\\RBAC 2021\\Price\\LNG Daily\\LNG_20200814.pdf", pages='3')
a2 = df[0]

B = [["JKM", "2020/9/01", "3.875"], \
["JKM Singapore","2020/9/01", a.iloc[7,3]], \
["JKM London","2020/9/01", a.iloc[13,3]], \
["MED","2020/9/01", a.iloc[18,3]], \
["NWE","2020/9/01", a.iloc[23,3]], \
["MEM","2020/9/01", a.iloc[29,3]], \
["WIM","2020/9/01", a.iloc[35,3]], \
["GCM","2020/9/01", a.iloc[42,3]], \
["TTF","2020/9/01", a2.iloc[53,2]], \
["FOB Australia","2020/8/15", "3.510"], \
["FOB Middle East","2020/8/15", "3.500"], \
["FOB Brazil Marker","2020/8/15", a1.iloc[0,9]], \
["FOB Singaporee","2020/8/15", a1.iloc[1,9]], \
["FOB Murmansk","2020/8/15", a1.iloc[2,9]]]

z20Sep = pd.DataFrame(B,columns=["Marker","month","$/MMBtu"])


# 20Aug
df = tabula.read_pdf("C:\\Users\\jiaxi\\OneDrive\\Desktop\\RBAC 2021\\Price\\LNG Daily\\LNG_20200715.pdf", pages='1')
a = df[0]
a1 = df[1]

df = tabula.read_pdf("C:\\Users\\jiaxi\\OneDrive\\Desktop\\RBAC 2021\\Price\\LNG Daily\\LNG_20200715.pdf", pages='3')
a2 = df[0]

B = [["JKM", "2020/8/01", "2.250"], \
["JKM Singapore","2020/8/01", a.iloc[9,3]], \
["JKM London","2020/8/01", "2.150"], \
["MED","2020/8/01", a.iloc[18,3]], \
["NWE","2020/8/01", a.iloc[23,3]], \
["MEM","2020/8/01", a.iloc[28,3]], \
["WIM","2020/8/01", "2.250"], \
["GCM","2020/8/01", a.iloc[40,3]], \
["TTF","2020/8/01", a2.iloc[55,2]], \
["FOB Australia","2020/7/15", "1.970"], \
["FOB Middle East","2020/7/15", "2.150"], \
["FOB Brazil Marker","2020/7/15", a1.iloc[0,9]], \
["FOB Singaporee","2020/7/15", a1.iloc[1,9]], \
["FOB Murmansk","2020/7/15", a1.iloc[2,9]]]

z20Aug = pd.DataFrame(B,columns=["Marker","month","$/MMBtu"])



# 20Jul
df = tabula.read_pdf("C:\\Users\\jiaxi\\OneDrive\\Desktop\\RBAC 2021\\Price\\LNG Daily\\LNG_20200615.pdf", pages='1')
a = df[0]

df = tabula.read_pdf("C:\\Users\\jiaxi\\OneDrive\\Desktop\\RBAC 2021\\Price\\LNG Daily\\LNG_20200615.pdf", pages='3')
a2 = df[0]

B = [["JKM", "2020/7/01", "2.100"], \
["JKM Singapore","2020/7/01", a.iloc[9,3]], \
["JKM London","2020/7/01", "2.050"], \
["MED","2020/7/01", a.iloc[18,3]], \
["NWE","2020/7/01", "1.746"], \
["MEM","2020/7/01", "2.075"], \
["WIM","2020/7/01", "2.075"], \
["GCM","2020/7/01", "1.625"], \
["TTF","2020/7/01", a2.iloc[57,1]], \
["FOB Australia","2020/6/15", "1.83"], \
["FOB Middle East","2020/6/15", "1.96"], \
["FOB Brazil Marker","2020/6/15", "1.895"], \
["FOB Singaporee","2020/6/15", "1.900"], \
["FOB Murmansk","2020/6/15", "1.586"]]

z20Jul = pd.DataFrame(B,columns=["Marker","month","$/MMBtu"])


# 20Jun
df = tabula.read_pdf("C:\\Users\\jiaxi\\OneDrive\\Desktop\\RBAC 2021\\Price\\LNG Daily\\LNG_20200515.pdf", pages='1')
a = df[0]

df = tabula.read_pdf("C:\\Users\\jiaxi\\OneDrive\\Desktop\\RBAC 2021\\Price\\LNG Daily\\LNG_20200515.pdf", pages='3')
a2 = df[0]

B = [["JKM", "2020/6/01", "2.363"], \
["JKM Singapore","2020/6/01", "2.107"], \
["JKM London","2020/6/01", "2.100"], \
["MED","2020/6/01", "1.590"], \
["NWE","2020/6/01", "1.590"], \
["MEM","2020/6/01", "2.263"], \
["WIM","2020/6/01", "2.263"], \
["GCM","2020/6/01", "1.525"], \
["TTF","2020/6/01", a2.iloc[57,1]], \
["FOB Australia","2020/5/15", "2.090"], \
["FOB Middle East","2020/5/15", "2.150"], \
["FOB Brazil Marker","2020/5/15", "1.868"], \
["FOB Singaporee","2020/5/15", "2.163"], \
["FOB Murmansk","2020/5/15", "1.410"]]

z20Jun = pd.DataFrame(B,columns=["Marker","month","$/MMBtu"])

###############################


Price1 = [z20Jun, z20Jul, z20Aug, z20Sep, z20Oct, z20Nov, z20Dec, \
          z21Jan, z21Feb, z21Mar, z21Apr, z21May, z21Jun, z21Jul]
    
Price2 = pd.concat(Price1,ignore_index=True)


# export dataframe to .csv
Price2.to_csv('C:\\Users\\jiaxi\\OneDrive\\Desktop\\RBAC 2021\\Price\\LNG Daily 2021 0623.csv',index=None)

endtime = datetime.datetime.now()
print (endtime - starttime)

print("Congradutions! Finished :)")
