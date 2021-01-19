
"""
# task: grab tables from PDF to .csv, South America seasonality
# Note: in different years, the location of target tables are different;
# in different tables, the location of target cells are different.
""" 
# use camelot
# https://github.com/camelot-dev/camelot 
# $ pip install tk
# $ pip install ghostscript
# $ pip install "camelot-py[cv]"

import camelot
import pandas as pd
import datetime

# data source for monthly data: http://www.mme.gov.br/web/guest/secretarias/petroleo-gas-natural-e-biocombustiveis/publicacoes/boletim-mensal-de-acompanhamento-da-industria-de-gas-natural
# for UGS in Brazil: http://www.anp.gov.br/movimentacao-estocagem-e-comercializacao-de-gas-natural/estocagem-subterranea-de-gas-natural

starttime = datetime.datetime.now()

# Brazil
# 2010 
# read tables in Page 11
tables = camelot.read_pdf("C:\\RBAC\\Data\\South America\\Raw Files\\Boletim_Gas_Natural_nr_46_jan_11.pdf", pages = '11')
# transfer Table lists to DataFrame
tableB2010 = tables[0].df

B2010 = [["Brazil","ind","2010",tableB2010.iloc[2,4],tableB2010.iloc[2,5],tableB2010.iloc[2,6],tableB2010.iloc[2,7],tableB2010.iloc[2,8],tableB2010.iloc[2,9],tableB2010.iloc[2,10],tableB2010.iloc[2,11],tableB2010.iloc[2,12],tableB2010.iloc[2,13],tableB2010.iloc[2,14],tableB2010.iloc[2,15]], \
         ["Brazil","trn","2010",tableB2010.iloc[3,4],tableB2010.iloc[3,5],tableB2010.iloc[3,6],tableB2010.iloc[3,7],tableB2010.iloc[3,8],tableB2010.iloc[3,9],tableB2010.iloc[3,10],tableB2010.iloc[3,11],tableB2010.iloc[3,12],tableB2010.iloc[3,13],tableB2010.iloc[3,14],tableB2010.iloc[3,15]], \
         ["Brazil","res","2010",tableB2010.iloc[4,4],tableB2010.iloc[4,5],tableB2010.iloc[4,6],tableB2010.iloc[4,7],tableB2010.iloc[4,8],tableB2010.iloc[4,9],tableB2010.iloc[4,10],tableB2010.iloc[4,11],tableB2010.iloc[4,12],tableB2010.iloc[4,13],tableB2010.iloc[4,14],tableB2010.iloc[4,15]], \
         ["Brazil","com","2010",tableB2010.iloc[5,4],tableB2010.iloc[5,5],tableB2010.iloc[5,6],tableB2010.iloc[5,7],tableB2010.iloc[5,8],tableB2010.iloc[5,9],tableB2010.iloc[5,10],tableB2010.iloc[5,11],tableB2010.iloc[5,12],tableB2010.iloc[5,13],tableB2010.iloc[5,14],tableB2010.iloc[5,15]], \
         ["Brazil","elc1","2010",tableB2010.iloc[6,4],tableB2010.iloc[6,5],tableB2010.iloc[6,6],tableB2010.iloc[6,7],tableB2010.iloc[6,8],tableB2010.iloc[6,9],tableB2010.iloc[6,10],tableB2010.iloc[6,11],tableB2010.iloc[6,12],tableB2010.iloc[6,13],tableB2010.iloc[6,14],tableB2010.iloc[6,15]], \
         ["Brazil","elc2","2010",tableB2010.iloc[7,4], tableB2010.iloc[7,5],tableB2010.iloc[7,6],tableB2010.iloc[7,7],tableB2010.iloc[7,8],tableB2010.iloc[7,9],tableB2010.iloc[7,10],tableB2010.iloc[7,11],tableB2010.iloc[7,12],tableB2010.iloc[7,13],tableB2010.iloc[7,14],tableB2010.iloc[7,15]]] 

# into dataframe
dfB2010 = pd.DataFrame(B2010,columns=["country","sector","year","1","2","3","4","5","6","7","8","9","10","11","12"])

# 2011 
# read tables in Page 8
tables = camelot.read_pdf("C:\\RBAC\\Data\\South America\\Raw Files\\Boletim_Gas_Natural_nr_58_jan_12.pdf", pages = '8')
# transfer Table lists to DataFrame
tableB2011 = tables[0].df

B2011 = [["Brazil","ind","2011",tableB2011.iloc[2,5],tableB2011.iloc[2,6],tableB2011.iloc[2,7],tableB2011.iloc[2,8],tableB2011.iloc[2,9],tableB2011.iloc[2,10],tableB2011.iloc[2,11],tableB2011.iloc[2,12],tableB2011.iloc[2,13],tableB2011.iloc[2,14],tableB2011.iloc[2,15],tableB2011.iloc[2,16]], \
         ["Brazil","trn","2011",tableB2011.iloc[3,5],tableB2011.iloc[3,6],tableB2011.iloc[3,7],tableB2011.iloc[3,8],tableB2011.iloc[3,9],tableB2011.iloc[3,10],tableB2011.iloc[3,11],tableB2011.iloc[3,12],tableB2011.iloc[3,13],tableB2011.iloc[3,14],tableB2011.iloc[3,15],tableB2011.iloc[3,16]], \
         ["Brazil","res","2011",tableB2011.iloc[4,5],tableB2011.iloc[4,6],tableB2011.iloc[4,7],tableB2011.iloc[4,8],tableB2011.iloc[4,9],tableB2011.iloc[4,10],tableB2011.iloc[4,11],tableB2011.iloc[4,12],tableB2011.iloc[4,13],tableB2011.iloc[4,14],tableB2011.iloc[4,15],tableB2011.iloc[4,16]], \
         ["Brazil","com","2011",tableB2011.iloc[5,5],tableB2011.iloc[5,6],tableB2011.iloc[5,7],tableB2011.iloc[5,8],tableB2011.iloc[5,9],tableB2011.iloc[5,10],tableB2011.iloc[5,11],tableB2011.iloc[5,12],tableB2011.iloc[5,13],tableB2011.iloc[5,14],tableB2011.iloc[5,15],tableB2011.iloc[5,16]], \
         ["Brazil","elc1","2011",tableB2011.iloc[6,5],tableB2011.iloc[6,6],tableB2011.iloc[6,7],tableB2011.iloc[6,8],tableB2011.iloc[6,9],tableB2011.iloc[6,10],tableB2011.iloc[6,11],tableB2011.iloc[6,12],tableB2011.iloc[6,13],tableB2011.iloc[6,14],tableB2011.iloc[6,15],tableB2011.iloc[6,16]], \
         ["Brazil","elc2","2011",tableB2011.iloc[7,5],tableB2011.iloc[7,6],tableB2011.iloc[7,7],tableB2011.iloc[7,8],tableB2011.iloc[7,9],tableB2011.iloc[7,10],tableB2011.iloc[7,11],tableB2011.iloc[7,12],tableB2011.iloc[7,13],tableB2011.iloc[7,14],tableB2011.iloc[7,15],tableB2011.iloc[7,16]]] 

# into dataframe
dfB2011 = pd.DataFrame(B2011,columns=["country","sector","year","1","2","3","4","5","6","7","8","9","10","11","12"])

# 2012 
# read tables in Page 8
tables = camelot.read_pdf("C:\\RBAC\\Data\\South America\\Raw Files\\Boletim_Gas_Natural_nr_70_jan_13_.pdf", pages = '8')
# transfer Table lists to DataFrame
tableB2012 = tables[0].df

