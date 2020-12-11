
# 2020 December
# Source: http://www.kesis.net/sub/sub_0003.jsp

# South Korea, imports, stocks & monthly consumption by sector
# Note: the unit of generation is 1000 ton; unit of res, com, ind is million m^3
##### year 

# trap: 1. no lines so can not be read as tables. So for most years, use 'getPageText';
#       2. be careful about locations. The locations of target values are different among years;
#       3. be careful about units;
#       4. monthly imports by origin can be obtained from http://www.kesis.net/sub/subChartEng.jsp?report_id=7020100&reportType=0


import camelot
import pandas as pd
import numpy as np
import datetime
import fitz


starttime = datetime.datetime.now()


##### 2009 & 2010

tablea = camelot.read_pdf("C:\\Users\\jiaxi\\OneDrive\\桌面\\RBAC\\demand model\\seasonality\\South Korea\\PDF\\KEMS_1103.pdf", pages = '34')
tableb = camelot.read_pdf("C:\\Users\\jiaxi\\OneDrive\\桌面\\RBAC\\demand model\\seasonality\\South Korea\\PDF\\KEMS_1103.pdf", pages = '35')

# transfer Table lists to DataFrame
dfa = tablea[0].df
dfb = tableb[0].df


a1 = dfa.loc[3,1]
a2 = (a1.split())

b1 = dfb.loc[3,1]
b2 = (b1.split())

step = 8
a3 = [a2[i:i+step] for i in range(0,len(a2),step)]
a4 = pd.DataFrame(a3, columns = ['Cargo', 'Imports', 'Total', 'Generation', 'Town Gas', 'Own Use', 'Stocks', 'Amounts'])

step = 9
b3 = [b2[i:i+step] for i in range(0,len(b2),step)]
b4 = pd.DataFrame(b3, columns = ['Raw-Total', 'Raw-LPG', 'Naphtha', 'LNG', 'Production', 'Total Consumption', 'Resdential', 'Commercial', "Industrial"])

#
im2009 = list(a4.iloc[21:33, 1])
im2009.insert(0,"2009")
im2009.insert(1,"1000 ton")

im2010 = list(a4.iloc[33:45, 1])
im2010.insert(0,"2010")
im2010.insert(1,"1000 ton")

st2009 = list(a4.iloc[21:33, 6])
st2009.insert(0,"2009")
st2009.insert(1,"1000 ton")


#
elc2009 = list(a4.iloc[21:33, 3])
elc2009.insert(0,"South Korea")
elc2009.insert(1,"elc")
elc2009.insert(2,"2009")
elc2009.insert(3,"1000 ton")

elc2010 = list(a4.iloc[33:45, 3])
elc2010.insert(0,"South Korea")
elc2010.insert(1,"elc")
elc2010.insert(2,"2010")
elc2010.insert(3,"1000 ton")

#
res2009 = list(b4.iloc[21:33, 6])
res2009.insert(0,"South Korea")
res2009.insert(1,"res")
res2009.insert(2,"2009")
res2009.insert(3,"million m3")

res2010 = list(b4.iloc[33:45, 6])
res2010.insert(0,"South Korea")
res2010.insert(1,"res")
res2010.insert(2,"2010")
res2010.insert(3,"million m3")

#
com2009 = list(b4.iloc[21:33, 7])
com2009.insert(0,"South Korea")
com2009.insert(1,"com")
com2009.insert(2,"2009")
com2009.insert(3,"million m3")

com2010 = list(b4.iloc[33:45, 7])
com2010.insert(0,"South Korea")
com2010.insert(1,"com")
com2010.insert(2,"2010")
com2010.insert(3,"million m3")

#
ind2009 = list(b4.iloc[21:33, 8])
ind2009.insert(0,"South Korea")
ind2009.insert(1,"ind")
ind2009.insert(2,"2009")
ind2009.insert(3,"million m3")

ind2010 = list(b4.iloc[33:45, 8])
ind2010.insert(0,"South Korea")
ind2010.insert(1,"ind")
ind2010.insert(2,"2010")
ind2010.insert(3,"million m3")


