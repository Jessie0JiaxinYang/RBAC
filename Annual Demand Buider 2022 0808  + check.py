# -*- coding: utf-8 -*-
# 2021 0428 
# finished com, ind, res, trn in one file


# 2021 0625： transfer the format that Birdy needs.

# 2021 0628: big bug.....
#            line 136, data should equal to "country_data", not "data". If just "data", one method under different 
#            countries are the same, see in "scenarios-results total 2021 0624 and you will find that.

# 2021 0628: add forecast into this 

# 2021 0701: delete when independent variable is more than 5

# 2021 0702: delete wrong combination which has cross-term variables
#            add pet sector into this 

# 2021 0707: replace pet with ind3
#            change format of cagr into another one, more convenient

# 2021 0708： fixed Algeria in com
#            made an easier selection for final scenario
#            combined final scenario into total scenario 
#            which means one run-file for all demand annual buider. only 18 minutes. 


# 2021 0820： updated till 2019 with UN
#            fixed the bug for double regression types

# 2021 0917： found the bug about the zigzag in results for those whose regression types include urban population
#            changed ind final regression type

# 2021 0921: deleted superfluous regression types 
#            cut ruuning time with 4 minutes

# 2021 0922: add year dummy

# 2021 1005: updated IMF till 2026, which is updated in April 2021,
# fixed 2020 decrease

# 2021 1020： add lgdpp^2, try

# 2021 1030: replace UN country with GPU country

# 2022 0208: add checks

# 2022 0714： annual update，independent variables and UN gas. history year till 2025

# 2022 0715: history year till 2022

# 2022 0803 update: reason to update: in UNGas in input data, forgot to drag dowm when transferring the format

# 2022 0808： update

import pandas as pd
import numpy as np
from itertools import combinations
import datetime
from pandas.core.frame import DataFrame
import math

starttime = datetime.datetime.now()

import statsmodels.formula.api as smf  # this allows us to write down our statistical model with an R-like string
import statsmodels.stats.api as sms  # not needed unless you want to run a test
import statsmodels.api as sm # not needed unless you want to do something fancier
from statsmodels.compat import lzip # useful for printing out complicated test statistics, also not needed now

table1 = pd.read_excel(r'C:\Users\jiaxi\OneDrive\Desktop\RBAC 2022\Demand\Demand Annual Builder\2022 0808\Input Data 2022 0808-run.xlsx', sheet_name = 'Target2')
table =table1.iloc[6:, 31: ]

table.columns = [ 'Country', 'Year', 'lcom', 'lelc', 'lind', 'lres', 'ltrn', 'lpet' ,'lgdp', 'lppl', 'lgdpp', 'lgdpp2', 'lgdp_man', 'lche', 'lfoo', 'lmac', 'ltex', 'loth', 'luppl', 'llf', 'lgop', 'lgou', 'lpou', 'lgasprice', 'loilprice','coviddummy']
table[['Year']] = table[['Year']].astype('float')
table[['lcom']] = table[['lcom']].astype('float')
table[['lelc']] = table[['lelc']].astype('float')
table[['lind']] = table[['lind']].astype('float')
table[['lres']] = table[['lres']].astype('float')
table[['ltrn']] = table[['ltrn']].astype('float')
table[['lpet']] = table[['lpet']].astype('float')
table[['lgdp']] = table[['lgdp']].astype('float')
table[['lppl']] = table[['lppl']].astype('float')
table[['lgdpp']] = table[['lgdpp']].astype('float')
table[['lgdpp2']] = table[['lgdpp2']].astype('float')
table[['lgdp_man']] = table[['lgdp_man']].astype('float')
table[['lche']] = table[['lche']].astype('float')
table[['lfoo']] = table[['lfoo']].astype('float')
table[['lmac']] = table[['lmac']].astype('float')
table[['ltex']] = table[['ltex']].astype('float')
table[['loth']] = table[['loth']].astype('float')
table[['luppl']] = table[['luppl']].astype('float')
table[['llf']] = table[['llf']].astype('float')
table[['lgop']] = table[['lgop']].astype('float')
table[['lgou']] = table[['lgou']].astype('float')
table[['lpou']] = table[['lpou']].astype('float')
table[['lgasprice']] = table[['lgasprice']].astype('float')
table[['loilprice']] = table[['loilprice']].astype('float')
table[['coviddummy']] = table[['coviddummy']].astype('float')

yrs = pd.read_excel(r'C:\Users\jiaxi\OneDrive\Desktop\RBAC 2022\Demand\Demand Annual Builder\2022 0808\Input Final Scenario 2022 0808.xlsx', sheet_name = 'Yr_Index')

# COM
data = table.drop(['lelc', 'lind', 'lres', 'ltrn', 'lpet', 'lgdp_man', 'lche', 'lfoo', 'lmac', 'ltex', 'loth', 'lgasprice', 'loilprice'], axis = 1)

r_table = pd.read_excel(r'C:\\Users\\jiaxi\\OneDrive\\Desktop\\RBAC 2022\\Demand\\Demand Annual Builder\\2022 0808\\Input Scenarios 2022 0808.xlsx', sheet_name = 'COM')
comcountry = r_table.loc[:,['Country ID',  'Country']]

country_name = r_table['Country'].to_list()

ref_country = table['Country'].unique()

df = pd.DataFrame()
df2 = pd.DataFrame()
df3 = pd.DataFrame()
df4 = pd.DataFrame()

for i in country_name:
    if i != 'ALL':
        if i in ref_country:

                Country = data[data['Country']== i]
                country_filter = r_table[r_table['Country']== i]
                
                retr_country = country_filter['Country'].to_list()[0]
                
                country_data = data[data['Country']==retr_country]

                x_labels = country_filter[['x0','x1','x2','x3','x4','x5','x6','x7', 'x8', 'x9', 'coviddummy', 'y']]
                rid = country_filter['Country ID'].tolist()[0]
                y_var = x_labels['y'].to_list()[0]

                def subcombs_2(dset):
                    data_ = []
                    for i in range(1,len(dset)+1):
                        for j in combinations(dset,i):
                            data_.append(list(j))
                    return data_


                def stitch(f):
                    out = ""
                    for k,i in enumerate(f):
                        if len(i) > 1:
                            out += i
                        else:
                            try:
                                out += i
                            except:
                                out +=i[0]
                        if k < len(f)-1:
                            out+=" + "
                    return out

                regressors = ['lgdp', 'lppl', 'lgdpp', 'luppl', 'llf']
                allcombs = subcombs_2(regressors)               
                del allcombs[0:]
                allcombs.append(['lgdp' , 'coviddummy'])
                allcombs.append(['lgdpp' , 'coviddummy'])
                allcombs.append(['lgdpp2' , 'coviddummy'])
                allcombs.append(['lppl' , 'coviddummy'])
                allcombs.append(['luppl' , 'coviddummy'])               
                allcombs.append(['lgdp' , 'lppl', 'coviddummy'])
                allcombs.append(['lgdp' , 'luppl', 'coviddummy'])
                allcombs.append(['lgdpp' , 'llf', 'coviddummy'])
                allcombs.append(['lgdpp' , 'luppl', 'coviddummy'])
                allcombs.append(['lppl' , 'luppl', 'coviddummy'])
                allcombs.append(['lgdp', 'lppl', 'lgdpp', 'coviddummy'])
                allcombs.append(['lgdp', 'lppl', 'lgop', 'coviddummy'])
                allcombs.append(['lppl', 'luppl', 'lpou', 'coviddummy'])
                allcombs.append(['lgdp', 'luppl', 'lgou', 'coviddummy'])
                

            
                
                aclist = []

                for i in allcombs:
                     aclist.append('lcom~'+stitch(i)) 

                for i in aclist:
                    model = smf.ols(i, data=country_data)

                    
                    results = model.fit()
                    a = i.replace('lcom~', '')
                    
                    values = pd.DataFrame(results.params).reset_index()
                    values.columns = ['names', 'coef']
                    xfinal = x_labels
                    xfinal['Intercept'] = 'Intercept'
                    xfinal = xfinal.T.reset_index()
                    xfinal.columns = ['labels', 'names']
                    export_val = xfinal.merge(values, on = 'names', how='left')
                    results.tvalues
                    t_stat = pd.DataFrame(results.tvalues).reset_index()
                    t_stat.columns = ['names', 't-statistic']
                    export_val1 = export_val.merge(t_stat, on = 'names', how='left')
                    # p-value
                    p_value = pd.DataFrame(results.pvalues).reset_index()
                    p_value.columns = ['names', 'p-value']
                    export_val1 = export_val1.merge(p_value, on = 'names', how='left')
                    
                    
                    r_columns = ['Year'] + values.xs("names", axis = 1).tolist()
                    del r_columns[1: 2]
                    forecast_var = country_data[r_columns].reset_index(drop=True)
                    forecast_var['Intercept'] = 1           
                    test = forecast_var[forecast_var['Year']>2022] # last history year
                    xval = test.drop(columns = ['Year'])

                    
                    entry2 = pd.DataFrame({'Country ID': [rid, rid, rid, rid,rid, rid, rid, rid, rid, rid, rid, rid],
                                   'R-square': [results.rsquared, results.rsquared, results.rsquared, results.rsquared, results.rsquared, results.rsquared, results.rsquared, results.rsquared, results.rsquared, results.rsquared, results.rsquared, results.rsquared],
                                   'RegType': [a, a, a, a, a, a, a, a, a, a, a, a],
                                   'CoeID': ['intercept', 'x0', 'x1', 'x2', 'x3', 'x4', 'x5', 'x6', 'x7', 'x8', 'x9', 'coviddummy'],
                                   'Coe': [export_val1[export_val1['labels']=='Intercept']['coef'].to_list()[0], export_val1[export_val1['labels']=='x0']['coef'].to_list()[0], export_val1[export_val1['labels']=='x1']['coef'].to_list()[0], export_val1[export_val1['labels']=='x2']['coef'].to_list()[0], export_val1[export_val1['labels']=='x3']['coef'].to_list()[0], export_val1[export_val1['labels']=='x4']['coef'].to_list()[0], export_val1[export_val1['labels']=='x5']['coef'].to_list()[0], export_val1[export_val1['labels']=='x6']['coef'].to_list()[0], export_val1[export_val1['labels']=='x7']['coef'].to_list()[0], export_val1[export_val1['labels']=='x8']['coef'].to_list()[0], export_val1[export_val1['labels']=='x9']['coef'].to_list()[0], export_val1[export_val1['labels']=='coviddummy']['coef'].to_list()[0]],
                                   'tvalueID': ['t_intercept', 't_x0', 't_x1', 't_x2', 't_x3', 't_x4', 't_x5', 't_x6', 't_x7', 't_x8', 't_x9', 't_coviddummy'],
                                   'tvalue': [export_val1[export_val1['labels']=='Intercept']['t-statistic'].to_list()[0], export_val1[export_val1['labels']=='x0']['t-statistic'].to_list()[0], export_val1[export_val1['labels']=='x1']['t-statistic'].to_list()[0], export_val1[export_val1['labels']=='x2']['t-statistic'].to_list()[0], export_val1[export_val1['labels']=='x3']['t-statistic'].to_list()[0], export_val1[export_val1['labels']=='x4']['t-statistic'].to_list()[0], export_val1[export_val1['labels']=='x5']['t-statistic'].to_list()[0], export_val1[export_val1['labels']=='x6']['t-statistic'].to_list()[0], export_val1[export_val1['labels']=='x7']['t-statistic'].to_list()[0], export_val1[export_val1['labels']=='x8']['t-statistic'].to_list()[0], export_val1[export_val1['labels']=='x9']['t-statistic'].to_list()[0], export_val1[export_val1['labels']=='coviddummy']['t-statistic'].to_list()[0]],
                                   'pvalueID': ['p_intercept', 'p_x0', 'p_x1', 'p_x2', 'p_x3', 'p_x4', 'p_x5', 'p_x6', 'p_x7', 'p_x8', 'p_x9', 'p_coviddummy'],
                                   'pvalue': [export_val1[export_val1['labels']=='Intercept']['p-value'].to_list()[0], export_val1[export_val1['labels']=='x0']['p-value'].to_list()[0], export_val1[export_val1['labels']=='x1']['p-value'].to_list()[0], export_val1[export_val1['labels']=='x2']['p-value'].to_list()[0], export_val1[export_val1['labels']=='x3']['p-value'].to_list()[0], export_val1[export_val1['labels']=='x4']['p-value'].to_list()[0], export_val1[export_val1['labels']=='x5']['p-value'].to_list()[0], export_val1[export_val1['labels']=='x6']['p-value'].to_list()[0], export_val1[export_val1['labels']=='x7']['p-value'].to_list()[0], export_val1[export_val1['labels']=='x8']['p-value'].to_list()[0], export_val1[export_val1['labels']=='x9']['p-value'].to_list()[0], export_val1[export_val1['labels']=='coviddummy']['p-value'].to_list()[0]]})
                    
                    y_hat = results.predict(xval) 
                    yr_p = yrs[yrs['Year']>=2023]  # first forecast year          
                    p_export = pd.concat([yr_p, y_hat], axis=1, sort=False)
                    p_export['Country ID'] = rid
                    p_export["RegType"] = a
                    
                    cagr = p_export
                    cagr.columns = ['Year', 'lvalue', 'Country ID', 'RegType']
                    cagr['value'] = math.exp(1) ** cagr['lvalue']                    
                    cagr['test1'] = cagr['Year'] % 5
                    def fun(x): # this function is to calculate cagr, test for delete useless rows
                      if x == 2023: # the base year that you would like to calculate cagr
                        return 0
                      else:
                        return 1
                    cagr['test2'] =cagr['Year'].apply(lambda x: fun(x))
                    cagr['test'] = cagr['test1'] * cagr['test2']
                    cagr = cagr.drop(cagr[cagr.test > 0].index)
                    cagr['CAGR'] = (cagr['value'] / cagr['value'].shift(+1) ) ** (1/(cagr['Year'] - cagr['Year'].shift(+1))) - 1
                    cagr = cagr.drop(['test1', 'test2', 'test'], axis = 1)
                    
                    cagr_check = cagr.drop(cagr[cagr.Year == 2025 ].index)
                    cagr_check = cagr_check.drop(cagr_check[cagr_check.Year == 2030 ].index)
                    cagr_check = cagr_check.drop(cagr_check[cagr_check.Year == 2035 ].index)
                    cagr_check = cagr_check.drop(cagr_check[cagr_check.Year == 2040 ].index)
                    cagr_check = cagr_check.drop(cagr_check[cagr_check.Year == 2045 ].index)
                    cagr_check = cagr_check.drop(['CAGR'], axis = 1)
                    cagr_check['CAGR'] = (cagr_check['value'] / cagr_check['value'].shift(+1) ) ** (1/27) - 1 # 2050 - base year
                    cagr_check = cagr_check.drop(cagr_check[cagr_check.Year == 2023 ].index) # the base year that you would like to calculate cagr

                    
                    p_export = p_export.drop(['test1', 'test2', 'test'], axis = 1)

                    df = pd.concat([df,entry2])
                    df2 = pd.concat([df2,p_export])
                    df3 = pd.concat([df3,cagr])
                    df4 = pd.concat([df4,cagr_check])
            