B2012 = [["Brazil","ind","2012",tableB2012.iloc[2,5],tableB2012.iloc[2,6],tableB2012.iloc[2,7],tableB2012.iloc[2,8],tableB2012.iloc[2,9],tableB2012.iloc[2,10],tableB2012.iloc[2,11],tableB2012.iloc[2,12],tableB2012.iloc[2,13],tableB2012.iloc[2,14],tableB2012.iloc[2,15],tableB2012.iloc[2,16]], \
         ["Brazil","trn","2012",tableB2012.iloc[3,5],tableB2012.iloc[3,6],tableB2012.iloc[3,7],tableB2012.iloc[3,8],tableB2012.iloc[3,9],tableB2012.iloc[3,10],tableB2012.iloc[3,11],tableB2012.iloc[3,12],tableB2012.iloc[3,13],tableB2012.iloc[3,14],tableB2012.iloc[3,15],tableB2012.iloc[3,16]], \
         ["Brazil","res","2012",tableB2012.iloc[4,5],tableB2012.iloc[4,6],tableB2012.iloc[4,7],tableB2012.iloc[4,8],tableB2012.iloc[4,9],tableB2012.iloc[4,10],tableB2012.iloc[4,11],tableB2012.iloc[4,12],tableB2012.iloc[4,13],tableB2012.iloc[4,14],tableB2012.iloc[4,15],tableB2012.iloc[4,16]], \
         ["Brazil","com","2012",tableB2012.iloc[5,5],tableB2012.iloc[5,6],tableB2012.iloc[5,7],tableB2012.iloc[5,8],tableB2012.iloc[5,9],tableB2012.iloc[5,10],tableB2012.iloc[5,11],tableB2012.iloc[5,12],tableB2012.iloc[5,13],tableB2012.iloc[5,14],tableB2012.iloc[5,15],tableB2012.iloc[5,16]], \
         ["Brazil","elc1","2012",tableB2012.iloc[6,5],tableB2012.iloc[6,6],tableB2012.iloc[6,7],tableB2012.iloc[6,8],tableB2012.iloc[6,9],tableB2012.iloc[6,10],tableB2012.iloc[6,11],tableB2012.iloc[6,12],tableB2012.iloc[6,13],tableB2012.iloc[6,14],tableB2012.iloc[6,15],tableB2012.iloc[6,16]], \
         ["Brazil","elc2","2012",tableB2012.iloc[7,5],tableB2012.iloc[7,6],tableB2012.iloc[7,7],tableB2012.iloc[7,8],tableB2012.iloc[7,9],tableB2012.iloc[7,10],tableB2012.iloc[7,11],tableB2012.iloc[7,12],tableB2012.iloc[7,13],tableB2012.iloc[7,14],tableB2012.iloc[7,15],tableB2012.iloc[7,16]]] 

# into dataframe
dfB2012 = pd.DataFrame(B2012,columns=["country","sector","year","1","2","3","4","5","6","7","8","9","10","11","12"])


# 2013 
# read tables in Page 8
tables = camelot.read_pdf("C:\\RBAC\\Data\\South America\\Raw Files\\Boletim Mensal de Acompanhamento da Indústria de Gás Natural n 82 - Janeiro 2014.pdf", pages = '9')
# transfer Table lists to DataFrame
tableB2013 = tables[0].df

B2013 = [["Brazil","ind","2013",tableB2013.iloc[2,6],tableB2013.iloc[2,7],tableB2013.iloc[2,8],tableB2013.iloc[2,9],tableB2013.iloc[2,10],tableB2013.iloc[2,11],tableB2013.iloc[2,12],tableB2013.iloc[2,13],tableB2013.iloc[2,14],tableB2013.iloc[2,15],tableB2013.iloc[2,16],tableB2013.iloc[2,17]], \
         ["Brazil","trn","2013",tableB2013.iloc[3,6],tableB2013.iloc[3,7],tableB2013.iloc[3,8],tableB2013.iloc[3,9],tableB2013.iloc[3,10],tableB2013.iloc[3,11],tableB2013.iloc[3,12],tableB2013.iloc[3,13],tableB2013.iloc[3,14],tableB2013.iloc[3,15],tableB2013.iloc[3,16],tableB2013.iloc[3,17]], \
         ["Brazil","res","2013",tableB2013.iloc[4,6],tableB2013.iloc[4,7],tableB2013.iloc[4,8],tableB2013.iloc[4,9],tableB2013.iloc[4,10],tableB2013.iloc[4,11],tableB2013.iloc[4,12],tableB2013.iloc[4,13],tableB2013.iloc[4,14],tableB2013.iloc[4,15],tableB2013.iloc[4,16],tableB2013.iloc[4,17]], \
         ["Brazil","com","2013",tableB2013.iloc[5,6],tableB2013.iloc[5,7],tableB2013.iloc[5,8],tableB2013.iloc[5,9],tableB2013.iloc[5,10],tableB2013.iloc[5,11],tableB2013.iloc[5,12],tableB2013.iloc[5,13],tableB2013.iloc[5,14],tableB2013.iloc[5,15],tableB2013.iloc[5,16],tableB2013.iloc[5,17]], \
         ["Brazil","elc1","2013",tableB2013.iloc[6,6],tableB2013.iloc[6,7],tableB2013.iloc[6,8],tableB2013.iloc[6,9],tableB2013.iloc[6,10],tableB2013.iloc[6,11],tableB2013.iloc[6,12],tableB2013.iloc[6,13],tableB2013.iloc[6,14],tableB2013.iloc[6,15],tableB2013.iloc[6,16],tableB2013.iloc[6,17]], \
         ["Brazil","elc2","2013",tableB2013.iloc[7,6],tableB2013.iloc[7,7],tableB2013.iloc[7,8],tableB2013.iloc[7,9],tableB2013.iloc[7,10],tableB2013.iloc[7,11],tableB2013.iloc[7,12],tableB2013.iloc[7,13],tableB2013.iloc[7,14],tableB2013.iloc[7,15],tableB2013.iloc[7,16],tableB2013.iloc[7,17]]] 

# into dataframe
dfB2013 = pd.DataFrame(B2013,columns=["country","sector","year","1","2","3","4","5","6","7","8","9","10","11","12"])

# 2014 
# read tables in Page 8
tables = camelot.read_pdf("C:\\RBAC\\Data\\South America\\Raw Files\\Boletim_Gas_Natural_nr_94_jan_15 - Completo.pdf", pages = '9')
# transfer Table lists to DataFrame
tableB2014 = tables[0].df

B2014 = [["Brazil","ind","2014",tableB2014.iloc[2,6],tableB2014.iloc[2,7],tableB2014.iloc[2,8],tableB2014.iloc[2,9],tableB2014.iloc[2,10],tableB2014.iloc[2,11],tableB2014.iloc[2,12],tableB2014.iloc[2,13],tableB2014.iloc[2,14],tableB2014.iloc[2,15],tableB2014.iloc[2,16],tableB2014.iloc[2,17]], \
         ["Brazil","trn","2014",tableB2014.iloc[3,6],tableB2014.iloc[3,7],tableB2014.iloc[3,8],tableB2014.iloc[3,9],tableB2014.iloc[3,10],tableB2014.iloc[3,11],tableB2014.iloc[3,12],tableB2014.iloc[3,13],tableB2014.iloc[3,14],tableB2014.iloc[3,15],tableB2014.iloc[3,16],tableB2014.iloc[3,17]], \
         ["Brazil","res","2014",tableB2014.iloc[4,6],tableB2014.iloc[4,7],tableB2014.iloc[4,8],tableB2014.iloc[4,9],tableB2014.iloc[4,10],tableB2014.iloc[4,11],tableB2014.iloc[4,12],tableB2014.iloc[4,13],tableB2014.iloc[4,14],tableB2014.iloc[4,15],tableB2014.iloc[4,16],tableB2014.iloc[4,17]], \
         ["Brazil","com","2014",tableB2014.iloc[5,6],tableB2014.iloc[5,7],tableB2014.iloc[5,8],tableB2014.iloc[5,9],tableB2014.iloc[5,10],tableB2014.iloc[5,11],tableB2014.iloc[5,12],tableB2014.iloc[5,13],tableB2014.iloc[5,14],tableB2014.iloc[5,15],tableB2014.iloc[5,16],tableB2014.iloc[5,17]], \
         ["Brazil","elc1","2014",tableB2014.iloc[6,6],tableB2014.iloc[6,7],tableB2014.iloc[6,8],tableB2014.iloc[6,9],tableB2014.iloc[6,10],tableB2014.iloc[6,11],tableB2014.iloc[6,12],tableB2014.iloc[6,13],tableB2014.iloc[6,14],tableB2014.iloc[6,15],tableB2014.iloc[6,16],tableB2014.iloc[6,17]], \
         ["Brazil","elc2","2014",tableB2014.iloc[7,6],tableB2014.iloc[7,7],tableB2014.iloc[7,8],tableB2014.iloc[7,9],tableB2014.iloc[7,10],tableB2014.iloc[7,11],tableB2014.iloc[7,12],tableB2014.iloc[7,13],tableB2014.iloc[7,14],tableB2014.iloc[7,15],tableB2014.iloc[7,16],tableB2014.iloc[7,17]]] 