#### 2010 stock
tablea = camelot.read_pdf("C:\\Users\\jiaxi\\OneDrive\\桌面\\RBAC\\demand model\\seasonality\\South Korea\\PDF\\MES1203.pdf", pages = '34')
dfa = tablea[0].df

a1 = dfa.loc[3,1]
a2 = (a1.split())

step = 8
a3 = [a2[i:i+step] for i in range(0,len(a2),step)]
a4 = pd.DataFrame(a3, columns = ['Cargo', 'Imports', 'Total', 'Generation', 'Town Gas', 'Own Use', 'Stocks', 'Amounts'])

st2010 = list(a4.iloc[22:34, 6])
st2010.insert(0,"2010")
st2010.insert(1,"1000 ton")

##### 2011 & 2012
## impots + elc
doc = fitz.open(r"C:\\Users\\jiaxi\\OneDrive\\桌面\\RBAC\\demand model\\seasonality\\South Korea\\PDF\\MES1303.pdf")
print(doc.pageCount)  #获取总页数
print(doc.getPageText(32))  #获取pdf文件32页文本
a0 = doc.getPageText(32)
a1 = (a0.split())
a2 = a1[256:364]
aa1 = (a0.split())
aa2 = aa1[365:473]

step = 9
a3 = [a2[i:i+step] for i in range(0,len(a2),step)]
a4 = pd.DataFrame(a3, columns = ['Month', 'Cargo', 'Imports', 'Total', 'Generation', 'Town Gas', 'Own Use', 'Stocks', 'Amounts'])
aa3 = [aa2[i:i+step] for i in range(0,len(aa2),step)]
aa4 = pd.DataFrame(aa3, columns = ['Month', 'Cargo', 'Imports', 'Total', 'Generation', 'Town Gas', 'Own Use', 'Stocks', 'Amounts'])

#
im2011 = list(a4.iloc[0:12, 2])
im2011.insert(0,"2011")
im2011.insert(1,"1000 ton")

st2011 = list(a4.iloc[0:12, 7])
st2011.insert(0,"2011")
st2011.insert(1,"1000 ton")

im2012 = list(aa4.iloc[0:12, 2])
im2012.insert(0,"2012")
im2012.insert(1,"1000 ton")

st2012 = list(aa4.iloc[0:12, 7])
st2012.insert(0,"2012")
st2012.insert(1,"1000 ton")

#
elc2011 = list(a4.iloc[0:12, 4])
elc2011.insert(0,"South Korea")
elc2011.insert(1,"elc")
elc2011.insert(2,"2011")
elc2011.insert(3,"1000 ton")

elc2012 = list(aa4.iloc[0:12, 4])
elc2012.insert(0,"South Korea")
elc2012.insert(1,"elc")
elc2012.insert(2,"2012")
elc2012.insert(3,"1000 ton")

## res + com + ind
doc = fitz.open(r"C:\\Users\\jiaxi\\OneDrive\\桌面\\RBAC\\demand model\\seasonality\\South Korea\\PDF\\MES1303.pdf")
print(doc.pageCount)  #获取总页数
print(doc.getPageText(33))  #获取pdf文件33页文本
b0 = doc.getPageText(33)
b1 = (b0.split())
b2 = b1[276:396]
bb1 = (b0.split())
bb2 = bb1[397:517]

step = 10
b3 = [b2[i:i+step] for i in range(0,len(b2),step)]
b4 = pd.DataFrame(b3, columns = ['Month', 'Raw-Total', 'Raw-LPG', 'Naphtha', 'LNG', 'Production', 'Total Consumption', 'Resdential', 'Commercial', "Industrial"])
bb3 = [bb2[i:i+step] for i in range(0,len(bb2),step)]
bb4 = pd.DataFrame(bb3, columns = ['Month', 'Raw-Total', 'Raw-LPG', 'Naphtha', 'LNG', 'Production', 'Total Consumption', 'Resdential', 'Commercial', "Industrial"])

#
res2011 = list(b4.iloc[0:12, 7])
res2011.insert(0,"South Korea")
res2011.insert(1,"res")
res2011.insert(2,"2011")
res2011.insert(3,"million m3")