df.insert(1, "Sector", "com")
df = df[df['Coe'].notna()]
df = pd.merge(df,comcountry,on='Country ID',how='inner') 

df2["Sector"] = 'com'
df2.columns = ['Year', 'lvalue', 'Country ID', 'RegType', 'value', 'Sector']             
df2 = pd.merge(df2,comcountry,on='Country ID',how='inner') 

df3["Sector"] = 'com'
df3.columns = ['CAGRYear', 'lvalue', 'Country ID', 'RegType', 'value', 'CAGR', 'Sector']             
df3 = pd.merge(df3,comcountry,on='Country ID',how='inner') 

df4["Sector"] = 'com'
df4.columns = ['CAGRYear', 'lvalue', 'Country ID', 'RegType', 'value', 'CAGR', 'Sector']             
df4 = pd.merge(df4,comcountry,on='Country ID',how='inner') 


allcombs2  = DataFrame(aclist)
allcombs2["ID"] =  range(len(allcombs2)) 
allcombs2["ID"] = allcombs2["ID"] + 1
allcombs2["Sector"] = "com"
allcombs2['RegID'] = allcombs2['ID'].apply(lambda x: 'com00' + str(x)  if x<10 else 'com0' +str(x) if x<100 else 'com' + str(x))
allcombs2.columns = ['RegType', 'ID', 'Sector', 'RegID']
allcombs2['RegType']  = allcombs2['RegType'].str.replace("lcom~", "")
com_regid = allcombs2.drop(['ID','Sector'],axis = 1)

com = pd.merge(df,com_regid,on='RegType',how='inner') 
com_p = pd.merge(df2,com_regid,on='RegType',how='inner') 
com_cagr = pd.merge(df3,com_regid,on='RegType',how='inner') 
com_cagr_check = pd.merge(df4,com_regid,on='RegType',how='inner') 
com_regid["Sector"] = "com"

endtime = datetime.datetime.now()
print (endtime - starttime)

print("Congradulations! Com Finished :)")


# IND
data = table.drop(['lelc', 'ltrn', 'lcom', 'lres', 'lpet', 'lgasprice', 'loilprice'], axis = 1)

r_table = pd.read_excel(r'C:\Users\jiaxi\OneDrive\Desktop\RBAC 2022\Demand\Demand Annual Builder\2022 0808\Input Scenarios 2022 0808.xlsx', sheet_name = 'IND')
indcountry = r_table.loc[:,['Country ID',  'Country']]

country_name = r_table['Country'].to_list()

ref_country = table['Country'].unique()

df = pd.DataFrame()
df2 = pd.DataFrame()
df3 = pd.DataFrame()
df4 = pd.DataFrame()