# into dataframe
dfB2014 = pd.DataFrame(B2014,columns=["country","sector","year","1","2","3","4","5","6","7","8","9","10","11","12"])


# 2015 
# read tables in Page 8
tables = camelot.read_pdf("C:\\RBAC\\Data\\South America\\Raw Files\\Boletim_Gas_Natural_nr_106_dez_15.pdf", pages = '2')
# transfer Table lists to DataFrame
tableB2015 = tables[0].df

B2015 = [["Brazil","ind","2015",tableB2015.iloc[17,6],tableB2015.iloc[17,7],tableB2015.iloc[17,8],tableB2015.iloc[17,9],tableB2015.iloc[17,10],tableB2015.iloc[17,11],tableB2015.iloc[17,12],tableB2015.iloc[17,13],tableB2015.iloc[17,14],tableB2015.iloc[17,15],tableB2015.iloc[17,16],tableB2015.iloc[17,17]], \
         ["Brazil","trn","2015",tableB2015.iloc[18,6],tableB2015.iloc[18,7],tableB2015.iloc[18,8],tableB2015.iloc[18,9],tableB2015.iloc[18,10],tableB2015.iloc[18,11],tableB2015.iloc[18,12],tableB2015.iloc[18,13],tableB2015.iloc[18,14],tableB2015.iloc[18,15],tableB2015.iloc[18,16],tableB2015.iloc[18,17]], \
         ["Brazil","res","2015",tableB2015.iloc[19,6],tableB2015.iloc[19,7],tableB2015.iloc[19,8],tableB2015.iloc[19,9],tableB2015.iloc[19,10],tableB2015.iloc[19,11],tableB2015.iloc[19,12],tableB2015.iloc[19,13],tableB2015.iloc[19,14],tableB2015.iloc[19,15],tableB2015.iloc[19,16],tableB2015.iloc[19,17]], \
         ["Brazil","com","2015",tableB2015.iloc[20,6],tableB2015.iloc[20,7],tableB2015.iloc[20,8],tableB2015.iloc[20,9],tableB2015.iloc[20,10],tableB2015.iloc[20,11],tableB2015.iloc[20,12],tableB2015.iloc[20,13],tableB2015.iloc[20,14],tableB2015.iloc[20,15],tableB2015.iloc[20,16],tableB2015.iloc[20,17]], \
         ["Brazil","elc1","2015",tableB2015.iloc[21,6],tableB2015.iloc[21,7],tableB2015.iloc[21,8],tableB2015.iloc[21,9],tableB2015.iloc[21,10],tableB2015.iloc[21,11],tableB2015.iloc[21,12],tableB2015.iloc[21,13],tableB2015.iloc[21,14],tableB2015.iloc[21,15],tableB2015.iloc[21,16],tableB2015.iloc[21,17]], \
         ["Brazil","elc2","2015",tableB2015.iloc[22,6],tableB2015.iloc[22,7],tableB2015.iloc[22,8],tableB2015.iloc[22,9],tableB2015.iloc[22,10],tableB2015.iloc[22,11],tableB2015.iloc[22,12],tableB2015.iloc[22,13],tableB2015.iloc[22,14],tableB2015.iloc[22,15],tableB2015.iloc[22,16],tableB2015.iloc[22,17]]] 

# into dataframe
dfB2015 = pd.DataFrame(B2015,columns=["country","sector","year","1","2","3","4","5","6","7","8","9","10","11","12"])


# 2016 
# read tables in Page 8
tables = camelot.read_pdf("C:\\RBAC\\Data\\South America\\Raw Files\\Boletim_Gas_Natural_nr_118_DEZ_16.pdf", pages = '2')
# transfer Table lists to DataFrame
tableB2016 = tables[0].df

B2016 = [["Brazil","ind","2016",tableB2016.iloc[16,7],tableB2016.iloc[16,8],tableB2016.iloc[16,9],tableB2016.iloc[16,10],tableB2016.iloc[16,11],tableB2016.iloc[16,12],tableB2016.iloc[16,13],tableB2016.iloc[16,14],tableB2016.iloc[16,15],tableB2016.iloc[16,16],tableB2016.iloc[16,17],tableB2016.iloc[16,18]], \
         ["Brazil","trn","2016",tableB2016.iloc[17,7],tableB2016.iloc[17,8],tableB2016.iloc[17,9],tableB2016.iloc[17,10],tableB2016.iloc[17,11],tableB2016.iloc[17,12],tableB2016.iloc[17,13],tableB2016.iloc[17,14],tableB2016.iloc[17,15],tableB2016.iloc[17,16],tableB2016.iloc[17,17],tableB2016.iloc[17,18]], \
         ["Brazil","res","2016",tableB2016.iloc[18,7],tableB2016.iloc[18,8],tableB2016.iloc[18,9],tableB2016.iloc[18,10],tableB2016.iloc[18,11],tableB2016.iloc[18,12],tableB2016.iloc[18,13],tableB2016.iloc[18,14],tableB2016.iloc[18,15],tableB2016.iloc[18,16],tableB2016.iloc[18,17],tableB2016.iloc[18,18]], \
         ["Brazil","com","2016",tableB2016.iloc[19,7],tableB2016.iloc[19,8],tableB2016.iloc[19,9],tableB2016.iloc[19,10],tableB2016.iloc[19,11],tableB2016.iloc[19,12],tableB2016.iloc[19,13],tableB2016.iloc[19,14],tableB2016.iloc[19,15],tableB2016.iloc[19,16],tableB2016.iloc[19,17],tableB2016.iloc[19,18]], \
         ["Brazil","elc1","2016",tableB2016.iloc[20,7],tableB2016.iloc[20,8],tableB2016.iloc[20,9],tableB2016.iloc[20,10],tableB2016.iloc[20,11],tableB2016.iloc[20,12],tableB2016.iloc[20,13],tableB2016.iloc[20,14],tableB2016.iloc[20,15],tableB2016.iloc[20,16],tableB2016.iloc[20,17],tableB2016.iloc[20,18]], \
         ["Brazil","elc2","2016",tableB2016.iloc[21,7],tableB2016.iloc[21,8],tableB2016.iloc[21,9],tableB2016.iloc[21,10],tableB2016.iloc[21,11],tableB2016.iloc[21,12],tableB2016.iloc[21,13],tableB2016.iloc[21,14],tableB2016.iloc[21,15],tableB2016.iloc[21,16],tableB2016.iloc[21,17],tableB2016.iloc[21,18]]] 

# into dataframe
dfB2016 = pd.DataFrame(B2016,columns=["country","sector","year","1","2","3","4","5","6","7","8","9","10","11","12"]) 


