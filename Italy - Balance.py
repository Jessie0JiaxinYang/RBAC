
import pandas as pd
import numpy as np
import statsmodels.api as sm

import datetime

starttime = datetime.datetime.now()

## 2010
table = pd.read_excel(r'C:\Users\jiaxi\OneDrive\Desktop\RBAC 2022\Balance\local\Italy\Italy\Reports\Gas Balance\Bilancio_GAS_2010_01.xls', sheet_name = 'Preconsuntivo Gennaio 2010')
B = [["2010", "1", table.iloc[5,3], table.iloc[5,6]], \
     ["2010", "1", table.iloc[6,3], table.iloc[6,6]], \
     ["2010", "1", table.iloc[7,4], table.iloc[7,6]], \
     ["2010", "1", table.iloc[8,4], table.iloc[8,6]], \
     ["2010", "1", table.iloc[9,4], table.iloc[9,6]], \
     ["2010", "1", table.iloc[10,4], table.iloc[10,6]], \
     ["2010", "1", table.iloc[11,4], table.iloc[11,6]], \
     ["2010", "1", table.iloc[12,4], table.iloc[12,6]], \
     ["2010", "1", table.iloc[13,4], table.iloc[13,6]], \
     ["2010", "1", table.iloc[14,4], table.iloc[14,6]], \
     ["2010", "1", table.iloc[15,3], table.iloc[15,6]], \
     ["2010", "1", table.iloc[16,3], table.iloc[16,6]], \
     ["2010", "1", table.iloc[17,3], table.iloc[17,6]]]
     
Gen10 = pd.DataFrame(B,columns=["year", "monnth", "sector", "value"])

table = pd.read_excel(r'C:\Users\jiaxi\OneDrive\Desktop\RBAC 2022\Balance\local\Italy\Italy\Reports\Gas Balance\Bilancio_GAS_2010_02.xls', sheet_name = 'Preconsuntivo febbraio  2010')
B = [["2010", "2", table.iloc[5,3], table.iloc[5,6]], \
     ["2010", "2", table.iloc[6,3], table.iloc[6,6]], \
     ["2010", "2", table.iloc[7,4], table.iloc[7,6]], \
     ["2010", "2", table.iloc[8,4], table.iloc[8,6]], \
     ["2010", "2", table.iloc[9,4], table.iloc[9,6]], \
     ["2010", "2", table.iloc[10,4], table.iloc[10,6]], \
     ["2010", "2", table.iloc[11,4], table.iloc[11,6]], \
     ["2010", "2", table.iloc[12,4], table.iloc[12,6]], \
     ["2010", "2", table.iloc[13,4], table.iloc[13,6]], \
     ["2010", "2", table.iloc[14,4], table.iloc[14,6]], \
     ["2010", "2", table.iloc[15,3], table.iloc[15,6]], \
     ["2010", "2", table.iloc[16,3], table.iloc[16,6]], \
     ["2010", "2", table.iloc[17,3], table.iloc[17,6]]]
     
Feb10 = pd.DataFrame(B,columns=["year", "monnth", "sector", "value"])

table = pd.read_excel(r'C:\Users\jiaxi\OneDrive\Desktop\RBAC 2022\Balance\local\Italy\Italy\Reports\Gas Balance\Bilancio_GAS_2010_03.xls', sheet_name = 'Preconsuntivo marzo  2010')
B = [["2010", "3", table.iloc[5,3], table.iloc[5,6]], \
     ["2010", "3", table.iloc[6,3], table.iloc[6,6]], \
     ["2010", "3", table.iloc[7,4], table.iloc[7,6]], \
     ["2010", "3", table.iloc[8,4], table.iloc[8,6]], \
     ["2010", "3", table.iloc[9,4], table.iloc[9,6]], \
     ["2010", "3", table.iloc[10,4], table.iloc[10,6]], \
     ["2010", "3", table.iloc[11,4], table.iloc[11,6]], \
     ["2010", "3", table.iloc[12,4], table.iloc[12,6]], \
     ["2010", "3", table.iloc[13,4], table.iloc[13,6]], \
     ["2010", "3", table.iloc[14,4], table.iloc[14,6]], \
     ["2010", "3", table.iloc[15,3], table.iloc[15,6]], \
     ["2010", "3", table.iloc[16,3], table.iloc[16,6]], \
     ["2010", "3", table.iloc[17,3], table.iloc[17,6]]]
     
Mar10 = pd.DataFrame(B,columns=["year", "monnth", "sector", "value"])

table = pd.read_excel(r'C:\Users\jiaxi\OneDrive\Desktop\RBAC 2022\Balance\local\Italy\Italy\Reports\Gas Balance\Bilancio_GAS_2010_04.xls', sheet_name = 'Preconsuntivo aprile  2010')
B = [["2010", "4", table.iloc[5,3], table.iloc[5,6]], \
     ["2010", "4", table.iloc[6,3], table.iloc[6,6]], \
     ["2010", "4", table.iloc[7,4], table.iloc[7,6]], \
     ["2010", "4", table.iloc[8,4], table.iloc[8,6]], \
     ["2010", "4", table.iloc[9,4], table.iloc[9,6]], \
     ["2010", "4", table.iloc[10,4], table.iloc[10,6]], \
     ["2010", "4", table.iloc[11,4], table.iloc[11,6]], \
     ["2010", "4", table.iloc[12,4], table.iloc[12,6]], \
     ["2010", "4", table.iloc[13,4], table.iloc[13,6]], \
     ["2010", "4", table.iloc[14,4], table.iloc[14,6]], \
     ["2010", "4", table.iloc[15,3], table.iloc[15,6]], \
     ["2010", "4", table.iloc[16,3], table.iloc[16,6]], \
     ["2010", "4", table.iloc[17,3], table.iloc[17,6]]]
     
Apr10 = pd.DataFrame(B,columns=["year", "monnth", "sector", "value"])

table = pd.read_excel(r'C:\Users\jiaxi\OneDrive\Desktop\RBAC 2022\Balance\local\Italy\Italy\Reports\Gas Balance\Bilancio_GAS_2010_05.xls', sheet_name = 'Preconsuntivo maggio  2010')
B = [["2010", "5", table.iloc[5,3], table.iloc[5,6]], \
     ["2010", "5", table.iloc[6,3], table.iloc[6,6]], \
     ["2010", "5", table.iloc[7,4], table.iloc[7,6]], \
     ["2010", "5", table.iloc[8,4], table.iloc[8,6]], \
     ["2010", "5", table.iloc[9,4], table.iloc[9,6]], \
     ["2010", "5", table.iloc[10,4], table.iloc[10,6]], \
     ["2010", "5", table.iloc[11,4], table.iloc[11,6]], \
     ["2010", "5", table.iloc[12,4], table.iloc[12,6]], \
     ["2010", "5", table.iloc[13,4], table.iloc[13,6]], \
     ["2010", "5", table.iloc[14,4], table.iloc[14,6]], \
     ["2010", "5", table.iloc[15,3], table.iloc[15,6]], \
     ["2010", "5", table.iloc[16,3], table.iloc[16,6]], \
     ["2010", "5", table.iloc[17,3], table.iloc[17,6]]]
     
Mag10 = pd.DataFrame(B,columns=["year", "monnth", "sector", "value"])

table = pd.read_excel(r'C:\Users\jiaxi\OneDrive\Desktop\RBAC 2022\Balance\local\Italy\Italy\Reports\Gas Balance\Bilancio_GAS_2010_06.xls', sheet_name = 'Preconsuntivo giugno  2010')
B = [["2010", "6", table.iloc[5,3], table.iloc[5,6]], \
     ["2010", "6", table.iloc[6,3], table.iloc[6,6]], \
     ["2010", "6", table.iloc[7,4], table.iloc[7,6]], \
     ["2010", "6", table.iloc[8,4], table.iloc[8,6]], \
     ["2010", "6", table.iloc[9,4], table.iloc[9,6]], \
     ["2010", "6", table.iloc[10,4], table.iloc[10,6]], \
     ["2010", "6", table.iloc[11,4], table.iloc[11,6]], \
     ["2010", "6", table.iloc[12,4], table.iloc[12,6]], \
     ["2010", "6", table.iloc[13,4], table.iloc[13,6]], \
     ["2010", "6", table.iloc[14,4], table.iloc[14,6]], \
     ["2010", "6", table.iloc[15,3], table.iloc[15,6]], \
     ["2010", "6", table.iloc[16,3], table.iloc[16,6]], \
     ["2010", "6", table.iloc[17,3], table.iloc[17,6]]]
     
Giu10 = pd.DataFrame(B,columns=["year", "monnth", "sector", "value"])


table = pd.read_excel(r'C:\Users\jiaxi\OneDrive\Desktop\RBAC 2022\Balance\local\Italy\Italy\Reports\Gas Balance\Bilancio_GAS_2010_07.xls', sheet_name = 'Preconsuntivo luglio  2010')
B = [["2010", "7", table.iloc[5,3], table.iloc[5,6]], \
     ["2010", "7", table.iloc[6,3], table.iloc[6,6]], \
     ["2010", "7", table.iloc[7,4], table.iloc[7,6]], \
     ["2010", "7", table.iloc[8,4], table.iloc[8,6]], \
     ["2010", "7", table.iloc[9,4], table.iloc[9,6]], \
     ["2010", "7", table.iloc[10,4], table.iloc[10,6]], \
     ["2010", "7", table.iloc[11,4], table.iloc[11,6]], \
     ["2010", "7", table.iloc[12,4], table.iloc[12,6]], \
     ["2010", "7", table.iloc[13,4], table.iloc[13,6]], \
     ["2010", "7", table.iloc[14,4], table.iloc[14,6]], \
     ["2010", "7", table.iloc[15,3], table.iloc[15,6]], \
     ["2010", "7", table.iloc[16,3], table.iloc[16,6]], \
     ["2010", "7", table.iloc[17,3], table.iloc[17,6]]]
     
Lug10 = pd.DataFrame(B,columns=["year", "monnth", "sector", "value"])

table = pd.read_excel(r'C:\Users\jiaxi\OneDrive\Desktop\RBAC 2022\Balance\local\Italy\Italy\Reports\Gas Balance\Bilancio_GAS_2010_08.xls', sheet_name = 'Preconsuntivo agosto  2010')
B = [["2010", "8", table.iloc[5,3], table.iloc[5,6]], \
     ["2010", "8", table.iloc[6,3], table.iloc[6,6]], \
     ["2010", "8", table.iloc[7,4], table.iloc[7,6]], \
     ["2010", "8", table.iloc[8,4], table.iloc[8,6]], \
     ["2010", "8", table.iloc[9,4], table.iloc[9,6]], \
     ["2010", "8", table.iloc[10,4], table.iloc[10,6]], \
     ["2010", "8", table.iloc[11,4], table.iloc[11,6]], \
     ["2010", "8", table.iloc[12,4], table.iloc[12,6]], \
     ["2010", "8", table.iloc[13,4], table.iloc[13,6]], \
     ["2010", "8", table.iloc[14,4], table.iloc[14,6]], \
     ["2010", "8", table.iloc[15,3], table.iloc[15,6]], \
     ["2010", "8", table.iloc[16,3], table.iloc[16,6]], \
     ["2010", "8", table.iloc[17,3], table.iloc[17,6]]]
     
Ago10 = pd.DataFrame(B,columns=["year", "monnth", "sector", "value"])

table = pd.read_excel(r'C:\Users\jiaxi\OneDrive\Desktop\RBAC 2022\Balance\local\Italy\Italy\Reports\Gas Balance\Bilancio_GAS_2010_09.xls', sheet_name = 'Preconsuntivo settembre  2010')
B = [["2010", "9", table.iloc[5,3], table.iloc[5,6]], \
     ["2010", "9", table.iloc[6,3], table.iloc[6,6]], \
     ["2010", "9", table.iloc[7,4], table.iloc[7,6]], \
     ["2010", "9", table.iloc[8,4], table.iloc[8,6]], \
     ["2010", "9", table.iloc[9,4], table.iloc[9,6]], \
     ["2010", "9", table.iloc[10,4], table.iloc[10,6]], \
     ["2010", "9", table.iloc[11,4], table.iloc[11,6]], \
     ["2010", "9", table.iloc[12,4], table.iloc[12,6]], \
     ["2010", "9", table.iloc[13,4], table.iloc[13,6]], \
     ["2010", "9", table.iloc[14,4], table.iloc[14,6]], \
     ["2010", "9", table.iloc[15,3], table.iloc[15,6]], \
     ["2010", "9", table.iloc[16,3], table.iloc[16,6]], \
     ["2010", "9", table.iloc[17,3], table.iloc[17,6]]]
     
Set10 = pd.DataFrame(B,columns=["year", "monnth", "sector", "value"])

table = pd.read_excel(r'C:\Users\jiaxi\OneDrive\Desktop\RBAC 2022\Balance\local\Italy\Italy\Reports\Gas Balance\Bilancio_GAS_2010_09.xls', sheet_name = 'Preconsuntivo settembre  2010')
B = [["2010", "9", table.iloc[5,3], table.iloc[5,6]], \
     ["2010", "9", table.iloc[6,3], table.iloc[6,6]], \
     ["2010", "9", table.iloc[7,4], table.iloc[7,6]], \
     ["2010", "9", table.iloc[8,4], table.iloc[8,6]], \
     ["2010", "9", table.iloc[9,4], table.iloc[9,6]], \
     ["2010", "9", table.iloc[10,4], table.iloc[10,6]], \
     ["2010", "9", table.iloc[11,4], table.iloc[11,6]], \
     ["2010", "9", table.iloc[12,4], table.iloc[12,6]], \
     ["2010", "9", table.iloc[13,4], table.iloc[13,6]], \
     ["2010", "9", table.iloc[14,4], table.iloc[14,6]], \
     ["2010", "9", table.iloc[15,3], table.iloc[15,6]], \
     ["2010", "9", table.iloc[16,3], table.iloc[16,6]], \
     ["2010", "9", table.iloc[17,3], table.iloc[17,6]]]
     
Set10 = pd.DataFrame(B,columns=["year", "monnth", "sector", "value"])

table = pd.read_excel(r'C:\Users\jiaxi\OneDrive\Desktop\RBAC 2022\Balance\local\Italy\Italy\Reports\Gas Balance\Bilancio_GAS_2010_10.xls', sheet_name = 'Preconsuntivo ottobre  2010')
B = [["2010", "10", table.iloc[5,3], table.iloc[5,6]], \
     ["2010", "10", table.iloc[6,3], table.iloc[6,6]], \
     ["2010", "10", table.iloc[7,4], table.iloc[7,6]], \
     ["2010", "10", table.iloc[8,4], table.iloc[8,6]], \
     ["2010", "10", table.iloc[9,4], table.iloc[9,6]], \
     ["2010", "10", table.iloc[10,4], table.iloc[10,6]], \
     ["2010", "10", table.iloc[11,4], table.iloc[11,6]], \
     ["2010", "10", table.iloc[12,4], table.iloc[12,6]], \
     ["2010", "10", table.iloc[13,4], table.iloc[13,6]], \
     ["2010", "10", table.iloc[14,4], table.iloc[14,6]], \
     ["2010", "10", table.iloc[15,3], table.iloc[15,6]], \
     ["2010", "10", table.iloc[16,3], table.iloc[16,6]], \
     ["2010", "10", table.iloc[17,3], table.iloc[17,6]]]
     
Ott10 = pd.DataFrame(B,columns=["year", "monnth", "sector", "value"])


table = pd.read_excel(r'C:\Users\jiaxi\OneDrive\Desktop\RBAC 2022\Balance\local\Italy\Italy\Reports\Gas Balance\Bilancio_GAS_2010_11.xls', sheet_name = 'Preconsuntivo novembre  2010')
B = [["2010", "11", table.iloc[5,3], table.iloc[5,6]], \
     ["2010", "11", table.iloc[6,3], table.iloc[6,6]], \
     ["2010", "11", table.iloc[7,4], table.iloc[7,6]], \
     ["2010", "11", table.iloc[8,4], table.iloc[8,6]], \
     ["2010", "11", table.iloc[9,4], table.iloc[9,6]], \
     ["2010", "11", table.iloc[10,4], table.iloc[10,6]], \
     ["2010", "11", table.iloc[11,4], table.iloc[11,6]], \
     ["2010", "11", table.iloc[12,4], table.iloc[12,6]], \
     ["2010", "11", table.iloc[13,4], table.iloc[13,6]], \
     ["2010", "11", table.iloc[14,4], table.iloc[14,6]], \
     ["2010", "11", table.iloc[15,3], table.iloc[15,6]], \
     ["2010", "11", table.iloc[16,3], table.iloc[16,6]], \
     ["2010", "11", table.iloc[17,3], table.iloc[17,6]]]
     
Nov10 = pd.DataFrame(B,columns=["year", "monnth", "sector", "value"])

table = pd.read_excel(r'C:\Users\jiaxi\OneDrive\Desktop\RBAC 2022\Balance\local\Italy\Italy\Reports\Gas Balance\Bilancio_GAS_2010_12.xls', sheet_name = 'Preconsuntivo dicembre  2010')
B = [["2010", "12", table.iloc[5,3], table.iloc[5,6]], \
     ["2010", "12", table.iloc[6,3], table.iloc[6,6]], \
     ["2010", "12", table.iloc[7,4], table.iloc[7,6]], \
     ["2010", "12", table.iloc[8,4], table.iloc[8,6]], \
     ["2010", "12", table.iloc[9,4], table.iloc[9,6]], \
     ["2010", "12", table.iloc[10,4], table.iloc[10,6]], \
     ["2010", "12", table.iloc[11,4], table.iloc[11,6]], \
     ["2010", "12", table.iloc[12,4], table.iloc[12,6]], \
     ["2010", "12", table.iloc[13,4], table.iloc[13,6]], \
     ["2010", "12", table.iloc[14,4], table.iloc[14,6]], \
     ["2010", "12", table.iloc[15,3], table.iloc[15,6]], \
     ["2010", "12", table.iloc[16,3], table.iloc[16,6]], \
     ["2010", "12", table.iloc[17,3], table.iloc[17,6]]]
     
Dic10 = pd.DataFrame(B,columns=["year", "monnth", "sector", "value"])

##2011
table = pd.read_excel(r'C:\Users\jiaxi\OneDrive\Desktop\RBAC 2022\Balance\local\Italy\Italy\Reports\Gas Balance\Bilancio_GAS_2011_01.xls', sheet_name = 'Preconsuntivo Gennaio 2011')
B = [["2011", "1", table.iloc[5,3], table.iloc[5,6]], \
     ["2011", "1", table.iloc[6,3], table.iloc[6,6]], \
     ["2011", "1", table.iloc[7,4], table.iloc[7,6]], \
     ["2011", "1", table.iloc[8,4], table.iloc[8,6]], \
     ["2011", "1", table.iloc[9,4], table.iloc[9,6]], \
     ["2011", "1", table.iloc[10,4], table.iloc[10,6]], \
     ["2011", "1", table.iloc[11,4], table.iloc[11,6]], \
     ["2011", "1", table.iloc[12,4], table.iloc[12,6]], \
     ["2011", "1", table.iloc[13,4], table.iloc[13,6]], \
     ["2011", "1", table.iloc[14,4], table.iloc[14,6]], \
     ["2011", "1", table.iloc[15,3], table.iloc[15,6]], \
     ["2011", "1", table.iloc[16,3], table.iloc[16,6]], \
     ["2011", "1", table.iloc[17,3], table.iloc[17,6]]]
     
Gen11 = pd.DataFrame(B,columns=["year", "monnth", "sector", "value"])

table = pd.read_excel(r'C:\Users\jiaxi\OneDrive\Desktop\RBAC 2022\Balance\local\Italy\Italy\Reports\Gas Balance\Bilancio_GAS_2011_02.xls', sheet_name = 'Preconsuntivo febbraio  2011')
B = [["2011", "2", table.iloc[5,3], table.iloc[5,6]], \
     ["2011", "2", table.iloc[6,3], table.iloc[6,6]], \
     ["2011", "2", table.iloc[7,4], table.iloc[7,6]], \
     ["2011", "2", table.iloc[8,4], table.iloc[8,6]], \
     ["2011", "2", table.iloc[9,4], table.iloc[9,6]], \
     ["2011", "2", table.iloc[10,4], table.iloc[10,6]], \
     ["2011", "2", table.iloc[11,4], table.iloc[11,6]], \
     ["2011", "2", table.iloc[12,4], table.iloc[12,6]], \
     ["2011", "2", table.iloc[13,4], table.iloc[13,6]], \
     ["2011", "2", table.iloc[14,4], table.iloc[14,6]], \
     ["2011", "2", table.iloc[15,3], table.iloc[15,6]], \
     ["2011", "2", table.iloc[16,3], table.iloc[16,6]], \
     ["2011", "2", table.iloc[17,3], table.iloc[17,6]]]
     
Feb11 = pd.DataFrame(B,columns=["year", "monnth", "sector", "value"])

table = pd.read_excel(r'C:\Users\jiaxi\OneDrive\Desktop\RBAC 2022\Balance\local\Italy\Italy\Reports\Gas Balance\Bilancio_GAS_2011_03.xls', sheet_name = 'Preconsuntivo marzo  2011')
B = [["2011", "3", table.iloc[5,3], table.iloc[5,6]], \
     ["2011", "3", table.iloc[6,3], table.iloc[6,6]], \
     ["2011", "3", table.iloc[7,4], table.iloc[7,6]], \
     ["2011", "3", table.iloc[8,4], table.iloc[8,6]], \
     ["2011", "3", table.iloc[9,4], table.iloc[9,6]], \
     ["2011", "3", table.iloc[10,4], table.iloc[10,6]], \
     ["2011", "3", table.iloc[11,4], table.iloc[11,6]], \
     ["2011", "3", table.iloc[12,4], table.iloc[12,6]], \
     ["2011", "3", table.iloc[13,4], table.iloc[13,6]], \
     ["2011", "3", table.iloc[14,4], table.iloc[14,6]], \
     ["2011", "3", table.iloc[15,3], table.iloc[15,6]], \
     ["2011", "3", table.iloc[16,3], table.iloc[16,6]], \
     ["2011", "3", table.iloc[17,3], table.iloc[17,6]]]
     
Mar11 = pd.DataFrame(B,columns=["year", "monnth", "sector", "value"])

table = pd.read_excel(r'C:\Users\jiaxi\OneDrive\Desktop\RBAC 2022\Balance\local\Italy\Italy\Reports\Gas Balance\Bilancio_GAS_2011_04.xls', sheet_name = 'Preconsuntivo aprile  2011')
B = [["2011", "4", table.iloc[5,3], table.iloc[5,6]], \
     ["2011", "4", table.iloc[6,3], table.iloc[6,6]], \
     ["2011", "4", table.iloc[7,4], table.iloc[7,6]], \
     ["2011", "4", table.iloc[8,4], table.iloc[8,6]], \
     ["2011", "4", table.iloc[9,4], table.iloc[9,6]], \
     ["2011", "4", table.iloc[10,4], table.iloc[10,6]], \
     ["2011", "4", table.iloc[11,4], table.iloc[11,6]], \
     ["2011", "4", table.iloc[12,4], table.iloc[12,6]], \
     ["2011", "4", table.iloc[13,4], table.iloc[13,6]], \
     ["2011", "4", table.iloc[14,4], table.iloc[14,6]], \
     ["2011", "4", table.iloc[15,3], table.iloc[15,6]], \
     ["2011", "4", table.iloc[16,3], table.iloc[16,6]], \
     ["2011", "4", table.iloc[17,3], table.iloc[17,6]]]
     
Apr11 = pd.DataFrame(B,columns=["year", "monnth", "sector", "value"])

table = pd.read_excel(r'C:\Users\jiaxi\OneDrive\Desktop\RBAC 2022\Balance\local\Italy\Italy\Reports\Gas Balance\Bilancio_GAS_2011_05.xls', sheet_name = 'Preconsuntivo maggio  2011')
B = [["2011", "5", table.iloc[5,3], table.iloc[5,6]], \
     ["2011", "5", table.iloc[6,3], table.iloc[6,6]], \
     ["2011", "5", table.iloc[7,4], table.iloc[7,6]], \
     ["2011", "5", table.iloc[8,4], table.iloc[8,6]], \
     ["2011", "5", table.iloc[9,4], table.iloc[9,6]], \
     ["2011", "5", table.iloc[10,4], table.iloc[10,6]], \
     ["2011", "5", table.iloc[11,4], table.iloc[11,6]], \
     ["2011", "5", table.iloc[12,4], table.iloc[12,6]], \
     ["2011", "5", table.iloc[13,4], table.iloc[13,6]], \
     ["2011", "5", table.iloc[14,4], table.iloc[14,6]], \
     ["2011", "5", table.iloc[15,3], table.iloc[15,6]], \
     ["2011", "5", table.iloc[16,3], table.iloc[16,6]], \
     ["2011", "5", table.iloc[17,3], table.iloc[17,6]]]
     
Mag11 = pd.DataFrame(B,columns=["year", "monnth", "sector", "value"])

table = pd.read_excel(r'C:\Users\jiaxi\OneDrive\Desktop\RBAC 2022\Balance\local\Italy\Italy\Reports\Gas Balance\Bilancio_GAS_2011_06.xls', sheet_name = 'Preconsuntivo giugno  2011')
B = [["2011", "6", table.iloc[5,3], table.iloc[5,6]], \
     ["2011", "6", table.iloc[6,3], table.iloc[6,6]], \
     ["2011", "6", table.iloc[7,4], table.iloc[7,6]], \
     ["2011", "6", table.iloc[8,4], table.iloc[8,6]], \
     ["2011", "6", table.iloc[9,4], table.iloc[9,6]], \
     ["2011", "6", table.iloc[10,4], table.iloc[10,6]], \
     ["2011", "6", table.iloc[11,4], table.iloc[11,6]], \
     ["2011", "6", table.iloc[12,4], table.iloc[12,6]], \
     ["2011", "6", table.iloc[13,4], table.iloc[13,6]], \
     ["2011", "6", table.iloc[14,4], table.iloc[14,6]], \
     ["2011", "6", table.iloc[15,3], table.iloc[15,6]], \
     ["2011", "6", table.iloc[16,3], table.iloc[16,6]], \
     ["2011", "6", table.iloc[17,3], table.iloc[17,6]]]
     
Giu11 = pd.DataFrame(B,columns=["year", "monnth", "sector", "value"])


table = pd.read_excel(r'C:\Users\jiaxi\OneDrive\Desktop\RBAC 2022\Balance\local\Italy\Italy\Reports\Gas Balance\Bilancio_GAS_2011_07.xls', sheet_name = 'Preconsuntivo luglio  2011')
B = [["2011", "7", table.iloc[5,3], table.iloc[5,6]], \
     ["2011", "7", table.iloc[6,3], table.iloc[6,6]], \
     ["2011", "7", table.iloc[7,4], table.iloc[7,6]], \
     ["2011", "7", table.iloc[8,4], table.iloc[8,6]], \
     ["2011", "7", table.iloc[9,4], table.iloc[9,6]], \
     ["2011", "7", table.iloc[10,4], table.iloc[10,6]], \
     ["2011", "7", table.iloc[11,4], table.iloc[11,6]], \
     ["2011", "7", table.iloc[12,4], table.iloc[12,6]], \
     ["2011", "7", table.iloc[13,4], table.iloc[13,6]], \
     ["2011", "7", table.iloc[14,4], table.iloc[14,6]], \
     ["2011", "7", table.iloc[15,3], table.iloc[15,6]], \
     ["2011", "7", table.iloc[16,3], table.iloc[16,6]], \
     ["2011", "7", table.iloc[17,3], table.iloc[17,6]]]
     
Lug11 = pd.DataFrame(B,columns=["year", "monnth", "sector", "value"])