res2012 = list(bb4.iloc[0:12, 7])
res2012.insert(0,"South Korea")
res2012.insert(1,"res")
res2012.insert(2,"2012")
res2012.insert(3,"million m3")

#
com2011 = list(b4.iloc[0:12, 8])
com2011.insert(0,"South Korea")
com2011.insert(1,"com")
com2011.insert(2,"2011")
com2011.insert(3,"million m3")

com2012 = list(bb4.iloc[0:12, 8])
com2012.insert(0,"South Korea")
com2012.insert(1,"com")
com2012.insert(2,"2012")
com2012.insert(3,"million m3")

#
ind2011 = list(b4.iloc[0:12, 9])
ind2011.insert(0,"South Korea")
ind2011.insert(1,"ind")
ind2011.insert(2,"2011")
ind2011.insert(3,"million m3")

ind2012 = list(bb4.iloc[0:12, 9])
ind2012.insert(0,"South Korea")
ind2012.insert(1,"ind")
ind2012.insert(2,"2012")
ind2012.insert(3,"million m3")

##### 2013 & 2014
## impots
doc = fitz.open(r"C:\\Users\\jiaxi\\OneDrive\\桌面\\RBAC\\demand model\\seasonality\\South Korea\\PDF\\MES1503.pdf")
print(doc.pageCount)  #获取总页数
print(doc.getPageText(66))  #获取pdf文件67页文本
a0 = doc.getPageText(66)
a1 = (a0.split())
a2 = a1[275:383]
aa1 = (a0.split())
aa2 = aa1[384:492]

step = 9
a3 = [a2[i:i+step] for i in range(0,len(a2),step)]
a4 = pd.DataFrame(a3, columns = ['Month', 'Cargo', 'Import value', 'Total', 'Qatar', 'Indonesia', 'Oman', 'Malaysia', 'Other'])
aa3 = [aa2[i:i+step] for i in range(0,len(aa2),step)]
aa4 = pd.DataFrame(aa3, columns = ['Month', 'Cargo', 'Import value', 'Total', 'Qatar', 'Indonesia', 'Oman', 'Malaysia', 'Other'])

im2013 = list(a4.iloc[0:12, 3])
im2013.insert(0,"2013")
im2013.insert(1,"1000 ton")


im2014 = list(aa4.iloc[0:12, 3])
im2014.insert(0,"2014")
im2014.insert(1,"1000 ton")

## elc + stocks
doc = fitz.open(r"C:\\Users\\jiaxi\\OneDrive\\桌面\\RBAC\\demand model\\seasonality\\South Korea\\PDF\\MES1503.pdf")
print(doc.pageCount)  #获取总页数
print(doc.getPageText(67))  #获取pdf文件67页文本
a0 = doc.getPageText(67)
a1 = (a0.split())
a2 = a1[255:351]
aa1 = (a0.split())
aa2 = aa1[352:448]

step = 8
a3 = [a2[i:i+step] for i in range(0,len(a2),step)]
a4 = pd.DataFrame(a3, columns = ['Month', 'Domestic production',  'Total', 'Power Generation', 'District Heating', 'City Gas', 'Own use and loss', 'Stock'])
aa3 = [aa2[i:i+step] for i in range(0,len(aa2),step)]
aa4 = pd.DataFrame(aa3, columns = ['Month', 'Domestic production',  'Total', 'Power Generation', 'District Heating', 'City Gas', 'Own use and loss', 'Stock'])

st2013 = list(a4.iloc[0:12, 7])
st2013.insert(0,"2013")
st2013.insert(1,"1000 ton")

st2014 = list(aa4.iloc[0:12, 7])
st2014.insert(0,"2014")
st2014.insert(1,"1000 ton")

elc2013 = list(a4.iloc[0:12, 3])
elc2013.insert(0,"South Korea")
elc2013.insert(1,"elc")
elc2013.insert(2,"2013")
elc2013.insert(3,"1000 ton")

elc2014 = list(aa4.iloc[0:12, 3])
elc2014.insert(0,"South Korea")
elc2014.insert(1,"elc")
elc2014.insert(2,"2014")
elc2014.insert(3,"1000 ton")