# 2017 
# read tables in Page 8
tables = camelot.read_pdf("C:\\RBAC\\Data\\South America\\Raw Files\\Boletim_Gas_Natural_nr_130_DEZ_17.pdf", pages = '2')
# transfer Table lists to DataFrame
tableB2017 = tables[0].df

B2017 = [["Brazil","ind","2017",tableB2017.iloc[17,6],tableB2017.iloc[17,7],tableB2017.iloc[17,8],tableB2017.iloc[17,9],tableB2017.iloc[17,10],tableB2017.iloc[17,11],tableB2017.iloc[17,12],tableB2017.iloc[17,13],tableB2017.iloc[17,14],tableB2017.iloc[17,15],tableB2017.iloc[17,16],tableB2017.iloc[17,17]], \
         ["Brazil","trn","2017",tableB2017.iloc[18,6],tableB2017.iloc[18,7],tableB2017.iloc[18,8],tableB2017.iloc[18,9],tableB2017.iloc[18,10],tableB2017.iloc[18,11],tableB2017.iloc[18,12],tableB2017.iloc[18,13],tableB2017.iloc[18,14],tableB2017.iloc[18,15],tableB2017.iloc[18,16],tableB2017.iloc[18,17]], \
         ["Brazil","res","2017",tableB2017.iloc[19,6],tableB2017.iloc[19,7],tableB2017.iloc[19,8],tableB2017.iloc[19,9],tableB2017.iloc[19,10],tableB2017.iloc[19,11],tableB2017.iloc[19,12],tableB2017.iloc[19,13],tableB2017.iloc[19,14],tableB2017.iloc[19,15],tableB2017.iloc[19,16],tableB2017.iloc[19,17]], \
         ["Brazil","com","2017",tableB2017.iloc[20,6],tableB2017.iloc[20,7],tableB2017.iloc[20,8],tableB2017.iloc[20,9],tableB2017.iloc[20,10],tableB2017.iloc[20,11],tableB2017.iloc[20,12],tableB2017.iloc[20,13],tableB2017.iloc[20,14],tableB2017.iloc[20,15],tableB2017.iloc[20,16],tableB2017.iloc[20,17]], \
         ["Brazil","elc1","2017",tableB2017.iloc[21,6],tableB2017.iloc[21,7],tableB2017.iloc[21,8],tableB2017.iloc[21,9],tableB2017.iloc[21,10],tableB2017.iloc[21,11],tableB2017.iloc[21,12],tableB2017.iloc[21,13],tableB2017.iloc[21,14],tableB2017.iloc[21,15],tableB2017.iloc[21,16],tableB2017.iloc[21,17]], \
         ["Brazil","elc2","2017",tableB2017.iloc[22,6],tableB2017.iloc[22,7],tableB2017.iloc[22,8],tableB2017.iloc[22,9],tableB2017.iloc[22,10],tableB2017.iloc[22,11],tableB2017.iloc[22,12],tableB2017.iloc[22,13],tableB2017.iloc[22,14],tableB2017.iloc[22,15],tableB2017.iloc[22,16],tableB2017.iloc[22,17]]] 

# into dataframe
dfB2017 = pd.DataFrame(B2017,columns=["country","sector","year","1","2","3","4","5","6","7","8","9","10","11","12"]) 

# 2018 
# read tables in Page 8
tables = camelot.read_pdf("C:\\RBAC\\Data\\South America\\Raw Files\\Boletim_Gas_Natural_nr_142_DEZ_18.pdf", pages = '2')
# transfer Table lists to DataFrame
tableB2018 = tables[0].df

B2018 = [["Brazil","ind","2018",tableB2018.iloc[18,6],tableB2018.iloc[18,7],tableB2018.iloc[18,8],tableB2018.iloc[18,9],tableB2018.iloc[18,10],tableB2018.iloc[18,11],tableB2018.iloc[18,12],tableB2018.iloc[18,13],tableB2018.iloc[18,14],tableB2018.iloc[18,15],tableB2018.iloc[18,16],tableB2018.iloc[18,17]], \
         ["Brazil","trn","2018",tableB2018.iloc[19,6],tableB2018.iloc[19,7],tableB2018.iloc[19,8],tableB2018.iloc[19,9],tableB2018.iloc[19,10],tableB2018.iloc[19,11],tableB2018.iloc[19,12],tableB2018.iloc[19,13],tableB2018.iloc[19,14],tableB2018.iloc[19,15],tableB2018.iloc[19,16],tableB2018.iloc[19,17]], \
         ["Brazil","res","2018",tableB2018.iloc[20,6],tableB2018.iloc[20,7],tableB2018.iloc[20,8],tableB2018.iloc[20,9],tableB2018.iloc[20,10],tableB2018.iloc[20,11],tableB2018.iloc[20,12],tableB2018.iloc[20,13],tableB2018.iloc[20,14],tableB2018.iloc[20,15],tableB2018.iloc[20,16],tableB2018.iloc[20,17]], \
         ["Brazil","com","2018",tableB2018.iloc[21,6],tableB2018.iloc[21,7],tableB2018.iloc[21,8],tableB2018.iloc[21,9],tableB2018.iloc[21,10],tableB2018.iloc[21,11],tableB2018.iloc[21,12],tableB2018.iloc[21,13],tableB2018.iloc[21,14],tableB2018.iloc[21,15],tableB2018.iloc[21,16],tableB2018.iloc[21,17]], \
         ["Brazil","elc1","2018",tableB2018.iloc[22,6],tableB2018.iloc[22,7],tableB2018.iloc[22,8],tableB2018.iloc[22,9],tableB2018.iloc[22,10],tableB2018.iloc[22,11],tableB2018.iloc[22,12],tableB2018.iloc[22,13],tableB2018.iloc[22,14],tableB2018.iloc[22,15],tableB2018.iloc[22,16],tableB2018.iloc[22,17]], \
         ["Brazil","elc2","2018",tableB2018.iloc[23,6],tableB2018.iloc[23,7],tableB2018.iloc[23,8],tableB2018.iloc[23,9],tableB2018.iloc[23,10],tableB2018.iloc[23,11],tableB2018.iloc[23,12],tableB2018.iloc[23,13],tableB2018.iloc[23,14],tableB2018.iloc[23,15],tableB2018.iloc[23,16],tableB2018.iloc[23,17]]] 

# into dataframe
dfB2018 = pd.DataFrame(B2018,columns=["country","sector","year","1","2","3","4","5","6","7","8","9","10","11","12"]) 


# 2019 
# read tables in Page 8
tables = camelot.read_pdf("C:\\RBAC\\Data\\South America\\Raw Files\\12 - Boletim Mensal de Acompanhamento da Indústria de Gás Natural Dezembro 2019.pdf", pages = '2')
# transfer Table lists to DataFrame
tableB2019 = tables[0].df