table = pd.read_excel(r'C:\Users\jiaxi\OneDrive\Desktop\RBAC 2022\Balance\local\Italy\Italy\Reports\Gas Balance\Bilancio_GAS_2011_08.xls', sheet_name = 'Preconsuntivo agosto  2011')
B = [["2011", "8", table.iloc[5,3], table.iloc[5,6]], \
     ["2011", "8", table.iloc[6,3], table.iloc[6,6]], \
     ["2011", "8", table.iloc[7,4], table.iloc[7,6]], \
     ["2011", "8", table.iloc[8,4], table.iloc[8,6]], \
     ["2011", "8", table.iloc[9,4], table.iloc[9,6]], \
     ["2011", "8", table.iloc[10,4], table.iloc[10,6]], \
     ["2011", "8", table.iloc[11,4], table.iloc[11,6]], \
     ["2011", "8", table.iloc[12,4], table.iloc[12,6]], \
     ["2011", "8", table.iloc[13,4], table.iloc[13,6]], \
     ["2011", "8", table.iloc[14,4], table.iloc[14,6]], \
     ["2011", "8", table.iloc[15,3], table.iloc[15,6]], \
     ["2011", "8", table.iloc[16,3], table.iloc[16,6]], \
     ["2011", "8", table.iloc[17,3], table.iloc[17,6]]]
     
Ago11 = pd.DataFrame(B,columns=["year", "monnth", "sector", "value"])

table = pd.read_excel(r'C:\Users\jiaxi\OneDrive\Desktop\RBAC 2022\Balance\local\Italy\Italy\Reports\Gas Balance\Bilancio_GAS_2011_09.xls', sheet_name = 'Preconsuntivo settembre  2011')
B = [["2011", "9", table.iloc[5,3], table.iloc[5,6]], \
     ["2011", "9", table.iloc[6,3], table.iloc[6,6]], \
     ["2011", "9", table.iloc[7,4], table.iloc[7,6]], \
     ["2011", "9", table.iloc[8,4], table.iloc[8,6]], \
     ["2011", "9", table.iloc[9,4], table.iloc[9,6]], \
     ["2011", "9", table.iloc[10,4], table.iloc[10,6]], \
     ["2011", "9", table.iloc[11,4], table.iloc[11,6]], \
     ["2011", "9", table.iloc[12,4], table.iloc[12,6]], \
     ["2011", "9", table.iloc[13,4], table.iloc[13,6]], \
     ["2011", "9", table.iloc[14,4], table.iloc[14,6]], \
     ["2011", "9", table.iloc[15,3], table.iloc[15,6]], \
     ["2011", "9", table.iloc[16,3], table.iloc[16,6]], \
     ["2011", "9", table.iloc[17,3], table.iloc[17,6]]]
     
Set11 = pd.DataFrame(B,columns=["year", "monnth", "sector", "value"])


table = pd.read_excel(r'C:\Users\jiaxi\OneDrive\Desktop\RBAC 2022\Balance\local\Italy\Italy\Reports\Gas Balance\Bilancio_GAS_2011_10.xls', sheet_name = 'Preconsuntivo ottobre  2011')
B = [["2011", "10", table.iloc[5,3], table.iloc[5,6]], \
     ["2011", "10", table.iloc[6,3], table.iloc[6,6]], \
     ["2011", "10", table.iloc[7,4], table.iloc[7,6]], \
     ["2011", "10", table.iloc[8,4], table.iloc[8,6]], \
     ["2011", "10", table.iloc[9,4], table.iloc[9,6]], \
     ["2011", "10", table.iloc[10,4], table.iloc[10,6]], \
     ["2011", "10", table.iloc[11,4], table.iloc[11,6]], \
     ["2011", "10", table.iloc[12,4], table.iloc[12,6]], \
     ["2011", "10", table.iloc[13,4], table.iloc[13,6]], \
     ["2011", "10", table.iloc[14,4], table.iloc[14,6]], \
     ["2011", "10", table.iloc[15,3], table.iloc[15,6]], \
     ["2011", "10", table.iloc[16,3], table.iloc[16,6]], \
     ["2011", "10", table.iloc[17,3], table.iloc[17,6]]]
     
Ott11 = pd.DataFrame(B,columns=["year", "monnth", "sector", "value"])


table = pd.read_excel(r'C:\Users\jiaxi\OneDrive\Desktop\RBAC 2022\Balance\local\Italy\Italy\Reports\Gas Balance\Bilancio_GAS_2011_11.xls', sheet_name = 'Preconsuntivo novembre  2011')
B = [["2011", "11", table.iloc[5,3], table.iloc[5,6]], \
     ["2011", "11", table.iloc[6,3], table.iloc[6,6]], \
     ["2011", "11", table.iloc[7,4], table.iloc[7,6]], \
     ["2011", "11", table.iloc[8,4], table.iloc[8,6]], \
     ["2011", "11", table.iloc[9,4], table.iloc[9,6]], \
     ["2011", "11", table.iloc[10,4], table.iloc[10,6]], \
     ["2011", "11", table.iloc[11,4], table.iloc[11,6]], \
     ["2011", "11", table.iloc[12,4], table.iloc[12,6]], \
     ["2011", "11", table.iloc[13,4], table.iloc[13,6]], \
     ["2011", "11", table.iloc[14,4], table.iloc[14,6]], \
     ["2011", "11", table.iloc[15,3], table.iloc[15,6]], \
     ["2011", "11", table.iloc[16,3], table.iloc[16,6]], \
     ["2011", "11", table.iloc[17,3], table.iloc[17,6]]]
     
Nov11 = pd.DataFrame(B,columns=["year", "monnth", "sector", "value"])

table = pd.read_excel(r'C:\Users\jiaxi\OneDrive\Desktop\RBAC 2022\Balance\local\Italy\Italy\Reports\Gas Balance\Bilancio_GAS_2011_12.xls', sheet_name = 'Preconsuntivo dicembre  2011')
B = [["2011", "12", table.iloc[5,3], table.iloc[5,6]], \
     ["2011", "12", table.iloc[6,3], table.iloc[6,6]], \
     ["2011", "12", table.iloc[7,4], table.iloc[7,6]], \
     ["2011", "12", table.iloc[8,4], table.iloc[8,6]], \
     ["2011", "12", table.iloc[9,4], table.iloc[9,6]], \
     ["2011", "12", table.iloc[10,4], table.iloc[10,6]], \
     ["2011", "12", table.iloc[11,4], table.iloc[11,6]], \
     ["2011", "12", table.iloc[12,4], table.iloc[12,6]], \
     ["2011", "12", table.iloc[13,4], table.iloc[13,6]], \
     ["2011", "12", table.iloc[14,4], table.iloc[14,6]], \
     ["2011", "12", table.iloc[15,3], table.iloc[15,6]], \
     ["2011", "12", table.iloc[16,3], table.iloc[16,6]], \
     ["2011", "12", table.iloc[17,3], table.iloc[17,6]]]
     
Dic11 = pd.DataFrame(B,columns=["year", "monnth", "sector", "value"])

##2012
table = pd.read_excel(r'C:\Users\jiaxi\OneDrive\Desktop\RBAC 2022\Balance\local\Italy\Italy\Reports\Gas Balance\Bilancio_GAS_2012_01.xls', sheet_name = 'Preconsuntivo Gennaio 2012')
B = [["2012", "1", table.iloc[5,3], table.iloc[5,6]], \
     ["2012", "1", table.iloc[6,3], table.iloc[6,6]], \
     ["2012", "1", table.iloc[7,4], table.iloc[7,6]], \
     ["2012", "1", table.iloc[8,4], table.iloc[8,6]], \
     ["2012", "1", table.iloc[9,4], table.iloc[9,6]], \
     ["2012", "1", table.iloc[10,4], table.iloc[10,6]], \
     ["2012", "1", table.iloc[11,4], table.iloc[11,6]], \
     ["2012", "1", table.iloc[12,4], table.iloc[12,6]], \
     ["2012", "1", table.iloc[13,4], table.iloc[13,6]], \
     ["2012", "1", table.iloc[14,4], table.iloc[14,6]], \
     ["2012", "1", table.iloc[15,3], table.iloc[15,6]], \
     ["2012", "1", table.iloc[16,3], table.iloc[16,6]], \
     ["2012", "1", table.iloc[17,3], table.iloc[17,6]]]
     
Gen12 = pd.DataFrame(B,columns=["year", "monnth", "sector", "value"])

table = pd.read_excel(r'C:\Users\jiaxi\OneDrive\Desktop\RBAC 2022\Balance\local\Italy\Italy\Reports\Gas Balance\Bilancio_GAS_2012_02.xls', sheet_name = 'Preconsuntivo febbraio  2012')
B = [["2012", "2", table.iloc[5,3], table.iloc[5,6]], \
     ["2012", "2", table.iloc[6,3], table.iloc[6,6]], \
     ["2012", "2", table.iloc[7,4], table.iloc[7,6]], \
     ["2012", "2", table.iloc[8,4], table.iloc[8,6]], \
     ["2012", "2", table.iloc[9,4], table.iloc[9,6]], \
     ["2012", "2", table.iloc[10,4], table.iloc[10,6]], \
     ["2012", "2", table.iloc[11,4], table.iloc[11,6]], \
     ["2012", "2", table.iloc[12,4], table.iloc[12,6]], \
     ["2012", "2", table.iloc[13,4], table.iloc[13,6]], \
     ["2012", "2", table.iloc[14,4], table.iloc[14,6]], \
     ["2012", "2", table.iloc[15,3], table.iloc[15,6]], \
     ["2012", "2", table.iloc[16,3], table.iloc[16,6]], \
     ["2012", "2", table.iloc[17,3], table.iloc[17,6]]]
     
Feb12 = pd.DataFrame(B,columns=["year", "monnth", "sector", "value"])

table = pd.read_excel(r'C:\Users\jiaxi\OneDrive\Desktop\RBAC 2022\Balance\local\Italy\Italy\Reports\Gas Balance\Bilancio_GAS_2012_03.xls', sheet_name = 'Preconsuntivo marzo  2012')
B = [["2012", "3", table.iloc[5,3], table.iloc[5,6]], \
     ["2012", "3", table.iloc[6,3], table.iloc[6,6]], \
     ["2012", "3", table.iloc[7,4], table.iloc[7,6]], \
     ["2012", "3", table.iloc[8,4], table.iloc[8,6]], \
     ["2012", "3", table.iloc[9,4], table.iloc[9,6]], \
     ["2012", "3", table.iloc[10,4], table.iloc[10,6]], \
     ["2012", "3", table.iloc[11,4], table.iloc[11,6]], \
     ["2012", "3", table.iloc[12,4], table.iloc[12,6]], \
     ["2012", "3", table.iloc[13,4], table.iloc[13,6]], \
     ["2012", "3", table.iloc[14,4], table.iloc[14,6]], \
     ["2012", "3", table.iloc[15,3], table.iloc[15,6]], \
     ["2012", "3", table.iloc[16,3], table.iloc[16,6]], \
     ["2012", "3", table.iloc[17,3], table.iloc[17,6]]]
     
Mar12 = pd.DataFrame(B,columns=["year", "monnth", "sector", "value"])

table = pd.read_excel(r'C:\Users\jiaxi\OneDrive\Desktop\RBAC 2022\Balance\local\Italy\Italy\Reports\Gas Balance\Bilancio_GAS_2012_04.xls', sheet_name = 'Preconsuntivo aprile  2012')
B = [["2012", "4", table.iloc[5,3], table.iloc[5,6]], \
     ["2012", "4", table.iloc[6,3], table.iloc[6,6]], \
     ["2012", "4", table.iloc[7,4], table.iloc[7,6]], \
     ["2012", "4", table.iloc[8,4], table.iloc[8,6]], \
     ["2012", "4", table.iloc[9,4], table.iloc[9,6]], \
     ["2012", "4", table.iloc[10,4], table.iloc[10,6]], \
     ["2012", "4", table.iloc[11,4], table.iloc[11,6]], \
     ["2012", "4", table.iloc[12,4], table.iloc[12,6]], \
     ["2012", "4", table.iloc[13,4], table.iloc[13,6]], \
     ["2012", "4", table.iloc[14,4], table.iloc[14,6]], \
     ["2012", "4", table.iloc[15,3], table.iloc[15,6]], \
     ["2012", "4", table.iloc[16,3], table.iloc[16,6]], \
     ["2012", "4", table.iloc[17,3], table.iloc[17,6]]]
     
Apr12 = pd.DataFrame(B,columns=["year", "monnth", "sector", "value"])

table = pd.read_excel(r'C:\Users\jiaxi\OneDrive\Desktop\RBAC 2022\Balance\local\Italy\Italy\Reports\Gas Balance\Bilancio_GAS_2012_05.xls', sheet_name = 'Preconsuntivo maggio  2012')
B = [["2012", "5", table.iloc[5,3], table.iloc[5,6]], \
     ["2012", "5", table.iloc[6,3], table.iloc[6,6]], \
     ["2012", "5", table.iloc[7,4], table.iloc[7,6]], \
     ["2012", "5", table.iloc[8,4], table.iloc[8,6]], \
     ["2012", "5", table.iloc[9,4], table.iloc[9,6]], \
     ["2012", "5", table.iloc[10,4], table.iloc[10,6]], \
     ["2012", "5", table.iloc[11,4], table.iloc[11,6]], \
     ["2012", "5", table.iloc[12,4], table.iloc[12,6]], \
     ["2012", "5", table.iloc[13,4], table.iloc[13,6]], \
     ["2012", "5", table.iloc[14,4], table.iloc[14,6]], \
     ["2012", "5", table.iloc[15,3], table.iloc[15,6]], \
     ["2012", "5", table.iloc[16,3], table.iloc[16,6]], \
     ["2012", "5", table.iloc[17,3], table.iloc[17,6]]]
     
Mag12 = pd.DataFrame(B,columns=["year", "monnth", "sector", "value"])

table = pd.read_excel(r'C:\Users\jiaxi\OneDrive\Desktop\RBAC 2022\Balance\local\Italy\Italy\Reports\Gas Balance\Bilancio_GAS_2012_06.xls', sheet_name = 'Preconsuntivo giugno  2012')
B = [["2012", "6", table.iloc[5,3], table.iloc[5,6]], \
     ["2012", "6", table.iloc[6,3], table.iloc[6,6]], \
     ["2012", "6", table.iloc[7,4], table.iloc[7,6]], \
     ["2012", "6", table.iloc[8,4], table.iloc[8,6]], \
     ["2012", "6", table.iloc[9,4], table.iloc[9,6]], \
     ["2012", "6", table.iloc[10,4], table.iloc[10,6]], \
     ["2012", "6", table.iloc[11,4], table.iloc[11,6]], \
     ["2012", "6", table.iloc[12,4], table.iloc[12,6]], \
     ["2012", "6", table.iloc[13,4], table.iloc[13,6]], \
     ["2012", "6", table.iloc[14,4], table.iloc[14,6]], \
     ["2012", "6", table.iloc[15,3], table.iloc[15,6]], \
     ["2012", "6", table.iloc[16,3], table.iloc[16,6]], \
     ["2012", "6", table.iloc[17,3], table.iloc[17,6]]]
     
Giu12 = pd.DataFrame(B,columns=["year", "monnth", "sector", "value"])


table = pd.read_excel(r'C:\Users\jiaxi\OneDrive\Desktop\RBAC 2022\Balance\local\Italy\Italy\Reports\Gas Balance\Bilancio_GAS_2012_07.xls', sheet_name = 'Preconsuntivo luglio 2012')
B = [["2012", "7", table.iloc[5,3], table.iloc[5,6]], \
     ["2012", "7", table.iloc[6,3], table.iloc[6,6]], \
     ["2012", "7", table.iloc[7,4], table.iloc[7,6]], \
     ["2012", "7", table.iloc[8,4], table.iloc[8,6]], \
     ["2012", "7", table.iloc[9,4], table.iloc[9,6]], \
     ["2012", "7", table.iloc[10,4], table.iloc[10,6]], \
     ["2012", "7", table.iloc[11,4], table.iloc[11,6]], \
     ["2012", "7", table.iloc[12,4], table.iloc[12,6]], \
     ["2012", "7", table.iloc[13,4], table.iloc[13,6]], \
     ["2012", "7", table.iloc[14,4], table.iloc[14,6]], \
     ["2012", "7", table.iloc[15,3], table.iloc[15,6]], \
     ["2012", "7", table.iloc[16,3], table.iloc[16,6]], \
     ["2012", "7", table.iloc[17,3], table.iloc[17,6]]]
     
Lug12 = pd.DataFrame(B,columns=["year", "monnth", "sector", "value"])

table = pd.read_excel(r'C:\Users\jiaxi\OneDrive\Desktop\RBAC 2022\Balance\local\Italy\Italy\Reports\Gas Balance\Bilancio_GAS_2012_08.xls', sheet_name = 'Preconsuntivo agosto 2012')
B = [["2012", "8", table.iloc[5,3], table.iloc[5,6]], \
     ["2012", "8", table.iloc[6,3], table.iloc[6,6]], \
     ["2012", "8", table.iloc[7,4], table.iloc[7,6]], \
     ["2012", "8", table.iloc[8,4], table.iloc[8,6]], \
     ["2012", "8", table.iloc[9,4], table.iloc[9,6]], \
     ["2012", "8", table.iloc[10,4], table.iloc[10,6]], \
     ["2012", "8", table.iloc[11,4], table.iloc[11,6]], \
     ["2012", "8", table.iloc[12,4], table.iloc[12,6]], \
     ["2012", "8", table.iloc[13,4], table.iloc[13,6]], \
     ["2012", "8", table.iloc[14,4], table.iloc[14,6]], \
     ["2012", "8", table.iloc[15,3], table.iloc[15,6]], \
     ["2012", "8", table.iloc[16,3], table.iloc[16,6]], \
     ["2012", "8", table.iloc[17,3], table.iloc[17,6]]]
     
Ago12 = pd.DataFrame(B,columns=["year", "monnth", "sector", "value"])

table = pd.read_excel(r'C:\Users\jiaxi\OneDrive\Desktop\RBAC 2022\Balance\local\Italy\Italy\Reports\Gas Balance\Bilancio_GAS_2012_09.xls', sheet_name = 'Preconsuntivo settembre 2012')
B = [["2012", "9", table.iloc[5,3], table.iloc[5,6]], \
     ["2012", "9", table.iloc[6,3], table.iloc[6,6]], \
     ["2012", "9", table.iloc[7,4], table.iloc[7,6]], \
     ["2012", "9", table.iloc[8,4], table.iloc[8,6]], \
     ["2012", "9", table.iloc[9,4], table.iloc[9,6]], \
     ["2012", "9", table.iloc[10,4], table.iloc[10,6]], \
     ["2012", "9", table.iloc[11,4], table.iloc[11,6]], \
     ["2012", "9", table.iloc[12,4], table.iloc[12,6]], \
     ["2012", "9", table.iloc[13,4], table.iloc[13,6]], \
     ["2012", "9", table.iloc[14,4], table.iloc[14,6]], \
     ["2012", "9", table.iloc[15,3], table.iloc[15,6]], \
     ["2012", "9", table.iloc[16,3], table.iloc[16,6]], \
     ["2012", "9", table.iloc[17,3], table.iloc[17,6]]]
     
Set12 = pd.DataFrame(B,columns=["year", "monnth", "sector", "value"])


table = pd.read_excel(r'C:\Users\jiaxi\OneDrive\Desktop\RBAC 2022\Balance\local\Italy\Italy\Reports\Gas Balance\Bilancio_GAS_2012_10.xls', sheet_name = 'Preconsuntivo ottobre 2012')
B = [["2012", "10", table.iloc[5,3], table.iloc[5,6]], \
     ["2012", "10", table.iloc[6,3], table.iloc[6,6]], \
     ["2012", "10", table.iloc[7,4], table.iloc[7,6]], \
     ["2012", "10", table.iloc[8,4], table.iloc[8,6]], \
     ["2012", "10", table.iloc[9,4], table.iloc[9,6]], \
     ["2012", "10", table.iloc[10,4], table.iloc[10,6]], \
     ["2012", "10", table.iloc[11,4], table.iloc[11,6]], \
     ["2012", "10", table.iloc[12,4], table.iloc[12,6]], \
     ["2012", "10", table.iloc[13,4], table.iloc[13,6]], \
     ["2012", "10", table.iloc[14,4], table.iloc[14,6]], \
     ["2012", "10", table.iloc[15,3], table.iloc[15,6]], \
     ["2012", "10", table.iloc[16,3], table.iloc[16,6]], \
     ["2012", "10", table.iloc[17,3], table.iloc[17,6]]]
     
Ott12 = pd.DataFrame(B,columns=["year", "monnth", "sector", "value"])


table = pd.read_excel(r'C:\Users\jiaxi\OneDrive\Desktop\RBAC 2022\Balance\local\Italy\Italy\Reports\Gas Balance\Bilancio_GAS_2012_11.xls', sheet_name = 'Preconsuntivo novembre 2012')
B = [["2012", "11", table.iloc[5,3], table.iloc[5,6]], \
     ["2012", "11", table.iloc[6,3], table.iloc[6,6]], \
     ["2012", "11", table.iloc[7,4], table.iloc[7,6]], \
     ["2012", "11", table.iloc[8,4], table.iloc[8,6]], \
     ["2012", "11", table.iloc[9,4], table.iloc[9,6]], \
     ["2012", "11", table.iloc[10,4], table.iloc[10,6]], \
     ["2012", "11", table.iloc[11,4], table.iloc[11,6]], \
     ["2012", "11", table.iloc[12,4], table.iloc[12,6]], \
     ["2012", "11", table.iloc[13,4], table.iloc[13,6]], \
     ["2012", "11", table.iloc[14,4], table.iloc[14,6]], \
     ["2012", "11", table.iloc[15,3], table.iloc[15,6]], \
     ["2012", "11", table.iloc[16,3], table.iloc[16,6]], \
     ["2012", "11", table.iloc[17,3], table.iloc[17,6]]]
     
Nov12 = pd.DataFrame(B,columns=["year", "monnth", "sector", "value"])

table = pd.read_excel(r'C:\Users\jiaxi\OneDrive\Desktop\RBAC 2022\Balance\local\Italy\Italy\Reports\Gas Balance\Bilancio_GAS_2012_12.xls', sheet_name = 'Preconsuntivo dicembre 2012')
B = [["2012", "12", table.iloc[5,3], table.iloc[5,6]], \
     ["2012", "12", table.iloc[6,3], table.iloc[6,6]], \
     ["2012", "12", table.iloc[7,4], table.iloc[7,6]], \
     ["2012", "12", table.iloc[8,4], table.iloc[8,6]], \
     ["2012", "12", table.iloc[9,4], table.iloc[9,6]], \
     ["2012", "12", table.iloc[10,4], table.iloc[10,6]], \
     ["2012", "12", table.iloc[11,4], table.iloc[11,6]], \
     ["2012", "12", table.iloc[12,4], table.iloc[12,6]], \
     ["2012", "12", table.iloc[13,4], table.iloc[13,6]], \
     ["2012", "12", table.iloc[14,4], table.iloc[14,6]], \
     ["2012", "12", table.iloc[15,3], table.iloc[15,6]], \
     ["2012", "12", table.iloc[16,3], table.iloc[16,6]], \
     ["2012", "12", table.iloc[17,3], table.iloc[17,6]]]
     
Dic12 = pd.DataFrame(B,columns=["year", "monnth", "sector", "value"])

##2013
table = pd.read_excel(r'C:\Users\jiaxi\OneDrive\Desktop\RBAC 2022\Balance\local\Italy\Italy\Reports\Gas Balance\Bilancio_GAS_2013_01_rev1.xls', sheet_name = 'Preconsuntivo Gennaio 2013')
B = [["2013", "1", table.iloc[5,3], table.iloc[5,6]], \
     ["2013", "1", table.iloc[6,3], table.iloc[6,6]], \
     ["2013", "1", table.iloc[7,4], table.iloc[7,6]], \
     ["2013", "1", table.iloc[8,4], table.iloc[8,6]], \
     ["2013", "1", table.iloc[9,4], table.iloc[9,6]], \
     ["2013", "1", table.iloc[10,4], table.iloc[10,6]], \
     ["2013", "1", table.iloc[11,4], table.iloc[11,6]], \
     ["2013", "1", table.iloc[12,4], table.iloc[12,6]], \
     ["2013", "1", table.iloc[13,4], table.iloc[13,6]], \
     ["2013", "1", table.iloc[14,4], table.iloc[14,6]], \
     ["2013", "1", table.iloc[15,3], table.iloc[15,6]], \
     ["2013", "1", table.iloc[16,3], table.iloc[16,6]], \
     ["2013", "1", table.iloc[17,3], table.iloc[17,6]]]
     
Gen13 = pd.DataFrame(B,columns=["year", "monnth", "sector", "value"])

table = pd.read_excel(r'C:\Users\jiaxi\OneDrive\Desktop\RBAC 2022\Balance\local\Italy\Italy\Reports\Gas Balance\Bilancio_GAS_2013_02_rev1.xls', sheet_name = 'Preconsuntivo febbraio  2013')
B = [["2013", "2", table.iloc[5,3], table.iloc[5,6]], \
     ["2013", "2", table.iloc[6,3], table.iloc[6,6]], \
     ["2013", "2", table.iloc[7,4], table.iloc[7,6]], \
     ["2013", "2", table.iloc[8,4], table.iloc[8,6]], \
     ["2013", "2", table.iloc[9,4], table.iloc[9,6]], \
     ["2013", "2", table.iloc[10,4], table.iloc[10,6]], \
     ["2013", "2", table.iloc[11,4], table.iloc[11,6]], \
     ["2013", "2", table.iloc[12,4], table.iloc[12,6]], \
     ["2013", "2", table.iloc[13,4], table.iloc[13,6]], \
     ["2013", "2", table.iloc[14,4], table.iloc[14,6]], \
     ["2013", "2", table.iloc[15,3], table.iloc[15,6]], \
     ["2013", "2", table.iloc[16,3], table.iloc[16,6]], \
     ["2013", "2", table.iloc[17,3], table.iloc[17,6]]]
     
Feb13 = pd.DataFrame(B,columns=["year", "monnth", "sector", "value"])

table = pd.read_excel(r'C:\Users\jiaxi\OneDrive\Desktop\RBAC 2022\Balance\local\Italy\Italy\Reports\Gas Balance\Bilancio_GAS_2013_03_rev1.xls', sheet_name = 'Preconsuntivo marzo  2013')
B = [["2013", "3", table.iloc[5,3], table.iloc[5,6]], \
     ["2013", "3", table.iloc[6,3], table.iloc[6,6]], \
     ["2013", "3", table.iloc[7,4], table.iloc[7,6]], \
     ["2013", "3", table.iloc[8,4], table.iloc[8,6]], \
     ["2013", "3", table.iloc[9,4], table.iloc[9,6]], \
     ["2013", "3", table.iloc[10,4], table.iloc[10,6]], \
     ["2013", "3", table.iloc[11,4], table.iloc[11,6]], \
     ["2013", "3", table.iloc[12,4], table.iloc[12,6]], \
     ["2013", "3", table.iloc[13,4], table.iloc[13,6]], \
     ["2013", "3", table.iloc[14,4], table.iloc[14,6]], \
     ["2013", "3", table.iloc[15,3], table.iloc[15,6]], \
     ["2013", "3", table.iloc[16,3], table.iloc[16,6]], \
     ["2013", "3", table.iloc[17,3], table.iloc[17,6]]]
     
Mar13 = pd.DataFrame(B,columns=["year", "monnth", "sector", "value"])