## res + com + ind
doc = fitz.open(r"C:\\Users\\jiaxi\\OneDrive\\桌面\\RBAC\\demand model\\seasonality\\South Korea\\PDF\\MES1503.pdf")
print(doc.pageCount)  #获取总页数
print(doc.getPageText(68))  #获取pdf文件33页文本
b0 = doc.getPageText(68)
b1 = (b0.split())
b2 = b1[302:422]
bb1 = (b0.split())
bb2 = bb1[423:543]

step = 10
b3 = [b2[i:i+step] for i in range(0,len(b2),step)]
b4 = pd.DataFrame(b3, columns = ['Month', 'Propane', 'LNG', 'Production',  'Total',"Industrial", 'Transportation', 'Resdential', 'Commercial', 'Public' ])
bb3 = [bb2[i:i+step] for i in range(0,len(bb2),step)]
bb4 = pd.DataFrame(bb3, columns = ['Month', 'Propane', 'LNG', 'Production',  'Total',"Industrial", 'Transportation', 'Resdential', 'Commercial', 'Public' ])

#
ind2013 = list(b4.iloc[0:12, 5])
ind2013.insert(0,"South Korea")
ind2013.insert(1,"ind")
ind2013.insert(2,"2013")
ind2013.insert(3,"million m3")

ind2014 = list(bb4.iloc[0:12, 5])
ind2014.insert(0,"South Korea")
ind2014.insert(1,"ind")
ind2014.insert(2,"2014")
ind2014.insert(3,"million m3")

#
trn2013 = list(b4.iloc[0:12, 6])
trn2013.insert(0,"South Korea")
trn2013.insert(1,"trn")
trn2013.insert(2,"2013")
trn2013.insert(3,"million m3")

trn2014 = list(bb4.iloc[0:12, 6])
trn2014.insert(0,"South Korea")
trn2014.insert(1,"trn")
trn2014.insert(2,"2014")
trn2014.insert(3,"million m3")

#
res2013 = list(b4.iloc[0:12, 7])
res2013.insert(0,"South Korea")
res2013.insert(1,"res")
res2013.insert(2,"2013")
res2013.insert(3,"million m3")

res2014 = list(bb4.iloc[0:12, 7])
res2014.insert(0,"South Korea")
res2014.insert(1,"res")
res2014.insert(2,"2014")
res2014.insert(3,"million m3")

#
com2013 = list(b4.iloc[0:12, 8])
com2013.insert(0,"South Korea")
com2013.insert(1,"com")
com2013.insert(2,"2013")
com2013.insert(3,"million m3")

com2014 = list(bb4.iloc[0:12, 8])
com2014.insert(0,"South Korea")
com2014.insert(1,"com")
com2014.insert(2,"2014")
com2014.insert(3,"million m3")


##### 2015 & 2016
## impots
doc = fitz.open(r"C:\\Users\\jiaxi\\OneDrive\\桌面\\RBAC\\demand model\\seasonality\\South Korea\\PDF\\MES1703.pdf")
print(doc.pageCount)  #获取总页数
print(doc.getPageText(67))  #获取pdf文件68页文本
a0 = doc.getPageText(67)
a1 = (a0.split())
a2 = a1[293:401]
aa1 = (a0.split())
aa2 = aa1[402:510]

step = 9
a3 = [a2[i:i+step] for i in range(0,len(a2),step)]
a4 = pd.DataFrame(a3, columns = ['Month', 'Cargo', 'Import value', 'Total', 'Qatar', 'Indonesia', 'Oman', 'Malaysia', 'Other'])
aa3 = [aa2[i:i+step] for i in range(0,len(aa2),step)]
aa4 = pd.DataFrame(aa3, columns = ['Month', 'Cargo', 'Import value', 'Total', 'Qatar', 'Indonesia', 'Oman', 'Malaysia', 'Other'])

im2015 = list(a4.iloc[0:12, 3])
im2015.insert(0,"2015")
im2015.insert(1,"1000 ton")

im2016 = list(aa4.iloc[0:12, 3])
im2016.insert(0,"2016")
im2016.insert(1,"1000 ton")