for i in country_name:
    if i != 'ALL':
        if i in ref_country:

                Country = data[data['Country']== i]
                country_filter = r_table[r_table['Country']== i]
                
                retr_country = country_filter['Country'].to_list()[0]
                
                country_data = data[data['Country']==retr_country]

                x_labels = country_filter[['x0','x1','x2','x3','x4','x5','x6','x7', 'x8', 'x9', 'coviddummy',  'y']]
                rid = country_filter['Country ID'].tolist()[0]
                y_var = x_labels['y'].to_list()[0]

                def subcombs_2(dset):
                    data_ = []
                    for i in range(1,len(dset)+1):
                        for j in combinations(dset,i):
                            data_.append(list(j))
                    return data_


                def stitch(f):
                    out = ""
                    for k,i in enumerate(f):
                        if len(i) > 1:
                            out += i
                        else:
                            try:
                                out += i
                            except:
                                out +=i[0]
                        if k < len(f)-1:
                            out+=" + "
                    return out

                regressors = ['lgdp', 'lppl', 'lgdpp', 'luppl', 'llf', 'lgdp_man']
                
                allcombs = subcombs_2(regressors)
                del allcombs[0:]
                allcombs.append(['lgdp', 'coviddummy'])
                allcombs.append(['lppl', 'coviddummy'])
                allcombs.append(['lgdpp2' , 'coviddummy'])
                allcombs.append(['lgdp_man', 'coviddummy'])
                allcombs.append(['lgdp' , 'lppl', 'coviddummy'])
                allcombs.append(['lppl', 'lgdp_man', 'coviddummy'])
                allcombs.append(['lgdp', 'lppl', 'lgop', 'coviddummy'])
                
                #allcombs.append([lgdp
                



                aclist = []

                for i in allcombs:
                     aclist.append('lind~'+stitch(i)) 

                for i in aclist:
                    model = smf.ols(i, data=country_data)
                    results = model.fit()
                    a = i.replace('lind~', '')
                    
                    values = pd.DataFrame(results.params).reset_index()
                    values.columns = ['names', 'coef']
                    xfinal = x_labels
                    xfinal['Intercept'] = 'Intercept'
                    xfinal = xfinal.T.reset_index()
                    xfinal.columns = ['labels', 'names']
                    export_val = xfinal.merge(values, on = 'names', how='left')
                    results.tvalues
                    t_stat = pd.DataFrame(results.tvalues).reset_index()
                    t_stat.columns = ['names', 't-statistic']
                    export_val1 = export_val.merge(t_stat, on = 'names', how='left')
                    # p-value
                    p_value = pd.DataFrame(results.pvalues).reset_index()
                    p_value.columns = ['names', 'p-value']
                    export_val1 = export_val1.merge(p_value, on = 'names', how='left')
                    
                    r_columns = ['Year'] + values.xs("names", axis = 1).tolist()
                    del r_columns[1: 2]
                    forecast_var = country_data[r_columns].reset_index(drop=True)
                    forecast_var['Intercept'] = 1           
                    test = forecast_var[forecast_var['Year']>2022] # last history year
                    xval = test.drop(columns = ['Year'])

                    
                    entry2 = pd.DataFrame({'Country ID': [rid, rid, rid, rid,rid, rid, rid, rid, rid, rid, rid,rid],
                                   'R-square': [results.rsquared, results.rsquared, results.rsquared, results.rsquared, results.rsquared, results.rsquared, results.rsquared, results.rsquared, results.rsquared, results.rsquared, results.rsquared, results.rsquared],
                                   'RegType': [a, a, a, a, a, a, a, a, a, a, a, a ],
                                   'CoeID': ['intercept', 'x0', 'x1', 'x2', 'x3', 'x4', 'x5', 'x6', 'x7', 'x8', 'x9', 'coviddummy'],
                                   'Coe': [export_val1[export_val1['labels']=='Intercept']['coef'].to_list()[0], export_val1[export_val1['labels']=='x0']['coef'].to_list()[0], export_val1[export_val1['labels']=='x1']['coef'].to_list()[0], export_val1[export_val1['labels']=='x2']['coef'].to_list()[0], export_val1[export_val1['labels']=='x3']['coef'].to_list()[0], export_val1[export_val1['labels']=='x4']['coef'].to_list()[0], export_val1[export_val1['labels']=='x5']['coef'].to_list()[0], export_val1[export_val1['labels']=='x6']['coef'].to_list()[0], export_val1[export_val1['labels']=='x7']['coef'].to_list()[0], export_val1[export_val1['labels']=='x8']['coef'].to_list()[0], export_val1[export_val1['labels']=='x9']['coef'].to_list()[0], export_val1[export_val1['labels']=='coviddummy']['coef'].to_list()[0]],
                                   'tvalueID': ['t_intercept', 't_x0', 't_x1', 't_x2', 't_x3', 't_x4', 't_x5', 't_x6', 't_x7', 't_x8', 't_x9', 't_coviddummy'],
                                   'tvalue': [export_val1[export_val1['labels']=='Intercept']['t-statistic'].to_list()[0], export_val1[export_val1['labels']=='x0']['t-statistic'].to_list()[0], export_val1[export_val1['labels']=='x1']['t-statistic'].to_list()[0], export_val1[export_val1['labels']=='x2']['t-statistic'].to_list()[0], export_val1[export_val1['labels']=='x3']['t-statistic'].to_list()[0], export_val1[export_val1['labels']=='x4']['t-statistic'].to_list()[0], export_val1[export_val1['labels']=='x5']['t-statistic'].to_list()[0], export_val1[export_val1['labels']=='x6']['t-statistic'].to_list()[0], export_val1[export_val1['labels']=='x7']['t-statistic'].to_list()[0], export_val1[export_val1['labels']=='x8']['t-statistic'].to_list()[0], export_val1[export_val1['labels']=='x9']['t-statistic'].to_list()[0], export_val1[export_val1['labels']=='coviddummy']['t-statistic'].to_list()[0]],
                                   'pvalueID': ['p_intercept', 'p_x0', 'p_x1', 'p_x2', 'p_x3', 'p_x4', 'p_x5', 'p_x6', 'p_x7', 'p_x8', 'p_x9', 'p_coviddummy'],
                                   'pvalue': [export_val1[export_val1['labels']=='Intercept']['p-value'].to_list()[0], export_val1[export_val1['labels']=='x0']['p-value'].to_list()[0], export_val1[export_val1['labels']=='x1']['p-value'].to_list()[0], export_val1[export_val1['labels']=='x2']['p-value'].to_list()[0], export_val1[export_val1['labels']=='x3']['p-value'].to_list()[0], export_val1[export_val1['labels']=='x4']['p-value'].to_list()[0], export_val1[export_val1['labels']=='x5']['p-value'].to_list()[0], export_val1[export_val1['labels']=='x6']['p-value'].to_list()[0], export_val1[export_val1['labels']=='x7']['p-value'].to_list()[0], export_val1[export_val1['labels']=='x8']['p-value'].to_list()[0], export_val1[export_val1['labels']=='x9']['p-value'].to_list()[0], export_val1[export_val1['labels']=='coviddummy']['p-value'].to_list()[0]]})
                   
                    y_hat = results.predict(xval) 
                    yr_p = yrs[yrs['Year']>=2023]   # first forecast year          
                    p_export = pd.concat([yr_p, y_hat], axis=1, sort=False)
                    p_export['Country ID'] = rid
                    p_export["RegType"] = a
                    
                    cagr = p_export
                    cagr.columns = ['Year', 'lvalue', 'Country ID', 'RegType']
                    cagr['value'] = math.exp(1) ** cagr['lvalue']                    
                    cagr['test1'] = cagr['Year'] % 5
                    def fun(x): # this function is to calculate cagr, test for delete useless rows
                      if x == 2023: # the base year that you would like to calculate cagr
                        return 0
                      else:
                        return 1
                    cagr['test2'] =cagr['Year'].apply(lambda x: fun(x))
                    cagr['test'] = cagr['test1'] * cagr['test2']
                    cagr = cagr.drop(cagr[cagr.test > 0].index)
                    cagr['CAGR'] = (cagr['value'] / cagr['value'].shift(+1) ) ** (1/(cagr['Year'] - cagr['Year'].shift(+1))) - 1
                    cagr = cagr.drop(['test1', 'test2', 'test'], axis = 1)
                    
                    cagr_check = cagr.drop(cagr[cagr.Year == 2025 ].index)
                    cagr_check = cagr_check.drop(cagr_check[cagr_check.Year == 2030 ].index)
                    cagr_check = cagr_check.drop(cagr_check[cagr_check.Year == 2035 ].index)
                    cagr_check = cagr_check.drop(cagr_check[cagr_check.Year == 2040 ].index)
                    cagr_check = cagr_check.drop(cagr_check[cagr_check.Year == 2045 ].index)
                    cagr_check = cagr_check.drop(['CAGR'], axis = 1)
                    cagr_check['CAGR'] = (cagr_check['value'] / cagr_check['value'].shift(+1) ) ** (1/27) - 1 # 2050 - base year
                    cagr_check = cagr_check.drop(cagr_check[cagr_check.Year == 2023 ].index) # the base year that you would like to calculate cagr

                    p_export = p_export.drop(['test1', 'test2', 'test'], axis = 1)

                    df = pd.concat([df,entry2])
                    df2 = pd.concat([df2,p_export])
                    df3 = pd.concat([df3,cagr])
                    df4 = pd.concat([df4,cagr])
            
df.insert(1, "Sector", "ind")
df = df[df['Coe'].notna()]
df = pd.merge(df,indcountry,on='Country ID',how='inner') 

df2["Sector"] = 'ind'
df2.columns = ['Year', 'lvalue', 'Country ID', 'RegType', 'value', 'Sector']             
df2 = pd.merge(df2,indcountry,on='Country ID',how='inner') 

df3["Sector"] = 'ind'
df3.columns = ['CAGRYear', 'lvalue', 'Country ID', 'RegType', 'value', 'CAGR', 'Sector']             
df3 = pd.merge(df3,indcountry,on='Country ID',how='inner') 

df4["Sector"] = 'ind'
df4.columns = ['CAGRYear', 'lvalue', 'Country ID', 'RegType', 'value', 'CAGR', 'Sector']             
df4 = pd.merge(df4,indcountry,on='Country ID',how='inner') 

allcombs2  = DataFrame(aclist)
allcombs2["ID"] =  range(len(allcombs2)) 
allcombs2["ID"] = allcombs2["ID"] + 1
allcombs2["Sector"] = "ind"
allcombs2['RegID'] = allcombs2['ID'].apply(lambda x: 'ind00' + str(x)  if x<10 else 'ind0' +str(x) if x<100 else 'ind' + str(x))
allcombs2.columns = ['RegType', 'ID', 'Sector', 'RegID']
allcombs2['RegType']  = allcombs2['RegType'].str.replace("lind~", "")
ind_regid = allcombs2.drop(['ID','Sector'],axis = 1)

ind = pd.merge(df,ind_regid,on='RegType',how='inner') 
ind_p = pd.merge(df2,ind_regid,on='RegType',how='inner')
ind_cagr = pd.merge(df3,ind_regid,on='RegType',how='inner') 
ind_cagr_check = pd.merge(df4,ind_regid,on='RegType',how='inner') 

endtime = datetime.datetime.now()
print (endtime - starttime)

print("Congradulations! Ind1 Finished :)")


## IND2

main_data = table.drop(['lelc', 'lcom', 'lres', 'ltrn', 'lpet',  'lgdp_man', 'lgdp', 'lppl', 'lgdpp', 'lgdp_man',  'luppl', 'llf', 'lgop', 'lgou', 'lpou', 'lgasprice', 'loilprice'], axis = 1)

# main_data = pd.read_excel('/Users/adishluitel/Desktop/RBAC_Work/Trial/PY_Workflow.xlsx', sheet_name = 'Input_Data')
r_table = pd.read_excel(r'C:\Users\jiaxi\OneDrive\Desktop\RBAC 2022\Demand\Demand Annual Builder\2022 0808\Input Scenarios 2022 0808.xlsx', sheet_name = 'IND2')
ind2country = r_table.loc[:,['Country ID',  'Country']]

country_name = r_table['Country'].to_list()
ref_country = main_data['Country'].unique()
df = pd.DataFrame()
df2 = pd.DataFrame()
df3 = pd.DataFrame()
df4 = pd.DataFrame()