table = pd.read_excel(r'C:\Users\jiaxi\OneDrive\Desktop\RBAC 2022\Balance\local\Italy\Italy\Reports\Gas Balance\Bilancio_GAS_2013_04_rev1.xls', sheet_name = 'Preconsuntivo aprile  2013')
B = [["2013", "4", table.iloc[5,3], table.iloc[5,6]], \
     ["2013", "4", table.iloc[6,3], table.iloc[6,6]], \
     ["2013", "4", table.iloc[7,4], table.iloc[7,6]], \
     ["2013", "4", table.iloc[8,4], table.iloc[8,6]], \
     ["2013", "4", table.iloc[9,4], table.iloc[9,6]], \
     ["2013", "4", table.iloc[10,4], table.iloc[10,6]], \
     ["2013", "4", table.iloc[11,4], table.iloc[11,6]], \
     ["2013", "4", table.iloc[12,4], table.iloc[12,6]], \
     ["2013", "4", table.iloc[13,4], table.iloc[13,6]], \
     ["2013", "4", table.iloc[14,4], table.iloc[14,6]], \
     ["2013", "4", table.iloc[15,3], table.iloc[15,6]], \
     ["2013", "4", table.iloc[16,3], table.iloc[16,6]], \
     ["2013", "4", table.iloc[17,3], table.iloc[17,6]]]
     
Apr13 = pd.DataFrame(B,columns=["year", "monnth", "sector", "value"])

table = pd.read_excel(r'C:\Users\jiaxi\OneDrive\Desktop\RBAC 2022\Balance\local\Italy\Italy\Reports\Gas Balance\Bilancio_GAS_2013_05_rev1.xls', sheet_name = 'Preconsuntivo maggio  2013')
B = [["2013", "5", table.iloc[5,3], table.iloc[5,6]], \
     ["2013", "5", table.iloc[6,3], table.iloc[6,6]], \
     ["2013", "5", table.iloc[7,4], table.iloc[7,6]], \
     ["2013", "5", table.iloc[8,4], table.iloc[8,6]], \
     ["2013", "5", table.iloc[9,4], table.iloc[9,6]], \
     ["2013", "5", table.iloc[10,4], table.iloc[10,6]], \
     ["2013", "5", table.iloc[11,4], table.iloc[11,6]], \
     ["2013", "5", table.iloc[12,4], table.iloc[12,6]], \
     ["2013", "5", table.iloc[13,4], table.iloc[13,6]], \
     ["2013", "5", table.iloc[14,4], table.iloc[14,6]], \
     ["2013", "5", table.iloc[15,3], table.iloc[15,6]], \
     ["2013", "5", table.iloc[16,3], table.iloc[16,6]], \
     ["2013", "5", table.iloc[17,3], table.iloc[17,6]]]
     
Mag13 = pd.DataFrame(B,columns=["year", "monnth", "sector", "value"])

table = pd.read_excel(r'C:\Users\jiaxi\OneDrive\Desktop\RBAC 2022\Balance\local\Italy\Italy\Reports\Gas Balance\Bilancio_GAS_2013_06_rev1.xls', sheet_name = 'Preconsuntivo giugno  2013')
B = [["2013", "6", table.iloc[5,3], table.iloc[5,6]], \
     ["2013", "6", table.iloc[6,3], table.iloc[6,6]], \
     ["2013", "6", table.iloc[7,4], table.iloc[7,6]], \
     ["2013", "6", table.iloc[8,4], table.iloc[8,6]], \
     ["2013", "6", table.iloc[9,4], table.iloc[9,6]], \
     ["2013", "6", table.iloc[10,4], table.iloc[10,6]], \
     ["2013", "6", table.iloc[11,4], table.iloc[11,6]], \
     ["2013", "6", table.iloc[12,4], table.iloc[12,6]], \
     ["2013", "6", table.iloc[13,4], table.iloc[13,6]], \
     ["2013", "6", table.iloc[14,4], table.iloc[14,6]], \
     ["2013", "6", table.iloc[15,3], table.iloc[15,6]], \
     ["2013", "6", table.iloc[16,3], table.iloc[16,6]], \
     ["2013", "6", table.iloc[17,3], table.iloc[17,6]]]
     
Giu13 = pd.DataFrame(B,columns=["year", "monnth", "sector", "value"])


table = pd.read_excel(r'C:\Users\jiaxi\OneDrive\Desktop\RBAC 2022\Balance\local\Italy\Italy\Reports\Gas Balance\Bilancio_GAS_2013_07_rev1.xls', sheet_name = 'Preconsuntivo luglio  2013')
B = [["2013", "7", table.iloc[5,3], table.iloc[5,6]], \
     ["2013", "7", table.iloc[6,3], table.iloc[6,6]], \
     ["2013", "7", table.iloc[7,4], table.iloc[7,6]], \
     ["2013", "7", table.iloc[8,4], table.iloc[8,6]], \
     ["2013", "7", table.iloc[9,4], table.iloc[9,6]], \
     ["2013", "7", table.iloc[10,4], table.iloc[10,6]], \
     ["2013", "7", table.iloc[11,4], table.iloc[11,6]], \
     ["2013", "7", table.iloc[12,4], table.iloc[12,6]], \
     ["2013", "7", table.iloc[13,4], table.iloc[13,6]], \
     ["2013", "7", table.iloc[14,4], table.iloc[14,6]], \
     ["2013", "7", table.iloc[15,3], table.iloc[15,6]], \
     ["2013", "7", table.iloc[16,3], table.iloc[16,6]], \
     ["2013", "7", table.iloc[17,3], table.iloc[17,6]]]
     
Lug13 = pd.DataFrame(B,columns=["year", "monnth", "sector", "value"])

table = pd.read_excel(r'C:\Users\jiaxi\OneDrive\Desktop\RBAC 2022\Balance\local\Italy\Italy\Reports\Gas Balance\Bilancio_GAS_2013_08_rev1.xls', sheet_name = 'Preconsuntivo agosto  2013')
B = [["2013", "8", table.iloc[5,3], table.iloc[5,6]], \
     ["2013", "8", table.iloc[6,3], table.iloc[6,6]], \
     ["2013", "8", table.iloc[7,4], table.iloc[7,6]], \
     ["2013", "8", table.iloc[8,4], table.iloc[8,6]], \
     ["2013", "8", table.iloc[9,4], table.iloc[9,6]], \
     ["2013", "8", table.iloc[10,4], table.iloc[10,6]], \
     ["2013", "8", table.iloc[11,4], table.iloc[11,6]], \
     ["2013", "8", table.iloc[12,4], table.iloc[12,6]], \
     ["2013", "8", table.iloc[13,4], table.iloc[13,6]], \
     ["2013", "8", table.iloc[14,4], table.iloc[14,6]], \
     ["2013", "8", table.iloc[15,3], table.iloc[15,6]], \
     ["2013", "8", table.iloc[16,3], table.iloc[16,6]], \
     ["2013", "8", table.iloc[17,3], table.iloc[17,6]]]
     
Ago13 = pd.DataFrame(B,columns=["year", "monnth", "sector", "value"])

table = pd.read_excel(r'C:\Users\jiaxi\OneDrive\Desktop\RBAC 2022\Balance\local\Italy\Italy\Reports\Gas Balance\Bilancio_GAS_2013_09_rev1.xls', sheet_name = 'Preconsuntivo settembre  2013')
B = [["2013", "9", table.iloc[5,3], table.iloc[5,6]], \
     ["2013", "9", table.iloc[6,3], table.iloc[6,6]], \
     ["2013", "9", table.iloc[7,4], table.iloc[7,6]], \
     ["2013", "9", table.iloc[8,4], table.iloc[8,6]], \
     ["2013", "9", table.iloc[9,4], table.iloc[9,6]], \
     ["2013", "9", table.iloc[10,4], table.iloc[10,6]], \
     ["2013", "9", table.iloc[11,4], table.iloc[11,6]], \
     ["2013", "9", table.iloc[12,4], table.iloc[12,6]], \
     ["2013", "9", table.iloc[13,4], table.iloc[13,6]], \
     ["2013", "9", table.iloc[14,4], table.iloc[14,6]], \
     ["2013", "9", table.iloc[15,4], table.iloc[15,6]], \
     ["2013", "9", table.iloc[16,3], table.iloc[16,6]], \
     ["2013", "9", table.iloc[17,3], table.iloc[17,6]], \
     ["2013", "9", table.iloc[18,3], table.iloc[18,6]]]
     
Set13 = pd.DataFrame(B,columns=["year", "monnth", "sector", "value"])


table = pd.read_excel(r'C:\Users\jiaxi\OneDrive\Desktop\RBAC 2022\Balance\local\Italy\Italy\Reports\Gas Balance\Bilancio_GAS_2013_10.xls', sheet_name = 'Preconsuntivo ottobre  2013')
B = [["2013", "10", table.iloc[5,3], table.iloc[5,6]], \
     ["2013", "10", table.iloc[6,3], table.iloc[6,6]], \
     ["2013", "10", table.iloc[7,4], table.iloc[7,6]], \
     ["2013", "10", table.iloc[8,4], table.iloc[8,6]], \
     ["2013", "10", table.iloc[9,4], table.iloc[9,6]], \
     ["2013", "10", table.iloc[10,4], table.iloc[10,6]], \
     ["2013", "10", table.iloc[11,4], table.iloc[11,6]], \
     ["2013", "10", table.iloc[12,4], table.iloc[12,6]], \
     ["2013", "10", table.iloc[13,4], table.iloc[13,6]], \
     ["2013", "10", table.iloc[14,4], table.iloc[14,6]], \
     ["2013", "10", table.iloc[15,4], table.iloc[15,6]], \
     ["2013", "10", table.iloc[16,3], table.iloc[16,6]], \
     ["2013", "10", table.iloc[17,3], table.iloc[17,6]], \
     ["2013", "10", table.iloc[18,3], table.iloc[18,6]]]
     
Ott13 = pd.DataFrame(B,columns=["year", "monnth", "sector", "value"])


table = pd.read_excel(r'C:\Users\jiaxi\OneDrive\Desktop\RBAC 2022\Balance\local\Italy\Italy\Reports\Gas Balance\Bilancio_GAS_2013_11.xls', sheet_name = 'Preconsuntivo Novembre  2013')
B = [["2013", "11", table.iloc[5,3], table.iloc[5,6]], \
     ["2013", "11", table.iloc[6,3], table.iloc[6,6]], \
     ["2013", "11", table.iloc[7,4], table.iloc[7,6]], \
     ["2013", "11", table.iloc[8,4], table.iloc[8,6]], \
     ["2013", "11", table.iloc[9,4], table.iloc[9,6]], \
     ["2013", "11", table.iloc[10,4], table.iloc[10,6]], \
     ["2013", "11", table.iloc[11,4], table.iloc[11,6]], \
     ["2013", "11", table.iloc[12,4], table.iloc[12,6]], \
     ["2013", "11", table.iloc[13,4], table.iloc[13,6]], \
     ["2013", "11", table.iloc[14,4], table.iloc[14,6]], \
     ["2013", "11", table.iloc[15,4], table.iloc[15,6]], \
     ["2013", "11", table.iloc[16,3], table.iloc[16,6]], \
     ["2013", "11", table.iloc[17,3], table.iloc[17,6]], \
     ["2013", "11", table.iloc[18,3], table.iloc[18,6]]]
     
Nov13 = pd.DataFrame(B,columns=["year", "monnth", "sector", "value"])

table = pd.read_excel(r'C:\Users\jiaxi\OneDrive\Desktop\RBAC 2022\Balance\local\Italy\Italy\Reports\Gas Balance\Bilancio_GAS_2013_12.xls', sheet_name = 'Preconsuntivo Dicembre  2013')
B = [["2013", "12", table.iloc[5,3], table.iloc[5,6]], \
     ["2013", "12", table.iloc[6,3], table.iloc[6,6]], \
     ["2013", "12", table.iloc[7,4], table.iloc[7,6]], \
     ["2013", "12", table.iloc[8,4], table.iloc[8,6]], \
     ["2013", "12", table.iloc[9,4], table.iloc[9,6]], \
     ["2013", "12", table.iloc[10,4], table.iloc[10,6]], \
     ["2013", "12", table.iloc[11,4], table.iloc[11,6]], \
     ["2013", "12", table.iloc[12,4], table.iloc[12,6]], \
     ["2013", "12", table.iloc[13,4], table.iloc[13,6]], \
     ["2013", "12", table.iloc[14,4], table.iloc[14,6]], \
     ["2013", "12", table.iloc[15,4], table.iloc[15,6]], \
     ["2013", "12", table.iloc[16,3], table.iloc[16,6]], \
     ["2013", "12", table.iloc[17,3], table.iloc[17,6]], \
     ["2013", "12", table.iloc[18,3], table.iloc[18,6]]]
     
Dic13 = pd.DataFrame(B,columns=["year", "monnth", "sector", "value"])


##2014
table = pd.read_excel(r'C:\Users\jiaxi\OneDrive\Desktop\RBAC 2022\Balance\local\Italy\Italy\Reports\Gas Balance\Bilancio_GAS_2014_01_rev1.xls', sheet_name = 'Preconsuntivo Gennaio  2014')
B = [["2014", "1", table.iloc[5,3], table.iloc[5,6]], \
     ["2014", "1", table.iloc[6,3], table.iloc[6,6]], \
     ["2014", "1", table.iloc[7,4], table.iloc[7,6]], \
     ["2014", "1", table.iloc[8,4], table.iloc[8,6]], \
     ["2014", "1", table.iloc[9,4], table.iloc[9,6]], \
     ["2014", "1", table.iloc[10,4], table.iloc[10,6]], \
     ["2014", "1", table.iloc[11,4], table.iloc[11,6]], \
     ["2014", "1", table.iloc[12,4], table.iloc[12,6]], \
     ["2014", "1", table.iloc[13,4], table.iloc[13,6]], \
     ["2014", "1", table.iloc[14,4], table.iloc[14,6]], \
     ["2014", "1", table.iloc[15,4], table.iloc[15,6]], \
     ["2014", "1", table.iloc[16,3], table.iloc[16,6]], \
     ["2014", "1", table.iloc[17,3], table.iloc[17,6]], \
     ["2014", "1", table.iloc[18,3], table.iloc[18,6]]]
     
Gen14 = pd.DataFrame(B,columns=["year", "monnth", "sector", "value"])

table = pd.read_excel(r'C:\Users\jiaxi\OneDrive\Desktop\RBAC 2022\Balance\local\Italy\Italy\Reports\Gas Balance\Bilancio_GAS_2014_02.xls', sheet_name = 'Preconsuntivo Febbraio  2014')
B = [["2014", "2", table.iloc[5,3], table.iloc[5,6]], \
     ["2014", "2", table.iloc[6,3], table.iloc[6,6]], \
     ["2014", "2", table.iloc[7,4], table.iloc[7,6]], \
     ["2014", "2", table.iloc[8,4], table.iloc[8,6]], \
     ["2014", "2", table.iloc[9,4], table.iloc[9,6]], \
     ["2014", "2", table.iloc[10,4], table.iloc[10,6]], \
     ["2014", "2", table.iloc[11,4], table.iloc[11,6]], \
     ["2014", "2", table.iloc[12,4], table.iloc[12,6]], \
     ["2014", "2", table.iloc[13,4], table.iloc[13,6]], \
     ["2014", "2", table.iloc[14,4], table.iloc[14,6]], \
     ["2014", "2", table.iloc[15,4], table.iloc[15,6]], \
     ["2014", "2", table.iloc[16,3], table.iloc[16,6]], \
     ["2014", "2", table.iloc[17,3], table.iloc[17,6]], \
     ["2014", "2", table.iloc[18,3], table.iloc[18,6]]]
     
Feb14 = pd.DataFrame(B,columns=["year", "monnth", "sector", "value"])

table = pd.read_excel(r'C:\Users\jiaxi\OneDrive\Desktop\RBAC 2022\Balance\local\Italy\Italy\Reports\Gas Balance\Bilancio_GAS_2014_03.xls', sheet_name = 'Preconsuntivo Marzo  2014')
B = [["2014", "3", table.iloc[5,3], table.iloc[5,6]], \
     ["2014", "3", table.iloc[6,3], table.iloc[6,6]], \
     ["2014", "3", table.iloc[7,4], table.iloc[7,6]], \
     ["2014", "3", table.iloc[8,4], table.iloc[8,6]], \
     ["2014", "3", table.iloc[9,4], table.iloc[9,6]], \
     ["2014", "3", table.iloc[10,4], table.iloc[10,6]], \
     ["2014", "3", table.iloc[11,4], table.iloc[11,6]], \
     ["2014", "3", table.iloc[12,4], table.iloc[12,6]], \
     ["2014", "3", table.iloc[13,4], table.iloc[13,6]], \
     ["2014", "3", table.iloc[14,4], table.iloc[14,6]], \
     ["2014", "3", table.iloc[15,4], table.iloc[15,6]], \
     ["2014", "3", table.iloc[16,3], table.iloc[16,6]], \
     ["2014", "3", table.iloc[17,3], table.iloc[17,6]], \
     ["2014", "3", table.iloc[18,3], table.iloc[18,6]]]
     
Mar14 = pd.DataFrame(B,columns=["year", "monnth", "sector", "value"])

table = pd.read_excel(r'C:\Users\jiaxi\OneDrive\Desktop\RBAC 2022\Balance\local\Italy\Italy\Reports\Gas Balance\Bilancio_GAS_2014_04.xls', sheet_name = 'Preconsuntivo Aprile 2014')
B = [["2014", "4", table.iloc[5,3], table.iloc[5,6]], \
     ["2014", "4", table.iloc[6,3], table.iloc[6,6]], \
     ["2014", "4", table.iloc[7,4], table.iloc[7,6]], \
     ["2014", "4", table.iloc[8,4], table.iloc[8,6]], \
     ["2014", "4", table.iloc[9,4], table.iloc[9,6]], \
     ["2014", "4", table.iloc[10,4], table.iloc[10,6]], \
     ["2014", "4", table.iloc[11,4], table.iloc[11,6]], \
     ["2014", "4", table.iloc[12,4], table.iloc[12,6]], \
     ["2014", "4", table.iloc[13,4], table.iloc[13,6]], \
     ["2014", "4", table.iloc[14,4], table.iloc[14,6]], \
     ["2014", "4", table.iloc[15,4], table.iloc[15,6]], \
     ["2014", "4", table.iloc[16,3], table.iloc[16,6]], \
     ["2014", "4", table.iloc[17,3], table.iloc[17,6]], \
     ["2014", "4", table.iloc[18,3], table.iloc[18,6]]]
     
Apr14 = pd.DataFrame(B,columns=["year", "monnth", "sector", "value"])

table = pd.read_excel(r'C:\Users\jiaxi\OneDrive\Desktop\RBAC 2022\Balance\local\Italy\Italy\Reports\Gas Balance\Bilancio_GAS_2014_05.xls', sheet_name = 'Preconsuntivo Maggio 2014')
B = [["2014", "5", table.iloc[5,3], table.iloc[5,6]], \
     ["2014", "5", table.iloc[6,3], table.iloc[6,6]], \
     ["2014", "5", table.iloc[7,4], table.iloc[7,6]], \
     ["2014", "5", table.iloc[8,4], table.iloc[8,6]], \
     ["2014", "5", table.iloc[9,4], table.iloc[9,6]], \
     ["2014", "5", table.iloc[10,4], table.iloc[10,6]], \
     ["2014", "5", table.iloc[11,4], table.iloc[11,6]], \
     ["2014", "5", table.iloc[12,4], table.iloc[12,6]], \
     ["2014", "5", table.iloc[13,4], table.iloc[13,6]], \
     ["2014", "5", table.iloc[14,4], table.iloc[14,6]], \
     ["2014", "5", table.iloc[15,4], table.iloc[15,6]], \
     ["2014", "5", table.iloc[16,3], table.iloc[16,6]], \
     ["2014", "5", table.iloc[17,3], table.iloc[17,6]], \
     ["2014", "5", table.iloc[18,3], table.iloc[18,6]]]
     
Mag14 = pd.DataFrame(B,columns=["year", "monnth", "sector", "value"])

table = pd.read_excel(r'C:\Users\jiaxi\OneDrive\Desktop\RBAC 2022\Balance\local\Italy\Italy\Reports\Gas Balance\Bilancio_GAS_2014_06.xls', sheet_name = 'Preconsuntivo Giugno 2014')
B = [["2014", "6", table.iloc[5,3], table.iloc[5,6]], \
     ["2014", "6", table.iloc[6,3], table.iloc[6,6]], \
     ["2014", "6", table.iloc[7,4], table.iloc[7,6]], \
     ["2014", "6", table.iloc[8,4], table.iloc[8,6]], \
     ["2014", "6", table.iloc[9,4], table.iloc[9,6]], \
     ["2014", "6", table.iloc[10,4], table.iloc[10,6]], \
     ["2014", "6", table.iloc[11,4], table.iloc[11,6]], \
     ["2014", "6", table.iloc[12,4], table.iloc[12,6]], \
     ["2014", "6", table.iloc[13,4], table.iloc[13,6]], \
     ["2014", "6", table.iloc[14,4], table.iloc[14,6]], \
     ["2014", "6", table.iloc[15,4], table.iloc[15,6]], \
     ["2014", "6", table.iloc[16,3], table.iloc[16,6]], \
     ["2014", "6", table.iloc[17,3], table.iloc[17,6]], \
     ["2014", "6", table.iloc[18,3], table.iloc[18,6]]]
     
Giu14 = pd.DataFrame(B,columns=["year", "monnth", "sector", "value"])


table = pd.read_excel(r'C:\Users\jiaxi\OneDrive\Desktop\RBAC 2022\Balance\local\Italy\Italy\Reports\Gas Balance\Bilancio_GAS_2014_07.xls', sheet_name = 'Preconsuntivo Luglio 2014')
B = [["2014", "7", table.iloc[5,3], table.iloc[5,6]], \
     ["2014", "7", table.iloc[6,3], table.iloc[6,6]], \
     ["2014", "7", table.iloc[7,4], table.iloc[7,6]], \
     ["2014", "7", table.iloc[8,4], table.iloc[8,6]], \
     ["2014", "7", table.iloc[9,4], table.iloc[9,6]], \
     ["2014", "7", table.iloc[10,4], table.iloc[10,6]], \
     ["2014", "7", table.iloc[11,4], table.iloc[11,6]], \
     ["2014", "7", table.iloc[12,4], table.iloc[12,6]], \
     ["2014", "7", table.iloc[13,4], table.iloc[13,6]], \
     ["2014", "7", table.iloc[14,4], table.iloc[14,6]], \
     ["2014", "7", table.iloc[15,4], table.iloc[15,6]], \
     ["2014", "7", table.iloc[16,3], table.iloc[16,6]], \
     ["2014", "7", table.iloc[17,3], table.iloc[17,6]], \
     ["2014", "7", table.iloc[18,3], table.iloc[18,6]]]
     
Lug14 = pd.DataFrame(B,columns=["year", "monnth", "sector", "value"])

table = pd.read_excel(r'C:\Users\jiaxi\OneDrive\Desktop\RBAC 2022\Balance\local\Italy\Italy\Reports\Gas Balance\Bilancio_GAS_2014_08.xls', sheet_name = 'Preconsuntivo Agosto 2014')
B = [["2014", "8", table.iloc[5,3], table.iloc[5,6]], \
     ["2014", "8", table.iloc[6,3], table.iloc[6,6]], \
     ["2014", "8", table.iloc[7,4], table.iloc[7,6]], \
     ["2014", "8", table.iloc[8,4], table.iloc[8,6]], \
     ["2014", "8", table.iloc[9,4], table.iloc[9,6]], \
     ["2014", "8", table.iloc[10,4], table.iloc[10,6]], \
     ["2014", "8", table.iloc[11,4], table.iloc[11,6]], \
     ["2014", "8", table.iloc[12,4], table.iloc[12,6]], \
     ["2014", "8", table.iloc[13,4], table.iloc[13,6]], \
     ["2014", "8", table.iloc[14,4], table.iloc[14,6]], \
     ["2014", "8", table.iloc[15,4], table.iloc[15,6]], \
     ["2014", "8", table.iloc[16,3], table.iloc[16,6]], \
     ["2014", "8", table.iloc[17,3], table.iloc[17,6]], \
     ["2014", "8", table.iloc[18,3], table.iloc[18,6]]]
     
Ago14 = pd.DataFrame(B,columns=["year", "monnth", "sector", "value"])

table = pd.read_excel(r'C:\Users\jiaxi\OneDrive\Desktop\RBAC 2022\Balance\local\Italy\Italy\Reports\Gas Balance\Bilancio_GAS_2014_09.xls', sheet_name = 'Preconsuntivo Settembre 2014')
B = [["2014", "9", table.iloc[5,3], table.iloc[5,6]], \
     ["2014", "9", table.iloc[6,3], table.iloc[6,6]], \
     ["2014", "9", table.iloc[7,4], table.iloc[7,6]], \
     ["2014", "9", table.iloc[8,4], table.iloc[8,6]], \
     ["2014", "9", table.iloc[9,4], table.iloc[9,6]], \
     ["2014", "9", table.iloc[10,4], table.iloc[10,6]], \
     ["2014", "9", table.iloc[11,4], table.iloc[11,6]], \
     ["2014", "9", table.iloc[12,4], table.iloc[12,6]], \
     ["2014", "9", table.iloc[13,4], table.iloc[13,6]], \
     ["2014", "9", table.iloc[14,4], table.iloc[14,6]], \
     ["2014", "9", table.iloc[15,4], table.iloc[15,6]], \
     ["2014", "9", table.iloc[16,3], table.iloc[16,6]], \
     ["2014", "9", table.iloc[17,3], table.iloc[17,6]], \
     ["2014", "9", table.iloc[18,3], table.iloc[18,6]]]
     
Set14 = pd.DataFrame(B,columns=["year", "monnth", "sector", "value"])


table = pd.read_excel(r'C:\Users\jiaxi\OneDrive\Desktop\RBAC 2022\Balance\local\Italy\Italy\Reports\Gas Balance\Bilancio_GAS_2014_10.xls', sheet_name = 'Preconsuntivo Ottobre 2014')
B = [["2014", "10", table.iloc[5,3], table.iloc[5,6]], \
     ["2014", "10", table.iloc[6,3], table.iloc[6,6]], \
     ["2014", "10", table.iloc[7,4], table.iloc[7,6]], \
     ["2014", "10", table.iloc[8,4], table.iloc[8,6]], \
     ["2014", "10", table.iloc[9,4], table.iloc[9,6]], \
     ["2014", "10", table.iloc[10,4], table.iloc[10,6]], \
     ["2014", "10", table.iloc[11,4], table.iloc[11,6]], \
     ["2014", "10", table.iloc[12,4], table.iloc[12,6]], \
     ["2014", "10", table.iloc[13,4], table.iloc[13,6]], \
     ["2014", "10", table.iloc[14,4], table.iloc[14,6]], \
     ["2014", "10", table.iloc[15,4], table.iloc[15,6]], \
     ["2014", "10", table.iloc[16,3], table.iloc[16,6]], \
     ["2014", "10", table.iloc[17,3], table.iloc[17,6]], \
     ["2014", "10", table.iloc[18,3], table.iloc[18,6]]]
     
Ott14 = pd.DataFrame(B,columns=["year", "monnth", "sector", "value"])


table = pd.read_excel(r'C:\Users\jiaxi\OneDrive\Desktop\RBAC 2022\Balance\local\Italy\Italy\Reports\Gas Balance\Bilancio_GAS_2014_11.xls', sheet_name = 'Preconsuntivo novembre 2014')
B = [["2014", "11", table.iloc[5,3], table.iloc[5,6]], \
     ["2014", "11", table.iloc[6,3], table.iloc[6,6]], \
     ["2014", "11", table.iloc[7,4], table.iloc[7,6]], \
     ["2014", "11", table.iloc[8,4], table.iloc[8,6]], \
     ["2014", "11", table.iloc[9,4], table.iloc[9,6]], \
     ["2014", "11", table.iloc[10,4], table.iloc[10,6]], \
     ["2014", "11", table.iloc[11,4], table.iloc[11,6]], \
     ["2014", "11", table.iloc[12,4], table.iloc[12,6]], \
     ["2014", "11", table.iloc[13,4], table.iloc[13,6]], \
     ["2014", "11", table.iloc[14,4], table.iloc[14,6]], \
     ["2014", "11", table.iloc[15,4], table.iloc[15,6]], \
     ["2014", "11", table.iloc[16,3], table.iloc[16,6]], \
     ["2014", "11", table.iloc[17,3], table.iloc[17,6]], \
     ["2014", "11", table.iloc[18,3], table.iloc[18,6]]]
     