## elc, stocks
doc = fitz.open(r"C:\\Users\\jiaxi\\OneDrive\\桌面\\RBAC\\demand model\\seasonality\\South Korea\\PDF\\MES1703.pdf")
print(doc.pageCount)  #获取总页数
print(doc.getPageText(68))  #获取pdf文件69页文本
a0 = doc.getPageText(68)
a1 = (a0.split())
a2 = a1[271:367]
aa1 = (a0.split())
aa2 = aa1[368:464]

step = 8
a3 = [a2[i:i+step] for i in range(0,len(a2),step)]
a4 = pd.DataFrame(a3, columns = ['Month', 'Domestic production',  'Total', 'Power Generation', 'District Heating', 'City Gas', 'Own use and loss', 'Stock'])
aa3 = [aa2[i:i+step] for i in range(0,len(aa2),step)]
aa4 = pd.DataFrame(aa3, columns = ['Month', 'Domestic production',  'Total', 'Power Generation', 'District Heating', 'City Gas', 'Own use and loss', 'Stock'])

st2015 = list(a4.iloc[0:12, 7])
st2015.insert(0,"2015")
st2015.insert(1,"1000 ton")

st2016 = list(aa4.iloc[0:12, 7])
st2016.insert(0,"2016")
st2016.insert(1,"1000 ton")

elc2015 = list(a4.iloc[0:12, 3])
elc2015.insert(0,"South Korea")
elc2015.insert(1,"elc")
elc2015.insert(2,"2015")
elc2015.insert(3,"1000 ton")

elc2016 = list(aa4.iloc[0:12, 3])
elc2016.insert(0,"South Korea")
elc2016.insert(1,"elc")
elc2016.insert(2,"2016")
elc2016.insert(3,"1000 ton")

## res + com + ind
doc = fitz.open(r"C:\\Users\\jiaxi\\OneDrive\\桌面\\RBAC\\demand model\\seasonality\\South Korea\\PDF\\MES1703.pdf")
print(doc.pageCount)  #获取总页数
print(doc.getPageText(69))  #获取pdf文件70页文本
b0 = doc.getPageText(69)
b1 = (b0.split())
b2 = b1[322:442]
bb1 = (b0.split())
bb2 = bb1[443:563]

step = 10
b3 = [b2[i:i+step] for i in range(0,len(b2),step)]
b4 = pd.DataFrame(b3, columns = ['Month', 'Propane', 'LNG', 'Production',  'Total',"Industrial", 'Transportation', 'Resdential', 'Commercial', 'Public' ])
bb3 = [bb2[i:i+step] for i in range(0,len(bb2),step)]
bb4 = pd.DataFrame(bb3, columns = ['Month', 'Propane', 'LNG', 'Production',  'Total',"Industrial", 'Transportation', 'Resdential', 'Commercial', 'Public' ])

#
ind2015 = list(b4.iloc[0:12, 5])
ind2015.insert(0,"South Korea")
ind2015.insert(1,"ind")
ind2015.insert(2,"2015")
ind2015.insert(3,"million m3")

ind2016 = list(bb4.iloc[0:12, 5])
ind2016.insert(0,"South Korea")
ind2016.insert(1,"ind")
ind2016.insert(2,"2016")
ind2016.insert(3,"million m3")

#
trn2015 = list(b4.iloc[0:12, 6])
trn2015.insert(0,"South Korea")
trn2015.insert(1,"trn")
trn2015.insert(2,"2015")
trn2015.insert(3,"million m3")

trn2016 = list(bb4.iloc[0:12, 6])
trn2016.insert(0,"South Korea")
trn2016.insert(1,"trn")
trn2016.insert(2,"2016")
trn2016.insert(3,"million m3")

#
res2015 = list(b4.iloc[0:12, 7])
res2015.insert(0,"South Korea")
res2015.insert(1,"res")
res2015.insert(2,"2015")
res2015.insert(3,"million m3")

res2016 = list(bb4.iloc[0:12, 7])
res2016.insert(0,"South Korea")
res2016.insert(1,"res")
res2016.insert(2,"2016")
res2016.insert(3,"million m3")

#
com2015 = list(b4.iloc[0:12, 8])
com2015.insert(0,"South Korea")
com2015.insert(1,"com")
com2015.insert(2,"2015")
com2015.insert(3,"million m3")