B2019 = [["Brazil","ind","2019",tableB2019.iloc[20,5],tableB2019.iloc[20,6],tableB2019.iloc[20,7],tableB2019.iloc[20,8],tableB2019.iloc[20,9],tableB2019.iloc[20,10],tableB2019.iloc[20,11],tableB2019.iloc[20,12],tableB2019.iloc[20,13],tableB2019.iloc[20,14],tableB2019.iloc[20,15],tableB2019.iloc[20,16]], \
         ["Brazil","trn","2019",tableB2019.iloc[21,5],tableB2019.iloc[21,6],tableB2019.iloc[21,7],tableB2019.iloc[21,8],tableB2019.iloc[21,9],tableB2019.iloc[21,10],tableB2019.iloc[21,11],tableB2019.iloc[21,12],tableB2019.iloc[21,13],tableB2019.iloc[21,14],tableB2019.iloc[21,15],tableB2019.iloc[21,16]], \
         ["Brazil","res","2019",tableB2019.iloc[22,5],tableB2019.iloc[22,6],tableB2019.iloc[22,7],tableB2019.iloc[22,8],tableB2019.iloc[22,9],tableB2019.iloc[22,10],tableB2019.iloc[22,11],tableB2019.iloc[22,12],tableB2019.iloc[22,13],tableB2019.iloc[22,14],tableB2019.iloc[22,15],tableB2019.iloc[22,16]], \
         ["Brazil","com","2019",tableB2019.iloc[23,5],tableB2019.iloc[23,6],tableB2019.iloc[23,7],tableB2019.iloc[23,8],tableB2019.iloc[23,9],tableB2019.iloc[23,10],tableB2019.iloc[23,11],tableB2019.iloc[23,12],tableB2019.iloc[23,13],tableB2019.iloc[23,14],tableB2019.iloc[23,15],tableB2019.iloc[23,16]], \
         ["Brazil","elc1","2019",tableB2019.iloc[24,5],tableB2019.iloc[24,6],tableB2019.iloc[24,7],tableB2019.iloc[24,8],tableB2019.iloc[24,9],tableB2019.iloc[24,10],tableB2019.iloc[24,11],tableB2019.iloc[24,12],tableB2019.iloc[24,13],tableB2019.iloc[24,14],tableB2019.iloc[24,15],tableB2019.iloc[24,16]], \
         ["Brazil","elc2","2019",tableB2019.iloc[25,5],tableB2019.iloc[25,6],tableB2019.iloc[25,7],tableB2019.iloc[25,8],tableB2019.iloc[25,9],tableB2019.iloc[25,10],tableB2019.iloc[25,11],tableB2019.iloc[25,12],tableB2019.iloc[25,13],tableB2019.iloc[25,14],tableB2019.iloc[25,15],tableB2019.iloc[25,16]]] 

# into dataframe
dfB2019 = pd.DataFrame(B2019,columns=["country","sector","year","1","2","3","4","5","6","7","8","9","10","11","12"]) 

# 2020 
# read tables in Page 8
tables = camelot.read_pdf("C:\\RBAC\\Data\\South America\\Raw Files\\07. Boletim Mensal de Acompanhamento da Indústria de Gás Natural - Julho 2020.pdf", pages = '2')
# transfer Table lists to DataFrame
tableB2020 = tables[0].df

B2020 = [["Brazil","ind","2020",tableB2020.iloc[19,6],tableB2020.iloc[19,7],tableB2020.iloc[19,8],tableB2020.iloc[19,9],tableB2020.iloc[19,10],tableB2020.iloc[19,11],tableB2020.iloc[19,12],tableB2020.iloc[19,13],tableB2020.iloc[19,14],tableB2020.iloc[19,15],tableB2020.iloc[19,16],tableB2020.iloc[19,17]], \
         ["Brazil","trn","2020",tableB2020.iloc[20,6],tableB2020.iloc[20,7],tableB2020.iloc[20,8],tableB2020.iloc[20,9],tableB2020.iloc[20,10],tableB2020.iloc[20,11],tableB2020.iloc[20,12],tableB2020.iloc[20,13],tableB2020.iloc[20,14],tableB2020.iloc[20,15],tableB2020.iloc[20,16],tableB2020.iloc[20,17]], \
         ["Brazil","res","2020",tableB2020.iloc[21,6],tableB2020.iloc[21,7],tableB2020.iloc[21,8],tableB2020.iloc[21,9],tableB2020.iloc[21,10],tableB2020.iloc[21,11],tableB2020.iloc[21,12],tableB2020.iloc[21,13],tableB2020.iloc[21,14],tableB2020.iloc[21,15],tableB2020.iloc[21,16],tableB2020.iloc[21,17]], \
         ["Brazil","com","2020",tableB2020.iloc[22,6],tableB2020.iloc[22,7],tableB2020.iloc[22,8],tableB2020.iloc[22,9],tableB2020.iloc[22,10],tableB2020.iloc[22,11],tableB2020.iloc[22,12],tableB2020.iloc[22,13],tableB2020.iloc[22,14],tableB2020.iloc[22,15],tableB2020.iloc[22,16],tableB2020.iloc[22,17]], \
         ["Brazil","elc1","2020",tableB2020.iloc[23,6],tableB2020.iloc[23,7],tableB2020.iloc[23,8],tableB2020.iloc[23,9],tableB2020.iloc[23,10],tableB2020.iloc[23,11],tableB2020.iloc[23,12],tableB2020.iloc[23,13],tableB2020.iloc[23,14],tableB2020.iloc[23,15],tableB2020.iloc[23,16],tableB2020.iloc[23,17]], \
         ["Brazil","elc2","2020",tableB2020.iloc[24,6],tableB2020.iloc[24,7],tableB2020.iloc[24,8],tableB2020.iloc[24,9],tableB2020.iloc[24,10],tableB2020.iloc[24,11],tableB2020.iloc[24,12],tableB2020.iloc[24,13],tableB2020.iloc[24,14],tableB2020.iloc[24,15],tableB2020.iloc[24,16],tableB2020.iloc[24,17]]] 

# into dataframe
dfB2020 = pd.DataFrame(B2020,columns=["country","sector","year","1","2","3","4","5","6","7","8","9","10","11","12"]) 



####################################################################
# Argentina
# 2010 
tables = camelot.read_pdf("C:\\RBAC\\Data\\South America\\Raw Files\\Argentina\\Boletim_Gas_Natural_nr_47_fev_11.pdf", pages = '10')
# transfer Table lists to DataFrame
tableA2010 = tables[0].df

A2010 = [["Argentina","res","2010",tableA2010.iloc[20,4],tableA2010.iloc[20,5],tableA2010.iloc[20,6],tableA2010.iloc[20,7],tableA2010.iloc[20,8],tableA2010.iloc[20,9],tableA2010.iloc[20,10],tableA2010.iloc[20,11],tableA2010.iloc[20,12],tableA2010.iloc[20,13],tableA2010.iloc[20,14],tableA2010.iloc[20,15]], \
         ["Argentina","com","2010",tableA2010.iloc[21,4],tableA2010.iloc[21,5],tableA2010.iloc[21,6],tableA2010.iloc[21,7],tableA2010.iloc[21,8],tableA2010.iloc[21,9],tableA2010.iloc[21,10],tableA2010.iloc[21,11],tableA2010.iloc[21,12],tableA2010.iloc[21,13],tableA2010.iloc[21,14],tableA2010.iloc[21,15]], \
         ["Argentina","trn","2010",tableA2010.iloc[22,4],tableA2010.iloc[22,5],tableA2010.iloc[22,6],tableA2010.iloc[22,7],tableA2010.iloc[22,8],tableA2010.iloc[22,9],tableA2010.iloc[22,10],tableA2010.iloc[22,11],tableA2010.iloc[22,12],tableA2010.iloc[22,13],tableA2010.iloc[22,14],tableA2010.iloc[22,15]], \
         ["Argentina","elc","2010",tableA2010.iloc[23,4],tableA2010.iloc[23,5],tableA2010.iloc[23,6],tableA2010.iloc[23,7],tableA2010.iloc[23,8],tableA2010.iloc[23,9],tableA2010.iloc[23,10],tableA2010.iloc[23,11],tableA2010.iloc[23,12],tableA2010.iloc[23,13],tableA2010.iloc[23,14],tableA2010.iloc[23,15]], \
         ["Argentina","ind","2010",tableA2010.iloc[24,4],tableA2010.iloc[24,5],tableA2010.iloc[24,6],tableA2010.iloc[24,7],tableA2010.iloc[24,8],tableA2010.iloc[24,9],tableA2010.iloc[24,10],tableA2010.iloc[24,11],tableA2010.iloc[24,12],tableA2010.iloc[24,13],tableA2010.iloc[24,14],tableA2010.iloc[24,15]]]                     