Nov14 = pd.DataFrame(B,columns=["year", "monnth", "sector", "value"])

table = pd.read_excel(r'C:\Users\jiaxi\OneDrive\Desktop\RBAC 2022\Balance\local\Italy\Italy\Reports\Gas Balance\Bilancio_GAS_2014_12.xls', sheet_name = 'Preconsuntivo dicembre 2014')
B = [["2014", "12", table.iloc[5,3], table.iloc[5,6]], \
     ["2014", "12", table.iloc[6,3], table.iloc[6,6]], \
     ["2014", "12", table.iloc[7,4], table.iloc[7,6]], \
     ["2014", "12", table.iloc[8,4], table.iloc[8,6]], \
     ["2014", "12", table.iloc[9,4], table.iloc[9,6]], \
     ["2014", "12", table.iloc[10,4], table.iloc[10,6]], \
     ["2014", "12", table.iloc[11,4], table.iloc[11,6]], \
     ["2014", "12", table.iloc[12,4], table.iloc[12,6]], \
     ["2014", "12", table.iloc[13,4], table.iloc[13,6]], \
     ["2014", "12", table.iloc[14,4], table.iloc[14,6]], \
     ["2014", "12", table.iloc[15,4], table.iloc[15,6]], \
     ["2014", "12", table.iloc[16,3], table.iloc[16,6]], \
     ["2014", "12", table.iloc[17,3], table.iloc[17,6]], \
     ["2014", "12", table.iloc[18,3], table.iloc[18,6]]]
     
Dic14 = pd.DataFrame(B,columns=["year", "monnth", "sector", "value"])

##2015
table = pd.read_excel(r'C:\Users\jiaxi\OneDrive\Desktop\RBAC 2022\Balance\local\Italy\Italy\Reports\Gas Balance\Bilancio_GAS_2015_01.xlsx', sheet_name = 'Preconsuntivo Gennaio  2015')
B = [["2015", "1", table.iloc[5,3], table.iloc[5,6]], \
     ["2015", "1", table.iloc[6,3], table.iloc[6,6]], \
     ["2015", "1", table.iloc[7,4], table.iloc[7,6]], \
     ["2015", "1", table.iloc[8,4], table.iloc[8,6]], \
     ["2015", "1", table.iloc[9,4], table.iloc[9,6]], \
     ["2015", "1", table.iloc[10,4], table.iloc[10,6]], \
     ["2015", "1", table.iloc[11,4], table.iloc[11,6]], \
     ["2015", "1", table.iloc[12,4], table.iloc[12,6]], \
     ["2015", "1", table.iloc[13,4], table.iloc[13,6]], \
     ["2015", "1", table.iloc[14,4], table.iloc[14,6]], \
     ["2015", "1", table.iloc[15,4], table.iloc[15,6]], \
     ["2015", "1", table.iloc[16,3], table.iloc[16,6]], \
     ["2015", "1", table.iloc[17,3], table.iloc[17,6]], \
     ["2015", "1", table.iloc[18,3], table.iloc[18,6]]]
     
Gen15 = pd.DataFrame(B,columns=["year", "monnth", "sector", "value"])

table = pd.read_excel(r'C:\Users\jiaxi\OneDrive\Desktop\RBAC 2022\Balance\local\Italy\Italy\Reports\Gas Balance\Bilancio_GAS_2015_02.xlsx', sheet_name = 'Preconsuntivo febbraio  2015')
B = [["2015", "2", table.iloc[5,3], table.iloc[5,6]], \
     ["2015", "2", table.iloc[6,3], table.iloc[6,6]], \
     ["2015", "2", table.iloc[7,4], table.iloc[7,6]], \
     ["2015", "2", table.iloc[8,4], table.iloc[8,6]], \
     ["2015", "2", table.iloc[9,4], table.iloc[9,6]], \
     ["2015", "2", table.iloc[10,4], table.iloc[10,6]], \
     ["2015", "2", table.iloc[11,4], table.iloc[11,6]], \
     ["2015", "2", table.iloc[12,4], table.iloc[12,6]], \
     ["2015", "2", table.iloc[13,4], table.iloc[13,6]], \
     ["2015", "2", table.iloc[14,4], table.iloc[14,6]], \
     ["2015", "2", table.iloc[15,4], table.iloc[15,6]], \
     ["2015", "2", table.iloc[16,3], table.iloc[16,6]], \
     ["2015", "2", table.iloc[17,3], table.iloc[17,6]], \
     ["2015", "2", table.iloc[18,3], table.iloc[18,6]]]
     
Feb15 = pd.DataFrame(B,columns=["year", "monnth", "sector", "value"])

table = pd.read_excel(r'C:\Users\jiaxi\OneDrive\Desktop\RBAC 2022\Balance\local\Italy\Italy\Reports\Gas Balance\Bilancio_GAS_2015_03.xlsx', sheet_name = 'Preconsuntivo marzo  2015')
B = [["2015", "3", table.iloc[5,3], table.iloc[5,6]], \
     ["2015", "3", table.iloc[6,3], table.iloc[6,6]], \
     ["2015", "3", table.iloc[7,4], table.iloc[7,6]], \
     ["2015", "3", table.iloc[8,4], table.iloc[8,6]], \
     ["2015", "3", table.iloc[9,4], table.iloc[9,6]], \
     ["2015", "3", table.iloc[10,4], table.iloc[10,6]], \
     ["2015", "3", table.iloc[11,4], table.iloc[11,6]], \
     ["2015", "3", table.iloc[12,4], table.iloc[12,6]], \
     ["2015", "3", table.iloc[13,4], table.iloc[13,6]], \
     ["2015", "3", table.iloc[14,4], table.iloc[14,6]], \
     ["2015", "3", table.iloc[15,4], table.iloc[15,6]], \
     ["2015", "3", table.iloc[16,3], table.iloc[16,6]], \
     ["2015", "3", table.iloc[17,3], table.iloc[17,6]], \
     ["2015", "3", table.iloc[18,3], table.iloc[18,6]]]
     
Mar15 = pd.DataFrame(B,columns=["year", "monnth", "sector", "value"])

table = pd.read_excel(r'C:\Users\jiaxi\OneDrive\Desktop\RBAC 2022\Balance\local\Italy\Italy\Reports\Gas Balance\Bilancio_GAS_2015_04.xlsx', sheet_name = 'Preconsuntivo aprile  2015')
B = [["2015", "4", table.iloc[5,3], table.iloc[5,6]], \
     ["2015", "4", table.iloc[6,3], table.iloc[6,6]], \
     ["2015", "4", table.iloc[7,4], table.iloc[7,6]], \
     ["2015", "4", table.iloc[8,4], table.iloc[8,6]], \
     ["2015", "4", table.iloc[9,4], table.iloc[9,6]], \
     ["2015", "4", table.iloc[10,4], table.iloc[10,6]], \
     ["2015", "4", table.iloc[11,4], table.iloc[11,6]], \
     ["2015", "4", table.iloc[12,4], table.iloc[12,6]], \
     ["2015", "4", table.iloc[13,4], table.iloc[13,6]], \
     ["2015", "4", table.iloc[14,4], table.iloc[14,6]], \
     ["2015", "4", table.iloc[15,4], table.iloc[15,6]], \
     ["2015", "4", table.iloc[16,3], table.iloc[16,6]], \
     ["2015", "4", table.iloc[17,3], table.iloc[17,6]], \
     ["2015", "4", table.iloc[18,3], table.iloc[18,6]]]
     
Apr15 = pd.DataFrame(B,columns=["year", "monnth", "sector", "value"])

table = pd.read_excel(r'C:\Users\jiaxi\OneDrive\Desktop\RBAC 2022\Balance\local\Italy\Italy\Reports\Gas Balance\Bilancio_GAS_2015_05.xlsx', sheet_name = 'Preconsuntivo maggio  2015')
B = [["2015", "5", table.iloc[5,3], table.iloc[5,6]], \
     ["2015", "5", table.iloc[6,3], table.iloc[6,6]], \
     ["2015", "5", table.iloc[7,4], table.iloc[7,6]], \
     ["2015", "5", table.iloc[8,4], table.iloc[8,6]], \
     ["2015", "5", table.iloc[9,4], table.iloc[9,6]], \
     ["2015", "5", table.iloc[10,4], table.iloc[10,6]], \
     ["2015", "5", table.iloc[11,4], table.iloc[11,6]], \
     ["2015", "5", table.iloc[12,4], table.iloc[12,6]], \
     ["2015", "5", table.iloc[13,4], table.iloc[13,6]], \
     ["2015", "5", table.iloc[14,4], table.iloc[14,6]], \
     ["2015", "5", table.iloc[15,4], table.iloc[15,6]], \
     ["2015", "5", table.iloc[16,3], table.iloc[16,6]], \
     ["2015", "5", table.iloc[17,3], table.iloc[17,6]], \
     ["2015", "5", table.iloc[18,3], table.iloc[18,6]]]
     
Mag15 = pd.DataFrame(B,columns=["year", "monnth", "sector", "value"])

table = pd.read_excel(r'C:\Users\jiaxi\OneDrive\Desktop\RBAC 2022\Balance\local\Italy\Italy\Reports\Gas Balance\Bilancio_GAS_2015_06.xlsx', sheet_name = 'Preconsuntivo giugno  2015')
B = [["2015", "6", table.iloc[5,3], table.iloc[5,6]], \
     ["2015", "6", table.iloc[6,3], table.iloc[6,6]], \
     ["2015", "6", table.iloc[7,4], table.iloc[7,6]], \
     ["2015", "6", table.iloc[8,4], table.iloc[8,6]], \
     ["2015", "6", table.iloc[9,4], table.iloc[9,6]], \
     ["2015", "6", table.iloc[10,4], table.iloc[10,6]], \
     ["2015", "6", table.iloc[11,4], table.iloc[11,6]], \
     ["2015", "6", table.iloc[12,4], table.iloc[12,6]], \
     ["2015", "6", table.iloc[13,4], table.iloc[13,6]], \
     ["2015", "6", table.iloc[14,4], table.iloc[14,6]], \
     ["2015", "6", table.iloc[15,4], table.iloc[15,6]], \
     ["2015", "6", table.iloc[16,3], table.iloc[16,6]], \
     ["2015", "6", table.iloc[17,3], table.iloc[17,6]], \
     ["2015", "6", table.iloc[18,3], table.iloc[18,6]]]
     
Giu15 = pd.DataFrame(B,columns=["year", "monnth", "sector", "value"])


table = pd.read_excel(r'C:\Users\jiaxi\OneDrive\Desktop\RBAC 2022\Balance\local\Italy\Italy\Reports\Gas Balance\Bilancio_GAS_2015_07.xlsx', sheet_name = 'Preconsuntivo luglio  2015')
B = [["2015", "7", table.iloc[5,3], table.iloc[5,6]], \
     ["2015", "7", table.iloc[6,3], table.iloc[6,6]], \
     ["2015", "7", table.iloc[7,4], table.iloc[7,6]], \
     ["2015", "7", table.iloc[8,4], table.iloc[8,6]], \
     ["2015", "7", table.iloc[9,4], table.iloc[9,6]], \
     ["2015", "7", table.iloc[10,4], table.iloc[10,6]], \
     ["2015", "7", table.iloc[11,4], table.iloc[11,6]], \
     ["2015", "7", table.iloc[12,4], table.iloc[12,6]], \
     ["2015", "7", table.iloc[13,4], table.iloc[13,6]], \
     ["2015", "7", table.iloc[14,4], table.iloc[14,6]], \
     ["2015", "7", table.iloc[15,4], table.iloc[15,6]], \
     ["2015", "7", table.iloc[16,3], table.iloc[16,6]], \
     ["2015", "7", table.iloc[17,3], table.iloc[17,6]], \
     ["2015", "7", table.iloc[18,3], table.iloc[18,6]]]
     
Lug15 = pd.DataFrame(B,columns=["year", "monnth", "sector", "value"])

table = pd.read_excel(r'C:\Users\jiaxi\OneDrive\Desktop\RBAC 2022\Balance\local\Italy\Italy\Reports\Gas Balance\Bilancio_GAS_2015_08.xlsx', sheet_name = 'Preconsuntivo agosto  2015')
B = [["2015", "8", table.iloc[5,3], table.iloc[5,6]], \
     ["2015", "8", table.iloc[6,3], table.iloc[6,6]], \
     ["2015", "8", table.iloc[7,4], table.iloc[7,6]], \
     ["2015", "8", table.iloc[8,4], table.iloc[8,6]], \
     ["2015", "8", table.iloc[9,4], table.iloc[9,6]], \
     ["2015", "8", table.iloc[10,4], table.iloc[10,6]], \
     ["2015", "8", table.iloc[11,4], table.iloc[11,6]], \
     ["2015", "8", table.iloc[12,4], table.iloc[12,6]], \
     ["2015", "8", table.iloc[13,4], table.iloc[13,6]], \
     ["2015", "8", table.iloc[14,4], table.iloc[14,6]], \
     ["2015", "8", table.iloc[15,4], table.iloc[15,6]], \
     ["2015", "8", table.iloc[16,3], table.iloc[16,6]], \
     ["2015", "8", table.iloc[17,3], table.iloc[17,6]], \
     ["2015", "8", table.iloc[18,3], table.iloc[18,6]]]
     
Ago15 = pd.DataFrame(B,columns=["year", "monnth", "sector", "value"])

table = pd.read_excel(r'C:\Users\jiaxi\OneDrive\Desktop\RBAC 2022\Balance\local\Italy\Italy\Reports\Gas Balance\Bilancio_GAS_2015_09.xlsx', sheet_name = 'Preconsuntivo settembre 2015')
B = [["2015", "9", table.iloc[5,3], table.iloc[5,6]], \
     ["2015", "9", table.iloc[6,3], table.iloc[6,6]], \
     ["2015", "9", table.iloc[7,4], table.iloc[7,6]], \
     ["2015", "9", table.iloc[8,4], table.iloc[8,6]], \
     ["2015", "9", table.iloc[9,4], table.iloc[9,6]], \
     ["2015", "9", table.iloc[10,4], table.iloc[10,6]], \
     ["2015", "9", table.iloc[11,4], table.iloc[11,6]], \
     ["2015", "9", table.iloc[12,4], table.iloc[12,6]], \
     ["2015", "9", table.iloc[13,4], table.iloc[13,6]], \
     ["2015", "9", table.iloc[14,4], table.iloc[14,6]], \
     ["2015", "9", table.iloc[15,4], table.iloc[15,6]], \
     ["2015", "9", table.iloc[16,3], table.iloc[16,6]], \
     ["2015", "9", table.iloc[17,3], table.iloc[17,6]], \
     ["2015", "9", table.iloc[18,3], table.iloc[18,6]]]
     
Set15 = pd.DataFrame(B,columns=["year", "monnth", "sector", "value"])


table = pd.read_excel(r'C:\Users\jiaxi\OneDrive\Desktop\RBAC 2022\Balance\local\Italy\Italy\Reports\Gas Balance\Bilancio_GAS_2015_10.xlsx', sheet_name = 'Preconsuntivo ottobre 2015')
B = [["2015", "10", table.iloc[5,3], table.iloc[5,6]], \
     ["2015", "10", table.iloc[6,3], table.iloc[6,6]], \
     ["2015", "10", table.iloc[7,4], table.iloc[7,6]], \
     ["2015", "10", table.iloc[8,4], table.iloc[8,6]], \
     ["2015", "10", table.iloc[9,4], table.iloc[9,6]], \
     ["2015", "10", table.iloc[10,4], table.iloc[10,6]], \
     ["2015", "10", table.iloc[11,4], table.iloc[11,6]], \
     ["2015", "10", table.iloc[12,4], table.iloc[12,6]], \
     ["2015", "10", table.iloc[13,4], table.iloc[13,6]], \
     ["2015", "10", table.iloc[14,4], table.iloc[14,6]], \
     ["2015", "10", table.iloc[15,4], table.iloc[15,6]], \
     ["2015", "10", table.iloc[16,3], table.iloc[16,6]], \
     ["2015", "10", table.iloc[17,3], table.iloc[17,6]], \
     ["2015", "10", table.iloc[18,3], table.iloc[18,6]]]
     
Ott15 = pd.DataFrame(B,columns=["year", "monnth", "sector", "value"])


table = pd.read_excel(r'C:\Users\jiaxi\OneDrive\Desktop\RBAC 2022\Balance\local\Italy\Italy\Reports\Gas Balance\Bilancio_GAS_2015_11.xlsx', sheet_name = 'Preconsuntivo novembre 2015')
B = [["2015", "11", table.iloc[5,3], table.iloc[5,6]], \
     ["2015", "11", table.iloc[6,3], table.iloc[6,6]], \
     ["2015", "11", table.iloc[7,4], table.iloc[7,6]], \
     ["2015", "11", table.iloc[8,4], table.iloc[8,6]], \
     ["2015", "11", table.iloc[9,4], table.iloc[9,6]], \
     ["2015", "11", table.iloc[10,4], table.iloc[10,6]], \
     ["2015", "11", table.iloc[11,4], table.iloc[11,6]], \
     ["2015", "11", table.iloc[12,4], table.iloc[12,6]], \
     ["2015", "11", table.iloc[13,4], table.iloc[13,6]], \
     ["2015", "11", table.iloc[14,4], table.iloc[14,6]], \
     ["2015", "11", table.iloc[15,4], table.iloc[15,6]], \
     ["2015", "11", table.iloc[16,3], table.iloc[16,6]], \
     ["2015", "11", table.iloc[17,3], table.iloc[17,6]], \
     ["2015", "11", table.iloc[18,3], table.iloc[18,6]]]
     
Nov15 = pd.DataFrame(B,columns=["year", "monnth", "sector", "value"])

table = pd.read_excel(r'C:\Users\jiaxi\OneDrive\Desktop\RBAC 2022\Balance\local\Italy\Italy\Reports\Gas Balance\Bilancio_GAS_2015_12.xlsx', sheet_name = 'Preconsuntivo dicembre 2015')
B = [["2015", "12", table.iloc[5,3], table.iloc[5,6]], \
     ["2015", "12", table.iloc[6,3], table.iloc[6,6]], \
     ["2015", "12", table.iloc[7,4], table.iloc[7,6]], \
     ["2015", "12", table.iloc[8,4], table.iloc[8,6]], \
     ["2015", "12", table.iloc[9,4], table.iloc[9,6]], \
     ["2015", "12", table.iloc[10,4], table.iloc[10,6]], \
     ["2015", "12", table.iloc[11,4], table.iloc[11,6]], \
     ["2015", "12", table.iloc[12,4], table.iloc[12,6]], \
     ["2015", "12", table.iloc[13,4], table.iloc[13,6]], \
     ["2015", "12", table.iloc[14,4], table.iloc[14,6]], \
     ["2015", "12", table.iloc[15,4], table.iloc[15,6]], \
     ["2015", "12", table.iloc[16,3], table.iloc[16,6]], \
     ["2015", "12", table.iloc[17,3], table.iloc[17,6]], \
     ["2015", "12", table.iloc[18,3], table.iloc[18,6]]]
     
Dic15 = pd.DataFrame(B,columns=["year", "monnth", "sector", "value"])


##2016
table = pd.read_excel(r'C:\Users\jiaxi\OneDrive\Desktop\RBAC 2022\Balance\local\Italy\Italy\Reports\Gas Balance\Bilancio_GAS_2016_01.xlsx', sheet_name = 'Preconsuntivo Gennaio  2016')
B = [["2016", "1", table.iloc[5,3], table.iloc[5,6]], \
     ["2016", "1", table.iloc[6,3], table.iloc[6,6]], \
     ["2016", "1", table.iloc[7,4], table.iloc[7,6]], \
     ["2016", "1", table.iloc[8,4], table.iloc[8,6]], \
     ["2016", "1", table.iloc[9,4], table.iloc[9,6]], \
     ["2016", "1", table.iloc[10,4], table.iloc[10,6]], \
     ["2016", "1", table.iloc[11,4], table.iloc[11,6]], \
     ["2016", "1", table.iloc[12,4], table.iloc[12,6]], \
     ["2016", "1", table.iloc[13,4], table.iloc[13,6]], \
     ["2016", "1", table.iloc[14,4], table.iloc[14,6]], \
     ["2016", "1", table.iloc[15,4], table.iloc[15,6]], \
     ["2016", "1", table.iloc[16,3], table.iloc[16,6]], \
     ["2016", "1", table.iloc[17,3], table.iloc[17,6]], \
     ["2016", "1", table.iloc[18,3], table.iloc[18,6]]]
     
Gen16 = pd.DataFrame(B,columns=["year", "monnth", "sector", "value"])

table = pd.read_excel(r'C:\Users\jiaxi\OneDrive\Desktop\RBAC 2022\Balance\local\Italy\Italy\Reports\Gas Balance\Bilancio_GAS_2016_02.xlsx', sheet_name = 'Preconsuntivo Febbraio  2016')
B = [["2016", "2", table.iloc[5,3], table.iloc[5,6]], \
     ["2016", "2", table.iloc[6,3], table.iloc[6,6]], \
     ["2016", "2", table.iloc[7,4], table.iloc[7,6]], \
     ["2016", "2", table.iloc[8,4], table.iloc[8,6]], \
     ["2016", "2", table.iloc[9,4], table.iloc[9,6]], \
     ["2016", "2", table.iloc[10,4], table.iloc[10,6]], \
     ["2016", "2", table.iloc[11,4], table.iloc[11,6]], \
     ["2016", "2", table.iloc[12,4], table.iloc[12,6]], \
     ["2016", "2", table.iloc[13,4], table.iloc[13,6]], \
     ["2016", "2", table.iloc[14,4], table.iloc[14,6]], \
     ["2016", "2", table.iloc[15,4], table.iloc[15,6]], \
     ["2016", "2", table.iloc[16,3], table.iloc[16,6]], \
     ["2016", "2", table.iloc[17,3], table.iloc[17,6]], \
     ["2016", "2", table.iloc[18,3], table.iloc[18,6]]]
     
Feb16 = pd.DataFrame(B,columns=["year", "monnth", "sector", "value"])

table = pd.read_excel(r'C:\Users\jiaxi\OneDrive\Desktop\RBAC 2022\Balance\local\Italy\Italy\Reports\Gas Balance\Bilancio_GAS_2016_03.xlsx', sheet_name = 'Preconsuntivo Marzo  2016')
B = [["2016", "3", table.iloc[5,3], table.iloc[5,6]], \
     ["2016", "3", table.iloc[6,3], table.iloc[6,6]], \
     ["2016", "3", table.iloc[7,4], table.iloc[7,6]], \
     ["2016", "3", table.iloc[8,4], table.iloc[8,6]], \
     ["2016", "3", table.iloc[9,4], table.iloc[9,6]], \
     ["2016", "3", table.iloc[10,4], table.iloc[10,6]], \
     ["2016", "3", table.iloc[11,4], table.iloc[11,6]], \
     ["2016", "3", table.iloc[12,4], table.iloc[12,6]], \
     ["2016", "3", table.iloc[13,4], table.iloc[13,6]], \
     ["2016", "3", table.iloc[14,4], table.iloc[14,6]], \
     ["2016", "3", table.iloc[15,4], table.iloc[15,6]], \
     ["2016", "3", table.iloc[16,3], table.iloc[16,6]], \
     ["2016", "3", table.iloc[17,3], table.iloc[17,6]], \
     ["2016", "3", table.iloc[18,3], table.iloc[18,6]]]
     
Mar16 = pd.DataFrame(B,columns=["year", "monnth", "sector", "value"])

table = pd.read_excel(r'C:\Users\jiaxi\OneDrive\Desktop\RBAC 2022\Balance\local\Italy\Italy\Reports\Gas Balance\Bilancio_GAS_2016_04.xlsx', sheet_name = 'Preconsuntivo Aprile  2016')
B = [["2016", "4", table.iloc[5,3], table.iloc[5,6]], \
     ["2016", "4", table.iloc[6,3], table.iloc[6,6]], \
     ["2016", "4", table.iloc[7,4], table.iloc[7,6]], \
     ["2016", "4", table.iloc[8,4], table.iloc[8,6]], \
     ["2016", "4", table.iloc[9,4], table.iloc[9,6]], \
     ["2016", "4", table.iloc[10,4], table.iloc[10,6]], \
     ["2016", "4", table.iloc[11,4], table.iloc[11,6]], \
     ["2016", "4", table.iloc[12,4], table.iloc[12,6]], \
     ["2016", "4", table.iloc[13,4], table.iloc[13,6]], \
     ["2016", "4", table.iloc[14,4], table.iloc[14,6]], \
     ["2016", "4", table.iloc[15,4], table.iloc[15,6]], \
     ["2016", "4", table.iloc[16,3], table.iloc[16,6]], \
     ["2016", "4", table.iloc[17,3], table.iloc[17,6]], \
     ["2016", "4", table.iloc[18,3], table.iloc[18,6]]]
     
Apr16 = pd.DataFrame(B,columns=["year", "monnth", "sector", "value"])

table = pd.read_excel(r'C:\Users\jiaxi\OneDrive\Desktop\RBAC 2022\Balance\local\Italy\Italy\Reports\Gas Balance\Bilancio_GAS_2016_05.xlsx', sheet_name = 'Preconsuntivo Maggio  2016')
B = [["2016", "5", table.iloc[5,3], table.iloc[5,6]], \
     ["2016", "5", table.iloc[6,3], table.iloc[6,6]], \
     ["2016", "5", table.iloc[7,4], table.iloc[7,6]], \
     ["2016", "5", table.iloc[8,4], table.iloc[8,6]], \
     ["2016", "5", table.iloc[9,4], table.iloc[9,6]], \
     ["2016", "5", table.iloc[10,4], table.iloc[10,6]], \
     ["2016", "5", table.iloc[11,4], table.iloc[11,6]], \
     ["2016", "5", table.iloc[12,4], table.iloc[12,6]], \
     ["2016", "5", table.iloc[13,4], table.iloc[13,6]], \
     ["2016", "5", table.iloc[14,4], table.iloc[14,6]], \
     ["2016", "5", table.iloc[15,4], table.iloc[15,6]], \
     ["2016", "5", table.iloc[16,3], table.iloc[16,6]], \
     ["2016", "5", table.iloc[17,3], table.iloc[17,6]], \
     ["2016", "5", table.iloc[18,3], table.iloc[18,6]]]
     
Mag16 = pd.DataFrame(B,columns=["year", "monnth", "sector", "value"])

table = pd.read_excel(r'C:\Users\jiaxi\OneDrive\Desktop\RBAC 2022\Balance\local\Italy\Italy\Reports\Gas Balance\Bilancio_GAS_2016_06.xlsx', sheet_name = 'Preconsuntivo Giugno  2016')
B = [["2016", "6", table.iloc[5,3], table.iloc[5,6]], \
     ["2016", "6", table.iloc[6,3], table.iloc[6,6]], \
     ["2016", "6", table.iloc[7,4], table.iloc[7,6]], \
     ["2016", "6", table.iloc[8,4], table.iloc[8,6]], \
     ["2016", "6", table.iloc[9,4], table.iloc[9,6]], \
     ["2016", "6", table.iloc[10,4], table.iloc[10,6]], \
     ["2016", "6", table.iloc[11,4], table.iloc[11,6]], \
     ["2016", "6", table.iloc[12,4], table.iloc[12,6]], \
     ["2016", "6", table.iloc[13,4], table.iloc[13,6]], \
     ["2016", "6", table.iloc[14,4], table.iloc[14,6]], \
     ["2016", "6", table.iloc[15,4], table.iloc[15,6]], \
     ["2016", "6", table.iloc[16,3], table.iloc[16,6]], \
     ["2016", "6", table.iloc[17,3], table.iloc[17,6]], \
     ["2016", "6", table.iloc[18,3], table.iloc[18,6]]]
     