for i in country_name:
    if i != 'ALL':
        if i in ref_country:


            country_filter = r_table[r_table['Country']== i]

            retr_country = country_filter['Country'].to_list()[0]

            country_data = main_data[main_data['Country']==retr_country]

            x_labels = country_filter[['xi0','xi1','xi2','xi3','xi4','x5','x6','x7', 'coviddummy','y']]
               
            x_labels2 =x_labels.astype(str)    
            a = x_labels2.iloc[0,0] + " + " + x_labels2.iloc[0,1] + " + " + x_labels2.iloc[0,2] + \
                " + " + x_labels2.iloc[0,3] + " + "+ x_labels2.iloc[0,4] + " + "+ x_labels2.iloc[0,5] + \
                " + " + x_labels2.iloc[0,6] + " + "+ x_labels2.iloc[0,7] + " + "+ x_labels2.iloc[0,8]
            a = a.replace(' + nan', '')
            a = a.replace('lind ', '')
    
            rid = country_filter['Country ID'].tolist()[0]
            y_var = x_labels['y'].to_list()[0]

            r_columns = ['Year'] + x_labels.dropna(axis=1,how='all').reset_index(drop=True).loc[0].tolist()

            regressors = country_data[r_columns].reset_index(drop=True)
            regressors['intercept'] = 1

            train = regressors[regressors['Year']<=2022] # the last history year
            test = regressors[regressors['Year']>2022] # the last history year

            X = train.drop(columns = ['Year',y_var]) 
            y = train[[y_var]]
            xval = test.drop(columns = ['Year',y_var])

            model = sm.OLS(y, X, missing='drop')
            results = model.fit()

            y_hat = results.predict(xval) 

            values = pd.DataFrame(results.params).reset_index()

            values.columns = ['names', 'coef']

            xfinal = x_labels
            xfinal['Intercept'] = 'Intercept'
            xfinal = xfinal.T.reset_index()

            xfinal.columns = ['labels', 'names']

            export_val = xfinal.merge(values, on = 'names', how='left')
            t_stat = pd.DataFrame(results.tvalues).reset_index()
            t_stat.columns = ['names', 't-statistic']
            export_val1 = export_val.merge(t_stat, on = 'names', how='left')
            # p-value
            p_value = pd.DataFrame(results.pvalues).reset_index()
            p_value.columns = ['names', 'p-value']
            export_val1 = export_val1.merge(p_value, on = 'names', how='left')

            entry2 = pd.DataFrame({'Country ID': [rid, rid, rid, rid,rid, rid, rid, rid, rid, rid],
                                   'R-square': [results.rsquared, results.rsquared, results.rsquared, results.rsquared, results.rsquared, results.rsquared, results.rsquared, results.rsquared, results.rsquared, results.rsquared],
                                   'RegType': [a, a, a, a, a, a, a, a, a,a],
                                   'CoeID': ['intercept', 'xi0', 'xi1', 'xi2', 'xi3', 'xi4', 'x5', 'x6', 'x7', 'coviddummy'],
                                   'Coe': [export_val1[export_val1['labels']=='Intercept']['coef'].to_list()[0], export_val1[export_val1['labels']=='xi0']['coef'].to_list()[0], export_val1[export_val1['labels']=='xi1']['coef'].to_list()[0], export_val1[export_val1['labels']=='xi2']['coef'].to_list()[0], export_val1[export_val1['labels']=='xi3']['coef'].to_list()[0], export_val1[export_val1['labels']=='xi4']['coef'].to_list()[0], export_val1[export_val1['labels']=='x5']['coef'].to_list()[0], export_val1[export_val1['labels']=='x6']['coef'].to_list()[0], export_val1[export_val1['labels']=='x7']['coef'].to_list()[0], export_val1[export_val1['labels']=='coviddummy']['coef'].to_list()[0]],
                                   'tvalueID': ['t_intercept', 't_xi0', 't_xi1', 't_xi2', 't_xi3', 't_xi4', 't_x5', 't_x6', 't_x7', 't_coviddummy'],
                                   'tvalue': [export_val1[export_val1['labels']=='Intercept']['t-statistic'].to_list()[0], export_val1[export_val1['labels']=='xi0']['t-statistic'].to_list()[0], export_val1[export_val1['labels']=='xi1']['t-statistic'].to_list()[0], export_val1[export_val1['labels']=='xi2']['t-statistic'].to_list()[0], export_val1[export_val1['labels']=='xi3']['t-statistic'].to_list()[0], export_val1[export_val1['labels']=='xi4']['t-statistic'].to_list()[0], export_val1[export_val1['labels']=='x5']['t-statistic'].to_list()[0], export_val1[export_val1['labels']=='x6']['t-statistic'].to_list()[0], export_val1[export_val1['labels']=='x7']['t-statistic'].to_list()[0], export_val1[export_val1['labels']=='coviddummy']['t-statistic'].to_list()[0]],
                                   'pvalueID': ['p_intercept', 'p_xi0', 'p_xi1', 'p_xi2', 'p_xi3', 'p_xi4', 'p_x5', 'p_x6', 'p_x7', 'p_coviddummy'],
                                   'pvalue': [export_val1[export_val1['labels']=='Intercept']['p-value'].to_list()[0], export_val1[export_val1['labels']=='xi0']['p-value'].to_list()[0], export_val1[export_val1['labels']=='xi1']['p-value'].to_list()[0], export_val1[export_val1['labels']=='xi2']['p-value'].to_list()[0], export_val1[export_val1['labels']=='xi3']['p-value'].to_list()[0], export_val1[export_val1['labels']=='xi4']['p-value'].to_list()[0], export_val1[export_val1['labels']=='x5']['p-value'].to_list()[0], export_val1[export_val1['labels']=='x6']['p-value'].to_list()[0], export_val1[export_val1['labels']=='x7']['p-value'].to_list()[0], export_val1[export_val1['labels']=='coviddummy']['p-value'].to_list()[0]]})
                   
            y_hat = results.predict(xval) 
            yr_p = yrs[yrs['Year']>=2023] # the first forecast year           
            p_export = pd.concat([yr_p, y_hat], axis=1, sort=False)
            p_export['Country ID'] = rid
            p_export["RegType"] = a 
           
            cagr = p_export
            cagr.columns = ['Year', 'lvalue', 'Country ID', 'RegType']
            cagr['value'] = math.exp(1) ** cagr['lvalue']                    
            cagr['test1'] = cagr['Year'] % 5
            def fun(x): # this function is to calculate cagr, test for delete useless rows
               if x == 2023: # the base year that you would like to calculate cagr
                 return 0
               else:
                 return 1
            cagr['test2'] =cagr['Year'].apply(lambda x: fun(x))
            cagr['test'] = cagr['test1'] * cagr['test2']
            cagr = cagr.drop(cagr[cagr.test > 0].index)
            cagr['CAGR'] = (cagr['value'] / cagr['value'].shift(+1) ) ** (1/(cagr['Year'] - cagr['Year'].shift(+1))) - 1
            cagr = cagr.drop(['test1', 'test2', 'test'], axis = 1)
                    
            cagr_check = cagr.drop(cagr[cagr.Year == 2025 ].index)
            cagr_check = cagr_check.drop(cagr_check[cagr_check.Year == 2030 ].index)
            cagr_check = cagr_check.drop(cagr_check[cagr_check.Year == 2035 ].index)
            cagr_check = cagr_check.drop(cagr_check[cagr_check.Year == 2040 ].index)
            cagr_check = cagr_check.drop(cagr_check[cagr_check.Year == 2045 ].index)
            cagr_check = cagr_check.drop(['CAGR'], axis = 1)
            cagr_check['CAGR'] = (cagr_check['value'] / cagr_check['value'].shift(+1) ) ** (1/27) - 1 # 2050 - base year
            cagr_check = cagr_check.drop(cagr_check[cagr_check.Year == 2023 ].index) # the base year that you would like to calculate cagr


            p_export = p_export.drop(['test1', 'test2', 'test'], axis = 1)

            df = pd.concat([df,entry2])
            df2 = pd.concat([df2,p_export])
            df3 = pd.concat([df3,cagr])
            df4 = pd.concat([df4,cagr])
            
df.insert(1, "Sector", "ind")
df = df[df['Coe'].notna()]
ind2 = pd.merge(df,ind2country,on='Country ID',how='inner') 

df2["Sector"] = 'ind'
df2.columns = ['Year', 'lvalue', 'Country ID', 'RegType', 'value', 'Sector']        
             
df3["Sector"] = 'ind'
df3.columns = ['CAGRYear', 'lvalue', 'Country ID', 'RegType', 'value', 'CAGR', 'Sector']             
df3 = pd.merge(df3,ind2country,on='Country ID',how='inner') 

df4["Sector"] = 'ind'
df4.columns = ['CAGRYear', 'lvalue', 'Country ID', 'RegType', 'value', 'CAGR', 'Sector']             
df4 = pd.merge(df4,ind2country,on='Country ID',how='inner') 


ind2_p = pd.merge(df2,ind2country,on='Country ID',how='inner') 

# 007 will be replaced if the numbers 0f IND changes
ind_regid = ind_regid.append({'RegType': 'lche + lfoo + lmac + ltex + loth + coviddummy', 'RegID': 'ind008'}, ignore_index=True)

ind2 = pd.merge(ind2,ind_regid,on='RegType',how='inner') 
ind2_p = pd.merge(ind2_p,ind_regid,on='RegType',how='inner') 
ind2_cagr = pd.merge(df3,ind_regid,on='RegType',how='inner') 
ind2_cagr_check = pd.merge(df4,ind_regid,on='RegType',how='inner') 


ind_regid["Sector"] = "ind"

endtime = datetime.datetime.now()
print (endtime - starttime)

print("Congradulations! Ind2 Finished :)")


# ind3
data = table.drop(['lelc', 'lpet', 'lcom', 'lres', 'ltrn','lgdp_man',  'lfoo', 'lmac', 'ltex', 'loth', 'lgop', 'lgou', 'lpou'], axis = 1)

r_table = pd.read_excel(r'C:\Users\jiaxi\OneDrive\Desktop\RBAC 2022\Demand\Demand Annual Builder\2022 0808\Input Scenarios 2022 0808.xlsx', sheet_name = 'IND3')
ind3country = r_table.loc[:,['Country ID',  'Country']]

country_name = r_table['Country'].to_list()

ref_country = table['Country'].unique()

df = pd.DataFrame()
df2 = pd.DataFrame()
df3 = pd.DataFrame()
df4 = pd.DataFrame()