dfA2010 = pd.DataFrame(A2010,columns=["country","sector","year","1","2","3","4","5","6","7","8","9","10","11","12"]) 


# 2011 
tables = camelot.read_pdf("C:\\RBAC\\Data\\South America\\Raw Files\\Argentina\\Boletim_Gas_Natural_nr_59_fev_12.pdf", pages = '17')
# transfer Table lists to DataFrame
tableA2011 = tables[0].df

A2011 = [["Argentina","res","2011",tableA2011.iloc[20,5],tableA2011.iloc[20,6],tableA2011.iloc[20,7],tableA2011.iloc[20,8],tableA2011.iloc[20,9],tableA2011.iloc[20,10],tableA2011.iloc[20,11],tableA2011.iloc[20,12],tableA2011.iloc[20,13],tableA2011.iloc[20,14],tableA2011.iloc[20,15],tableA2011.iloc[20,16]], \
         ["Argentina","com","2011",tableA2011.iloc[21,5],tableA2011.iloc[21,6],tableA2011.iloc[21,7],tableA2011.iloc[21,8],tableA2011.iloc[21,9],tableA2011.iloc[21,10],tableA2011.iloc[21,11],tableA2011.iloc[21,12],tableA2011.iloc[21,13],tableA2011.iloc[21,14],tableA2011.iloc[21,15],tableA2011.iloc[21,16]], \
         ["Argentina","trn","2011",tableA2011.iloc[22,5],tableA2011.iloc[22,6],tableA2011.iloc[22,7],tableA2011.iloc[22,8],tableA2011.iloc[22,9],tableA2011.iloc[22,10],tableA2011.iloc[22,11],tableA2011.iloc[22,12],tableA2011.iloc[22,13],tableA2011.iloc[22,14],tableA2011.iloc[22,15],tableA2011.iloc[22,16]], \
         ["Argentina","elc","2011",tableA2011.iloc[23,5],tableA2011.iloc[23,6],tableA2011.iloc[23,7],tableA2011.iloc[23,8],tableA2011.iloc[23,9],tableA2011.iloc[23,10],tableA2011.iloc[23,11],tableA2011.iloc[23,12],tableA2011.iloc[23,13],tableA2011.iloc[23,14],tableA2011.iloc[23,15],tableA2011.iloc[23,16]], \
         ["Argentina","ind","2011",tableA2011.iloc[24,5],tableA2011.iloc[24,6],tableA2011.iloc[24,7],tableA2011.iloc[24,8],tableA2011.iloc[24,9],tableA2011.iloc[24,10],tableA2011.iloc[24,11],tableA2011.iloc[24,12],tableA2011.iloc[24,13],tableA2011.iloc[24,14],tableA2011.iloc[24,15],tableA2011.iloc[24,16]]]                     

dfA2011 = pd.DataFrame(A2011,columns=["country","sector","year","1","2","3","4","5","6","7","8","9","10","11","12"]) 


# 2012 
tables = camelot.read_pdf("C:\\RBAC\\Data\\South America\\Raw Files\\Argentina\\Boletim_Gas_Natural_nr_73_abr_13.pdf", pages = '18')
# transfer Table lists to DataFrame
tableA2012 = tables[1].df

A2012 = [["Argentina","res","2012",tableA2012.iloc[1,7],tableA2012.iloc[1,8],tableA2012.iloc[1,9],tableA2012.iloc[1,10],tableA2012.iloc[1,11],tableA2012.iloc[1,12],tableA2012.iloc[1,13],tableA2012.iloc[1,14],tableA2012.iloc[1,15],tableA2012.iloc[1,16],tableA2012.iloc[1,17],tableA2012.iloc[1,18]], \
         ["Argentina","com","2012",tableA2012.iloc[2,7],tableA2012.iloc[2,8],tableA2012.iloc[2,9],tableA2012.iloc[2,10],tableA2012.iloc[2,11],tableA2012.iloc[2,12],tableA2012.iloc[2,13],tableA2012.iloc[2,14],tableA2012.iloc[2,15],tableA2012.iloc[2,16],tableA2012.iloc[2,17],tableA2012.iloc[2,18]], \
         ["Argentina","trn","2012",tableA2012.iloc[3,7],tableA2012.iloc[3,8],tableA2012.iloc[3,9],tableA2012.iloc[3,10],tableA2012.iloc[3,11],tableA2012.iloc[3,12],tableA2012.iloc[3,13],tableA2012.iloc[3,14],tableA2012.iloc[3,15],tableA2012.iloc[3,16],tableA2012.iloc[3,17],tableA2012.iloc[3,18]], \
         ["Argentina","elc","2012",tableA2012.iloc[4,7],tableA2012.iloc[4,8],tableA2012.iloc[4,9],tableA2012.iloc[4,10],tableA2012.iloc[4,11],tableA2012.iloc[4,12],tableA2012.iloc[4,13],tableA2012.iloc[4,14],tableA2012.iloc[4,15],tableA2012.iloc[4,16],tableA2012.iloc[4,17],tableA2012.iloc[4,18]], \
         ["Argentina","ind","2012",tableA2012.iloc[5,7],tableA2012.iloc[5,8],tableA2012.iloc[5,9],tableA2012.iloc[5,10],tableA2012.iloc[5,11],tableA2012.iloc[5,12],tableA2012.iloc[5,13],tableA2012.iloc[5,14],tableA2012.iloc[5,15],tableA2012.iloc[5,16],tableA2012.iloc[5,17],tableA2012.iloc[5,18]]] 
 
dfA2012 = pd.DataFrame(A2012,columns=["country","sector","year","1","2","3","4","5","6","7","8","9","10","11","12"]) 

  
# 2013 
tables = camelot.read_pdf("C:\\RBAC\\Data\\South America\\Raw Files\\Argentina\\Boletim Mensal de Acompanhamento da Indústria de Gás Natural n 86 - maio 2014.pdf", pages = '19')
# transfer Table lists to DataFrame
tableA2013 = tables[0].df

A2013 = [["Argentina","res","2013",tableA2013.iloc[21,7],tableA2013.iloc[21,8],tableA2013.iloc[21,9],tableA2013.iloc[21,10],tableA2013.iloc[21,11],tableA2013.iloc[21,12],tableA2013.iloc[21,13],tableA2013.iloc[21,14],tableA2013.iloc[21,15],tableA2013.iloc[21,16],tableA2013.iloc[21,17],tableA2013.iloc[21,18]], \
         ["Argentina","com","2013",tableA2013.iloc[22,7],tableA2013.iloc[22,8],tableA2013.iloc[22,9],tableA2013.iloc[22,10],tableA2013.iloc[22,11],tableA2013.iloc[22,12],tableA2013.iloc[22,13],tableA2013.iloc[22,14],tableA2013.iloc[22,15],tableA2013.iloc[22,16],tableA2013.iloc[22,17],tableA2013.iloc[22,18]], \
         ["Argentina","trn","2013",tableA2013.iloc[23,7],tableA2013.iloc[23,8],tableA2013.iloc[23,9],tableA2013.iloc[23,10],tableA2013.iloc[23,11],tableA2013.iloc[23,12],tableA2013.iloc[23,13],tableA2013.iloc[23,14],tableA2013.iloc[23,15],tableA2013.iloc[23,16],tableA2013.iloc[23,17],tableA2013.iloc[23,18]], \
         ["Argentina","elc","2013",tableA2013.iloc[24,7],tableA2013.iloc[24,8],tableA2013.iloc[24,9],tableA2013.iloc[24,10],tableA2013.iloc[24,11],tableA2013.iloc[24,12],tableA2013.iloc[24,13],tableA2013.iloc[24,14],tableA2013.iloc[24,15],tableA2013.iloc[24,16],tableA2013.iloc[24,17],tableA2013.iloc[24,18]], \
         ["Argentina","ind","2013",tableA2013.iloc[25,7],tableA2013.iloc[25,8],tableA2013.iloc[25,9],tableA2013.iloc[25,10],tableA2013.iloc[25,11],tableA2013.iloc[25,12],tableA2013.iloc[25,13],tableA2013.iloc[25,14],tableA2013.iloc[25,15],tableA2013.iloc[25,16],tableA2013.iloc[25,17],tableA2013.iloc[25,18]]] 
 