Giu16 = pd.DataFrame(B,columns=["year", "monnth", "sector", "value"])


table = pd.read_excel(r'C:\Users\jiaxi\OneDrive\Desktop\RBAC 2022\Balance\local\Italy\Italy\Reports\Gas Balance\Bilancio_GAS_2016_07.xlsx', sheet_name = 'Preconsuntivo Luglio  2016')
B = [["2016", "7", table.iloc[5,3], table.iloc[5,6]], \
     ["2016", "7", table.iloc[6,3], table.iloc[6,6]], \
     ["2016", "7", table.iloc[7,4], table.iloc[7,6]], \
     ["2016", "7", table.iloc[8,4], table.iloc[8,6]], \
     ["2016", "7", table.iloc[9,4], table.iloc[9,6]], \
     ["2016", "7", table.iloc[10,4], table.iloc[10,6]], \
     ["2016", "7", table.iloc[11,4], table.iloc[11,6]], \
     ["2016", "7", table.iloc[12,4], table.iloc[12,6]], \
     ["2016", "7", table.iloc[13,4], table.iloc[13,6]], \
     ["2016", "7", table.iloc[14,4], table.iloc[14,6]], \
     ["2016", "7", table.iloc[15,4], table.iloc[15,6]], \
     ["2016", "7", table.iloc[16,3], table.iloc[16,6]], \
     ["2016", "7", table.iloc[17,3], table.iloc[17,6]], \
     ["2016", "7", table.iloc[18,3], table.iloc[18,6]]]
     
Lug16 = pd.DataFrame(B,columns=["year", "monnth", "sector", "value"])

table = pd.read_excel(r'C:\Users\jiaxi\OneDrive\Desktop\RBAC 2022\Balance\local\Italy\Italy\Reports\Gas Balance\Bilancio_GAS_2016_08.xlsx', sheet_name = 'Preconsuntivo Agosto  2016')
B = [["2016", "8", table.iloc[5,3], table.iloc[5,6]], \
     ["2016", "8", table.iloc[6,3], table.iloc[6,6]], \
     ["2016", "8", table.iloc[7,4], table.iloc[7,6]], \
     ["2016", "8", table.iloc[8,4], table.iloc[8,6]], \
     ["2016", "8", table.iloc[9,4], table.iloc[9,6]], \
     ["2016", "8", table.iloc[10,4], table.iloc[10,6]], \
     ["2016", "8", table.iloc[11,4], table.iloc[11,6]], \
     ["2016", "8", table.iloc[12,4], table.iloc[12,6]], \
     ["2016", "8", table.iloc[13,4], table.iloc[13,6]], \
     ["2016", "8", table.iloc[14,4], table.iloc[14,6]], \
     ["2016", "8", table.iloc[15,4], table.iloc[15,6]], \
     ["2016", "8", table.iloc[16,3], table.iloc[16,6]], \
     ["2016", "8", table.iloc[17,3], table.iloc[17,6]], \
     ["2016", "8", table.iloc[18,3], table.iloc[18,6]]]
     
Ago16 = pd.DataFrame(B,columns=["year", "monnth", "sector", "value"])

table = pd.read_excel(r'C:\Users\jiaxi\OneDrive\Desktop\RBAC 2022\Balance\local\Italy\Italy\Reports\Gas Balance\Bilancio_GAS_2016_09.xlsx', sheet_name = 'Preconsuntivo Settembre  2016')
B = [["2016", "9", table.iloc[5,3], table.iloc[5,6]], \
     ["2016", "9", table.iloc[6,3], table.iloc[6,6]], \
     ["2016", "9", table.iloc[7,4], table.iloc[7,6]], \
     ["2016", "9", table.iloc[8,4], table.iloc[8,6]], \
     ["2016", "9", table.iloc[9,4], table.iloc[9,6]], \
     ["2016", "9", table.iloc[10,4], table.iloc[10,6]], \
     ["2016", "9", table.iloc[11,4], table.iloc[11,6]], \
     ["2016", "9", table.iloc[12,4], table.iloc[12,6]], \
     ["2016", "9", table.iloc[13,4], table.iloc[13,6]], \
     ["2016", "9", table.iloc[14,4], table.iloc[14,6]], \
     ["2016", "9", table.iloc[15,4], table.iloc[15,6]], \
     ["2016", "9", table.iloc[16,3], table.iloc[16,6]], \
     ["2016", "9", table.iloc[17,3], table.iloc[17,6]], \
     ["2016", "9", table.iloc[18,3], table.iloc[18,6]]]
     
Set16 = pd.DataFrame(B,columns=["year", "monnth", "sector", "value"])


table = pd.read_excel(r'C:\Users\jiaxi\OneDrive\Desktop\RBAC 2022\Balance\local\Italy\Italy\Reports\Gas Balance\Bilancio_GAS_2016_10.xlsx', sheet_name = 'Preconsuntivo Ottobre  2016')
B = [["2016", "10", table.iloc[5,3], table.iloc[5,6]], \
     ["2016", "10", table.iloc[6,3], table.iloc[6,6]], \
     ["2016", "10", table.iloc[7,4], table.iloc[7,6]], \
     ["2016", "10", table.iloc[8,4], table.iloc[8,6]], \
     ["2016", "10", table.iloc[9,4], table.iloc[9,6]], \
     ["2016", "10", table.iloc[10,4], table.iloc[10,6]], \
     ["2016", "10", table.iloc[11,4], table.iloc[11,6]], \
     ["2016", "10", table.iloc[12,4], table.iloc[12,6]], \
     ["2016", "10", table.iloc[13,4], table.iloc[13,6]], \
     ["2016", "10", table.iloc[14,4], table.iloc[14,6]], \
     ["2016", "10", table.iloc[15,4], table.iloc[15,6]], \
     ["2016", "10", table.iloc[16,3], table.iloc[16,6]], \
     ["2016", "10", table.iloc[17,3], table.iloc[17,6]], \
     ["2016", "10", table.iloc[18,3], table.iloc[18,6]]]
     
Ott16 = pd.DataFrame(B,columns=["year", "monnth", "sector", "value"])


table = pd.read_excel(r'C:\Users\jiaxi\OneDrive\Desktop\RBAC 2022\Balance\local\Italy\Italy\Reports\Gas Balance\Bilancio_GAS_2016_11.xlsx', sheet_name = 'Preconsuntivo Novembre  2016')
B = [["2016", "11", table.iloc[5,3], table.iloc[5,6]], \
     ["2016", "11", table.iloc[6,3], table.iloc[6,6]], \
     ["2016", "11", table.iloc[7,4], table.iloc[7,6]], \
     ["2016", "11", table.iloc[8,4], table.iloc[8,6]], \
     ["2016", "11", table.iloc[9,4], table.iloc[9,6]], \
     ["2016", "11", table.iloc[10,4], table.iloc[10,6]], \
     ["2016", "11", table.iloc[11,4], table.iloc[11,6]], \
     ["2016", "11", table.iloc[12,4], table.iloc[12,6]], \
     ["2016", "11", table.iloc[13,4], table.iloc[13,6]], \
     ["2016", "11", table.iloc[14,4], table.iloc[14,6]], \
     ["2016", "11", table.iloc[15,4], table.iloc[15,6]], \
     ["2016", "11", table.iloc[16,3], table.iloc[16,6]], \
     ["2016", "11", table.iloc[17,3], table.iloc[17,6]], \
     ["2016", "11", table.iloc[18,3], table.iloc[18,6]]]
     
Nov16 = pd.DataFrame(B,columns=["year", "monnth", "sector", "value"])

table = pd.read_excel(r'C:\Users\jiaxi\OneDrive\Desktop\RBAC 2022\Balance\local\Italy\Italy\Reports\Gas Balance\Bilancio_GAS_2016_12.xlsx', sheet_name = 'Preconsuntivo Dicembre  2016')
B = [["2016", "12", table.iloc[5,3], table.iloc[5,6]], \
     ["2016", "12", table.iloc[6,3], table.iloc[6,6]], \
     ["2016", "12", table.iloc[7,4], table.iloc[7,6]], \
     ["2016", "12", table.iloc[8,4], table.iloc[8,6]], \
     ["2016", "12", table.iloc[9,4], table.iloc[9,6]], \
     ["2016", "12", table.iloc[10,4], table.iloc[10,6]], \
     ["2016", "12", table.iloc[11,4], table.iloc[11,6]], \
     ["2016", "12", table.iloc[12,4], table.iloc[12,6]], \
     ["2016", "12", table.iloc[13,4], table.iloc[13,6]], \
     ["2016", "12", table.iloc[14,4], table.iloc[14,6]], \
     ["2016", "12", table.iloc[15,4], table.iloc[15,6]], \
     ["2016", "12", table.iloc[16,3], table.iloc[16,6]], \
     ["2016", "12", table.iloc[17,3], table.iloc[17,6]], \
     ["2016", "12", table.iloc[18,3], table.iloc[18,6]]]
     
Dic16 = pd.DataFrame(B,columns=["year", "monnth", "sector", "value"])

##2017
table = pd.read_excel(r'C:\Users\jiaxi\OneDrive\Desktop\RBAC 2022\Balance\local\Italy\Italy\Reports\Gas Balance\Bilancio_GAS_2017_01.xlsx', sheet_name = 'Preconsuntivo Gennaio  2017')
B = [["2017", "1", table.iloc[5,3], table.iloc[5,6]], \
     ["2017", "1", table.iloc[6,3], table.iloc[6,6]], \
     ["2017", "1", table.iloc[7,4], table.iloc[7,6]], \
     ["2017", "1", table.iloc[8,4], table.iloc[8,6]], \
     ["2017", "1", table.iloc[9,4], table.iloc[9,6]], \
     ["2017", "1", table.iloc[10,4], table.iloc[10,6]], \
     ["2017", "1", table.iloc[11,4], table.iloc[11,6]], \
     ["2017", "1", table.iloc[12,4], table.iloc[12,6]], \
     ["2017", "1", table.iloc[13,4], table.iloc[13,6]], \
     ["2017", "1", table.iloc[14,4], table.iloc[14,6]], \
     ["2017", "1", table.iloc[15,4], table.iloc[15,6]], \
     ["2017", "1", table.iloc[16,3], table.iloc[16,6]], \
     ["2017", "1", table.iloc[17,3], table.iloc[17,6]], \
     ["2017", "1", table.iloc[18,3], table.iloc[18,6]]]
     
Gen17 = pd.DataFrame(B,columns=["year", "monnth", "sector", "value"])

table = pd.read_excel(r'C:\Users\jiaxi\OneDrive\Desktop\RBAC 2022\Balance\local\Italy\Italy\Reports\Gas Balance\Bilancio_GAS_2017_02.xlsx', sheet_name = 'Preconsuntivo Febbraio  2017')
B = [["2017", "2", table.iloc[5,3], table.iloc[5,6]], \
     ["2017", "2", table.iloc[6,3], table.iloc[6,6]], \
     ["2017", "2", table.iloc[7,4], table.iloc[7,6]], \
     ["2017", "2", table.iloc[8,4], table.iloc[8,6]], \
     ["2017", "2", table.iloc[9,4], table.iloc[9,6]], \
     ["2017", "2", table.iloc[10,4], table.iloc[10,6]], \
     ["2017", "2", table.iloc[11,4], table.iloc[11,6]], \
     ["2017", "2", table.iloc[12,4], table.iloc[12,6]], \
     ["2017", "2", table.iloc[13,4], table.iloc[13,6]], \
     ["2017", "2", table.iloc[14,4], table.iloc[14,6]], \
     ["2017", "2", table.iloc[15,4], table.iloc[15,6]], \
     ["2017", "2", table.iloc[16,3], table.iloc[16,6]], \
     ["2017", "2", table.iloc[17,3], table.iloc[17,6]], \
     ["2017", "2", table.iloc[18,3], table.iloc[18,6]]]
     
Feb17 = pd.DataFrame(B,columns=["year", "monnth", "sector", "value"])

table = pd.read_excel(r'C:\Users\jiaxi\OneDrive\Desktop\RBAC 2022\Balance\local\Italy\Italy\Reports\Gas Balance\Bilancio_GAS_2017_03.xlsx', sheet_name = 'Preconsuntivo Marzo  2017')
B = [["2017", "3", table.iloc[5,3], table.iloc[5,6]], \
     ["2017", "3", table.iloc[6,3], table.iloc[6,6]], \
     ["2017", "3", table.iloc[7,4], table.iloc[7,6]], \
     ["2017", "3", table.iloc[8,4], table.iloc[8,6]], \
     ["2017", "3", table.iloc[9,4], table.iloc[9,6]], \
     ["2017", "3", table.iloc[10,4], table.iloc[10,6]], \
     ["2017", "3", table.iloc[11,4], table.iloc[11,6]], \
     ["2017", "3", table.iloc[12,4], table.iloc[12,6]], \
     ["2017", "3", table.iloc[13,4], table.iloc[13,6]], \
     ["2017", "3", table.iloc[14,4], table.iloc[14,6]], \
     ["2017", "3", table.iloc[15,4], table.iloc[15,6]], \
     ["2017", "3", table.iloc[16,3], table.iloc[16,6]], \
     ["2017", "3", table.iloc[17,3], table.iloc[17,6]], \
     ["2017", "3", table.iloc[18,3], table.iloc[18,6]]]
     
Mar17 = pd.DataFrame(B,columns=["year", "monnth", "sector", "value"])

table = pd.read_excel(r'C:\Users\jiaxi\OneDrive\Desktop\RBAC 2022\Balance\local\Italy\Italy\Reports\Gas Balance\Bilancio_GAS_2017_04.xlsx', sheet_name = 'Preconsuntivo Aprile  2017')
B = [["2017", "4", table.iloc[5,3], table.iloc[5,6]], \
     ["2017", "4", table.iloc[6,3], table.iloc[6,6]], \
     ["2017", "4", table.iloc[7,4], table.iloc[7,6]], \
     ["2017", "4", table.iloc[8,4], table.iloc[8,6]], \
     ["2017", "4", table.iloc[9,4], table.iloc[9,6]], \
     ["2017", "4", table.iloc[10,4], table.iloc[10,6]], \
     ["2017", "4", table.iloc[11,4], table.iloc[11,6]], \
     ["2017", "4", table.iloc[12,4], table.iloc[12,6]], \
     ["2017", "4", table.iloc[13,4], table.iloc[13,6]], \
     ["2017", "4", table.iloc[14,4], table.iloc[14,6]], \
     ["2017", "4", table.iloc[15,4], table.iloc[15,6]], \
     ["2017", "4", table.iloc[16,3], table.iloc[16,6]], \
     ["2017", "4", table.iloc[17,3], table.iloc[17,6]], \
     ["2017", "4", table.iloc[18,3], table.iloc[18,6]]]
     
Apr17 = pd.DataFrame(B,columns=["year", "monnth", "sector", "value"])

table = pd.read_excel(r'C:\Users\jiaxi\OneDrive\Desktop\RBAC 2022\Balance\local\Italy\Italy\Reports\Gas Balance\Bilancio_GAS_2017_05.xlsx', sheet_name = 'Preconsuntivo Maggio  2017')
B = [["2017", "5", table.iloc[5,3], table.iloc[5,6]], \
     ["2017", "5", table.iloc[6,3], table.iloc[6,6]], \
     ["2017", "5", table.iloc[7,4], table.iloc[7,6]], \
     ["2017", "5", table.iloc[8,4], table.iloc[8,6]], \
     ["2017", "5", table.iloc[9,4], table.iloc[9,6]], \
     ["2017", "5", table.iloc[10,4], table.iloc[10,6]], \
     ["2017", "5", table.iloc[11,4], table.iloc[11,6]], \
     ["2017", "5", table.iloc[12,4], table.iloc[12,6]], \
     ["2017", "5", table.iloc[13,4], table.iloc[13,6]], \
     ["2017", "5", table.iloc[14,4], table.iloc[14,6]], \
     ["2017", "5", table.iloc[15,4], table.iloc[15,6]], \
     ["2017", "5", table.iloc[16,3], table.iloc[16,6]], \
     ["2017", "5", table.iloc[17,3], table.iloc[17,6]], \
     ["2017", "5", table.iloc[18,3], table.iloc[18,6]]]
     
Mag17 = pd.DataFrame(B,columns=["year", "monnth", "sector", "value"])

table = pd.read_excel(r'C:\Users\jiaxi\OneDrive\Desktop\RBAC 2022\Balance\local\Italy\Italy\Reports\Gas Balance\Bilancio_GAS_2017_06.xlsx', sheet_name = 'Preconsuntivo Giugno  2017')
B = [["2017", "6", table.iloc[5,3], table.iloc[5,6]], \
     ["2017", "6", table.iloc[6,3], table.iloc[6,6]], \
     ["2017", "6", table.iloc[7,4], table.iloc[7,6]], \
     ["2017", "6", table.iloc[8,4], table.iloc[8,6]], \
     ["2017", "6", table.iloc[9,4], table.iloc[9,6]], \
     ["2017", "6", table.iloc[10,4], table.iloc[10,6]], \
     ["2017", "6", table.iloc[11,4], table.iloc[11,6]], \
     ["2017", "6", table.iloc[12,4], table.iloc[12,6]], \
     ["2017", "6", table.iloc[13,4], table.iloc[13,6]], \
     ["2017", "6", table.iloc[14,4], table.iloc[14,6]], \
     ["2017", "6", table.iloc[15,4], table.iloc[15,6]], \
     ["2017", "6", table.iloc[16,3], table.iloc[16,6]], \
     ["2017", "6", table.iloc[17,3], table.iloc[17,6]], \
     ["2017", "6", table.iloc[18,3], table.iloc[18,6]]]
     
Giu17 = pd.DataFrame(B,columns=["year", "monnth", "sector", "value"])


table = pd.read_excel(r'C:\Users\jiaxi\OneDrive\Desktop\RBAC 2022\Balance\local\Italy\Italy\Reports\Gas Balance\Bilancio_GAS_2017_07.xlsx', sheet_name = 'Preconsuntivo Luglio  2017')
B = [["2017", "7", table.iloc[5,3], table.iloc[5,6]], \
     ["2017", "7", table.iloc[6,3], table.iloc[6,6]], \
     ["2017", "7", table.iloc[7,4], table.iloc[7,6]], \
     ["2017", "7", table.iloc[8,4], table.iloc[8,6]], \
     ["2017", "7", table.iloc[9,4], table.iloc[9,6]], \
     ["2017", "7", table.iloc[10,4], table.iloc[10,6]], \
     ["2017", "7", table.iloc[11,4], table.iloc[11,6]], \
     ["2017", "7", table.iloc[12,4], table.iloc[12,6]], \
     ["2017", "7", table.iloc[13,4], table.iloc[13,6]], \
     ["2017", "7", table.iloc[14,4], table.iloc[14,6]], \
     ["2017", "7", table.iloc[15,4], table.iloc[15,6]], \
     ["2017", "7", table.iloc[16,3], table.iloc[16,6]], \
     ["2017", "7", table.iloc[17,3], table.iloc[17,6]], \
     ["2017", "7", table.iloc[18,3], table.iloc[18,6]]]
     
Lug17 = pd.DataFrame(B,columns=["year", "monnth", "sector", "value"])

table = pd.read_excel(r'C:\Users\jiaxi\OneDrive\Desktop\RBAC 2022\Balance\local\Italy\Italy\Reports\Gas Balance\Bilancio_GAS_2017_08.xlsx', sheet_name = 'Preconsuntivo Agosto  2017')
B = [["2017", "8", table.iloc[5,3], table.iloc[5,6]], \
     ["2017", "8", table.iloc[6,3], table.iloc[6,6]], \
     ["2017", "8", table.iloc[7,4], table.iloc[7,6]], \
     ["2017", "8", table.iloc[8,4], table.iloc[8,6]], \
     ["2017", "8", table.iloc[9,4], table.iloc[9,6]], \
     ["2017", "8", table.iloc[10,4], table.iloc[10,6]], \
     ["2017", "8", table.iloc[11,4], table.iloc[11,6]], \
     ["2017", "8", table.iloc[12,4], table.iloc[12,6]], \
     ["2017", "8", table.iloc[13,4], table.iloc[13,6]], \
     ["2017", "8", table.iloc[14,4], table.iloc[14,6]], \
     ["2017", "8", table.iloc[15,4], table.iloc[15,6]], \
     ["2017", "8", table.iloc[16,3], table.iloc[16,6]], \
     ["2017", "8", table.iloc[17,3], table.iloc[17,6]], \
     ["2017", "8", table.iloc[18,3], table.iloc[18,6]]]
     
Ago17 = pd.DataFrame(B,columns=["year", "monnth", "sector", "value"])

table = pd.read_excel(r'C:\Users\jiaxi\OneDrive\Desktop\RBAC 2022\Balance\local\Italy\Italy\Reports\Gas Balance\Bilancio_GAS_2017_09.xlsx', sheet_name = 'Preconsuntivo Settembre  2017')
B = [["2017", "9", table.iloc[5,3], table.iloc[5,6]], \
     ["2017", "9", table.iloc[6,3], table.iloc[6,6]], \
     ["2017", "9", table.iloc[7,4], table.iloc[7,6]], \
     ["2017", "9", table.iloc[8,4], table.iloc[8,6]], \
     ["2017", "9", table.iloc[9,4], table.iloc[9,6]], \
     ["2017", "9", table.iloc[10,4], table.iloc[10,6]], \
     ["2017", "9", table.iloc[11,4], table.iloc[11,6]], \
     ["2017", "9", table.iloc[12,4], table.iloc[12,6]], \
     ["2017", "9", table.iloc[13,4], table.iloc[13,6]], \
     ["2017", "9", table.iloc[14,4], table.iloc[14,6]], \
     ["2017", "9", table.iloc[15,4], table.iloc[15,6]], \
     ["2017", "9", table.iloc[16,3], table.iloc[16,6]], \
     ["2017", "9", table.iloc[17,3], table.iloc[17,6]], \
     ["2017", "9", table.iloc[18,3], table.iloc[18,6]]]
     
Set17 = pd.DataFrame(B,columns=["year", "monnth", "sector", "value"])


table = pd.read_excel(r'C:\Users\jiaxi\OneDrive\Desktop\RBAC 2022\Balance\local\Italy\Italy\Reports\Gas Balance\Bilancio_GAS_2017_10.xlsx', sheet_name = 'Preconsuntivo Ottobre  2017')
B = [["2017", "10", table.iloc[5,3], table.iloc[5,6]], \
     ["2017", "10", table.iloc[6,3], table.iloc[6,6]], \
     ["2017", "10", table.iloc[7,4], table.iloc[7,6]], \
     ["2017", "10", table.iloc[8,4], table.iloc[8,6]], \
     ["2017", "10", table.iloc[9,4], table.iloc[9,6]], \
     ["2017", "10", table.iloc[10,4], table.iloc[10,6]], \
     ["2017", "10", table.iloc[11,4], table.iloc[11,6]], \
     ["2017", "10", table.iloc[12,4], table.iloc[12,6]], \
     ["2017", "10", table.iloc[13,4], table.iloc[13,6]], \
     ["2017", "10", table.iloc[14,4], table.iloc[14,6]], \
     ["2017", "10", table.iloc[15,4], table.iloc[15,6]], \
     ["2017", "10", table.iloc[16,3], table.iloc[16,6]], \
     ["2017", "10", table.iloc[17,3], table.iloc[17,6]], \
     ["2017", "10", table.iloc[18,3], table.iloc[18,6]]]
     
Ott17 = pd.DataFrame(B,columns=["year", "monnth", "sector", "value"])


table = pd.read_excel(r'C:\Users\jiaxi\OneDrive\Desktop\RBAC 2022\Balance\local\Italy\Italy\Reports\Gas Balance\Bilancio_GAS_2017_11.xlsx', sheet_name = 'Preconsuntivo Novembre  2017')
B = [["2017", "11", table.iloc[5,3], table.iloc[5,6]], \
     ["2017", "11", table.iloc[6,3], table.iloc[6,6]], \
     ["2017", "11", table.iloc[7,4], table.iloc[7,6]], \
     ["2017", "11", table.iloc[8,4], table.iloc[8,6]], \
     ["2017", "11", table.iloc[9,4], table.iloc[9,6]], \
     ["2017", "11", table.iloc[10,4], table.iloc[10,6]], \
     ["2017", "11", table.iloc[11,4], table.iloc[11,6]], \
     ["2017", "11", table.iloc[12,4], table.iloc[12,6]], \
     ["2017", "11", table.iloc[13,4], table.iloc[13,6]], \
     ["2017", "11", table.iloc[14,4], table.iloc[14,6]], \
     ["2017", "11", table.iloc[15,4], table.iloc[15,6]], \
     ["2017", "11", table.iloc[16,3], table.iloc[16,6]], \
     ["2017", "11", table.iloc[17,3], table.iloc[17,6]], \
     ["2017", "11", table.iloc[18,3], table.iloc[18,6]]]
     
Nov17 = pd.DataFrame(B,columns=["year", "monnth", "sector", "value"])

table = pd.read_excel(r'C:\Users\jiaxi\OneDrive\Desktop\RBAC 2022\Balance\local\Italy\Italy\Reports\Gas Balance\Bilancio_GAS_2017_12.xlsx', sheet_name = 'Preconsuntivo Dicembre  2017')
B = [["2017", "12", table.iloc[5,3], table.iloc[5,6]], \
     ["2017", "12", table.iloc[6,3], table.iloc[6,6]], \
     ["2017", "12", table.iloc[7,4], table.iloc[7,6]], \
     ["2017", "12", table.iloc[8,4], table.iloc[8,6]], \
     ["2017", "12", table.iloc[9,4], table.iloc[9,6]], \
     ["2017", "12", table.iloc[10,4], table.iloc[10,6]], \
     ["2017", "12", table.iloc[11,4], table.iloc[11,6]], \
     ["2017", "12", table.iloc[12,4], table.iloc[12,6]], \
     ["2017", "12", table.iloc[13,4], table.iloc[13,6]], \
     ["2017", "12", table.iloc[14,4], table.iloc[14,6]], \
     ["2017", "12", table.iloc[15,4], table.iloc[15,6]], \
     ["2017", "12", table.iloc[16,3], table.iloc[16,6]], \
     ["2017", "12", table.iloc[17,3], table.iloc[17,6]], \
     ["2017", "12", table.iloc[18,3], table.iloc[18,6]]]
     
Dic17 = pd.DataFrame(B,columns=["year", "monnth", "sector", "value"])

##2018
table = pd.read_excel(r'C:\Users\jiaxi\OneDrive\Desktop\RBAC 2022\Balance\local\Italy\Italy\Reports\Gas Balance\Bilancio_GAS_2018_01.xlsx', sheet_name = 'Preconsuntivo Gennaio  2018')
B = [["2018", "1", table.iloc[5,3], table.iloc[5,6]], \
     ["2018", "1", table.iloc[6,3], table.iloc[6,6]], \
     ["2018", "1", table.iloc[7,4], table.iloc[7,6]], \
     ["2018", "1", table.iloc[8,4], table.iloc[8,6]], \
     ["2018", "1", table.iloc[9,4], table.iloc[9,6]], \
     ["2018", "1", table.iloc[10,4], table.iloc[10,6]], \
     ["2018", "1", table.iloc[11,4], table.iloc[11,6]], \
     ["2018", "1", table.iloc[12,4], table.iloc[12,6]], \
     ["2018", "1", table.iloc[13,4], table.iloc[13,6]], \
     ["2018", "1", table.iloc[14,4], table.iloc[14,6]], \
     ["2018", "1", table.iloc[15,4], table.iloc[15,6]], \
     ["2018", "1", table.iloc[16,3], table.iloc[16,6]], \
     ["2018", "1", table.iloc[17,3], table.iloc[17,6]], \
     ["2018", "1", table.iloc[18,3], table.iloc[18,6]]]
     