for i in country_name:
    if i != 'ALL':
        if i in ref_country:

                Country = data[data['Country']== i]
                country_filter = r_table[r_table['Country']== i]
                
                retr_country = country_filter['Country'].to_list()[0]
                
                country_data = data[data['Country']==retr_country]

                x_labels = country_filter[['x0','x1','xi0','xpg','xpo','x5','x6','x7', 'x8', 'x9', 'coviddummy',  'y']]
                rid = country_filter['Country ID'].tolist()[0]
                y_var = x_labels['y'].to_list()[0]

                def subcombs_2(dset):
                    data_ = []
                    for i in range(1,len(dset)+1):
                        for j in combinations(dset,i):
                            data_.append(list(j))
                    return data_


                def stitch(f):
                    out = ""
                    for k,i in enumerate(f):
                        if len(i) > 1:
                            out += i
                        else:
                            try:
                                out += i
                            except:
                                out +=i[0]
                        if k < len(f)-1:
                            out+=" + "
                    return out

                regressors = ['lgdp', 'lppl', 'lche', 'lgasprice', 'loilprice']
                allcombs = subcombs_2(regressors)               
                del allcombs[0:]
                
                allcombs.append(['lppl', 'lche', 'coviddummy'])
                allcombs.append(['lppl', 'lgasprice', 'coviddummy'])
                allcombs.append(['lgdp', 'lgasprice', 'coviddummy'])
                allcombs.append(['lgdp', 'lppl', 'lche', 'coviddummy'])
                allcombs.append(['lgdp', 'lppl',  'loilprice', 'coviddummy'])
                allcombs.append(['lgdp', 'lppl', 'lgasprice', 'loilprice', 'coviddummy'])
                allcombs.append(['lgdp', 'lppl', 'coviddummy'])
                allcombs.append(['lgdp', 'lppl', 'lche', 'lgasprice', 'coviddummy'])

                
                aclist = []

                for i in allcombs:
                     aclist.append('lind~'+stitch(i)) 

                for i in aclist:
                    model = smf.ols(i, data=country_data)
                    results = model.fit()
                    a = i.replace('lind~', '')
                    
                    values = pd.DataFrame(results.params).reset_index()
                    values.columns = ['names', 'coef']
                    xfinal = x_labels
                    xfinal['Intercept'] = 'Intercept'
                    xfinal = xfinal.T.reset_index()
                    xfinal.columns = ['labels', 'names']
                    export_val = xfinal.merge(values, on = 'names', how='left')
                    results.tvalues
                    t_stat = pd.DataFrame(results.tvalues).reset_index()
                    t_stat.columns = ['names', 't-statistic']
                    export_val1 = export_val.merge(t_stat, on = 'names', how='left')
                    # p-value
                    p_value = pd.DataFrame(results.pvalues).reset_index()
                    p_value.columns = ['names', 'p-value']
                    export_val1 = export_val1.merge(p_value, on = 'names', how='left')
                    
                    r_columns = ['Year'] + values.xs("names", axis = 1).tolist()
                    del r_columns[1: 2]
                    forecast_var = country_data[r_columns].reset_index(drop=True)
                    forecast_var['Intercept'] = 1           
                    test = forecast_var[forecast_var['Year']>2022] # last history year
                    xval = test.drop(columns = ['Year'])

                    
                    entry2 = pd.DataFrame({'Country ID': [rid, rid, rid, rid,rid, rid, rid, rid, rid, rid, rid, rid],
                                   'R-square': [results.rsquared, results.rsquared, results.rsquared, results.rsquared, results.rsquared, results.rsquared, results.rsquared, results.rsquared, results.rsquared, results.rsquared, results.rsquared, results.rsquared],
                                   'RegType': [a, a, a, a, a, a, a, a, a, a, a, a],
                                   'CoeID': ['intercept', 'x0', 'x1', 'xi0', 'xpg', 'xpo', 'x5', 'x6', 'x7', 'x8', 'x9', 'coviddummy'],
                                   'Coe': [export_val1[export_val1['labels']=='Intercept']['coef'].to_list()[0], export_val1[export_val1['labels']=='x0']['coef'].to_list()[0], export_val1[export_val1['labels']=='x1']['coef'].to_list()[0], export_val1[export_val1['labels']=='xi0']['coef'].to_list()[0], export_val1[export_val1['labels']=='xpg']['coef'].to_list()[0], export_val1[export_val1['labels']=='xpo']['coef'].to_list()[0], export_val1[export_val1['labels']=='x5']['coef'].to_list()[0], export_val1[export_val1['labels']=='x6']['coef'].to_list()[0], export_val1[export_val1['labels']=='x7']['coef'].to_list()[0], export_val1[export_val1['labels']=='x8']['coef'].to_list()[0], export_val1[export_val1['labels']=='x9']['coef'].to_list()[0], export_val1[export_val1['labels']=='coviddummy']['coef'].to_list()[0]],
                                   'tvalueID': ['t_intercept', 't_x0', 't_x1', 't_xi0', 't_xpg', 't_xpo', 't_x5', 't_x6', 't_x7', 't_x8', 't_x9', 't_coviddummy'],
                                   'tvalue': [export_val1[export_val1['labels']=='Intercept']['t-statistic'].to_list()[0], export_val1[export_val1['labels']=='x0']['t-statistic'].to_list()[0], export_val1[export_val1['labels']=='x1']['t-statistic'].to_list()[0], export_val1[export_val1['labels']=='xi0']['t-statistic'].to_list()[0], export_val1[export_val1['labels']=='xpg']['t-statistic'].to_list()[0], export_val1[export_val1['labels']=='xpo']['t-statistic'].to_list()[0], export_val1[export_val1['labels']=='x5']['t-statistic'].to_list()[0], export_val1[export_val1['labels']=='x6']['t-statistic'].to_list()[0], export_val1[export_val1['labels']=='x7']['t-statistic'].to_list()[0], export_val1[export_val1['labels']=='x8']['t-statistic'].to_list()[0], export_val1[export_val1['labels']=='x9']['t-statistic'].to_list()[0], export_val1[export_val1['labels']=='coviddummy']['t-statistic'].to_list()[0]],
                                   'pvalueID': ['p_intercept', 'p_x0', 'p_xi1', 'p_xi2', 'p_xpg', 'p_xpo', 'p_x5', 'p_x6', 'p_x7', 'p_x8', 'p_x9', 'p_coviddummy'],
                                   'pvalue': [export_val1[export_val1['labels']=='Intercept']['p-value'].to_list()[0], export_val1[export_val1['labels']=='x0']['p-value'].to_list()[0], export_val1[export_val1['labels']=='x1']['p-value'].to_list()[0], export_val1[export_val1['labels']=='xi0']['p-value'].to_list()[0], export_val1[export_val1['labels']=='xpg']['p-value'].to_list()[0], export_val1[export_val1['labels']=='xpo']['p-value'].to_list()[0], export_val1[export_val1['labels']=='x5']['p-value'].to_list()[0], export_val1[export_val1['labels']=='x6']['p-value'].to_list()[0], export_val1[export_val1['labels']=='x7']['p-value'].to_list()[0], export_val1[export_val1['labels']=='x8']['p-value'].to_list()[0], export_val1[export_val1['labels']=='x9']['p-value'].to_list()[0], export_val1[export_val1['labels']=='coviddummy']['p-value'].to_list()[0]]})
                   
                    y_hat = results.predict(xval) 
                    yr_p = yrs[yrs['Year']>=2023]  # first forecast year           
                    p_export = pd.concat([yr_p, y_hat], axis=1, sort=False)
                    p_export['Country ID'] = rid
                    p_export["RegType"] = a
                    
                    cagr = p_export
                    cagr.columns = ['Year', 'lvalue', 'Country ID', 'RegType']
                    cagr['value'] = math.exp(1) ** cagr['lvalue']                    
                    cagr['test1'] = cagr['Year'] % 5
                    def fun(x): # this function is to calculate cagr, test for delete useless rows
                      if x == 2023: # the base year that you would like to calculate cagr
                        return 0
                      else:
                        return 1
                    cagr['test2'] =cagr['Year'].apply(lambda x: fun(x))
                    cagr['test'] = cagr['test1'] * cagr['test2']
                    cagr = cagr.drop(cagr[cagr.test > 0].index)
                    cagr['CAGR'] = (cagr['value'] / cagr['value'].shift(+1) ) ** (1/(cagr['Year'] - cagr['Year'].shift(+1))) - 1
                    cagr = cagr.drop(['test1', 'test2', 'test'], axis = 1)
                    
                    cagr_check = cagr.drop(cagr[cagr.Year == 2025 ].index)
                    cagr_check = cagr_check.drop(cagr_check[cagr_check.Year == 2030 ].index)
                    cagr_check = cagr_check.drop(cagr_check[cagr_check.Year == 2035 ].index)
                    cagr_check = cagr_check.drop(cagr_check[cagr_check.Year == 2040 ].index)
                    cagr_check = cagr_check.drop(cagr_check[cagr_check.Year == 2045 ].index)
                    cagr_check = cagr_check.drop(['CAGR'], axis = 1)
                    cagr_check['CAGR'] = (cagr_check['value'] / cagr_check['value'].shift(+1) ) ** (1/27) - 1 # 2050 - base year
                    cagr_check = cagr_check.drop(cagr_check[cagr_check.Year == 2023 ].index)  # the base year that you would like to calculate cagr

                    p_export = p_export.drop(['test1', 'test2', 'test'], axis = 1)

                    df = pd.concat([df,entry2])
                    df2 = pd.concat([df2,p_export])
                    df3 = pd.concat([df3,cagr])
                    df4 = pd.concat([df4,cagr])        
                    
                    
            
df.insert(1, "Sector", "ind")
df = df[df['Coe'].notna()]
df = pd.merge(df,ind3country,on='Country ID',how='inner') 

df2["Sector"] = 'ind'
df2.columns = ['Year', 'lvalue', 'Country ID', 'RegType', 'value', 'Sector']             
df2 = pd.merge(df2,ind3country,on='Country ID',how='inner') 

df3["Sector"] = 'ind'
df3.columns = ['CAGRYear', 'lvalue', 'Country ID', 'RegType', 'value', 'CAGR', 'Sector']             
df3 = pd.merge(df3,ind3country,on='Country ID',how='inner') 

df4["Sector"] = 'ind'
df4.columns = ['CAGRYear', 'lvalue', 'Country ID', 'RegType', 'value', 'CAGR', 'Sector']             
df4 = pd.merge(df4,ind3country,on='Country ID',how='inner') 


allcombs2  = DataFrame(aclist)
allcombs2["ID"] =  range(len(allcombs2)) 
# 8 will be replaced if the numbers 0f IND+IND2 changes
allcombs2["ID"] = allcombs2["ID"] + 9
allcombs2["Sector"] = "ind"
allcombs2['RegID'] = allcombs2['ID'].apply(lambda x: 'ind00' + str(x)  if x<10 else 'ind0' +str(x) if x<100 else 'ind' + str(x))
allcombs2.columns = ['RegType', 'ID', 'Sector', 'RegID']
allcombs2['RegType']  = allcombs2['RegType'].str.replace("lind~", "")
ind3_regid = allcombs2.drop(['ID','Sector'],axis = 1)

ind3 = pd.merge(df,ind3_regid,on='RegType',how='inner') 
ind3_p = pd.merge(df2,ind3_regid,on='RegType',how='inner') 
ind3_cagr = pd.merge(df3,ind3_regid,on='RegType',how='inner') 
ind3_cagr_check = pd.merge(df4,ind3_regid,on='RegType',how='inner') 


ind3_regid["Sector"] = "ind"

ind_regid = pd.concat([ind_regid,ind3_regid])



endtime = datetime.datetime.now()
print (endtime - starttime)

print("Congradulations! Ind3 Finished :)")


# RES
data = table.drop(['lelc', 'lind', 'lcom', 'ltrn', 'lpet', 'lgdp_man', 'lche', 'lfoo', 'lmac', 'ltex', 'loth', 'lgasprice', 'loilprice'], axis = 1)

r_table = pd.read_excel(r'C:\Users\jiaxi\OneDrive\Desktop\RBAC 2022\Demand\Demand Annual Builder\2022 0808\Input Scenarios 2022 0808.xlsx', sheet_name = 'RES')
rescountry = r_table.loc[:,['Country ID',  'Country']]

country_name = r_table['Country'].to_list()

ref_country = table['Country'].unique()

df = pd.DataFrame()
df2 = pd.DataFrame()
df3 = pd.DataFrame()
df4 = pd.DataFrame()