dfA2013 = pd.DataFrame(A2013,columns=["country","sector","year","1","2","3","4","5","6","7","8","9","10","11","12"]) 


# 2014 
tables = camelot.read_pdf("C:\\RBAC\\Data\\South America\\Raw Files\\Argentina\\Boletim_Gas_Natural_nr_96_mar_15.pdf", pages = '19')
# transfer Table lists to DataFrame
tableA2014 = tables[1].df

A2014 = [["Argentina","res","2014",tableA2014.iloc[1,6],tableA2014.iloc[1,7],tableA2014.iloc[1,8],tableA2014.iloc[1,9],tableA2014.iloc[1,10],tableA2014.iloc[1,11],tableA2014.iloc[1,12],tableA2014.iloc[1,13],tableA2014.iloc[1,14],tableA2014.iloc[1,15],tableA2014.iloc[1,16],tableA2014.iloc[1,17]], \
         ["Argentina","com","2014",tableA2014.iloc[2,6],tableA2014.iloc[2,7],tableA2014.iloc[2,8],tableA2014.iloc[2,9],tableA2014.iloc[2,10],tableA2014.iloc[2,11],tableA2014.iloc[2,12],tableA2014.iloc[2,13],tableA2014.iloc[2,14],tableA2014.iloc[2,15],tableA2014.iloc[2,16],tableA2014.iloc[2,17]], \
         ["Argentina","trn","2014",tableA2014.iloc[3,6],tableA2014.iloc[3,7],tableA2014.iloc[3,8],tableA2014.iloc[3,9],tableA2014.iloc[3,10],tableA2014.iloc[3,11],tableA2014.iloc[3,12],tableA2014.iloc[3,13],tableA2014.iloc[3,14],tableA2014.iloc[3,15],tableA2014.iloc[3,16],tableA2014.iloc[3,17]], \
         ["Argentina","elc","2014",tableA2014.iloc[4,6],tableA2014.iloc[4,7],tableA2014.iloc[4,8],tableA2014.iloc[4,9],tableA2014.iloc[4,10],tableA2014.iloc[4,11],tableA2014.iloc[4,12],tableA2014.iloc[4,13],tableA2014.iloc[4,14],tableA2014.iloc[4,15],tableA2014.iloc[4,16],tableA2014.iloc[4,17]], \
         ["Argentina","ind","2014",tableA2014.iloc[5,6],tableA2014.iloc[5,7],tableA2014.iloc[5,8],tableA2014.iloc[5,9],tableA2014.iloc[5,10],tableA2014.iloc[5,11],tableA2014.iloc[5,12],tableA2014.iloc[5,13],tableA2014.iloc[5,14],tableA2014.iloc[5,15],tableA2014.iloc[5,16],tableA2014.iloc[5,17]]] 
  

dfA2014 = pd.DataFrame(A2014,columns=["country","sector","year","1","2","3","4","5","6","7","8","9","10","11","12"]) 
 
### lack Feb 2015 to Dec 2016, till report in Jan in 2017, the demand is 0. Page 18
### Jodi lacks data after Oct 2017


# 2017 
tables = camelot.read_pdf("C:\\RBAC\\Data\\South America\\Raw Files\\Argentina\\Boletim_Gas_Natural_nr_131_JAN_18.rev.pdf", pages = '30')
# transfer Table lists to DataFrame
tableA2017 = tables[0].df

A2017 = [["Argentina","res","2017",tableA2017.iloc[26,5],tableA2017.iloc[26,6],tableA2017.iloc[26,7],tableA2017.iloc[26,8],tableA2017.iloc[26,9],tableA2017.iloc[26,10],tableA2017.iloc[26,11],tableA2017.iloc[26,12],tableA2017.iloc[26,13],tableA2017.iloc[26,14],tableA2017.iloc[26,15],tableA2017.iloc[26,16]], \
         ["Argentina","com","2017",tableA2017.iloc[27,5],tableA2017.iloc[27,6],tableA2017.iloc[27,7],tableA2017.iloc[27,8],tableA2017.iloc[27,9],tableA2017.iloc[27,10],tableA2017.iloc[27,11],tableA2017.iloc[27,12],tableA2017.iloc[27,13],tableA2017.iloc[27,14],tableA2017.iloc[27,15],tableA2017.iloc[27,16]], \
         ["Argentina","trn","2017",tableA2017.iloc[28,5],tableA2017.iloc[28,6],tableA2017.iloc[28,7],tableA2017.iloc[28,8],tableA2017.iloc[28,9],tableA2017.iloc[28,10],tableA2017.iloc[28,11],tableA2017.iloc[28,12],tableA2017.iloc[28,13],tableA2017.iloc[28,14],tableA2017.iloc[28,15],tableA2017.iloc[28,16]], \
         ["Argentina","elc","2017",tableA2017.iloc[29,5],tableA2017.iloc[29,6],tableA2017.iloc[29,7],tableA2017.iloc[29,8],tableA2017.iloc[29,9],tableA2017.iloc[29,10],tableA2017.iloc[29,11],tableA2017.iloc[29,12],tableA2017.iloc[29,13],tableA2017.iloc[29,14],tableA2017.iloc[29,15],tableA2017.iloc[29,16]], \
         ["Argentina","ind","2017",tableA2017.iloc[30,5],tableA2017.iloc[30,6],tableA2017.iloc[30,7],tableA2017.iloc[30,8],tableA2017.iloc[30,9],tableA2017.iloc[30,10],tableA2017.iloc[30,11],tableA2017.iloc[30,12],tableA2017.iloc[30,13],tableA2017.iloc[30,14],tableA2017.iloc[30,15],tableA2017.iloc[30,16]]]     

dfA2017 = pd.DataFrame(A2017,columns=["country","sector","year","1","2","3","4","5","6","7","8","9","10","11","12"]) 
  

# 2018 
tables = camelot.read_pdf("C:\\RBAC\\Data\\South America\\Raw Files\\Argentina\\02 - Boletim Mensal de Acompanhamento da Indústria de Gás Natural Fevereiro 2019.pdf", pages = '30')
# transfer Table lists to DataFrame
tableA2018 = tables[0].df