com2016 = list(bb4.iloc[0:12, 8])
com2016.insert(0,"South Korea")
com2016.insert(1,"com")
com2016.insert(2,"2016")
com2016.insert(3,"million m3")

##### 2017 & 2018
## impots
doc = fitz.open(r"C:\\Users\\jiaxi\\OneDrive\\桌面\\RBAC\\demand model\\seasonality\\South Korea\\PDF\\MES1903.pdf")
print(doc.pageCount)  #获取总页数
print(doc.getPageText(73))  #获取pdf文件74页文本
a0 = doc.getPageText(73)
a1 = (a0.split())
a2 = a1[278:386]
aa1 = (a0.split())
aa2 = aa1[388:496]

step = 9
a3 = [a2[i:i+step] for i in range(0,len(a2),step)]
a4 = pd.DataFrame(a3, columns = ['Month', 'Cargo', 'Import value', 'Total', 'Qatar', 'Indonesia', 'Oman', 'Malaysia', 'Other'])
aa3 = [aa2[i:i+step] for i in range(0,len(aa2),step)]
aa4 = pd.DataFrame(aa3, columns = ['Month', 'Cargo', 'Import value', 'Total', 'Qatar', 'Indonesia', 'Oman', 'Malaysia', 'Other'])

im2017 = list(a4.iloc[0:12, 3])
im2017.insert(0,"2017")
im2017.insert(1,"1000 ton")

im2018 = list(aa4.iloc[0:12, 3])
im2018.insert(0,"2018")
im2018.insert(1,"1000 ton")

## elc, stocks
doc = fitz.open(r"C:\\Users\\jiaxi\\OneDrive\\桌面\\RBAC\\demand model\\seasonality\\South Korea\\PDF\\MES1903.pdf")
print(doc.pageCount)  #获取总页数
print(doc.getPageText(74))  #获取pdf文件75页文本
a0 = doc.getPageText(74)
a1 = (a0.split())
a2 = a1[257:353]
aa1 = (a0.split())
aa2 = aa1[355:451]

step = 8
a3 = [a2[i:i+step] for i in range(0,len(a2),step)]
a4 = pd.DataFrame(a3, columns = ['Month', 'Domestic production',  'Total', 'Power Generation', 'District Heating', 'City Gas', 'Own use and loss', 'Stock'])
aa3 = [aa2[i:i+step] for i in range(0,len(aa2),step)]
aa4 = pd.DataFrame(aa3, columns = ['Month', 'Domestic production',  'Total', 'Power Generation', 'District Heating', 'City Gas', 'Own use and loss', 'Stock'])

st2017 = list(a4.iloc[0:12, 7])
st2017.insert(0,"2017")
st2017.insert(1,"1000 ton")

st2018 = list(aa4.iloc[0:12, 7])
st2018.insert(0,"2018")
st2018.insert(1,"1000 ton")

elc2017 = list(a4.iloc[0:12, 3])
elc2017.insert(0,"South Korea")
elc2017.insert(1,"elc")
elc2017.insert(2,"2017")
elc2017.insert(3,"1000 ton")

elc2018 = list(aa4.iloc[0:12, 3])
elc2018.insert(0,"South Korea")
elc2018.insert(1,"elc")
elc2018.insert(2,"2018")
elc2018.insert(3,"1000 ton")

## res + com + ind
doc = fitz.open(r"C:\\Users\\jiaxi\\OneDrive\\桌面\\RBAC\\demand model\\seasonality\\South Korea\\PDF\\MES1903.pdf")
print(doc.pageCount)  #获取总页数
print(doc.getPageText(75))  #获取pdf文件76页文本
b0 = doc.getPageText(75)
b1 = (b0.split())
b2 = b1[304:424]
bb1 = (b0.split())
bb2 = bb1[426:546]

step = 10
b3 = [b2[i:i+step] for i in range(0,len(b2),step)]
b4 = pd.DataFrame(b3, columns = ['Month', 'Propane', 'LNG', 'Production',  'Total',"Industrial", 'Transportation', 'Resdential', 'Commercial', 'Public' ])
bb3 = [bb2[i:i+step] for i in range(0,len(bb2),step)]
bb4 = pd.DataFrame(bb3, columns = ['Month', 'Propane', 'LNG', 'Production',  'Total',"Industrial", 'Transportation', 'Resdential', 'Commercial', 'Public' ])