Gen18 = pd.DataFrame(B,columns=["year", "monnth", "sector", "value"])

table = pd.read_excel(r'C:\Users\jiaxi\OneDrive\Desktop\RBAC 2022\Balance\local\Italy\Italy\Reports\Gas Balance\Bilancio_GAS_2018_02.xlsx', sheet_name = 'Preconsuntivo Febbraio  2018')
B = [["2018", "2", table.iloc[5,3], table.iloc[5,6]], \
     ["2018", "2", table.iloc[6,3], table.iloc[6,6]], \
     ["2018", "2", table.iloc[7,4], table.iloc[7,6]], \
     ["2018", "2", table.iloc[8,4], table.iloc[8,6]], \
     ["2018", "2", table.iloc[9,4], table.iloc[9,6]], \
     ["2018", "2", table.iloc[10,4], table.iloc[10,6]], \
     ["2018", "2", table.iloc[11,4], table.iloc[11,6]], \
     ["2018", "2", table.iloc[12,4], table.iloc[12,6]], \
     ["2018", "2", table.iloc[13,4], table.iloc[13,6]], \
     ["2018", "2", table.iloc[14,4], table.iloc[14,6]], \
     ["2018", "2", table.iloc[15,4], table.iloc[15,6]], \
     ["2018", "2", table.iloc[16,3], table.iloc[16,6]], \
     ["2018", "2", table.iloc[17,3], table.iloc[17,6]], \
     ["2018", "2", table.iloc[18,3], table.iloc[18,6]]]
     
Feb18 = pd.DataFrame(B,columns=["year", "monnth", "sector", "value"])

table = pd.read_excel(r'C:\Users\jiaxi\OneDrive\Desktop\RBAC 2022\Balance\local\Italy\Italy\Reports\Gas Balance\Bilancio_GAS_2018_03.xlsx', sheet_name = 'Preconsuntivo Marzo  2018')
B = [["2018", "3", table.iloc[5,3], table.iloc[5,6]], \
     ["2018", "3", table.iloc[6,3], table.iloc[6,6]], \
     ["2018", "3", table.iloc[7,4], table.iloc[7,6]], \
     ["2018", "3", table.iloc[8,4], table.iloc[8,6]], \
     ["2018", "3", table.iloc[9,4], table.iloc[9,6]], \
     ["2018", "3", table.iloc[10,4], table.iloc[10,6]], \
     ["2018", "3", table.iloc[11,4], table.iloc[11,6]], \
     ["2018", "3", table.iloc[12,4], table.iloc[12,6]], \
     ["2018", "3", table.iloc[13,4], table.iloc[13,6]], \
     ["2018", "3", table.iloc[14,4], table.iloc[14,6]], \
     ["2018", "3", table.iloc[15,4], table.iloc[15,6]], \
     ["2018", "3", table.iloc[16,3], table.iloc[16,6]], \
     ["2018", "3", table.iloc[17,3], table.iloc[17,6]], \
     ["2018", "3", table.iloc[18,3], table.iloc[18,6]]]
     
Mar18 = pd.DataFrame(B,columns=["year", "monnth", "sector", "value"])

table = pd.read_excel(r'C:\Users\jiaxi\OneDrive\Desktop\RBAC 2022\Balance\local\Italy\Italy\Reports\Gas Balance\Bilancio_GAS_2018_04.xlsx', sheet_name = 'Preconsuntivo Aprile  2018')
B = [["2018", "4", table.iloc[5,3], table.iloc[5,6]], \
     ["2018", "4", table.iloc[6,3], table.iloc[6,6]], \
     ["2018", "4", table.iloc[7,4], table.iloc[7,6]], \
     ["2018", "4", table.iloc[8,4], table.iloc[8,6]], \
     ["2018", "4", table.iloc[9,4], table.iloc[9,6]], \
     ["2018", "4", table.iloc[10,4], table.iloc[10,6]], \
     ["2018", "4", table.iloc[11,4], table.iloc[11,6]], \
     ["2018", "4", table.iloc[12,4], table.iloc[12,6]], \
     ["2018", "4", table.iloc[13,4], table.iloc[13,6]], \
     ["2018", "4", table.iloc[14,4], table.iloc[14,6]], \
     ["2018", "4", table.iloc[15,4], table.iloc[15,6]], \
     ["2018", "4", table.iloc[16,3], table.iloc[16,6]], \
     ["2018", "4", table.iloc[17,3], table.iloc[17,6]], \
     ["2018", "4", table.iloc[18,3], table.iloc[18,6]]]
     
Apr18 = pd.DataFrame(B,columns=["year", "monnth", "sector", "value"])

table = pd.read_excel(r'C:\Users\jiaxi\OneDrive\Desktop\RBAC 2022\Balance\local\Italy\Italy\Reports\Gas Balance\Bilancio_GAS_2018_05.xlsx', sheet_name = 'Preconsuntivo maggio 2018')
B = [["2018", "5", table.iloc[5,3], table.iloc[5,6]], \
     ["2018", "5", table.iloc[6,3], table.iloc[6,6]], \
     ["2018", "5", table.iloc[7,4], table.iloc[7,6]], \
     ["2018", "5", table.iloc[8,4], table.iloc[8,6]], \
     ["2018", "5", table.iloc[9,4], table.iloc[9,6]], \
     ["2018", "5", table.iloc[10,4], table.iloc[10,6]], \
     ["2018", "5", table.iloc[11,4], table.iloc[11,6]], \
     ["2018", "5", table.iloc[12,4], table.iloc[12,6]], \
     ["2018", "5", table.iloc[13,4], table.iloc[13,6]], \
     ["2018", "5", table.iloc[14,4], table.iloc[14,6]], \
     ["2018", "5", table.iloc[15,4], table.iloc[15,6]], \
     ["2018", "5", table.iloc[16,3], table.iloc[16,6]], \
     ["2018", "5", table.iloc[17,3], table.iloc[17,6]], \
     ["2018", "5", table.iloc[18,3], table.iloc[18,6]]]
     
Mag18 = pd.DataFrame(B,columns=["year", "monnth", "sector", "value"])

table = pd.read_excel(r'C:\Users\jiaxi\OneDrive\Desktop\RBAC 2022\Balance\local\Italy\Italy\Reports\Gas Balance\Bilancio_GAS_2018_06.xlsx', sheet_name = 'Preconsuntivo giugno 2018')
B = [["2018", "6", table.iloc[5,3], table.iloc[5,6]], \
     ["2018", "6", table.iloc[6,3], table.iloc[6,6]], \
     ["2018", "6", table.iloc[7,4], table.iloc[7,6]], \
     ["2018", "6", table.iloc[8,4], table.iloc[8,6]], \
     ["2018", "6", table.iloc[9,4], table.iloc[9,6]], \
     ["2018", "6", table.iloc[10,4], table.iloc[10,6]], \
     ["2018", "6", table.iloc[11,4], table.iloc[11,6]], \
     ["2018", "6", table.iloc[12,4], table.iloc[12,6]], \
     ["2018", "6", table.iloc[13,4], table.iloc[13,6]], \
     ["2018", "6", table.iloc[14,4], table.iloc[14,6]], \
     ["2018", "6", table.iloc[15,4], table.iloc[15,6]], \
     ["2018", "6", table.iloc[16,3], table.iloc[16,6]], \
     ["2018", "6", table.iloc[17,3], table.iloc[17,6]], \
     ["2018", "6", table.iloc[18,3], table.iloc[18,6]]]
     
Giu18 = pd.DataFrame(B,columns=["year", "monnth", "sector", "value"])


table = pd.read_excel(r'C:\Users\jiaxi\OneDrive\Desktop\RBAC 2022\Balance\local\Italy\Italy\Reports\Gas Balance\Bilancio_GAS_2018_07.xlsx', sheet_name = 'Preconsuntivo luglio 2018')
B = [["2018", "7", table.iloc[5,3], table.iloc[5,6]], \
     ["2018", "7", table.iloc[6,3], table.iloc[6,6]], \
     ["2018", "7", table.iloc[7,4], table.iloc[7,6]], \
     ["2018", "7", table.iloc[8,4], table.iloc[8,6]], \
     ["2018", "7", table.iloc[9,4], table.iloc[9,6]], \
     ["2018", "7", table.iloc[10,4], table.iloc[10,6]], \
     ["2018", "7", table.iloc[11,4], table.iloc[11,6]], \
     ["2018", "7", table.iloc[12,4], table.iloc[12,6]], \
     ["2018", "7", table.iloc[13,4], table.iloc[13,6]], \
     ["2018", "7", table.iloc[14,4], table.iloc[14,6]], \
     ["2018", "7", table.iloc[15,4], table.iloc[15,6]], \
     ["2018", "7", table.iloc[16,3], table.iloc[16,6]], \
     ["2018", "7", table.iloc[17,3], table.iloc[17,6]], \
     ["2018", "7", table.iloc[18,3], table.iloc[18,6]]]
     
Lug18 = pd.DataFrame(B,columns=["year", "monnth", "sector", "value"])

table = pd.read_excel(r'C:\Users\jiaxi\OneDrive\Desktop\RBAC 2022\Balance\local\Italy\Italy\Reports\Gas Balance\Bilancio_GAS_2018_08.xlsx', sheet_name = 'Preconsuntivo agosto 2018')
B = [["2018", "8", table.iloc[5,3], table.iloc[5,6]], \
     ["2018", "8", table.iloc[6,3], table.iloc[6,6]], \
     ["2018", "8", table.iloc[7,4], table.iloc[7,6]], \
     ["2018", "8", table.iloc[8,4], table.iloc[8,6]], \
     ["2018", "8", table.iloc[9,4], table.iloc[9,6]], \
     ["2018", "8", table.iloc[10,4], table.iloc[10,6]], \
     ["2018", "8", table.iloc[11,4], table.iloc[11,6]], \
     ["2018", "8", table.iloc[12,4], table.iloc[12,6]], \
     ["2018", "8", table.iloc[13,4], table.iloc[13,6]], \
     ["2018", "8", table.iloc[14,4], table.iloc[14,6]], \
     ["2018", "8", table.iloc[15,4], table.iloc[15,6]], \
     ["2018", "8", table.iloc[16,3], table.iloc[16,6]], \
     ["2018", "8", table.iloc[17,3], table.iloc[17,6]], \
     ["2018", "8", table.iloc[18,3], table.iloc[18,6]]]
     
Ago18 = pd.DataFrame(B,columns=["year", "monnth", "sector", "value"])

table = pd.read_excel(r'C:\Users\jiaxi\OneDrive\Desktop\RBAC 2022\Balance\local\Italy\Italy\Reports\Gas Balance\Bilancio_GAS_2018_09.xlsx', sheet_name = 'Preconsuntivo settembre 2018')
B = [["2018", "9", table.iloc[5,3], table.iloc[5,6]], \
     ["2018", "9", table.iloc[6,3], table.iloc[6,6]], \
     ["2018", "9", table.iloc[7,4], table.iloc[7,6]], \
     ["2018", "9", table.iloc[8,4], table.iloc[8,6]], \
     ["2018", "9", table.iloc[9,4], table.iloc[9,6]], \
     ["2018", "9", table.iloc[10,4], table.iloc[10,6]], \
     ["2018", "9", table.iloc[11,4], table.iloc[11,6]], \
     ["2018", "9", table.iloc[12,4], table.iloc[12,6]], \
     ["2018", "9", table.iloc[13,4], table.iloc[13,6]], \
     ["2018", "9", table.iloc[14,4], table.iloc[14,6]], \
     ["2018", "9", table.iloc[15,4], table.iloc[15,6]], \
     ["2018", "9", table.iloc[16,3], table.iloc[16,6]], \
     ["2018", "9", table.iloc[17,3], table.iloc[17,6]], \
     ["2018", "9", table.iloc[18,3], table.iloc[18,6]]]
     
Set18 = pd.DataFrame(B,columns=["year", "monnth", "sector", "value"])


table = pd.read_excel(r'C:\Users\jiaxi\OneDrive\Desktop\RBAC 2022\Balance\local\Italy\Italy\Reports\Gas Balance\Bilancio_GAS_2018_10.xlsx', sheet_name = 'Preconsuntivo ottobre 2018')
B = [["2018", "10", table.iloc[5,3], table.iloc[5,6]], \
     ["2018", "10", table.iloc[6,3], table.iloc[6,6]], \
     ["2018", "10", table.iloc[7,4], table.iloc[7,6]], \
     ["2018", "10", table.iloc[8,4], table.iloc[8,6]], \
     ["2018", "10", table.iloc[9,4], table.iloc[9,6]], \
     ["2018", "10", table.iloc[10,4], table.iloc[10,6]], \
     ["2018", "10", table.iloc[11,4], table.iloc[11,6]], \
     ["2018", "10", table.iloc[12,4], table.iloc[12,6]], \
     ["2018", "10", table.iloc[13,4], table.iloc[13,6]], \
     ["2018", "10", table.iloc[14,4], table.iloc[14,6]], \
     ["2018", "10", table.iloc[15,4], table.iloc[15,6]], \
     ["2018", "10", table.iloc[16,3], table.iloc[16,6]], \
     ["2018", "10", table.iloc[17,3], table.iloc[17,6]], \
     ["2018", "10", table.iloc[18,3], table.iloc[18,6]]]
     
Ott18 = pd.DataFrame(B,columns=["year", "monnth", "sector", "value"])


table = pd.read_excel(r'C:\Users\jiaxi\OneDrive\Desktop\RBAC 2022\Balance\local\Italy\Italy\Reports\Gas Balance\Bilancio_GAS_2018_11.xlsx', sheet_name = 'Preconsuntivo novembre 2018')
B = [["2018", "11", table.iloc[5,3], table.iloc[5,6]], \
     ["2018", "11", table.iloc[6,3], table.iloc[6,6]], \
     ["2018", "11", table.iloc[7,4], table.iloc[7,6]], \
     ["2018", "11", table.iloc[8,4], table.iloc[8,6]], \
     ["2018", "11", table.iloc[9,4], table.iloc[9,6]], \
     ["2018", "11", table.iloc[10,4], table.iloc[10,6]], \
     ["2018", "11", table.iloc[11,4], table.iloc[11,6]], \
     ["2018", "11", table.iloc[12,4], table.iloc[12,6]], \
     ["2018", "11", table.iloc[13,4], table.iloc[13,6]], \
     ["2018", "11", table.iloc[14,4], table.iloc[14,6]], \
     ["2018", "11", table.iloc[15,4], table.iloc[15,6]], \
     ["2018", "11", table.iloc[16,3], table.iloc[16,6]], \
     ["2018", "11", table.iloc[17,3], table.iloc[17,6]], \
     ["2018", "11", table.iloc[18,3], table.iloc[18,6]]]
     
Nov18 = pd.DataFrame(B,columns=["year", "monnth", "sector", "value"])

table = pd.read_excel(r'C:\Users\jiaxi\OneDrive\Desktop\RBAC 2022\Balance\local\Italy\Italy\Reports\Gas Balance\Bilancio_GAS_2018_12.xlsx', sheet_name = 'Preconsuntivo dicembre 2018')
B = [["2018", "12", table.iloc[5,3], table.iloc[5,6]], \
     ["2018", "12", table.iloc[6,3], table.iloc[6,6]], \
     ["2018", "12", table.iloc[7,4], table.iloc[7,6]], \
     ["2018", "12", table.iloc[8,4], table.iloc[8,6]], \
     ["2018", "12", table.iloc[9,4], table.iloc[9,6]], \
     ["2018", "12", table.iloc[10,4], table.iloc[10,6]], \
     ["2018", "12", table.iloc[11,4], table.iloc[11,6]], \
     ["2018", "12", table.iloc[12,4], table.iloc[12,6]], \
     ["2018", "12", table.iloc[13,4], table.iloc[13,6]], \
     ["2018", "12", table.iloc[14,4], table.iloc[14,6]], \
     ["2018", "12", table.iloc[15,4], table.iloc[15,6]], \
     ["2018", "12", table.iloc[16,3], table.iloc[16,6]], \
     ["2018", "12", table.iloc[17,3], table.iloc[17,6]], \
     ["2018", "12", table.iloc[18,3], table.iloc[18,6]]]
     
Dic18 = pd.DataFrame(B,columns=["year", "monnth", "sector", "value"])

##2019
table = pd.read_excel(r'C:\Users\jiaxi\OneDrive\Desktop\RBAC 2022\Balance\local\Italy\Italy\Reports\Gas Balance\Bilancio_GAS_2019_01.xlsx', sheet_name = 'Preconsuntivo Gennaio  2019')
B = [["2019", "1", table.iloc[5,3], table.iloc[5,6]], \
     ["2019", "1", table.iloc[6,3], table.iloc[6,6]], \
     ["2019", "1", table.iloc[7,4], table.iloc[7,6]], \
     ["2019", "1", table.iloc[8,4], table.iloc[8,6]], \
     ["2019", "1", table.iloc[9,4], table.iloc[9,6]], \
     ["2019", "1", table.iloc[10,4], table.iloc[10,6]], \
     ["2019", "1", table.iloc[11,4], table.iloc[11,6]], \
     ["2019", "1", table.iloc[12,4], table.iloc[12,6]], \
     ["2019", "1", table.iloc[13,4], table.iloc[13,6]], \
     ["2019", "1", table.iloc[14,4], table.iloc[14,6]], \
     ["2019", "1", table.iloc[15,4], table.iloc[15,6]], \
     ["2019", "1", table.iloc[16,3], table.iloc[16,6]], \
     ["2019", "1", table.iloc[17,3], table.iloc[17,6]], \
     ["2019", "1", table.iloc[18,3], table.iloc[18,6]]]
     
Gen19 = pd.DataFrame(B,columns=["year", "monnth", "sector", "value"])

table = pd.read_excel(r'C:\Users\jiaxi\OneDrive\Desktop\RBAC 2022\Balance\local\Italy\Italy\Reports\Gas Balance\Bilancio_GAS_2019_02.xlsx', sheet_name = 'Preconsuntivo Febbraio  2019')
B = [["2019", "2", table.iloc[5,3], table.iloc[5,6]], \
     ["2019", "2", table.iloc[6,3], table.iloc[6,6]], \
     ["2019", "2", table.iloc[7,4], table.iloc[7,6]], \
     ["2019", "2", table.iloc[8,4], table.iloc[8,6]], \
     ["2019", "2", table.iloc[9,4], table.iloc[9,6]], \
     ["2019", "2", table.iloc[10,4], table.iloc[10,6]], \
     ["2019", "2", table.iloc[11,4], table.iloc[11,6]], \
     ["2019", "2", table.iloc[12,4], table.iloc[12,6]], \
     ["2019", "2", table.iloc[13,4], table.iloc[13,6]], \
     ["2019", "2", table.iloc[14,4], table.iloc[14,6]], \
     ["2019", "2", table.iloc[15,4], table.iloc[15,6]], \
     ["2019", "2", table.iloc[16,3], table.iloc[16,6]], \
     ["2019", "2", table.iloc[17,3], table.iloc[17,6]], \
     ["2019", "2", table.iloc[18,3], table.iloc[18,6]]]
     
Feb19 = pd.DataFrame(B,columns=["year", "monnth", "sector", "value"])

table = pd.read_excel(r'C:\Users\jiaxi\OneDrive\Desktop\RBAC 2022\Balance\local\Italy\Italy\Reports\Gas Balance\Bilancio_GAS_2019_03.xlsx', sheet_name = 'Preconsuntivo Marzo  2019')
B = [["2019", "3", table.iloc[5,3], table.iloc[5,6]], \
     ["2019", "3", table.iloc[6,3], table.iloc[6,6]], \
     ["2019", "3", table.iloc[7,4], table.iloc[7,6]], \
     ["2019", "3", table.iloc[8,4], table.iloc[8,6]], \
     ["2019", "3", table.iloc[9,4], table.iloc[9,6]], \
     ["2019", "3", table.iloc[10,4], table.iloc[10,6]], \
     ["2019", "3", table.iloc[11,4], table.iloc[11,6]], \
     ["2019", "3", table.iloc[12,4], table.iloc[12,6]], \
     ["2019", "3", table.iloc[13,4], table.iloc[13,6]], \
     ["2019", "3", table.iloc[14,4], table.iloc[14,6]], \
     ["2019", "3", table.iloc[15,4], table.iloc[15,6]], \
     ["2019", "3", table.iloc[16,3], table.iloc[16,6]], \
     ["2019", "3", table.iloc[17,3], table.iloc[17,6]], \
     ["2019", "3", table.iloc[18,3], table.iloc[18,6]]]
     
Mar19 = pd.DataFrame(B,columns=["year", "monnth", "sector", "value"])

table = pd.read_excel(r'C:\Users\jiaxi\OneDrive\Desktop\RBAC 2022\Balance\local\Italy\Italy\Reports\Gas Balance\Bilancio_GAS_2019_04.xlsx', sheet_name = 'Preconsuntivo Aprile  2019')
B = [["2019", "4", table.iloc[5,3], table.iloc[5,6]], \
     ["2019", "4", table.iloc[6,3], table.iloc[6,6]], \
     ["2019", "4", table.iloc[7,4], table.iloc[7,6]], \
     ["2019", "4", table.iloc[8,4], table.iloc[8,6]], \
     ["2019", "4", table.iloc[9,4], table.iloc[9,6]], \
     ["2019", "4", table.iloc[10,4], table.iloc[10,6]], \
     ["2019", "4", table.iloc[11,4], table.iloc[11,6]], \
     ["2019", "4", table.iloc[12,4], table.iloc[12,6]], \
     ["2019", "4", table.iloc[13,4], table.iloc[13,6]], \
     ["2019", "4", table.iloc[14,4], table.iloc[14,6]], \
     ["2019", "4", table.iloc[15,4], table.iloc[15,6]], \
     ["2019", "4", table.iloc[16,3], table.iloc[16,6]], \
     ["2019", "4", table.iloc[17,3], table.iloc[17,6]], \
     ["2019", "4", table.iloc[18,3], table.iloc[18,6]]]
     
Apr19 = pd.DataFrame(B,columns=["year", "monnth", "sector", "value"])

table = pd.read_excel(r'C:\Users\jiaxi\OneDrive\Desktop\RBAC 2022\Balance\local\Italy\Italy\Reports\Gas Balance\Bilancio_GAS_2019_05.xlsx', sheet_name = 'Preconsuntivo Maggio  2019')
B = [["2019", "5", table.iloc[5,3], table.iloc[5,6]], \
     ["2019", "5", table.iloc[6,3], table.iloc[6,6]], \
     ["2019", "5", table.iloc[7,4], table.iloc[7,6]], \
     ["2019", "5", table.iloc[8,4], table.iloc[8,6]], \
     ["2019", "5", table.iloc[9,4], table.iloc[9,6]], \
     ["2019", "5", table.iloc[10,4], table.iloc[10,6]], \
     ["2019", "5", table.iloc[11,4], table.iloc[11,6]], \
     ["2019", "5", table.iloc[12,4], table.iloc[12,6]], \
     ["2019", "5", table.iloc[13,4], table.iloc[13,6]], \
     ["2019", "5", table.iloc[14,4], table.iloc[14,6]], \
     ["2019", "5", table.iloc[15,4], table.iloc[15,6]], \
     ["2019", "5", table.iloc[16,3], table.iloc[16,6]], \
     ["2019", "5", table.iloc[17,3], table.iloc[17,6]], \
     ["2019", "5", table.iloc[18,3], table.iloc[18,6]]]
     
Mag19 = pd.DataFrame(B,columns=["year", "monnth", "sector", "value"])

table = pd.read_excel(r'C:\Users\jiaxi\OneDrive\Desktop\RBAC 2022\Balance\local\Italy\Italy\Reports\Gas Balance\Bilancio_GAS_2019_06.xlsx', sheet_name = 'Preconsuntivo Giugno  2019')
B = [["2019", "6", table.iloc[5,3], table.iloc[5,6]], \
     ["2019", "6", table.iloc[6,3], table.iloc[6,6]], \
     ["2019", "6", table.iloc[7,4], table.iloc[7,6]], \
     ["2019", "6", table.iloc[8,4], table.iloc[8,6]], \
     ["2019", "6", table.iloc[9,4], table.iloc[9,6]], \
     ["2019", "6", table.iloc[10,4], table.iloc[10,6]], \
     ["2019", "6", table.iloc[11,4], table.iloc[11,6]], \
     ["2019", "6", table.iloc[12,4], table.iloc[12,6]], \
     ["2019", "6", table.iloc[13,4], table.iloc[13,6]], \
     ["2019", "6", table.iloc[14,4], table.iloc[14,6]], \
     ["2019", "6", table.iloc[15,4], table.iloc[15,6]], \
     ["2019", "6", table.iloc[16,3], table.iloc[16,6]], \
     ["2019", "6", table.iloc[17,3], table.iloc[17,6]], \
     ["2019", "6", table.iloc[18,3], table.iloc[18,6]]]
     
Giu19 = pd.DataFrame(B,columns=["year", "monnth", "sector", "value"])


table = pd.read_excel(r'C:\Users\jiaxi\OneDrive\Desktop\RBAC 2022\Balance\local\Italy\Italy\Reports\Gas Balance\Bilancio_GAS_2019_07.xlsx', sheet_name = 'Preconsuntivo Luglio  2019')
B = [["2019", "7", table.iloc[5,3], table.iloc[5,6]], \
     ["2019", "7", table.iloc[6,3], table.iloc[6,6]], \
     ["2019", "7", table.iloc[7,4], table.iloc[7,6]], \
     ["2019", "7", table.iloc[8,4], table.iloc[8,6]], \
     ["2019", "7", table.iloc[9,4], table.iloc[9,6]], \
     ["2019", "7", table.iloc[10,4], table.iloc[10,6]], \
     ["2019", "7", table.iloc[11,4], table.iloc[11,6]], \
     ["2019", "7", table.iloc[12,4], table.iloc[12,6]], \
     ["2019", "7", table.iloc[13,4], table.iloc[13,6]], \
     ["2019", "7", table.iloc[14,4], table.iloc[14,6]], \
     ["2019", "7", table.iloc[15,4], table.iloc[15,6]], \
     ["2019", "7", table.iloc[16,3], table.iloc[16,6]], \
     ["2019", "7", table.iloc[17,3], table.iloc[17,6]], \
     ["2019", "7", table.iloc[18,3], table.iloc[18,6]]]
     
Lug19 = pd.DataFrame(B,columns=["year", "monnth", "sector", "value"])

table = pd.read_excel(r'C:\Users\jiaxi\OneDrive\Desktop\RBAC 2022\Balance\local\Italy\Italy\Reports\Gas Balance\Bilancio_GAS_2019_08.xlsx', sheet_name = 'Preconsuntivo Agosto  2019')
B = [["2019", "8", table.iloc[5,3], table.iloc[5,6]], \
     ["2019", "8", table.iloc[6,3], table.iloc[6,6]], \
     ["2019", "8", table.iloc[7,4], table.iloc[7,6]], \
     ["2019", "8", table.iloc[8,4], table.iloc[8,6]], \
     ["2019", "8", table.iloc[9,4], table.iloc[9,6]], \
     ["2019", "8", table.iloc[10,4], table.iloc[10,6]], \
     ["2019", "8", table.iloc[11,4], table.iloc[11,6]], \
     ["2019", "8", table.iloc[12,4], table.iloc[12,6]], \
     ["2019", "8", table.iloc[13,4], table.iloc[13,6]], \
     ["2019", "8", table.iloc[14,4], table.iloc[14,6]], \
     ["2019", "8", table.iloc[15,4], table.iloc[15,6]], \
     ["2019", "8", table.iloc[16,3], table.iloc[16,6]], \
     ["2019", "8", table.iloc[17,3], table.iloc[17,6]], \
     ["2019", "8", table.iloc[18,3], table.iloc[18,6]]]
     