for i in country_name:
    if i != 'ALL':
        if i in ref_country:

                Country = data[data['Country']== i]
                country_filter = r_table[r_table['Country']== i]
                
                retr_country = country_filter['Country'].to_list()[0]
                
                country_data = data[data['Country']==retr_country]

                x_labels = country_filter[['x0','x1','x2','x3','x4','x5','x6','x7', 'x8', 'x9',  'coviddummy', 'y']]
                rid = country_filter['Country ID'].tolist()[0]
                y_var = x_labels['y'].to_list()[0]

                def subcombs_2(dset):
                    data_ = []
                    for i in range(1,len(dset)+1):
                        for j in combinations(dset,i):
                            data_.append(list(j))
                    return data_


                def stitch(f):
                    out = ""
                    for k,i in enumerate(f):
                        if len(i) > 1:
                            out += i
                        else:
                            try:
                                out += i
                            except:
                                out +=i[0]
                        if k < len(f)-1:
                            out+=" + "
                    return out

                regressors = ['lgdp', 'lppl', 'lgdpp', 'luppl', 'llf']
                
                allcombs = subcombs_2(regressors)
                del allcombs[0:]
                allcombs.append(['lgdp', 'coviddummy'])
                allcombs.append(['lppl', 'coviddummy'])
                allcombs.append(['luppl', 'coviddummy'])
                allcombs.append(['lgdpp2' , 'coviddummy'])
                allcombs.append(['lgdp' , 'lppl', 'coviddummy'])
                allcombs.append(['lgdp' , 'luppl', 'coviddummy'])
                allcombs.append(['lppl' , 'luppl', 'coviddummy'])
                allcombs.append(['lgdp', 'lppl', 'lgdpp', 'coviddummy'])
                allcombs.append(['lgdp', 'lppl', 'lgop', 'coviddummy'])            
                allcombs.append(['lgdp', 'luppl', 'lgou', 'coviddummy'])
                allcombs.append(['lppl', 'luppl', 'lpou', 'coviddummy'])

                
                
                aclist = []

                for i in allcombs:
                     aclist.append('lres~'+stitch(i)) 

                for i in aclist:
                    model = smf.ols(i, data=country_data)
                    results = model.fit()
                    a = i.replace('lres~', '')
                    
                    values = pd.DataFrame(results.params).reset_index()
                    values.columns = ['names', 'coef']
                    xfinal = x_labels
                    xfinal['Intercept'] = 'Intercept'
                    xfinal = xfinal.T.reset_index()
                    xfinal.columns = ['labels', 'names']
                    export_val = xfinal.merge(values, on = 'names', how='left')
                    results.tvalues
                    t_stat = pd.DataFrame(results.tvalues).reset_index()
                    t_stat.columns = ['names', 't-statistic']
                    export_val1 = export_val.merge(t_stat, on = 'names', how='left')
                    # p-value
                    p_value = pd.DataFrame(results.pvalues).reset_index()
                    p_value.columns = ['names', 'p-value']
                    export_val1 = export_val1.merge(p_value, on = 'names', how='left')
                    
                    r_columns = ['Year'] + values.xs("names", axis = 1).tolist()
                    del r_columns[1: 2]
                    forecast_var = country_data[r_columns].reset_index(drop=True)
                    forecast_var['Intercept'] = 1           
                    test = forecast_var[forecast_var['Year']>2022] # last history year
                    xval = test.drop(columns = ['Year'])

                    
                    entry2 = pd.DataFrame({'Country ID': [rid, rid,rid, rid, rid,rid, rid, rid, rid, rid, rid, rid],
                                   'R-square': [results.rsquared, results.rsquared, results.rsquared, results.rsquared, results.rsquared, results.rsquared, results.rsquared, results.rsquared, results.rsquared, results.rsquared, results.rsquared, results.rsquared],
                                   'RegType': [a, a, a, a, a, a, a, a, a, a, a, a],
                                   'CoeID': ['intercept', 'x0', 'x1', 'x2', 'x3', 'x4', 'x5', 'x6', 'x7', 'x8', 'x9', 'coviddummy'],
                                   'Coe': [export_val1[export_val1['labels']=='Intercept']['coef'].to_list()[0], export_val1[export_val1['labels']=='x0']['coef'].to_list()[0], export_val1[export_val1['labels']=='x1']['coef'].to_list()[0], export_val1[export_val1['labels']=='x2']['coef'].to_list()[0], export_val1[export_val1['labels']=='x3']['coef'].to_list()[0], export_val1[export_val1['labels']=='x4']['coef'].to_list()[0], export_val1[export_val1['labels']=='x5']['coef'].to_list()[0], export_val1[export_val1['labels']=='x6']['coef'].to_list()[0], export_val1[export_val1['labels']=='x7']['coef'].to_list()[0], export_val1[export_val1['labels']=='x8']['coef'].to_list()[0], export_val1[export_val1['labels']=='x9']['coef'].to_list()[0], export_val1[export_val1['labels']=='coviddummy']['coef'].to_list()[0]],
                                   'tvalueID': ['t_intercept', 't_x0', 't_x1', 't_x2', 't_x3', 't_x4', 't_x5', 't_x6', 't_x7', 't_x8', 't_x9', 't_coviddummy'],
                                   'tvalue': [export_val1[export_val1['labels']=='Intercept']['t-statistic'].to_list()[0], export_val1[export_val1['labels']=='x0']['t-statistic'].to_list()[0], export_val1[export_val1['labels']=='x1']['t-statistic'].to_list()[0], export_val1[export_val1['labels']=='x2']['t-statistic'].to_list()[0], export_val1[export_val1['labels']=='x3']['t-statistic'].to_list()[0], export_val1[export_val1['labels']=='x4']['t-statistic'].to_list()[0], export_val1[export_val1['labels']=='x5']['t-statistic'].to_list()[0], export_val1[export_val1['labels']=='x6']['t-statistic'].to_list()[0], export_val1[export_val1['labels']=='x7']['t-statistic'].to_list()[0], export_val1[export_val1['labels']=='x8']['t-statistic'].to_list()[0], export_val1[export_val1['labels']=='x9']['t-statistic'].to_list()[0], export_val1[export_val1['labels']=='coviddummy']['t-statistic'].to_list()[0]],
                                   'pvalueID': ['p_intercept', 'p_x0', 'p_x1', 'p_x2', 'p_x3', 'p_x4', 'p_x5', 'p_x6', 'p_x7', 'p_x8', 'p_x9', 'p_coviddummy'],
                                   'pvalue': [export_val1[export_val1['labels']=='Intercept']['p-value'].to_list()[0], export_val1[export_val1['labels']=='x0']['p-value'].to_list()[0], export_val1[export_val1['labels']=='x1']['p-value'].to_list()[0], export_val1[export_val1['labels']=='x2']['p-value'].to_list()[0], export_val1[export_val1['labels']=='x3']['p-value'].to_list()[0], export_val1[export_val1['labels']=='x4']['p-value'].to_list()[0], export_val1[export_val1['labels']=='x5']['p-value'].to_list()[0], export_val1[export_val1['labels']=='x6']['p-value'].to_list()[0], export_val1[export_val1['labels']=='x7']['p-value'].to_list()[0], export_val1[export_val1['labels']=='x8']['p-value'].to_list()[0], export_val1[export_val1['labels']=='x9']['p-value'].to_list()[0], export_val1[export_val1['labels']=='coviddummy']['p-value'].to_list()[0]]})
                   
    
                    y_hat = results.predict(xval) 
                    yr_p = yrs[yrs['Year']>=2023] # first forecast year             
                    p_export = pd.concat([yr_p, y_hat], axis=1, sort=False)
                    p_export['Country ID'] = rid
                    p_export["RegType"] = a
                    
                    cagr = p_export
                    cagr.columns = ['Year', 'lvalue', 'Country ID', 'RegType']
                    cagr['value'] = math.exp(1) ** cagr['lvalue']                    
                    cagr['test1'] = cagr['Year'] % 5
                    def fun(x): # this function is to calculate cagr, test for delete useless rows
                      if x == 2023: # the base year that you would like to calculate cagr
                        return 0
                      else:
                        return 1
                    cagr['test2'] =cagr['Year'].apply(lambda x: fun(x))
                    cagr['test'] = cagr['test1'] * cagr['test2']
                    cagr = cagr.drop(cagr[cagr.test > 0].index)
                    cagr['CAGR'] = (cagr['value'] / cagr['value'].shift(+1) ) ** (1/(cagr['Year'] - cagr['Year'].shift(+1))) - 1
                    cagr = cagr.drop(['test1', 'test2', 'test'], axis = 1)
                    
                    cagr_check = cagr.drop(cagr[cagr.Year == 2025 ].index)
                    cagr_check = cagr_check.drop(cagr_check[cagr_check.Year == 2030 ].index)
                    cagr_check = cagr_check.drop(cagr_check[cagr_check.Year == 2035 ].index)
                    cagr_check = cagr_check.drop(cagr_check[cagr_check.Year == 2040 ].index)
                    cagr_check = cagr_check.drop(cagr_check[cagr_check.Year == 2045 ].index)
                    cagr_check = cagr_check.drop(['CAGR'], axis = 1)
                    cagr_check['CAGR'] = (cagr_check['value'] / cagr_check['value'].shift(+1) ) ** (1/27) - 1 # 2050 - base year
                    cagr_check = cagr_check.drop(cagr_check[cagr_check.Year == 2023 ].index) # the base year that you would like to calculate cagr

                    p_export = p_export.drop(['test1', 'test2', 'test'], axis = 1)

                    df = pd.concat([df,entry2])
                    df2 = pd.concat([df2,p_export])
                    df3 = pd.concat([df3,cagr])
                    df4 = pd.concat([df4,cagr])
                    
            
df.insert(1, "Sector", "res")
df = df[df['Coe'].notna()]
df = pd.merge(df,rescountry,on='Country ID',how='inner') 

df2["Sector"] = 'res'
df2.columns = ['Year', 'lvalue', 'Country ID', 'RegType', 'value', 'Sector']             
df2 = pd.merge(df2,rescountry,on='Country ID',how='inner') 

df3["Sector"] = 'res'
df3.columns = ['CAGRYear', 'lvalue', 'Country ID', 'RegType', 'value', 'CAGR', 'Sector']             
df3 = pd.merge(df3,rescountry,on='Country ID',how='inner') 

df4["Sector"] = 'res'
df4.columns = ['CAGRYear', 'lvalue', 'Country ID', 'RegType', 'value', 'CAGR', 'Sector']             
df4 = pd.merge(df4,rescountry,on='Country ID',how='inner') 


allcombs2  = DataFrame(aclist)
allcombs2["ID"] =  range(len(allcombs2)) 
allcombs2["ID"] = allcombs2["ID"] + 1
allcombs2["Sector"] = "res"
allcombs2['RegID'] = allcombs2['ID'].apply(lambda x: 'res00' + str(x)  if x<10 else 'res0' +str(x) if x<100 else 'res' + str(x))
allcombs2.columns = ['RegType', 'ID', 'Sector', 'RegID']
allcombs2['RegType']  = allcombs2['RegType'].str.replace("lres~", "")
res_regid = allcombs2.drop(['ID','Sector'],axis = 1)