A2018 = [["Argentina","res","2018",tableA2018.iloc[27,4],tableA2018.iloc[27,5],tableA2018.iloc[27,6],tableA2018.iloc[27,7],tableA2018.iloc[27,8],tableA2018.iloc[27,9],tableA2018.iloc[27,10],tableA2018.iloc[27,11],tableA2018.iloc[27,12],tableA2018.iloc[27,13],tableA2018.iloc[27,14],tableA2018.iloc[27,15]], \
         ["Argentina","com","2018",tableA2018.iloc[28,4],tableA2018.iloc[28,5],tableA2018.iloc[28,6],tableA2018.iloc[28,7],tableA2018.iloc[28,8],tableA2018.iloc[28,9],tableA2018.iloc[28,10],tableA2018.iloc[28,11],tableA2018.iloc[28,12],tableA2018.iloc[28,13],tableA2018.iloc[28,14],tableA2018.iloc[28,15]], \
         ["Argentina","trn","2018",tableA2018.iloc[29,4],tableA2018.iloc[29,5],tableA2018.iloc[29,6],tableA2018.iloc[29,7],tableA2018.iloc[29,8],tableA2018.iloc[29,9],tableA2018.iloc[29,10],tableA2018.iloc[29,11],tableA2018.iloc[29,12],tableA2018.iloc[29,13],tableA2018.iloc[29,14],tableA2018.iloc[29,15]], \
         ["Argentina","elc","2018",tableA2018.iloc[30,4],tableA2018.iloc[30,5],tableA2018.iloc[30,6],tableA2018.iloc[30,7],tableA2018.iloc[30,8],tableA2018.iloc[30,9],tableA2018.iloc[30,10],tableA2018.iloc[30,11],tableA2018.iloc[30,12],tableA2018.iloc[30,13],tableA2018.iloc[30,14],tableA2018.iloc[30,15]], \
         ["Argentina","ind","2018",tableA2018.iloc[31,4],tableA2018.iloc[31,5],tableA2018.iloc[31,6],tableA2018.iloc[31,7],tableA2018.iloc[31,8],tableA2018.iloc[31,9],tableA2018.iloc[31,10],tableA2018.iloc[31,11],tableA2018.iloc[31,12],tableA2018.iloc[31,13],tableA2018.iloc[31,14],tableA2018.iloc[31,15]]]                      

dfA2018 = pd.DataFrame(A2018,columns=["country","sector","year","1","2","3","4","5","6","7","8","9","10","11","12"]) 
   

# 2019 
# lacking Dec 2019 since in report in Dec 2019, there is no data in Dec 2019; while in Jan 2020, it jumped Dec 2019, showing Jan 2020 directly.
# Suggest to use the average Nov 2019 and Jan 2020 when editing in Excel working file

tables = camelot.read_pdf("C:\\RBAC\\Data\\South America\\Raw Files\\Argentina\\12 - Boletim Mensal de Acompanhamento da Indústria de Gás Natural Dezembro 2019.pdf", pages = '30')
# transfer Table lists to DataFrame
tableA2019 = tables[0].df

A2019 = [["Argentina","res","2019",tableA2019.iloc[27,5],tableA2019.iloc[27,6],tableA2019.iloc[27,7],tableA2019.iloc[27,8],tableA2019.iloc[27,9],tableA2019.iloc[27,10],tableA2019.iloc[27,11],tableA2019.iloc[27,12],tableA2019.iloc[27,13],tableA2019.iloc[27,14],tableA2019.iloc[27,15],tableA2019.iloc[27,16]], \
         ["Argentina","com","2019",tableA2019.iloc[28,5],tableA2019.iloc[28,6],tableA2019.iloc[28,7],tableA2019.iloc[28,8],tableA2019.iloc[28,9],tableA2019.iloc[28,10],tableA2019.iloc[28,11],tableA2019.iloc[28,12],tableA2019.iloc[28,13],tableA2019.iloc[28,14],tableA2019.iloc[28,15],tableA2019.iloc[28,16]], \
         ["Argentina","trn","2019",tableA2019.iloc[29,5],tableA2019.iloc[29,6],tableA2019.iloc[29,7],tableA2019.iloc[29,8],tableA2019.iloc[29,9],tableA2019.iloc[29,10],tableA2019.iloc[29,11],tableA2019.iloc[29,12],tableA2019.iloc[29,13],tableA2019.iloc[29,14],tableA2019.iloc[29,15],tableA2019.iloc[29,16]], \
         ["Argentina","elc","2019",tableA2019.iloc[30,5],tableA2019.iloc[30,6],tableA2019.iloc[30,7],tableA2019.iloc[30,8],tableA2019.iloc[30,9],tableA2019.iloc[30,10],tableA2019.iloc[30,11],tableA2019.iloc[30,12],tableA2019.iloc[30,13],tableA2019.iloc[30,14],tableA2019.iloc[30,15],tableA2019.iloc[30,16]], \
         ["Argentina","ind","2019",tableA2019.iloc[31,5],tableA2019.iloc[31,6],tableA2019.iloc[31,7],tableA2019.iloc[31,8],tableA2019.iloc[31,9],tableA2019.iloc[31,10],tableA2019.iloc[31,11],tableA2019.iloc[31,12],tableA2019.iloc[31,13],tableA2019.iloc[31,14],tableA2019.iloc[31,15],tableA2019.iloc[31,16]]]                      

dfA2019 = pd.DataFrame(A2019,columns=["country","sector","year","1","2","3","4","5","6","7","8","9","10","11","12"]) 
   
# 2020 
tables = camelot.read_pdf("C:\\RBAC\\Data\\South America\\Raw Files\\Argentina\\07. Boletim Mensal de Acompanhamento da Indústria de Gás Natural - Julho 2020.pdf", pages = '30')
# transfer Table lists to DataFrame
tableA2020 = tables[0].df

A2020 = [["Argentina","res","2020",tableA2020.iloc[27,5],tableA2020.iloc[27,6],tableA2020.iloc[27,7],tableA2020.iloc[27,8],tableA2020.iloc[27,9],tableA2020.iloc[27,10],tableA2020.iloc[27,11],tableA2020.iloc[27,12],tableA2020.iloc[27,13],tableA2020.iloc[27,14],tableA2020.iloc[27,15],tableA2020.iloc[27,16]], \
         ["Argentina","com","2020",tableA2020.iloc[28,5],tableA2020.iloc[28,6],tableA2020.iloc[28,7],tableA2020.iloc[28,8],tableA2020.iloc[28,9],tableA2020.iloc[28,10],tableA2020.iloc[28,11],tableA2020.iloc[28,12],tableA2020.iloc[28,13],tableA2020.iloc[28,14],tableA2020.iloc[28,15],tableA2020.iloc[28,16]], \
         ["Argentina","trn","2020",tableA2020.iloc[29,5],tableA2020.iloc[29,6],tableA2020.iloc[29,7],tableA2020.iloc[29,8],tableA2020.iloc[29,9],tableA2020.iloc[29,10],tableA2020.iloc[29,11],tableA2020.iloc[29,12],tableA2020.iloc[29,13],tableA2020.iloc[29,14],tableA2020.iloc[29,15],tableA2020.iloc[29,16]], \
         ["Argentina","elc","2020",tableA2020.iloc[30,5],tableA2020.iloc[30,6],tableA2020.iloc[30,7],tableA2020.iloc[30,8],tableA2020.iloc[30,9],tableA2020.iloc[30,10],tableA2020.iloc[30,11],tableA2020.iloc[30,12],tableA2020.iloc[30,13],tableA2020.iloc[30,14],tableA2020.iloc[30,15],tableA2020.iloc[30,16]], \
         ["Argentina","ind","2020",tableA2020.iloc[31,5],tableA2020.iloc[31,6],tableA2020.iloc[31,7],tableA2020.iloc[31,8],tableA2020.iloc[31,9],tableA2020.iloc[31,10],tableA2020.iloc[31,11],tableA2020.iloc[31,12],tableA2020.iloc[31,13],tableA2020.iloc[31,14],tableA2020.iloc[31,15],tableA2020.iloc[31,16]]]                      

dfA2020 = pd.DataFrame(A2020,columns=["country","sector","year","1","2","3","4","5","6","7","8","9","10","11","12"]) 
    
##########

South1 = [dfB2010, dfB2011, dfB2012, dfB2013, dfB2014, dfB2015, dfB2016, dfB2017, dfB2018, dfB2019, dfB2020, \
          dfA2010, dfA2011, dfA2012, dfA2013, dfA2014, dfA2017, dfA2018, dfA2019, dfA2020]

South2 = pd.concat(South1,ignore_index=True)


# export dataframe to .csv
South2.to_csv('C:\\RBAC\\Data\\South America\\Convert\\SouthCSV.csv',index=None)

endtime = datetime.datetime.now()
print (endtime - starttime)

print("Congradutions! Finished :)")