Ago19 = pd.DataFrame(B,columns=["year", "monnth", "sector", "value"])

table = pd.read_excel(r'C:\Users\jiaxi\OneDrive\Desktop\RBAC 2022\Balance\local\Italy\Italy\Reports\Gas Balance\Bilancio_GAS_2019_09.xlsx', sheet_name = 'Preconsuntivo Settembre  2019')
B = [["2019", "9", table.iloc[5,3], table.iloc[5,6]], \
     ["2019", "9", table.iloc[6,3], table.iloc[6,6]], \
     ["2019", "9", table.iloc[7,4], table.iloc[7,6]], \
     ["2019", "9", table.iloc[8,4], table.iloc[8,6]], \
     ["2019", "9", table.iloc[9,4], table.iloc[9,6]], \
     ["2019", "9", table.iloc[10,4], table.iloc[10,6]], \
     ["2019", "9", table.iloc[11,4], table.iloc[11,6]], \
     ["2019", "9", table.iloc[12,4], table.iloc[12,6]], \
     ["2019", "9", table.iloc[13,4], table.iloc[13,6]], \
     ["2019", "9", table.iloc[14,4], table.iloc[14,6]], \
     ["2019", "9", table.iloc[15,4], table.iloc[15,6]], \
     ["2019", "9", table.iloc[16,3], table.iloc[16,6]], \
     ["2019", "9", table.iloc[17,3], table.iloc[17,6]], \
     ["2019", "9", table.iloc[18,3], table.iloc[18,6]]]
     
Set19 = pd.DataFrame(B,columns=["year", "monnth", "sector", "value"])


table = pd.read_excel(r'C:\Users\jiaxi\OneDrive\Desktop\RBAC 2022\Balance\local\Italy\Italy\Reports\Gas Balance\Bilancio_GAS_2019_10.xlsx', sheet_name = 'Preconsuntivo Ottobre  2019')
B = [["2019", "10", table.iloc[5,3], table.iloc[5,6]], \
     ["2019", "10", table.iloc[6,3], table.iloc[6,6]], \
     ["2019", "10", table.iloc[7,4], table.iloc[7,6]], \
     ["2019", "10", table.iloc[8,4], table.iloc[8,6]], \
     ["2019", "10", table.iloc[9,4], table.iloc[9,6]], \
     ["2019", "10", table.iloc[10,4], table.iloc[10,6]], \
     ["2019", "10", table.iloc[11,4], table.iloc[11,6]], \
     ["2019", "10", table.iloc[12,4], table.iloc[12,6]], \
     ["2019", "10", table.iloc[13,4], table.iloc[13,6]], \
     ["2019", "10", table.iloc[14,4], table.iloc[14,6]], \
     ["2019", "10", table.iloc[15,4], table.iloc[15,6]], \
     ["2019", "10", table.iloc[16,3], table.iloc[16,6]], \
     ["2019", "10", table.iloc[17,3], table.iloc[17,6]], \
     ["2019", "10", table.iloc[18,3], table.iloc[18,6]]]
     
Ott19 = pd.DataFrame(B,columns=["year", "monnth", "sector", "value"])


table = pd.read_excel(r'C:\Users\jiaxi\OneDrive\Desktop\RBAC 2022\Balance\local\Italy\Italy\Reports\Gas Balance\Bilancio_GAS_2019_11.xlsx', sheet_name = 'Preconsuntivo Novembre  2019')
B = [["2019", "11", table.iloc[5,3], table.iloc[5,6]], \
     ["2019", "11", table.iloc[6,3], table.iloc[6,6]], \
     ["2019", "11", table.iloc[7,4], table.iloc[7,6]], \
     ["2019", "11", table.iloc[8,4], table.iloc[8,6]], \
     ["2019", "11", table.iloc[9,4], table.iloc[9,6]], \
     ["2019", "11", table.iloc[10,4], table.iloc[10,6]], \
     ["2019", "11", table.iloc[11,4], table.iloc[11,6]], \
     ["2019", "11", table.iloc[12,4], table.iloc[12,6]], \
     ["2019", "11", table.iloc[13,4], table.iloc[13,6]], \
     ["2019", "11", table.iloc[14,4], table.iloc[14,6]], \
     ["2019", "11", table.iloc[15,4], table.iloc[15,6]], \
     ["2019", "11", table.iloc[16,3], table.iloc[16,6]], \
     ["2019", "11", table.iloc[17,3], table.iloc[17,6]], \
     ["2019", "11", table.iloc[18,3], table.iloc[18,6]]]
     
Nov19 = pd.DataFrame(B,columns=["year", "monnth", "sector", "value"])

table = pd.read_excel(r'C:\Users\jiaxi\OneDrive\Desktop\RBAC 2022\Balance\local\Italy\Italy\Reports\Gas Balance\Bilancio_GAS_2019_12.xlsx', sheet_name = 'Preconsuntivo Dicembre  2019')
B = [["2019", "12", table.iloc[5,3], table.iloc[5,6]], \
     ["2019", "12", table.iloc[6,3], table.iloc[6,6]], \
     ["2019", "12", table.iloc[7,4], table.iloc[7,6]], \
     ["2019", "12", table.iloc[8,4], table.iloc[8,6]], \
     ["2019", "12", table.iloc[9,4], table.iloc[9,6]], \
     ["2019", "12", table.iloc[10,4], table.iloc[10,6]], \
     ["2019", "12", table.iloc[11,4], table.iloc[11,6]], \
     ["2019", "12", table.iloc[12,4], table.iloc[12,6]], \
     ["2019", "12", table.iloc[13,4], table.iloc[13,6]], \
     ["2019", "12", table.iloc[14,4], table.iloc[14,6]], \
     ["2019", "12", table.iloc[15,4], table.iloc[15,6]], \
     ["2019", "12", table.iloc[16,3], table.iloc[16,6]], \
     ["2019", "12", table.iloc[17,3], table.iloc[17,6]], \
     ["2019", "12", table.iloc[18,3], table.iloc[18,6]]]
     
Dic19 = pd.DataFrame(B,columns=["year", "monnth", "sector", "value"])


##2020
table = pd.read_excel(r'C:\Users\jiaxi\OneDrive\Desktop\RBAC 2022\Balance\local\Italy\Italy\Reports\Gas Balance\Bilancio_GAS_2020_01.xlsx', sheet_name = 'Preconsuntivo Gennaio  2020')
B = [["2020", "1", table.iloc[5,3], table.iloc[5,6]], \
     ["2020", "1", table.iloc[6,3], table.iloc[6,6]], \
     ["2020", "1", table.iloc[7,4], table.iloc[7,6]], \
     ["2020", "1", table.iloc[8,4], table.iloc[8,6]], \
     ["2020", "1", table.iloc[9,4], table.iloc[9,6]], \
     ["2020", "1", table.iloc[10,4], table.iloc[10,6]], \
     ["2020", "1", table.iloc[11,4], table.iloc[11,6]], \
     ["2020", "1", table.iloc[12,4], table.iloc[12,6]], \
     ["2020", "1", table.iloc[13,4], table.iloc[13,6]], \
     ["2020", "1", table.iloc[14,4], table.iloc[14,6]], \
     ["2020", "1", table.iloc[15,4], table.iloc[15,6]], \
     ["2020", "1", table.iloc[16,3], table.iloc[16,6]], \
     ["2020", "1", table.iloc[17,3], table.iloc[17,6]], \
     ["2020", "1", table.iloc[18,3], table.iloc[18,6]]]
     
Gen20 = pd.DataFrame(B,columns=["year", "monnth", "sector", "value"])

table = pd.read_excel(r'C:\Users\jiaxi\OneDrive\Desktop\RBAC 2022\Balance\local\Italy\Italy\Reports\Gas Balance\Bilancio_GAS_2020_02.xlsx', sheet_name = 'Preconsuntivo febbraio  2020')
B = [["2020", "2", table.iloc[5,3], table.iloc[5,6]], \
     ["2020", "2", table.iloc[6,3], table.iloc[6,6]], \
     ["2020", "2", table.iloc[7,4], table.iloc[7,6]], \
     ["2020", "2", table.iloc[8,4], table.iloc[8,6]], \
     ["2020", "2", table.iloc[9,4], table.iloc[9,6]], \
     ["2020", "2", table.iloc[10,4], table.iloc[10,6]], \
     ["2020", "2", table.iloc[11,4], table.iloc[11,6]], \
     ["2020", "2", table.iloc[12,4], table.iloc[12,6]], \
     ["2020", "2", table.iloc[13,4], table.iloc[13,6]], \
     ["2020", "2", table.iloc[14,4], table.iloc[14,6]], \
     ["2020", "2", table.iloc[15,4], table.iloc[15,6]], \
     ["2020", "2", table.iloc[16,3], table.iloc[16,6]], \
     ["2020", "2", table.iloc[17,3], table.iloc[17,6]], \
     ["2020", "2", table.iloc[18,3], table.iloc[18,6]]]
     
Feb20 = pd.DataFrame(B,columns=["year", "monnth", "sector", "value"])

table = pd.read_excel(r'C:\Users\jiaxi\OneDrive\Desktop\RBAC 2022\Balance\local\Italy\Italy\Reports\Gas Balance\Bilancio_GAS_2020_03.xlsx', sheet_name = 'Preconsuntivo marzo  2020')
B = [["2020", "3", table.iloc[5,3], table.iloc[5,6]], \
     ["2020", "3", table.iloc[6,3], table.iloc[6,6]], \
     ["2020", "3", table.iloc[7,4], table.iloc[7,6]], \
     ["2020", "3", table.iloc[8,4], table.iloc[8,6]], \
     ["2020", "3", table.iloc[9,4], table.iloc[9,6]], \
     ["2020", "3", table.iloc[10,4], table.iloc[10,6]], \
     ["2020", "3", table.iloc[11,4], table.iloc[11,6]], \
     ["2020", "3", table.iloc[12,4], table.iloc[12,6]], \
     ["2020", "3", table.iloc[13,4], table.iloc[13,6]], \
     ["2020", "3", table.iloc[14,4], table.iloc[14,6]], \
     ["2020", "3", table.iloc[15,4], table.iloc[15,6]], \
     ["2020", "3", table.iloc[16,3], table.iloc[16,6]], \
     ["2020", "3", table.iloc[17,3], table.iloc[17,6]], \
     ["2020", "3", table.iloc[18,3], table.iloc[18,6]]]
     
Mar20 = pd.DataFrame(B,columns=["year", "monnth", "sector", "value"])

table = pd.read_excel(r'C:\Users\jiaxi\OneDrive\Desktop\RBAC 2022\Balance\local\Italy\Italy\Reports\Gas Balance\Bilancio_GAS_2020_04.xlsx', sheet_name = 'Preconsuntivo aprile  2020')
B = [["2020", "4", table.iloc[5,3], table.iloc[5,6]], \
     ["2020", "4", table.iloc[6,3], table.iloc[6,6]], \
     ["2020", "4", table.iloc[7,4], table.iloc[7,6]], \
     ["2020", "4", table.iloc[8,4], table.iloc[8,6]], \
     ["2020", "4", table.iloc[9,4], table.iloc[9,6]], \
     ["2020", "4", table.iloc[10,4], table.iloc[10,6]], \
     ["2020", "4", table.iloc[11,4], table.iloc[11,6]], \
     ["2020", "4", table.iloc[12,4], table.iloc[12,6]], \
     ["2020", "4", table.iloc[13,4], table.iloc[13,6]], \
     ["2020", "4", table.iloc[14,4], table.iloc[14,6]], \
     ["2020", "4", table.iloc[15,4], table.iloc[15,6]], \
     ["2020", "4", table.iloc[16,3], table.iloc[16,6]], \
     ["2020", "4", table.iloc[17,3], table.iloc[17,6]], \
     ["2020", "4", table.iloc[18,3], table.iloc[18,6]]]
     
Apr20 = pd.DataFrame(B,columns=["year", "monnth", "sector", "value"])

table = pd.read_excel(r'C:\Users\jiaxi\OneDrive\Desktop\RBAC 2022\Balance\local\Italy\Italy\Reports\Gas Balance\Bilancio_GAS_2020_05.xlsx', sheet_name = 'Preconsuntivo maggio  2020')
B = [["2020", "5", table.iloc[5,3], table.iloc[5,6]], \
     ["2020", "5", table.iloc[6,3], table.iloc[6,6]], \
     ["2020", "5", table.iloc[7,4], table.iloc[7,6]], \
     ["2020", "5", table.iloc[8,4], table.iloc[8,6]], \
     ["2020", "5", table.iloc[9,4], table.iloc[9,6]], \
     ["2020", "5", table.iloc[10,4], table.iloc[10,6]], \
     ["2020", "5", table.iloc[11,4], table.iloc[11,6]], \
     ["2020", "5", table.iloc[12,4], table.iloc[12,6]], \
     ["2020", "5", table.iloc[13,4], table.iloc[13,6]], \
     ["2020", "5", table.iloc[14,4], table.iloc[14,6]], \
     ["2020", "5", table.iloc[15,4], table.iloc[15,6]], \
     ["2020", "5", table.iloc[16,3], table.iloc[16,6]], \
     ["2020", "5", table.iloc[17,3], table.iloc[17,6]], \
     ["2020", "5", table.iloc[18,3], table.iloc[18,6]]]
     
Mag20 = pd.DataFrame(B,columns=["year", "monnth", "sector", "value"])

table = pd.read_excel(r'C:\Users\jiaxi\OneDrive\Desktop\RBAC 2022\Balance\local\Italy\Italy\Reports\Gas Balance\Bilancio_GAS_2020_06.xlsx', sheet_name = 'Preconsuntivo giugno  2020')
B = [["2020", "6", table.iloc[5,3], table.iloc[5,6]], \
     ["2020", "6", table.iloc[6,3], table.iloc[6,6]], \
     ["2020", "6", table.iloc[7,4], table.iloc[7,6]], \
     ["2020", "6", table.iloc[8,4], table.iloc[8,6]], \
     ["2020", "6", table.iloc[9,4], table.iloc[9,6]], \
     ["2020", "6", table.iloc[10,4], table.iloc[10,6]], \
     ["2020", "6", table.iloc[11,4], table.iloc[11,6]], \
     ["2020", "6", table.iloc[12,4], table.iloc[12,6]], \
     ["2020", "6", table.iloc[13,4], table.iloc[13,6]], \
     ["2020", "6", table.iloc[14,4], table.iloc[14,6]], \
     ["2020", "6", table.iloc[15,4], table.iloc[15,6]], \
     ["2020", "6", table.iloc[16,3], table.iloc[16,6]], \
     ["2020", "6", table.iloc[17,3], table.iloc[17,6]], \
     ["2020", "6", table.iloc[18,3], table.iloc[18,6]]]
     
Giu20 = pd.DataFrame(B,columns=["year", "monnth", "sector", "value"])


table = pd.read_excel(r'C:\Users\jiaxi\OneDrive\Desktop\RBAC 2022\Balance\local\Italy\Italy\Reports\Gas Balance\Bilancio_GAS_2020_07.xlsx', sheet_name = 'Preconsuntivo luglio  2020')
B = [["2020", "7", table.iloc[5,3], table.iloc[5,6]], \
     ["2020", "7", table.iloc[6,3], table.iloc[6,6]], \
     ["2020", "7", table.iloc[7,4], table.iloc[7,6]], \
     ["2020", "7", table.iloc[8,4], table.iloc[8,6]], \
     ["2020", "7", table.iloc[9,4], table.iloc[9,6]], \
     ["2020", "7", table.iloc[10,4], table.iloc[10,6]], \
     ["2020", "7", table.iloc[11,4], table.iloc[11,6]], \
     ["2020", "7", table.iloc[12,4], table.iloc[12,6]], \
     ["2020", "7", table.iloc[13,4], table.iloc[13,6]], \
     ["2020", "7", table.iloc[14,4], table.iloc[14,6]], \
     ["2020", "7", table.iloc[15,4], table.iloc[15,6]], \
     ["2020", "7", table.iloc[16,3], table.iloc[16,6]], \
     ["2020", "7", table.iloc[17,3], table.iloc[17,6]], \
     ["2020", "7", table.iloc[18,3], table.iloc[18,6]]]
     
Lug20 = pd.DataFrame(B,columns=["year", "monnth", "sector", "value"])

table = pd.read_excel(r'C:\Users\jiaxi\OneDrive\Desktop\RBAC 2022\Balance\local\Italy\Italy\Reports\Gas Balance\Bilancio_GAS_2020_08.xlsx', sheet_name = 'Preconsuntivo agosto  2020')
B = [["2020", "8", table.iloc[5,3], table.iloc[5,6]], \
     ["2020", "8", table.iloc[6,3], table.iloc[6,6]], \
     ["2020", "8", table.iloc[7,4], table.iloc[7,6]], \
     ["2020", "8", table.iloc[8,4], table.iloc[8,6]], \
     ["2020", "8", table.iloc[9,4], table.iloc[9,6]], \
     ["2020", "8", table.iloc[10,4], table.iloc[10,6]], \
     ["2020", "8", table.iloc[11,4], table.iloc[11,6]], \
     ["2020", "8", table.iloc[12,4], table.iloc[12,6]], \
     ["2020", "8", table.iloc[13,4], table.iloc[13,6]], \
     ["2020", "8", table.iloc[14,4], table.iloc[14,6]], \
     ["2020", "8", table.iloc[15,4], table.iloc[15,6]], \
     ["2020", "8", table.iloc[16,3], table.iloc[16,6]], \
     ["2020", "8", table.iloc[17,3], table.iloc[17,6]], \
     ["2020", "8", table.iloc[18,3], table.iloc[18,6]]]
     
Ago20 = pd.DataFrame(B,columns=["year", "monnth", "sector", "value"])

table = pd.read_excel(r'C:\Users\jiaxi\OneDrive\Desktop\RBAC 2022\Balance\local\Italy\Italy\Reports\Gas Balance\Bilancio_GAS_2020_09.xlsx', sheet_name = 'Preconsuntivo settembre  2020')
B = [["2020", "9", table.iloc[5,3], table.iloc[5,6]], \
     ["2020", "9", table.iloc[6,3], table.iloc[6,6]], \
     ["2020", "9", table.iloc[7,4], table.iloc[7,6]], \
     ["2020", "9", table.iloc[8,4], table.iloc[8,6]], \
     ["2020", "9", table.iloc[9,4], table.iloc[9,6]], \
     ["2020", "9", table.iloc[10,4], table.iloc[10,6]], \
     ["2020", "9", table.iloc[11,4], table.iloc[11,6]], \
     ["2020", "9", table.iloc[12,4], table.iloc[12,6]], \
     ["2020", "9", table.iloc[13,4], table.iloc[13,6]], \
     ["2020", "9", table.iloc[14,4], table.iloc[14,6]], \
     ["2020", "9", table.iloc[15,4], table.iloc[15,6]], \
     ["2020", "9", table.iloc[16,3], table.iloc[16,6]], \
     ["2020", "9", table.iloc[17,3], table.iloc[17,6]], \
     ["2020", "9", table.iloc[18,3], table.iloc[18,6]]]
     
Set20 = pd.DataFrame(B,columns=["year", "monnth", "sector", "value"])


table = pd.read_excel(r'C:\Users\jiaxi\OneDrive\Desktop\RBAC 2022\Balance\local\Italy\Italy\Reports\Gas Balance\Bilancio_GAS_2020_10.xlsx', sheet_name = 'Preconsuntivo ottobre  2020')
B = [["2020", "10", table.iloc[5,3], table.iloc[5,6]], \
     ["2020", "10", table.iloc[6,3], table.iloc[6,6]], \
     ["2020", "10", table.iloc[7,4], table.iloc[7,6]], \
     ["2020", "10", table.iloc[8,4], table.iloc[8,6]], \
     ["2020", "10", table.iloc[9,4], table.iloc[9,6]], \
     ["2020", "10", table.iloc[10,4], table.iloc[10,6]], \
     ["2020", "10", table.iloc[11,4], table.iloc[11,6]], \
     ["2020", "10", table.iloc[12,4], table.iloc[12,6]], \
     ["2020", "10", table.iloc[13,4], table.iloc[13,6]], \
     ["2020", "10", table.iloc[14,4], table.iloc[14,6]], \
     ["2020", "10", table.iloc[15,4], table.iloc[15,6]], \
     ["2020", "10", table.iloc[16,3], table.iloc[16,6]], \
     ["2020", "10", table.iloc[17,3], table.iloc[17,6]], \
     ["2020", "10", table.iloc[18,3], table.iloc[18,6]]]
     
Ott20 = pd.DataFrame(B,columns=["year", "monnth", "sector", "value"])


table = pd.read_excel(r'C:\Users\jiaxi\OneDrive\Desktop\RBAC 2022\Balance\local\Italy\Italy\Reports\Gas Balance\Bilancio_GAS_2020_11.xlsx', sheet_name = 'Preconsuntivo novembre  2020')
B = [["2020", "11", table.iloc[5,3], table.iloc[5,6]], \
     ["2020", "11", table.iloc[6,3], table.iloc[6,6]], \
     ["2020", "11", table.iloc[7,4], table.iloc[7,6]], \
     ["2020", "11", table.iloc[8,4], table.iloc[8,6]], \
     ["2020", "11", table.iloc[9,4], table.iloc[9,6]], \
     ["2020", "11", table.iloc[10,4], table.iloc[10,6]], \
     ["2020", "11", table.iloc[11,4], table.iloc[11,6]], \
     ["2020", "11", table.iloc[12,4], table.iloc[12,6]], \
     ["2020", "11", table.iloc[13,4], table.iloc[13,6]], \
     ["2020", "11", table.iloc[14,4], table.iloc[14,6]], \
     ["2020", "11", table.iloc[15,4], table.iloc[15,6]], \
     ["2020", "11", table.iloc[16,3], table.iloc[16,6]], \
     ["2020", "11", table.iloc[17,3], table.iloc[17,6]], \
     ["2020", "11", table.iloc[18,3], table.iloc[18,6]]]
     
Nov20 = pd.DataFrame(B,columns=["year", "monnth", "sector", "value"])

table = pd.read_excel(r'C:\Users\jiaxi\OneDrive\Desktop\RBAC 2022\Balance\local\Italy\Italy\Reports\Gas Balance\Bilancio_GAS_2020_12.xlsx', sheet_name = 'Preconsuntivo dicembre  2020')
B = [["2020", "12", table.iloc[5,3], table.iloc[5,6]], \
     ["2020", "12", table.iloc[6,3], table.iloc[6,6]], \
     ["2020", "12", table.iloc[7,4], table.iloc[7,6]], \
     ["2020", "12", table.iloc[8,4], table.iloc[8,6]], \
     ["2020", "12", table.iloc[9,4], table.iloc[9,6]], \
     ["2020", "12", table.iloc[10,4], table.iloc[10,6]], \
     ["2020", "12", table.iloc[11,4], table.iloc[11,6]], \
     ["2020", "12", table.iloc[12,4], table.iloc[12,6]], \
     ["2020", "12", table.iloc[13,4], table.iloc[13,6]], \
     ["2020", "12", table.iloc[14,4], table.iloc[14,6]], \
     ["2020", "12", table.iloc[15,4], table.iloc[15,6]], \
     ["2020", "12", table.iloc[16,4], table.iloc[16,6]], \
     ["2020", "12", table.iloc[17,3], table.iloc[17,6]], \
     ["2020", "12", table.iloc[18,3], table.iloc[18,6]], \
     ["2020", "12", table.iloc[19,3], table.iloc[19,6]]]
     
Dic20 = pd.DataFrame(B,columns=["year", "monnth", "sector", "value"])


##2021
table = pd.read_excel(r'C:\Users\jiaxi\OneDrive\Desktop\RBAC 2022\Balance\local\Italy\Italy\Reports\Gas Balance\Bilancio_GAS_2021_01.xlsx', sheet_name = 'Preconsuntivo Gennaio  2021')
B = [["2021", "1", table.iloc[5,3], table.iloc[5,6]], \
     ["2021", "1", table.iloc[6,3], table.iloc[6,6]], \
     ["2021", "1", table.iloc[7,4], table.iloc[7,6]], \
     ["2021", "1", table.iloc[8,4], table.iloc[8,6]], \
     ["2021", "1", table.iloc[9,4], table.iloc[9,6]], \
     ["2021", "1", table.iloc[10,4], table.iloc[10,6]], \
     ["2021", "1", table.iloc[11,4], table.iloc[11,6]], \
     ["2021", "1", table.iloc[12,4], table.iloc[12,6]], \
     ["2021", "1", table.iloc[13,4], table.iloc[13,6]], \
     ["2021", "1", table.iloc[14,4], table.iloc[14,6]], \
     ["2021", "1", table.iloc[15,4], table.iloc[15,6]], \
     ["2021", "1", table.iloc[16,4], table.iloc[16,6]], \
     ["2021", "1", table.iloc[17,3], table.iloc[17,6]], \
     ["2021", "1", table.iloc[18,3], table.iloc[18,6]], \
     ["2021", "1", table.iloc[19,3], table.iloc[19,6]]]
     
Gen21 = pd.DataFrame(B,columns=["year", "monnth", "sector", "value"])

table = pd.read_excel(r'C:\Users\jiaxi\OneDrive\Desktop\RBAC 2022\Balance\local\Italy\Italy\Reports\Gas Balance\Bilancio_GAS_2021_02.xlsx', sheet_name = 'Preconsuntivo Febbraio  2021')
B = [["2021", "2", table.iloc[5,3], table.iloc[5,6]], \
     ["2021", "2", table.iloc[6,3], table.iloc[6,6]], \
     ["2021", "2", table.iloc[7,4], table.iloc[7,6]], \
     ["2021", "2", table.iloc[8,4], table.iloc[8,6]], \
     ["2021", "2", table.iloc[9,4], table.iloc[9,6]], \
     ["2021", "2", table.iloc[10,4], table.iloc[10,6]], \
     ["2021", "2", table.iloc[11,4], table.iloc[11,6]], \
     ["2021", "2", table.iloc[12,4], table.iloc[12,6]], \
     ["2021", "2", table.iloc[13,4], table.iloc[13,6]], \
     ["2021", "2", table.iloc[14,4], table.iloc[14,6]], \
     ["2021", "2", table.iloc[15,4], table.iloc[15,6]], \
     ["2021", "2", table.iloc[16,4], table.iloc[16,6]], \
     ["2021", "2", table.iloc[17,3], table.iloc[17,6]], \
     ["2021", "2", table.iloc[18,3], table.iloc[18,6]], \
     ["2021", "2", table.iloc[19,3], table.iloc[19,6]]]
     
Feb21 = pd.DataFrame(B,columns=["year", "monnth", "sector", "value"])