res = pd.merge(df,res_regid,on='RegType',how='inner') 
res_p = pd.merge(df2,res_regid,on='RegType',how='inner')
res_cagr = pd.merge(df3,res_regid,on='RegType',how='inner') 
res_cagr_check = pd.merge(df4,res_regid,on='RegType',how='inner') 

res_regid["Sector"] = "res"


endtime = datetime.datetime.now()
print (endtime - starttime)

print("Congradulations! Res Finished :)")


# TRN
data = table.drop(['lelc', 'lind', 'lcom', 'lres', 'lpet','lgdp_man', 'lche', 'lfoo', 'lmac', 'ltex', 'loth', 'lgasprice', 'loilprice'], axis = 1)

r_table = pd.read_excel(r'C:\Users\jiaxi\OneDrive\Desktop\RBAC 2022\Demand\Demand Annual Builder\2022 0808\Input Scenarios 2022 0808.xlsx', sheet_name = 'TRN')
trncountry = r_table.loc[:,['Country ID',  'Country']]

country_name = r_table['Country'].to_list()

ref_country = table['Country'].unique()

df = pd.DataFrame()
df2 = pd.DataFrame()
df3 = pd.DataFrame()
df4 = pd.DataFrame()

for i in country_name:
    if i != 'ALL':
        if i in ref_country:

                Country = data[data['Country']== i]
                country_filter = r_table[r_table['Country']== i]
                
                retr_country = country_filter['Country'].to_list()[0]
                
                country_data = data[data['Country']==retr_country]

                x_labels = country_filter[['x0','x1','x2','x3','x4','x5','x6','x7', 'x8', 'x9','coviddummy',  'y']]
                rid = country_filter['Country ID'].tolist()[0]
                y_var = x_labels['y'].to_list()[0]

                def subcombs_2(dset):
                    data_ = []
                    for i in range(1,len(dset)+1):
                        for j in combinations(dset,i):
                            data_.append(list(j))
                    return data_


                def stitch(f):
                    out = ""
                    for k,i in enumerate(f):
                        if len(i) > 1:
                            out += i
                        else:
                            try:
                                out += i
                            except:
                                out +=i[0]
                        if k < len(f)-1:
                            out+=" + "
                    return out

                regressors = ['lgdp', 'lppl', 'lgdpp', 'luppl', 'llf']                
                allcombs = subcombs_2(regressors)
                del allcombs[0:]
                allcombs.append(['lgdp','coviddummy'])
                allcombs.append(['lppl','coviddummy'])
                allcombs.append(['luppl','coviddummy'])
                allcombs.append(['lgdpp2' , 'coviddummy'])
                allcombs.append(['lgdp' , 'lppl','coviddummy'])
                allcombs.append(['lgdp' , 'luppl','coviddummy'])
                allcombs.append(['lgdp', 'lppl', 'lgdpp','coviddummy'])          
                allcombs.append(['lgdp', 'luppl', 'lgou','coviddummy'])
                allcombs.append(['lppl', 'luppl', 'lpou','coviddummy'])

                
                aclist = []

                for i in allcombs:
                     aclist.append('ltrn~'+stitch(i))
                     

                for i in aclist:
                    model = smf.ols(i, data=country_data)
                    results = model.fit()
                    a = i.replace('ltrn~', '')
                    
                    values = pd.DataFrame(results.params).reset_index()
                    values.columns = ['names', 'coef']
                    xfinal = x_labels
                    xfinal['Intercept'] = 'Intercept'
                    xfinal = xfinal.T.reset_index()
                    xfinal.columns = ['labels', 'names']
                    export_val = xfinal.merge(values, on = 'names', how='left')
                    results.tvalues
                    t_stat = pd.DataFrame(results.tvalues).reset_index()
                    t_stat.columns = ['names', 't-statistic']
                    export_val1 = export_val.merge(t_stat, on = 'names', how='left')
                    # p-value
                    p_value = pd.DataFrame(results.pvalues).reset_index()
                    p_value.columns = ['names', 'p-value']
                    export_val1 = export_val1.merge(p_value, on = 'names', how='left')
                    
                    r_columns = ['Year'] + values.xs("names", axis = 1).tolist()
                    del r_columns[1: 2]
                    forecast_var = country_data[r_columns].reset_index(drop=True)
                    forecast_var['Intercept'] = 1           
                    test = forecast_var[forecast_var['Year']>2022] # last history year
                    xval = test.drop(columns = ['Year'])

                    
                    entry2 = pd.DataFrame({'Country ID': [rid,rid, rid, rid, rid,rid, rid, rid, rid, rid, rid, rid],
                                   'R-square': [results.rsquared, results.rsquared, results.rsquared, results.rsquared, results.rsquared, results.rsquared, results.rsquared, results.rsquared, results.rsquared, results.rsquared, results.rsquared, results.rsquared],
                                   'RegType': [a, a, a, a, a, a, a, a, a, a, a, a],
                                   'CoeID': ['intercept', 'x0', 'x1', 'x2', 'x3', 'x4', 'x5', 'x6', 'x7', 'x8', 'x9', 'coviddummy'],
                                   'Coe': [export_val1[export_val1['labels']=='Intercept']['coef'].to_list()[0], export_val1[export_val1['labels']=='x0']['coef'].to_list()[0], export_val1[export_val1['labels']=='x1']['coef'].to_list()[0], export_val1[export_val1['labels']=='x2']['coef'].to_list()[0], export_val1[export_val1['labels']=='x3']['coef'].to_list()[0], export_val1[export_val1['labels']=='x4']['coef'].to_list()[0], export_val1[export_val1['labels']=='x5']['coef'].to_list()[0], export_val1[export_val1['labels']=='x6']['coef'].to_list()[0], export_val1[export_val1['labels']=='x7']['coef'].to_list()[0], export_val1[export_val1['labels']=='x8']['coef'].to_list()[0], export_val1[export_val1['labels']=='x9']['coef'].to_list()[0], export_val1[export_val1['labels']=='coviddummy']['coef'].to_list()[0]],
                                   'tvalueID': ['t_intercept', 't_x0', 't_x1', 't_x2', 't_x3', 't_x4', 't_x5', 't_x6', 't_x7', 't_x8', 't_x9', 't_coviddummy'],
                                   'tvalue': [export_val1[export_val1['labels']=='Intercept']['t-statistic'].to_list()[0], export_val1[export_val1['labels']=='x0']['t-statistic'].to_list()[0], export_val1[export_val1['labels']=='x1']['t-statistic'].to_list()[0], export_val1[export_val1['labels']=='x2']['t-statistic'].to_list()[0], export_val1[export_val1['labels']=='x3']['t-statistic'].to_list()[0], export_val1[export_val1['labels']=='x4']['t-statistic'].to_list()[0], export_val1[export_val1['labels']=='x5']['t-statistic'].to_list()[0], export_val1[export_val1['labels']=='x6']['t-statistic'].to_list()[0], export_val1[export_val1['labels']=='x7']['t-statistic'].to_list()[0], export_val1[export_val1['labels']=='x8']['t-statistic'].to_list()[0], export_val1[export_val1['labels']=='x9']['t-statistic'].to_list()[0], export_val1[export_val1['labels']=='coviddummy']['t-statistic'].to_list()[0]],
                                   'pvalueID': ['p_intercept', 'p_x0', 'p_x1', 'p_x2', 'p_x3', 'p_x4', 'p_x5', 'p_x6', 'p_x7', 'p_x8', 'p_x9', 'p_coviddummy'],
                                   'pvalue': [export_val1[export_val1['labels']=='Intercept']['p-value'].to_list()[0], export_val1[export_val1['labels']=='x0']['p-value'].to_list()[0], export_val1[export_val1['labels']=='x1']['p-value'].to_list()[0], export_val1[export_val1['labels']=='x2']['p-value'].to_list()[0], export_val1[export_val1['labels']=='x3']['p-value'].to_list()[0], export_val1[export_val1['labels']=='x4']['p-value'].to_list()[0], export_val1[export_val1['labels']=='x5']['p-value'].to_list()[0], export_val1[export_val1['labels']=='x6']['p-value'].to_list()[0], export_val1[export_val1['labels']=='x7']['p-value'].to_list()[0], export_val1[export_val1['labels']=='x8']['p-value'].to_list()[0], export_val1[export_val1['labels']=='x9']['p-value'].to_list()[0], export_val1[export_val1['labels']=='coviddummy']['p-value'].to_list()[0]]})
                   
                    y_hat = results.predict(xval) 
                    yr_p = yrs[yrs['Year']>=2023]  # first forecast year           
                    p_export = pd.concat([yr_p, y_hat], axis=1, sort=False)
                    p_export['Country ID'] = rid
                    p_export["RegType"] = a
                    
                    cagr = p_export
                    cagr.columns = ['Year', 'lvalue', 'Country ID', 'RegType']
                    cagr['value'] = math.exp(1) ** cagr['lvalue']                    
                    cagr['test1'] = cagr['Year'] % 5
                    def fun(x): # this function is to calculate cagr, test for delete useless rows
                      if x == 2023: # the base year that you would like to calculate cagr
                        return 0
                      else:
                        return 1
                    cagr['test2'] =cagr['Year'].apply(lambda x: fun(x))
                    cagr['test'] = cagr['test1'] * cagr['test2']
                    cagr = cagr.drop(cagr[cagr.test > 0].index)
                    cagr['CAGR'] = (cagr['value'] / cagr['value'].shift(+1) ) ** (1/(cagr['Year'] - cagr['Year'].shift(+1))) - 1
                    cagr = cagr.drop(['test1', 'test2', 'test'], axis = 1)
                    
                    cagr_check = cagr.drop(cagr[cagr.Year == 2025 ].index)
                    cagr_check = cagr_check.drop(cagr_check[cagr_check.Year == 2030 ].index)
                    cagr_check = cagr_check.drop(cagr_check[cagr_check.Year == 2035 ].index)
                    cagr_check = cagr_check.drop(cagr_check[cagr_check.Year == 2040 ].index)
                    cagr_check = cagr_check.drop(cagr_check[cagr_check.Year == 2045 ].index)
                    cagr_check = cagr_check.drop(['CAGR'], axis = 1)
                    cagr_check['CAGR'] = (cagr_check['value'] / cagr_check['value'].shift(+1) ) ** (1/27) - 1 # 2050 - base year
                    cagr_check = cagr_check.drop(cagr_check[cagr_check.Year == 2023 ].index) # the base year that you would like to calculate cagr

                    p_export = p_export.drop(['test1', 'test2', 'test'], axis = 1)

                    df = pd.concat([df,entry2])
                    df2 = pd.concat([df2,p_export])
                    df3 = pd.concat([df3,cagr])
                    df4 = pd.concat([df3,cagr_check])
            