#
ind2017 = list(b4.iloc[0:12, 5])
ind2017.insert(0,"South Korea")
ind2017.insert(1,"ind")
ind2017.insert(2,"2017")
ind2017.insert(3,"million m3")

ind2018 = list(bb4.iloc[0:12, 5])
ind2018.insert(0,"South Korea")
ind2018.insert(1,"ind")
ind2018.insert(2,"2018")
ind2018.insert(3,"million m3")
#
trn2017 = list(b4.iloc[0:12, 6])
trn2017.insert(0,"South Korea")
trn2017.insert(1,"trn")
trn2017.insert(2,"2017")
trn2017.insert(3,"million m3")

trn2018 = list(bb4.iloc[0:12, 6])
trn2018.insert(0,"South Korea")
trn2018.insert(1,"trn")
trn2018.insert(2,"2018")
trn2018.insert(3,"million m3")

#
res2017 = list(b4.iloc[0:12, 7])
res2017.insert(0,"South Korea")
res2017.insert(1,"res")
res2017.insert(2,"2017")
res2017.insert(3,"million m3")

res2018 = list(bb4.iloc[0:12, 7])
res2018.insert(0,"South Korea")
res2018.insert(1,"res")
res2018.insert(2,"2018")
res2018.insert(3,"million m3")

#
com2017 = list(b4.iloc[0:12, 8])
com2017.insert(0,"South Korea")
com2017.insert(1,"com")
com2017.insert(2,"2017")
com2017.insert(3,"million m3")

com2018 = list(bb4.iloc[0:12, 8])
com2018.insert(0,"South Korea")
com2018.insert(1,"com")
com2018.insert(2,"2018")
com2018.insert(3,"million m3")

##### 2019 & 2020
## impots + stock + elc
doc = fitz.open(r"C:\\Users\\jiaxi\\OneDrive\\桌面\\RBAC\\demand model\\seasonality\\South Korea\\PDF\\KERM(2020.11).pdf")
print(doc.pageCount)  #获取总页数
print(doc.getPageText(57))  #获取pdf文件58页文本
a0 = doc.getPageText(57)
a1 = (a0.split())
a2 = a1[322:430]
aa1 = (a0.split())
aa2 = aa1[431:503]

step = 9
a3 = [a2[i:i+step] for i in range(0,len(a2),step)]
a4 = pd.DataFrame(a3, columns = ['Month', 'Cargo', 'Import value', 'Total', 'Qatar', 'Indonesia', 'Oman', 'Malaysia', 'Other'])
aa3 = [aa2[i:i+step] for i in range(0,len(aa2),step)]
aa4 = pd.DataFrame(aa3, columns = ['Month', 'Cargo', 'Import value', 'Total', 'Qatar', 'Indonesia', 'Oman', 'Malaysia', 'Other'])

im2019 = list(a4.iloc[0:12, 2])
im2019.insert(0,"2019")
im2019.insert(1,"1000 ton")

im2020 = list(aa4.iloc[0:12, 2])
im2020.insert(0,"2020")
im2020.insert(1,"1000 ton")

st2019 = list(a4.iloc[0:12, 7])
st2019.insert(0,"2019")
st2019.insert(1,"1000 ton")

st2020 = list(aa4.iloc[0:12, 7])
st2020.insert(0,"2020")
st2020.insert(1,"1000 ton")

elc2019 = list(a4.iloc[0:12, 4])
elc2019.insert(0,"South Korea")
elc2019.insert(1,"elc")
elc2019.insert(2,"2019")
elc2019.insert(3,"1000 ton")

elc2020 = list(aa4.iloc[0:12, 4])
elc2020.insert(0,"South Korea")
elc2020.insert(1,"elc")
elc2020.insert(2,"2020")
elc2020.insert(3,"1000 ton")