table = pd.read_excel(r'C:\Users\jiaxi\OneDrive\Desktop\RBAC 2022\Balance\local\Italy\Italy\Reports\Gas Balance\Bilancio_GAS_2021_03.xlsx', sheet_name = 'Preconsuntivo Marzo  2021')
B = [["2021", "3", table.iloc[5,3], table.iloc[5,6]], \
     ["2021", "3", table.iloc[6,3], table.iloc[6,6]], \
     ["2021", "3", table.iloc[7,4], table.iloc[7,6]], \
     ["2021", "3", table.iloc[8,4], table.iloc[8,6]], \
     ["2021", "3", table.iloc[9,4], table.iloc[9,6]], \
     ["2021", "3", table.iloc[10,4], table.iloc[10,6]], \
     ["2021", "3", table.iloc[11,4], table.iloc[11,6]], \
     ["2021", "3", table.iloc[12,4], table.iloc[12,6]], \
     ["2021", "3", table.iloc[13,4], table.iloc[13,6]], \
     ["2021", "3", table.iloc[14,4], table.iloc[14,6]], \
     ["2021", "3", table.iloc[15,4], table.iloc[15,6]], \
     ["2021", "3", table.iloc[16,4], table.iloc[16,6]], \
     ["2021", "3", table.iloc[17,3], table.iloc[17,6]], \
     ["2021", "3", table.iloc[18,3], table.iloc[18,6]], \
     ["2021", "3", table.iloc[19,3], table.iloc[19,6]]]
     
Mar21 = pd.DataFrame(B,columns=["year", "monnth", "sector", "value"])

table = pd.read_excel(r'C:\Users\jiaxi\OneDrive\Desktop\RBAC 2022\Balance\local\Italy\Italy\Reports\Gas Balance\Bilancio_GAS_2021_04.xlsx', sheet_name = 'Preconsuntivo Aprile  2021')
B = [["2021", "4", table.iloc[5,3], table.iloc[5,6]], \
     ["2021", "4", table.iloc[6,3], table.iloc[6,6]], \
     ["2021", "4", table.iloc[7,4], table.iloc[7,6]], \
     ["2021", "4", table.iloc[8,4], table.iloc[8,6]], \
     ["2021", "4", table.iloc[9,4], table.iloc[9,6]], \
     ["2021", "4", table.iloc[10,4], table.iloc[10,6]], \
     ["2021", "4", table.iloc[11,4], table.iloc[11,6]], \
     ["2021", "4", table.iloc[12,4], table.iloc[12,6]], \
     ["2021", "4", table.iloc[13,4], table.iloc[13,6]], \
     ["2021", "4", table.iloc[14,4], table.iloc[14,6]], \
     ["2021", "4", table.iloc[15,4], table.iloc[15,6]], \
     ["2021", "4", table.iloc[16,4], table.iloc[16,6]], \
     ["2021", "4", table.iloc[17,3], table.iloc[17,6]], \
     ["2021", "4", table.iloc[18,3], table.iloc[18,6]], \
     ["2021", "4", table.iloc[19,3], table.iloc[19,6]]]
     
Apr21 = pd.DataFrame(B,columns=["year", "monnth", "sector", "value"])

table = pd.read_excel(r'C:\Users\jiaxi\OneDrive\Desktop\RBAC 2022\Balance\local\Italy\Italy\Reports\Gas Balance\Bilancio_GAS_2021_05.xlsx', sheet_name = 'Preconsuntivo maggio  2021')
B = [["2021", "5", table.iloc[5,3], table.iloc[5,6]], \
     ["2021", "5", table.iloc[6,3], table.iloc[6,6]], \
     ["2021", "5", table.iloc[7,4], table.iloc[7,6]], \
     ["2021", "5", table.iloc[8,4], table.iloc[8,6]], \
     ["2021", "5", table.iloc[9,4], table.iloc[9,6]], \
     ["2021", "5", table.iloc[10,4], table.iloc[10,6]], \
     ["2021", "5", table.iloc[11,4], table.iloc[11,6]], \
     ["2021", "5", table.iloc[12,4], table.iloc[12,6]], \
     ["2021", "5", table.iloc[13,4], table.iloc[13,6]], \
     ["2021", "5", table.iloc[14,4], table.iloc[14,6]], \
     ["2021", "5", table.iloc[15,4], table.iloc[15,6]], \
     ["2021", "5", table.iloc[16,4], table.iloc[16,6]], \
     ["2021", "5", table.iloc[17,3], table.iloc[17,6]], \
     ["2021", "5", table.iloc[18,3], table.iloc[18,6]], \
     ["2021", "5", table.iloc[19,3], table.iloc[19,6]]]
     
Mag21 = pd.DataFrame(B,columns=["year", "monnth", "sector", "value"])

table = pd.read_excel(r'C:\Users\jiaxi\OneDrive\Desktop\RBAC 2022\Balance\local\Italy\Italy\Reports\Gas Balance\Bilancio_GAS_2021_06.xlsx', sheet_name = 'Preconsuntivo giugno 2021')
B = [["2021", "6", table.iloc[5,3], table.iloc[5,6]], \
     ["2021", "6", table.iloc[6,3], table.iloc[6,6]], \
     ["2021", "6", table.iloc[7,4], table.iloc[7,6]], \
     ["2021", "6", table.iloc[8,4], table.iloc[8,6]], \
     ["2021", "6", table.iloc[9,4], table.iloc[9,6]], \
     ["2021", "6", table.iloc[10,4], table.iloc[10,6]], \
     ["2021", "6", table.iloc[11,4], table.iloc[11,6]], \
     ["2021", "6", table.iloc[12,4], table.iloc[12,6]], \
     ["2021", "6", table.iloc[13,4], table.iloc[13,6]], \
     ["2021", "6", table.iloc[14,4], table.iloc[14,6]], \
     ["2021", "6", table.iloc[15,4], table.iloc[15,6]], \
     ["2021", "6", table.iloc[16,4], table.iloc[16,6]], \
     ["2021", "6", table.iloc[17,3], table.iloc[17,6]], \
     ["2021", "6", table.iloc[18,3], table.iloc[18,6]], \
     ["2021", "6", table.iloc[19,3], table.iloc[19,6]]]
     
Giu21 = pd.DataFrame(B,columns=["year", "monnth", "sector", "value"])


table = pd.read_excel(r'C:\Users\jiaxi\OneDrive\Desktop\RBAC 2022\Balance\local\Italy\Italy\Reports\Gas Balance\Bilancio_GAS_2021_07.xlsx', sheet_name = 'Preconsuntivo luglio 2021')
B = [["2021", "7", table.iloc[5,3], table.iloc[5,6]], \
     ["2021", "7", table.iloc[6,3], table.iloc[6,6]], \
     ["2021", "7", table.iloc[7,4], table.iloc[7,6]], \
     ["2021", "7", table.iloc[8,4], table.iloc[8,6]], \
     ["2021", "7", table.iloc[9,4], table.iloc[9,6]], \
     ["2021", "7", table.iloc[10,4], table.iloc[10,6]], \
     ["2021", "7", table.iloc[11,4], table.iloc[11,6]], \
     ["2021", "7", table.iloc[12,4], table.iloc[12,6]], \
     ["2021", "7", table.iloc[13,4], table.iloc[13,6]], \
     ["2021", "7", table.iloc[14,4], table.iloc[14,6]], \
     ["2021", "7", table.iloc[15,4], table.iloc[15,6]], \
     ["2021", "7", table.iloc[16,4], table.iloc[16,6]], \
     ["2021", "7", table.iloc[17,3], table.iloc[17,6]], \
     ["2021", "7", table.iloc[18,3], table.iloc[18,6]], \
     ["2021", "7", table.iloc[19,3], table.iloc[19,6]]]
     
Lug21 = pd.DataFrame(B,columns=["year", "monnth", "sector", "value"])

table = pd.read_excel(r'C:\Users\jiaxi\OneDrive\Desktop\RBAC 2022\Balance\local\Italy\Italy\Reports\Gas Balance\Bilancio_GAS_2021_08.xlsx', sheet_name = 'Preconsuntivo agosto 2021')
B = [["2021", "8", table.iloc[5,3], table.iloc[5,6]], \
     ["2021", "8", table.iloc[6,3], table.iloc[6,6]], \
     ["2021", "8", table.iloc[7,4], table.iloc[7,6]], \
     ["2021", "8", table.iloc[8,4], table.iloc[8,6]], \
     ["2021", "8", table.iloc[9,4], table.iloc[9,6]], \
     ["2021", "8", table.iloc[10,4], table.iloc[10,6]], \
     ["2021", "8", table.iloc[11,4], table.iloc[11,6]], \
     ["2021", "8", table.iloc[12,4], table.iloc[12,6]], \
     ["2021", "8", table.iloc[13,4], table.iloc[13,6]], \
     ["2021", "8", table.iloc[14,4], table.iloc[14,6]], \
     ["2021", "8", table.iloc[15,4], table.iloc[15,6]], \
     ["2021", "8", table.iloc[16,4], table.iloc[16,6]], \
     ["2021", "8", table.iloc[17,3], table.iloc[17,6]], \
     ["2021", "8", table.iloc[18,3], table.iloc[18,6]], \
     ["2021", "8", table.iloc[19,3], table.iloc[19,6]]]
     
Ago21 = pd.DataFrame(B,columns=["year", "monnth", "sector", "value"])

table = pd.read_excel(r'C:\Users\jiaxi\OneDrive\Desktop\RBAC 2022\Balance\local\Italy\Italy\Reports\Gas Balance\Bilancio_GAS_2021_09.xlsx', sheet_name = 'Preconsuntivo settembre 2021')
B = [["2021", "9", table.iloc[5,3], table.iloc[5,6]], \
     ["2021", "9", table.iloc[6,3], table.iloc[6,6]], \
     ["2021", "9", table.iloc[7,4], table.iloc[7,6]], \
     ["2021", "9", table.iloc[8,4], table.iloc[8,6]], \
     ["2021", "9", table.iloc[9,4], table.iloc[9,6]], \
     ["2021", "9", table.iloc[10,4], table.iloc[10,6]], \
     ["2021", "9", table.iloc[11,4], table.iloc[11,6]], \
     ["2021", "9", table.iloc[12,4], table.iloc[12,6]], \
     ["2021", "9", table.iloc[13,4], table.iloc[13,6]], \
     ["2021", "9", table.iloc[14,4], table.iloc[14,6]], \
     ["2021", "9", table.iloc[15,4], table.iloc[15,6]], \
     ["2021", "9", table.iloc[16,4], table.iloc[16,6]], \
     ["2021", "9", table.iloc[17,3], table.iloc[17,6]], \
     ["2021", "9", table.iloc[18,3], table.iloc[18,6]], \
     ["2021", "9", table.iloc[19,3], table.iloc[19,6]]]
     
Set21 = pd.DataFrame(B,columns=["year", "monnth", "sector", "value"])


table = pd.read_excel(r'C:\Users\jiaxi\OneDrive\Desktop\RBAC 2022\Balance\local\Italy\Italy\Reports\Gas Balance\Bilancio_GAS_2021_10.xlsx', sheet_name = 'Preconsuntivo ottobre 2021')
B = [["2021", "10", table.iloc[5,3], table.iloc[5,6]], \
     ["2021", "10", table.iloc[6,3], table.iloc[6,6]], \
     ["2021", "10", table.iloc[7,4], table.iloc[7,6]], \
     ["2021", "10", table.iloc[8,4], table.iloc[8,6]], \
     ["2021", "10", table.iloc[9,4], table.iloc[9,6]], \
     ["2021", "10", table.iloc[10,4], table.iloc[10,6]], \
     ["2021", "10", table.iloc[11,4], table.iloc[11,6]], \
     ["2021", "10", table.iloc[12,4], table.iloc[12,6]], \
     ["2021", "10", table.iloc[13,4], table.iloc[13,6]], \
     ["2021", "10", table.iloc[14,4], table.iloc[14,6]], \
     ["2021", "10", table.iloc[15,4], table.iloc[15,6]], \
     ["2021", "10", table.iloc[16,4], table.iloc[16,6]], \
     ["2021", "10", table.iloc[17,3], table.iloc[17,6]], \
     ["2021", "10", table.iloc[18,3], table.iloc[18,6]], \
     ["2021", "10", table.iloc[19,3], table.iloc[19,6]]]
     
Ott21 = pd.DataFrame(B,columns=["year", "monnth", "sector", "value"])


table = pd.read_excel(r'C:\Users\jiaxi\OneDrive\Desktop\RBAC 2022\Balance\local\Italy\Italy\Reports\Gas Balance\Bilancio_GAS_2021_11.xlsx', sheet_name = 'Preconsuntivo novembre 2021')
B = [["2021", "11", table.iloc[5,3], table.iloc[5,6]], \
     ["2021", "11", table.iloc[6,3], table.iloc[6,6]], \
     ["2021", "11", table.iloc[7,4], table.iloc[7,6]], \
     ["2021", "11", table.iloc[8,4], table.iloc[8,6]], \
     ["2021", "11", table.iloc[9,4], table.iloc[9,6]], \
     ["2021", "11", table.iloc[10,4], table.iloc[10,6]], \
     ["2021", "11", table.iloc[11,4], table.iloc[11,6]], \
     ["2021", "11", table.iloc[12,4], table.iloc[12,6]], \
     ["2021", "11", table.iloc[13,4], table.iloc[13,6]], \
     ["2021", "11", table.iloc[14,4], table.iloc[14,6]], \
     ["2021", "11", table.iloc[15,4], table.iloc[15,6]], \
     ["2021", "11", table.iloc[16,4], table.iloc[16,6]], \
     ["2021", "11", table.iloc[17,3], table.iloc[17,6]], \
     ["2021", "11", table.iloc[18,3], table.iloc[18,6]], \
     ["2021", "11", table.iloc[19,3], table.iloc[19,6]]]
     
Nov21 = pd.DataFrame(B,columns=["year", "monnth", "sector", "value"])

table = pd.read_excel(r'C:\Users\jiaxi\OneDrive\Desktop\RBAC 2022\Balance\local\Italy\Italy\Reports\Gas Balance\Bilancio_GAS_2021_12.xlsx', sheet_name = 'Preconsuntivo dicembre 2021')
B = [["2021", "12", table.iloc[5,3], table.iloc[5,6]], \
     ["2021", "12", table.iloc[6,3], table.iloc[6,6]], \
     ["2021", "12", table.iloc[7,4], table.iloc[7,6]], \
     ["2021", "12", table.iloc[8,4], table.iloc[8,6]], \
     ["2021", "12", table.iloc[9,4], table.iloc[9,6]], \
     ["2021", "12", table.iloc[10,4], table.iloc[10,6]], \
     ["2021", "12", table.iloc[11,4], table.iloc[11,6]], \
     ["2021", "12", table.iloc[12,4], table.iloc[12,6]], \
     ["2021", "12", table.iloc[13,4], table.iloc[13,6]], \
     ["2021", "12", table.iloc[14,4], table.iloc[14,6]], \
     ["2021", "12", table.iloc[15,4], table.iloc[15,6]], \
     ["2021", "12", table.iloc[16,4], table.iloc[16,6]], \
     ["2021", "12", table.iloc[17,3], table.iloc[17,6]], \
     ["2021", "12", table.iloc[18,3], table.iloc[18,6]], \
     ["2021", "12", table.iloc[19,3], table.iloc[19,6]]]
     
Dic21 = pd.DataFrame(B,columns=["year", "monnth", "sector", "value"])


##2022
table = pd.read_excel(r'C:\Users\jiaxi\OneDrive\Desktop\RBAC 2022\Balance\local\Italy\Italy\Reports\Gas Balance\Bilancio_GAS_2022_01.xlsx', sheet_name = 'Preconsuntivo Gennaio  2022')
B = [["2022", "1", table.iloc[5,3], table.iloc[5,6]], \
     ["2022", "1", table.iloc[6,3], table.iloc[6,6]], \
     ["2022", "1", table.iloc[7,4], table.iloc[7,6]], \
     ["2022", "1", table.iloc[8,4], table.iloc[8,6]], \
     ["2022", "1", table.iloc[9,4], table.iloc[9,6]], \
     ["2022", "1", table.iloc[10,4], table.iloc[10,6]], \
     ["2022", "1", table.iloc[11,4], table.iloc[11,6]], \
     ["2022", "1", table.iloc[12,4], table.iloc[12,6]], \
     ["2022", "1", table.iloc[13,4], table.iloc[13,6]], \
     ["2022", "1", table.iloc[14,4], table.iloc[14,6]], \
     ["2022", "1", table.iloc[15,4], table.iloc[15,6]], \
     ["2022", "1", table.iloc[16,4], table.iloc[16,6]], \
     ["2022", "1", table.iloc[17,3], table.iloc[17,6]], \
     ["2022", "1", table.iloc[18,3], table.iloc[18,6]], \
     ["2022", "1", table.iloc[19,3], table.iloc[19,6]]]
     
Gen22 = pd.DataFrame(B,columns=["year", "monnth", "sector", "value"])

table = pd.read_excel(r'C:\Users\jiaxi\OneDrive\Desktop\RBAC 2022\Balance\local\Italy\Italy\Reports\Gas Balance\Bilancio_GAS_2022_02.xlsx', sheet_name = 'Preconsuntivo febbraio  2022')
B = [["2022", "2", table.iloc[5,3], table.iloc[5,6]], \
     ["2022", "2", table.iloc[6,3], table.iloc[6,6]], \
     ["2022", "2", table.iloc[7,4], table.iloc[7,6]], \
     ["2022", "2", table.iloc[8,4], table.iloc[8,6]], \
     ["2022", "2", table.iloc[9,4], table.iloc[9,6]], \
     ["2022", "2", table.iloc[10,4], table.iloc[10,6]], \
     ["2022", "2", table.iloc[11,4], table.iloc[11,6]], \
     ["2022", "2", table.iloc[12,4], table.iloc[12,6]], \
     ["2022", "2", table.iloc[13,4], table.iloc[13,6]], \
     ["2022", "2", table.iloc[14,4], table.iloc[14,6]], \
     ["2022", "2", table.iloc[15,4], table.iloc[15,6]], \
     ["2022", "2", table.iloc[16,4], table.iloc[16,6]], \
     ["2022", "2", table.iloc[17,3], table.iloc[17,6]], \
     ["2022", "2", table.iloc[18,3], table.iloc[18,6]], \
     ["2022", "2", table.iloc[19,3], table.iloc[19,6]]]
     
Feb22 = pd.DataFrame(B,columns=["year", "monnth", "sector", "value"])

table = pd.read_excel(r'C:\Users\jiaxi\OneDrive\Desktop\RBAC 2022\Balance\local\Italy\Italy\Reports\Gas Balance\Bilancio_GAS_2022_03.xlsx', sheet_name = 'Preconsuntivo Marzo  2022')
B = [["2022", "3", table.iloc[5,3], table.iloc[5,6]], \
     ["2022", "3", table.iloc[6,3], table.iloc[6,6]], \
     ["2022", "3", table.iloc[7,4], table.iloc[7,6]], \
     ["2022", "3", table.iloc[8,4], table.iloc[8,6]], \
     ["2022", "3", table.iloc[9,4], table.iloc[9,6]], \
     ["2022", "3", table.iloc[10,4], table.iloc[10,6]], \
     ["2022", "3", table.iloc[11,4], table.iloc[11,6]], \
     ["2022", "3", table.iloc[12,4], table.iloc[12,6]], \
     ["2022", "3", table.iloc[13,4], table.iloc[13,6]], \
     ["2022", "3", table.iloc[14,4], table.iloc[14,6]], \
     ["2022", "3", table.iloc[15,4], table.iloc[15,6]], \
     ["2022", "3", table.iloc[16,4], table.iloc[16,6]], \
     ["2022", "3", table.iloc[17,3], table.iloc[17,6]], \
     ["2022", "3", table.iloc[18,3], table.iloc[18,6]], \
     ["2022", "3", table.iloc[19,3], table.iloc[19,6]]]
     
Mar22 = pd.DataFrame(B,columns=["year", "monnth", "sector", "value"])

table = pd.read_excel(r'C:\Users\jiaxi\OneDrive\Desktop\RBAC 2022\Balance\local\Italy\Italy\Reports\Gas Balance\Bilancio_GAS_2022_04.xlsx', sheet_name = 'Preconsuntivo Aprile  2022')
B = [["2022", "4", table.iloc[5,3], table.iloc[5,6]], \
     ["2022", "4", table.iloc[6,3], table.iloc[6,6]], \
     ["2022", "4", table.iloc[7,4], table.iloc[7,6]], \
     ["2022", "4", table.iloc[8,4], table.iloc[8,6]], \
     ["2022", "4", table.iloc[9,4], table.iloc[9,6]], \
     ["2022", "4", table.iloc[10,4], table.iloc[10,6]], \
     ["2022", "4", table.iloc[11,4], table.iloc[11,6]], \
     ["2022", "4", table.iloc[12,4], table.iloc[12,6]], \
     ["2022", "4", table.iloc[13,4], table.iloc[13,6]], \
     ["2022", "4", table.iloc[14,4], table.iloc[14,6]], \
     ["2022", "4", table.iloc[15,4], table.iloc[15,6]], \
     ["2022", "4", table.iloc[16,4], table.iloc[16,6]], \
     ["2022", "4", table.iloc[17,3], table.iloc[17,6]], \
     ["2022", "4", table.iloc[18,3], table.iloc[18,6]], \
     ["2022", "4", table.iloc[19,3], table.iloc[19,6]]]
    
Apr22 = pd.DataFrame(B,columns=["year", "monnth", "sector", "value"])

table = pd.read_excel(r'C:\Users\jiaxi\OneDrive\Desktop\RBAC 2022\Balance\local\Italy\Italy\Reports\Gas Balance\Bilancio_GAS_2022_05.xlsx', sheet_name = 'Preconsuntivo Maggio  2022')
B = [["2022", "5", table.iloc[5,3], table.iloc[5,6]], \
     ["2022", "5", table.iloc[6,3], table.iloc[6,6]], \
     ["2022", "5", table.iloc[7,4], table.iloc[7,6]], \
     ["2022", "5", table.iloc[8,4], table.iloc[8,6]], \
     ["2022", "5", table.iloc[9,4], table.iloc[9,6]], \
     ["2022", "5", table.iloc[10,4], table.iloc[10,6]], \
     ["2022", "5", table.iloc[11,4], table.iloc[11,6]], \
     ["2022", "5", table.iloc[12,4], table.iloc[12,6]], \
     ["2022", "5", table.iloc[13,4], table.iloc[13,6]], \
     ["2022", "5", table.iloc[14,4], table.iloc[14,6]], \
     ["2022", "5", table.iloc[15,4], table.iloc[15,6]], \
     ["2022", "5", table.iloc[16,4], table.iloc[16,6]], \
     ["2022", "5", table.iloc[17,3], table.iloc[17,6]], \
     ["2022", "5", table.iloc[18,3], table.iloc[18,6]], \
     ["2022", "5", table.iloc[19,3], table.iloc[19,6]]]
     
Mag22 = pd.DataFrame(B,columns=["year", "monnth", "sector", "value"])

table = pd.read_excel(r'C:\Users\jiaxi\OneDrive\Desktop\RBAC 2022\Balance\local\Italy\Italy\Reports\Gas Balance\Bilancio_GAS_2022_06.xlsx', sheet_name = 'Preconsuntivo Giugno  2022')
B = [["2022", "6", table.iloc[5,3], table.iloc[5,6]], \
     ["2022", "6", table.iloc[6,3], table.iloc[6,6]], \
     ["2022", "6", table.iloc[7,4], table.iloc[7,6]], \
     ["2022", "6", table.iloc[8,4], table.iloc[8,6]], \
     ["2022", "6", table.iloc[9,4], table.iloc[9,6]], \
     ["2022", "6", table.iloc[10,4], table.iloc[10,6]], \
     ["2022", "6", table.iloc[11,4], table.iloc[11,6]], \
     ["2022", "6", table.iloc[12,4], table.iloc[12,6]], \
     ["2022", "6", table.iloc[13,4], table.iloc[13,6]], \
     ["2022", "6", table.iloc[14,4], table.iloc[14,6]], \
     ["2022", "6", table.iloc[15,4], table.iloc[15,6]], \
     ["2022", "6", table.iloc[16,4], table.iloc[16,6]], \
     ["2022", "6", table.iloc[17,3], table.iloc[17,6]], \
     ["2022", "6", table.iloc[18,3], table.iloc[18,6]], \
     ["2022", "6", table.iloc[19,3], table.iloc[19,6]]]
     
Giu22 = pd.DataFrame(B,columns=["year", "monnth", "sector", "value"])

table = pd.read_excel(r'C:\Users\jiaxi\OneDrive\Desktop\RBAC 2022\Balance\local\Italy\Italy\Reports\Gas Balance\Bilancio_GAS_2022_07.xlsx', sheet_name = 'Preconsuntivo Luglio  2022')
B = [["2022", "7", table.iloc[5,3], table.iloc[5,6]], \
     ["2022", "7", table.iloc[6,3], table.iloc[6,6]], \
     ["2022", "7", table.iloc[7,4], table.iloc[7,6]], \
     ["2022", "7", table.iloc[8,4], table.iloc[8,6]], \
     ["2022", "7", table.iloc[9,4], table.iloc[9,6]], \
     ["2022", "7", table.iloc[10,4], table.iloc[10,6]], \
     ["2022", "7", table.iloc[11,4], table.iloc[11,6]], \
     ["2022", "7", table.iloc[12,4], table.iloc[12,6]], \
     ["2022", "7", table.iloc[13,4], table.iloc[13,6]], \
     ["2022", "7", table.iloc[14,4], table.iloc[14,6]], \
     ["2022", "7", table.iloc[15,4], table.iloc[15,6]], \
     ["2022", "7", table.iloc[16,4], table.iloc[16,6]], \
     ["2022", "7", table.iloc[17,3], table.iloc[17,6]], \
     ["2022", "7", table.iloc[18,3], table.iloc[18,6]], \
     ["2022", "7", table.iloc[19,3], table.iloc[19,6]]]
     
Lug22 = pd.DataFrame(B,columns=["year", "monnth", "sector", "value"])

Output1 = [Gen10, Feb10, Mar10, Apr10, Mag10, Giu10, Lug10, Ago10, Set10, Ott10, Nov10, Dic10, \
           Gen11, Feb11, Mar11, Apr11, Mag11, Giu11, Lug11, Ago11, Set11, Ott11, Nov11, Dic11, \
           Gen12, Feb12, Mar12, Apr12, Mag12, Giu12, Lug12, Ago12, Set12, Ott12, Nov12, Dic12, \
           Gen13, Feb13, Mar13, Apr13, Mag13, Giu13, Lug13, Ago13, Set13, Ott13, Nov13, Dic13, \
           Gen14, Feb14, Mar14, Apr14, Mag14, Giu14, Lug14, Ago14, Set14, Ott14, Nov14, Dic14, \
           Gen15, Feb15, Mar15, Apr15, Mag15, Giu15, Lug15, Ago15, Set15, Ott15, Nov15, Dic15, \
           Gen16, Feb16, Mar16, Apr16, Mag16, Giu16, Lug16, Ago16, Set16, Ott16, Nov16, Dic16, \
           Gen17, Feb17, Mar17, Apr17, Mag17, Giu17, Lug17, Ago17, Set17, Ott17, Nov17, Dic17, \
           Gen18, Feb18, Mar18, Apr18, Mag18, Giu18, Lug18, Ago18, Set18, Ott18, Nov18, Dic18, \
           Gen19, Feb19, Mar19, Apr19, Mag19, Giu19, Lug19, Ago19, Set19, Ott19, Nov19, Dic19, \
           Gen20, Feb20, Mar20, Apr20, Mag20, Giu20, Lug20, Ago20, Set20, Ott20, Nov20, Dic20, \
           Gen21, Feb21, Mar21, Apr21, Mag21, Giu21, Lug21, Ago21, Set21, Ott21, Nov21, Dic21, \
           Gen22, Feb22, Mar22, Apr22, Mag22, Giu22]

Output2 = pd.concat(Output1)

Output2.to_csv("C:\\Users\\jiaxi\\OneDrive\\Desktop\\RBAC 2022\\Balance\\local\\Italy\\Italy Balance Output.csv",index=None)


endtime = datetime.datetime.now()
print("Congradulations! Finished") 
print("duraion", endtime - starttime)