df.insert(1, "Sector", "trn")
df = df[df['Coe'].notna()]
df = pd.merge(df,trncountry,on='Country ID',how='inner') 

df2["Sector"] = 'trn'
df2.columns = ['Year', 'lvalue', 'Country ID', 'RegType','value', 'Sector']             
df2 = pd.merge(df2,trncountry,on='Country ID',how='inner') 

df3["Sector"] = 'trn'
df3.columns = ['CAGRYear', 'lvalue', 'Country ID', 'RegType', 'value', 'CAGR', 'Sector']             
df3 = pd.merge(df3,trncountry,on='Country ID',how='inner') 

df4["Sector"] = 'trn'
df4.columns = ['CAGRYear', 'lvalue', 'Country ID', 'RegType', 'value', 'CAGR', 'Sector']             
df4 = pd.merge(df4,trncountry,on='Country ID',how='inner') 


allcombs2  = DataFrame(aclist)
allcombs2["ID"] =  range(len(allcombs2)) 
allcombs2["ID"] = allcombs2["ID"] + 1
allcombs2["Sector"] = "trn"
allcombs2['RegID'] = allcombs2['ID'].apply(lambda x: 'trn00' + str(x)  if x<10 else 'trn0' +str(x) if x<100 else 'trn' + str(x))
allcombs2.columns = ['RegType', 'ID', 'Sector', 'RegID']
allcombs2['RegType']  = allcombs2['RegType'].str.replace("ltrn~", "")
trn_regid = allcombs2.drop(['ID','Sector'],axis = 1)

trn = pd.merge(df,trn_regid,on='RegType',how='inner') 
trn_p = pd.merge(df2,trn_regid,on='RegType',how='inner')
trn_cagr = pd.merge(df3,trn_regid,on='RegType',how='inner') 
trn_cagr_check = pd.merge(df4,trn_regid,on='RegType',how='inner') 

trn_regid["Sector"] = "trn"

endtime = datetime.datetime.now()
print (endtime - starttime)

print("Congradulations! Trn Finished :)")



#############

tem = pd.DataFrame()
com['Sector'] = 'com'
ind['Sector'] = 'ind'
ind2['Sector'] = 'ind'
ind3['Sector'] = 'ind'
res['Sector'] = 'res'
trn['Sector'] = 'trn'
tem = [com, ind, ind2, ind3, res, trn]
totalresult = pd.concat(tem,ignore_index=True)
order = ['Country ID', 'Country', 'Sector','R-square', 'RegType', 'RegID', 'CoeID', 'Coe', 'tvalueID', 'tvalue', 'pvalueID', 'pvalue']
totalresult =  totalresult.reindex(columns = order)

tem = pd.DataFrame()
tem = [com_p, ind_p, ind2_p, ind3_p, res_p, trn_p]
totalforecast = pd.concat(tem,ignore_index=True)
order = ['Country ID','Country','RegType', 'RegID', 'Sector', 'Year', 'lvalue', 'value']
totalforecast = totalforecast.reindex(columns = order)

totalforecast2 = totalforecast.reindex(columns = order)
totalforecast2[['Year']] = totalforecast2[['Year']].astype('float')

def cagr(x):
     if x == 2017:
      return 0
     elif x < 2021:
      return 2020
     elif x < 2026:
      return 2025
     elif x < 2031:
      return 2030
     elif x < 2036:
      return 2035
     elif x < 2041:
      return 2040 
     elif x < 2046:
      return 2045
     else:
      return 2050
                    
totalforecast2['CAGRYear'] = totalforecast2['Year'].apply(lambda x: cagr(x))

tem = pd.DataFrame()
tem = [com_cagr, ind_cagr, ind2_cagr, ind3_cagr, res_cagr, trn_cagr]
tem = pd.concat(tem,ignore_index=True)
order = ['Country ID','Country', 'Sector', 'RegType', 'RegID', 'CAGRYear', 'lvalue', 'value', 'CAGR']
tem = tem.reindex(columns = order)

totalcagr = pd.merge(totalforecast2, tem , how='left',left_on=['CAGRYear', 'RegType', 'Country', 'Country ID','RegID', 'Sector'],right_on=['CAGRYear', 'RegType', 'Country', 'Country ID','RegID', 'Sector'])
totalcagr = totalcagr.drop(['CAGRYear', 'lvalue_x', 'value_x', 'lvalue_y', 'value_y'], axis = 1)

tem = pd.DataFrame()
tem = [com_regid, ind_regid, res_regid, trn_regid]
totalregID = pd.concat(tem,ignore_index=True)


tem = pd.DataFrame()
tem = [com_cagr_check, ind_cagr_check, ind2_cagr_check, ind3_cagr_check, res_cagr_check, trn_cagr_check]
tem = pd.concat(tem,ignore_index=True)
order = ['Country ID','Country', 'Sector', 'RegType', 'RegID', 'CAGRYear', 'lvalue', 'value', 'CAGR']
tem = tem.reindex(columns = order)
totalcagr_check = pd.merge(totalforecast2, tem , how='left',left_on=['CAGRYear', 'RegType', 'Country', 'Country ID','RegID', 'Sector'],right_on=['CAGRYear', 'RegType', 'Country', 'Country ID','RegID', 'Sector'])
totalcagr_check = totalcagr_check.drop(['CAGRYear', 'lvalue_x', 'value_x', 'lvalue_y', 'value_y'], axis = 1)
totalcagr_check = totalcagr_check[totalcagr_check['Year'] == 2050]
totalcagr_check["absCAGR"] = abs(totalcagr_check["CAGR"])
totalcagr_check = totalcagr_check.sort_values(['Country', 'Sector','absCAGR'], ascending=[True,True, True])

totalresult.to_csv(r'C:\Users\jiaxi\OneDrive\Desktop\RBAC 2022\Demand\Demand Annual Builder\2022 0808\Output - Total Results 2022 0808.csv',index=None)
totalforecast.to_csv(r'C:\Users\jiaxi\OneDrive\Desktop\RBAC 2022\Demand\Demand Annual Builder\2022 0808\Output - Total Forecast 2022 0808.csv',index=None)
totalregID.to_csv(r'C:\Users\jiaxi\OneDrive\Desktop\RBAC 2022\Demand\Demand Annual Builder\2022 0808\Output - Total RegID 2022 0808.csv',index=None)
totalcagr.to_csv(r'C:\Users\jiaxi\OneDrive\Desktop\RBAC 2022\Demand\Demand Annual Builder\2022 0808\Output - Total CAGR 2022 0808.csv',index=None)
totalcagr_check.to_csv(r'C:\Users\jiaxi\OneDrive\Desktop\RBAC 2022\Demand\Demand Annual Builder\2022 0808\Output - Total CAGR Check 2022 0808.csv',index=None)



endtime = datetime.datetime.now()
print (endtime - starttime)

print("Congradulations! Total Finished :)")


########## final selection
select = pd.read_excel(r'C:\Users\jiaxi\OneDrive\Desktop\RBAC 2022\Demand\Demand Annual Builder\2022 0808\Input Final Scenario 2022 0808.xlsx', sheet_name = 'Map')
select = select.iloc[2:,0:5]
select.columns = ['Country', 'com', 'ind', 'res', 'trn']

selectcom = select.drop(['ind', 'res', 'trn'], axis = 1)
selectcom = selectcom.dropna()
selectcom.columns = ['Country', 'RegType']
selectcom['Sector'] = 'com'

selectind = select.drop(['com', 'res', 'trn'], axis = 1)
selectind = selectind.dropna()
selectind.columns = ['Country', 'RegType']
selectind['Sector'] = 'ind'

selectres = select.drop(['ind', 'com', 'trn'], axis = 1)
selectres = selectres.dropna()
selectres.columns = ['Country', 'RegType']
selectres['Sector'] = 'res'

selecttrn = select.drop(['ind', 'res', 'com'], axis = 1)
selecttrn = selecttrn.dropna()
selecttrn.columns = ['Country', 'RegType']
selecttrn['Sector'] = 'trn'

selectionfinal = pd.concat([selectcom, selectind, selectres, selecttrn])

selectcagr = pd.merge(totalcagr, selectionfinal , how='right',left_on=['Country', 'RegType', 'Sector'],right_on=['Country', 'RegType', 'Sector'])
selectcagr = selectcagr.drop(["Country ID"], axis = 1)
selectcagr.sort_values(["Country", "Sector", "Year"] , inplace=True, ascending=True) 


selectcagr_check = pd.merge(totalcagr_check, selectionfinal , how='right',left_on=['Country', 'RegType', 'Sector'],right_on=['Country', 'RegType', 'Sector'])
selectcagr_check = selectcagr_check.drop(["Country ID"], axis = 1)
selectcagr_check.sort_values(["Country", "Sector", "Year"] , inplace=True, ascending=True) 

selectforecast = pd.merge(totalforecast, selectionfinal , how='right',left_on=['Country', 'RegType', 'Sector'],right_on=['Country', 'RegType', 'Sector'])
selectforecast = selectforecast.drop(["Country ID"], axis = 1)
selectforecast.sort_values(["Country", "Sector", "Year"] , inplace=True, ascending=True) 

selectresult = pd.merge(totalresult, selectionfinal , how='right',left_on=['Country', 'RegType', 'Sector'],right_on=['Country', 'RegType', 'Sector'])
selectresult = selectresult.drop(["Country ID"], axis = 1)
selectresult.sort_values([ "Sector","Country", "RegID", "CoeID"] , inplace=True, ascending=True) 


selectresult.to_csv(r'C:\Users\jiaxi\OneDrive\Desktop\RBAC 2022\Demand\Demand Annual Builder\2022 0808\Output - Final Results 2022 0808.csv',index=None)
selectforecast.to_csv(r'C:\Users\jiaxi\OneDrive\Desktop\RBAC 2022\Demand\Demand Annual Builder\2022 0808\Output - Final Forecast 2022 0808.csv',index=None)
selectcagr.to_csv(r'C:\Users\jiaxi\OneDrive\Desktop\RBAC 2022\Demand\Demand Annual Builder\2022 0808\Output - Final CAGR 2022 0808.csv',index=None)
selectcagr_check.to_csv(r'C:\Users\jiaxi\OneDrive\Desktop\RBAC 2022\Demand\Demand Annual Builder\2022 0808\Output - Final CAGR Check 2022 0808.csv',index=None)



endtime = datetime.datetime.now()
print (endtime - starttime)

print("Congradulations! Final Finished :)")