## res + com + ind
doc = fitz.open(r"C:\\Users\\jiaxi\\OneDrive\\桌面\\RBAC\\demand model\\seasonality\\South Korea\\PDF\\KERM(2020.11).pdf")
print(doc.pageCount)  #获取总页数
print(doc.getPageText(58))  #获取pdf文件59页文本
b0 = doc.getPageText(58)
b1 = (b0.split())
b2 = b1[280:376]
bb1 = (b0.split())
bb2 = bb1[377:441]

step = 8
b3 = [b2[i:i+step] for i in range(0,len(b2),step)]
b4 = pd.DataFrame(b3, columns = ['Month', 'Propane', 'LNG', 'Production',  'Total','Resdential', 'Commercial', 'Industrial' ])
bb3 = [bb2[i:i+step] for i in range(0,len(bb2),step)]
bb4 = pd.DataFrame(bb3, columns = ['Month', 'Propane', 'LNG', 'Production',  'Total','Resdential', 'Commercial', 'Industrial' ])


#
res2019 = list(b4.iloc[0:12, 5])
res2019.insert(0,"South Korea")
res2019.insert(1,"res")
res2019.insert(2,"2019")
res2019.insert(3,"million m3")

res2020 = list(bb4.iloc[0:12, 5])
res2020.insert(0,"South Korea")
res2020.insert(1,"res")
res2020.insert(2,"2020")
res2020.insert(3,"million m3")

#
com2019 = list(b4.iloc[0:12, 6])
com2019.insert(0,"South Korea")
com2019.insert(1,"com")
com2019.insert(2,"2019")
com2019.insert(3,"million m3")

com2020 = list(bb4.iloc[0:12, 6])
com2020.insert(0,"South Korea")
com2020.insert(1,"com")
com2020.insert(2,"2020")
com2020.insert(3,"million m3")

#
ind2019 = list(b4.iloc[0:12, 7])
ind2019.insert(0,"South Korea")
ind2019.insert(1,"ind")
ind2019.insert(2,"2019")
ind2019.insert(3,"million m3")

ind2020 = list(bb4.iloc[0:12, 7])
ind2020.insert(0,"South Korea")
ind2020.insert(1,"ind")
ind2020.insert(2,"2020")
ind2020.insert(3,"million m3")


########## Merge ###########

im0 = [im2009, im2010, im2011, im2012, im2013, im2014, im2015, im2016, im2017, im2018, im2019, im2020]
im = pd.DataFrame(im0, columns = ["year", "unit", "1","2","3","4","5","6","7","8","9","10","11","12"] )

st0 = [st2009, st2010, st2011, st2012, st2013, st2014, st2015, st2016, st2017, st2018, st2019, st2020]
st = pd.DataFrame(st0, columns = ["year", "unit", "1","2","3","4","5","6","7","8","9","10","11","12"] )

de0 = [elc2009, elc2010, elc2011, elc2012, elc2013, elc2014, elc2015, elc2016, elc2017, elc2018, elc2019, elc2020, \
       res2009, res2010, res2011, res2012, res2013, res2014, res2015, res2016, res2017, res2018, res2019, res2020, \
       com2009, com2010, com2011, com2012, com2013, com2014, com2015, com2016, com2017, com2018, com2019, com2020, \
       ind2009, ind2010, ind2011, ind2012, ind2013, ind2014, ind2015, ind2016, ind2017, ind2018, ind2019, ind2020, \
       trn2013, trn2014, trn2015, trn2016, trn2017, trn2018]
de = pd.DataFrame(de0, columns = ["country", "sector", "year","unit", "1","2","3","4","5","6","7","8","9","10","11","12"] )

# export dataframe to .csv
im.to_csv('C:\\Users\\jiaxi\\OneDrive\\桌面\\RBAC\\demand model\\seasonality\\South Korea\\Output\\LNGImports-South Korea.csv',index=None)
st.to_csv('C:\\Users\\jiaxi\\OneDrive\\桌面\\RBAC\\demand model\\seasonality\\South Korea\\Output\\Stock-South Korea.csv',index=None)
de.to_csv('C:\\Users\\jiaxi\\OneDrive\\桌面\\RBAC\\demand model\\seasonality\\South Korea\\Output\\Demand-South Korea.csv',index=None)


endtime = datetime.datetime.now()
print ("duration：", endtime - starttime)

print("Congradulations! Finished :)")


