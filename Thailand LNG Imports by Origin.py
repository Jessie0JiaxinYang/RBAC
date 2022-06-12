# 2022 0610 Thailand LNG Import by Origin
# https://www.customs.go.th/index.php?lang=en&left_menu=menu_homepage
# Difficulty: download historical one by one

import pandas as pd 
import numpy as np
from pandas import DataFrame
import datetime

import pandas

import statsmodels.api as sm
import matplotlib.pyplot as plt

starttime = datetime.datetime.now()

##2022
# 2022 01
Jan22 = pandas.read_csv(r'C:\Users\jiaxi\OneDrive\Desktop\RBAC 2022\Local\Thailand\Raw\2022 01.csv')
Jan22.columns = ['CountryID','Country', 'Quantity(KGM)', 'Value(Baht)', 'Cumulative Quantity(KGM)', 'Cumulative Value(Baht)']
Jan22.insert(Jan22.shape[1], "Date", "2022/01/01")

# 2022 02
Feb22 = pandas.read_csv(r'C:\Users\jiaxi\OneDrive\Desktop\RBAC 2022\Local\Thailand\Raw\2022 02.csv')
Feb22.columns = ['CountryID','Country', 'Quantity(KGM)', 'Value(Baht)', 'Cumulative Quantity(KGM)', 'Cumulative Value(Baht)']
Feb22.insert(Feb22.shape[1], "Date", "2022/02/01")

# 2022 03
Mar22 = pandas.read_csv(r'C:\Users\jiaxi\OneDrive\Desktop\RBAC 2022\Local\Thailand\Raw\2022 03.csv')
Mar22.columns = ['CountryID','Country', 'Quantity(KGM)', 'Value(Baht)', 'Cumulative Quantity(KGM)', 'Cumulative Value(Baht)']
Mar22.insert(Mar22.shape[1], "Date", "2022/03/01")

# 2022 04
Apr22 = pandas.read_csv(r'C:\Users\jiaxi\OneDrive\Desktop\RBAC 2022\Local\Thailand\Raw\2022 04.csv')
Apr22.columns = ['CountryID','Country', 'Quantity(KGM)', 'Value(Baht)', 'Cumulative Quantity(KGM)', 'Cumulative Value(Baht)']
Apr22.insert(Apr22.shape[1], "Date", "2022/04/01")

##2021
# 2021 01
Jan21 = pandas.read_csv(r'C:\Users\jiaxi\OneDrive\Desktop\RBAC 2022\Local\Thailand\Raw\2021 01.csv')
Jan21.columns = ['CountryID','Country', 'Quantity(KGM)', 'Value(Baht)', 'Cumulative Quantity(KGM)', 'Cumulative Value(Baht)']
Jan21.insert(Jan21.shape[1], "Date", "2021/01/01")

# 2021 02
Feb21 = pandas.read_csv(r'C:\Users\jiaxi\OneDrive\Desktop\RBAC 2022\Local\Thailand\Raw\2021 02.csv')
Feb21.columns = ['CountryID','Country', 'Quantity(KGM)', 'Value(Baht)', 'Cumulative Quantity(KGM)', 'Cumulative Value(Baht)']
Feb21.insert(Feb21.shape[1], "Date", "2021/02/01")

# 2021 03
Mar21 = pandas.read_csv(r'C:\Users\jiaxi\OneDrive\Desktop\RBAC 2022\Local\Thailand\Raw\2021 03.csv')
Mar21.columns = ['CountryID','Country', 'Quantity(KGM)', 'Value(Baht)', 'Cumulative Quantity(KGM)', 'Cumulative Value(Baht)']
Mar21.insert(Mar21.shape[1], "Date", "2021/03/01")

# 2021 04
Apr21 = pandas.read_csv(r'C:\Users\jiaxi\OneDrive\Desktop\RBAC 2022\Local\Thailand\Raw\2021 04.csv')
Apr21.columns = ['CountryID','Country', 'Quantity(KGM)', 'Value(Baht)', 'Cumulative Quantity(KGM)', 'Cumulative Value(Baht)']
Apr21.insert(Apr21.shape[1], "Date", "2021/04/01")

# 2021 05
May21 = pandas.read_csv(r'C:\Users\jiaxi\OneDrive\Desktop\RBAC 2022\Local\Thailand\Raw\2021 05.csv')
May21.columns = ['CountryID','Country', 'Quantity(KGM)', 'Value(Baht)', 'Cumulative Quantity(KGM)', 'Cumulative Value(Baht)']
May21.insert(May21.shape[1], "Date", "2021/05/01")

# 2021 06
Jun21 = pandas.read_csv(r'C:\Users\jiaxi\OneDrive\Desktop\RBAC 2022\Local\Thailand\Raw\2021 06.csv')
Jun21.columns = ['CountryID','Country', 'Quantity(KGM)', 'Value(Baht)', 'Cumulative Quantity(KGM)', 'Cumulative Value(Baht)']
Jun21.insert(Jun21.shape[1], "Date", "2021/06/01")

# 2021 07
Jul21 = pandas.read_csv(r'C:\Users\jiaxi\OneDrive\Desktop\RBAC 2022\Local\Thailand\Raw\2021 07.csv')
Jul21.columns = ['CountryID','Country', 'Quantity(KGM)', 'Value(Baht)', 'Cumulative Quantity(KGM)', 'Cumulative Value(Baht)']
Jul21.insert(Jul21.shape[1], "Date", "2021/07/01")

# 2021 08
Aug21 = pandas.read_csv(r'C:\Users\jiaxi\OneDrive\Desktop\RBAC 2022\Local\Thailand\Raw\2021 08.csv')
Aug21.columns = ['CountryID','Country', 'Quantity(KGM)', 'Value(Baht)', 'Cumulative Quantity(KGM)', 'Cumulative Value(Baht)']
Aug21.insert(Aug21.shape[1], "Date", "2021/08/01")

# 2021 09
Sep21 = pandas.read_csv(r'C:\Users\jiaxi\OneDrive\Desktop\RBAC 2022\Local\Thailand\Raw\2021 09.csv')
Sep21.columns = ['CountryID','Country', 'Quantity(KGM)', 'Value(Baht)', 'Cumulative Quantity(KGM)', 'Cumulative Value(Baht)']
Sep21.insert(Sep21.shape[1], "Date", "2021/09/01")

# 2021 10
Oct21 = pandas.read_csv(r'C:\Users\jiaxi\OneDrive\Desktop\RBAC 2022\Local\Thailand\Raw\2021 10.csv')
Oct21.columns = ['CountryID','Country', 'Quantity(KGM)', 'Value(Baht)', 'Cumulative Quantity(KGM)', 'Cumulative Value(Baht)']
Oct21.insert(Oct21.shape[1], "Date", "2021/10/01")

# 2021 11
Nov21 = pandas.read_csv(r'C:\Users\jiaxi\OneDrive\Desktop\RBAC 2022\Local\Thailand\Raw\2021 11.csv')
Nov21.columns = ['CountryID','Country', 'Quantity(KGM)', 'Value(Baht)', 'Cumulative Quantity(KGM)', 'Cumulative Value(Baht)']
Nov21.insert(Nov21.shape[1], "Date", "2021/11/01")

# 2021 12
Dec21 = pandas.read_csv(r'C:\Users\jiaxi\OneDrive\Desktop\RBAC 2022\Local\Thailand\Raw\2021 12.csv')
Dec21.columns = ['CountryID','Country', 'Quantity(KGM)', 'Value(Baht)', 'Cumulative Quantity(KGM)', 'Cumulative Value(Baht)']
Dec21.insert(Dec21.shape[1], "Date", "2021/12/01")

##2020
# 2020 01
Jan20 = pandas.read_csv(r'C:\Users\jiaxi\OneDrive\Desktop\RBAC 2022\Local\Thailand\Raw\2020 01.csv')
Jan20.columns = ['CountryID','Country', 'Quantity(KGM)', 'Value(Baht)', 'Cumulative Quantity(KGM)', 'Cumulative Value(Baht)']
Jan20.insert(Jan20.shape[1], "Date", "2020/01/01")

# 2020 02
Feb20 = pandas.read_csv(r'C:\Users\jiaxi\OneDrive\Desktop\RBAC 2022\Local\Thailand\Raw\2020 02.csv')
Feb20.columns = ['CountryID','Country', 'Quantity(KGM)', 'Value(Baht)', 'Cumulative Quantity(KGM)', 'Cumulative Value(Baht)']
Feb20.insert(Feb20.shape[1], "Date", "2020/02/01")

# 2020 03
Mar20 = pandas.read_csv(r'C:\Users\jiaxi\OneDrive\Desktop\RBAC 2022\Local\Thailand\Raw\2020 03.csv')
Mar20.columns = ['CountryID','Country', 'Quantity(KGM)', 'Value(Baht)', 'Cumulative Quantity(KGM)', 'Cumulative Value(Baht)']
Mar20.insert(Mar20.shape[1], "Date", "2020/03/01")

# 2020 04
Apr20 = pandas.read_csv(r'C:\Users\jiaxi\OneDrive\Desktop\RBAC 2022\Local\Thailand\Raw\2020 04.csv')
Apr20.columns = ['CountryID','Country', 'Quantity(KGM)', 'Value(Baht)', 'Cumulative Quantity(KGM)', 'Cumulative Value(Baht)']
Apr20.insert(Apr20.shape[1], "Date", "2020/04/01")

# 2020 05
May20 = pandas.read_csv(r'C:\Users\jiaxi\OneDrive\Desktop\RBAC 2022\Local\Thailand\Raw\2020 05.csv')
May20.columns = ['CountryID','Country', 'Quantity(KGM)', 'Value(Baht)', 'Cumulative Quantity(KGM)', 'Cumulative Value(Baht)']
May20.insert(May20.shape[1], "Date", "2020/05/01")

# 2020 06
Jun20 = pandas.read_csv(r'C:\Users\jiaxi\OneDrive\Desktop\RBAC 2022\Local\Thailand\Raw\2020 06.csv')
Jun20.columns = ['CountryID','Country', 'Quantity(KGM)', 'Value(Baht)', 'Cumulative Quantity(KGM)', 'Cumulative Value(Baht)']
Jun20.insert(Jun20.shape[1], "Date", "2020/06/01")

# 2020 07
Jul20 = pandas.read_csv(r'C:\Users\jiaxi\OneDrive\Desktop\RBAC 2022\Local\Thailand\Raw\2020 07.csv')
Jul20.columns = ['CountryID','Country', 'Quantity(KGM)', 'Value(Baht)', 'Cumulative Quantity(KGM)', 'Cumulative Value(Baht)']
Jul20.insert(Jul20.shape[1], "Date", "2020/07/01")

# 2020 08
Aug20 = pandas.read_csv(r'C:\Users\jiaxi\OneDrive\Desktop\RBAC 2022\Local\Thailand\Raw\2020 08.csv')
Aug20.columns = ['CountryID','Country', 'Quantity(KGM)', 'Value(Baht)', 'Cumulative Quantity(KGM)', 'Cumulative Value(Baht)']
Aug20.insert(Aug20.shape[1], "Date", "2020/08/01")

# 2020 09
Sep20 = pandas.read_csv(r'C:\Users\jiaxi\OneDrive\Desktop\RBAC 2022\Local\Thailand\Raw\2020 09.csv')
Sep20.columns = ['CountryID','Country', 'Quantity(KGM)', 'Value(Baht)', 'Cumulative Quantity(KGM)', 'Cumulative Value(Baht)']
Sep20.insert(Sep20.shape[1], "Date", "2020/09/01")

# 2020 10
Oct20 = pandas.read_csv(r'C:\Users\jiaxi\OneDrive\Desktop\RBAC 2022\Local\Thailand\Raw\2020 10.csv')
Oct20.columns = ['CountryID','Country', 'Quantity(KGM)', 'Value(Baht)', 'Cumulative Quantity(KGM)', 'Cumulative Value(Baht)']
Oct20.insert(Oct20.shape[1], "Date", "2020/10/01")

# 2020 11
Nov20 = pandas.read_csv(r'C:\Users\jiaxi\OneDrive\Desktop\RBAC 2022\Local\Thailand\Raw\2020 11.csv')
Nov20.columns = ['CountryID','Country', 'Quantity(KGM)', 'Value(Baht)', 'Cumulative Quantity(KGM)', 'Cumulative Value(Baht)']
Nov20.insert(Nov20.shape[1], "Date", "2020/11/01")

# 2020 12
Dec20 = pandas.read_csv(r'C:\Users\jiaxi\OneDrive\Desktop\RBAC 2022\Local\Thailand\Raw\2020 12.csv')
Dec20.columns = ['CountryID','Country', 'Quantity(KGM)', 'Value(Baht)', 'Cumulative Quantity(KGM)', 'Cumulative Value(Baht)']
Dec20.insert(Dec20.shape[1], "Date", "2020/12/01")

##2019
# 2019 01
Jan19 = pandas.read_csv(r'C:\Users\jiaxi\OneDrive\Desktop\RBAC 2022\Local\Thailand\Raw\2019 01.csv')
Jan19.columns = ['CountryID','Country', 'Quantity(KGM)', 'Value(Baht)', 'Cumulative Quantity(KGM)', 'Cumulative Value(Baht)']
Jan19.insert(Jan19.shape[1], "Date", "2019/01/01")

# 2019 02
Feb19 = pandas.read_csv(r'C:\Users\jiaxi\OneDrive\Desktop\RBAC 2022\Local\Thailand\Raw\2019 02.csv')
Feb19.columns = ['CountryID','Country', 'Quantity(KGM)', 'Value(Baht)', 'Cumulative Quantity(KGM)', 'Cumulative Value(Baht)']
Feb19.insert(Feb19.shape[1], "Date", "2019/02/01")

# 2019 03
Mar19 = pandas.read_csv(r'C:\Users\jiaxi\OneDrive\Desktop\RBAC 2022\Local\Thailand\Raw\2019 03.csv')
Mar19.columns = ['CountryID','Country', 'Quantity(KGM)', 'Value(Baht)', 'Cumulative Quantity(KGM)', 'Cumulative Value(Baht)']
Mar19.insert(Mar19.shape[1], "Date", "2019/03/01")

# 2019 04
Apr19 = pandas.read_csv(r'C:\Users\jiaxi\OneDrive\Desktop\RBAC 2022\Local\Thailand\Raw\2019 04.csv')
Apr19.columns = ['CountryID','Country', 'Quantity(KGM)', 'Value(Baht)', 'Cumulative Quantity(KGM)', 'Cumulative Value(Baht)']
Apr19.insert(Apr19.shape[1], "Date", "2019/04/01")

# 2019 05
May19 = pandas.read_csv(r'C:\Users\jiaxi\OneDrive\Desktop\RBAC 2022\Local\Thailand\Raw\2019 05.csv')
May19.columns = ['CountryID','Country', 'Quantity(KGM)', 'Value(Baht)', 'Cumulative Quantity(KGM)', 'Cumulative Value(Baht)']
May19.insert(May19.shape[1], "Date", "2019/05/01")

# 2019 06
Jun19 = pandas.read_csv(r'C:\Users\jiaxi\OneDrive\Desktop\RBAC 2022\Local\Thailand\Raw\2019 06.csv')
Jun19.columns = ['CountryID','Country', 'Quantity(KGM)', 'Value(Baht)', 'Cumulative Quantity(KGM)', 'Cumulative Value(Baht)']
Jun19.insert(Jun19.shape[1], "Date", "2019/06/01")

# 2019 07
Jul19 = pandas.read_csv(r'C:\Users\jiaxi\OneDrive\Desktop\RBAC 2022\Local\Thailand\Raw\2019 07.csv')
Jul19.columns = ['CountryID','Country', 'Quantity(KGM)', 'Value(Baht)', 'Cumulative Quantity(KGM)', 'Cumulative Value(Baht)']
Jul19.insert(Jul19.shape[1], "Date", "2019/07/01")

# 2019 08
Aug19 = pandas.read_csv(r'C:\Users\jiaxi\OneDrive\Desktop\RBAC 2022\Local\Thailand\Raw\2019 08.csv')
Aug19.columns = ['CountryID','Country', 'Quantity(KGM)', 'Value(Baht)', 'Cumulative Quantity(KGM)', 'Cumulative Value(Baht)']
Aug19.insert(Aug19.shape[1], "Date", "2019/08/01")

# 2019 09
Sep19 = pandas.read_csv(r'C:\Users\jiaxi\OneDrive\Desktop\RBAC 2022\Local\Thailand\Raw\2019 09.csv')
Sep19.columns = ['CountryID','Country', 'Quantity(KGM)', 'Value(Baht)', 'Cumulative Quantity(KGM)', 'Cumulative Value(Baht)']
Sep19.insert(Sep19.shape[1], "Date", "2019/09/01")

# 2019 10
Oct19 = pandas.read_csv(r'C:\Users\jiaxi\OneDrive\Desktop\RBAC 2022\Local\Thailand\Raw\2019 10.csv')
Oct19.columns = ['CountryID','Country', 'Quantity(KGM)', 'Value(Baht)', 'Cumulative Quantity(KGM)', 'Cumulative Value(Baht)']
Oct19.insert(Oct19.shape[1], "Date", "2019/10/01")

# 2019 11
Nov19 = pandas.read_csv(r'C:\Users\jiaxi\OneDrive\Desktop\RBAC 2022\Local\Thailand\Raw\2019 11.csv')
Nov19.columns = ['CountryID','Country', 'Quantity(KGM)', 'Value(Baht)', 'Cumulative Quantity(KGM)', 'Cumulative Value(Baht)']
Nov19.insert(Nov19.shape[1], "Date", "2019/11/01")

# 2019 12
Dec19 = pandas.read_csv(r'C:\Users\jiaxi\OneDrive\Desktop\RBAC 2022\Local\Thailand\Raw\2019 12.csv')
Dec19.columns = ['CountryID','Country', 'Quantity(KGM)', 'Value(Baht)', 'Cumulative Quantity(KGM)', 'Cumulative Value(Baht)']
Dec19.insert(Dec19.shape[1], "Date", "2019/12/01")


##2018
# 2018 01
Jan18 = pandas.read_csv(r'C:\Users\jiaxi\OneDrive\Desktop\RBAC 2022\Local\Thailand\Raw\2018 01.csv')
Jan18.columns = ['CountryID','Country', 'Quantity(KGM)', 'Value(Baht)', 'Cumulative Quantity(KGM)', 'Cumulative Value(Baht)']
Jan18.insert(Jan18.shape[1], "Date", "2018/01/01")

# 2018 02
Feb18 = pandas.read_csv(r'C:\Users\jiaxi\OneDrive\Desktop\RBAC 2022\Local\Thailand\Raw\2018 02.csv')
Feb18.columns = ['CountryID','Country', 'Quantity(KGM)', 'Value(Baht)', 'Cumulative Quantity(KGM)', 'Cumulative Value(Baht)']
Feb18.insert(Feb18.shape[1], "Date", "2018/02/01")

# 2018 03
Mar18 = pandas.read_csv(r'C:\Users\jiaxi\OneDrive\Desktop\RBAC 2022\Local\Thailand\Raw\2018 03.csv')
Mar18.columns = ['CountryID','Country', 'Quantity(KGM)', 'Value(Baht)', 'Cumulative Quantity(KGM)', 'Cumulative Value(Baht)']
Mar18.insert(Mar18.shape[1], "Date", "2018/03/01")

# 2018 04
Apr18 = pandas.read_csv(r'C:\Users\jiaxi\OneDrive\Desktop\RBAC 2022\Local\Thailand\Raw\2018 04.csv')
Apr18.columns = ['CountryID','Country', 'Quantity(KGM)', 'Value(Baht)', 'Cumulative Quantity(KGM)', 'Cumulative Value(Baht)']
Apr18.insert(Apr18.shape[1], "Date", "2018/04/01")

# 2018 05
May18 = pandas.read_csv(r'C:\Users\jiaxi\OneDrive\Desktop\RBAC 2022\Local\Thailand\Raw\2018 05.csv')
May18.columns = ['CountryID','Country', 'Quantity(KGM)', 'Value(Baht)', 'Cumulative Quantity(KGM)', 'Cumulative Value(Baht)']
May18.insert(May18.shape[1], "Date", "2018/05/01")

# 2018 06
Jun18 = pandas.read_csv(r'C:\Users\jiaxi\OneDrive\Desktop\RBAC 2022\Local\Thailand\Raw\2018 06.csv')
Jun18.columns = ['CountryID','Country', 'Quantity(KGM)', 'Value(Baht)', 'Cumulative Quantity(KGM)', 'Cumulative Value(Baht)']
Jun18.insert(Jun18.shape[1], "Date", "2018/06/01")

# 2018 07
Jul18 = pandas.read_csv(r'C:\Users\jiaxi\OneDrive\Desktop\RBAC 2022\Local\Thailand\Raw\2018 07.csv')
Jul18.columns = ['CountryID','Country', 'Quantity(KGM)', 'Value(Baht)', 'Cumulative Quantity(KGM)', 'Cumulative Value(Baht)']
Jul18.insert(Jul18.shape[1], "Date", "2018/07/01")

# 2018 08
Aug18 = pandas.read_csv(r'C:\Users\jiaxi\OneDrive\Desktop\RBAC 2022\Local\Thailand\Raw\2018 08.csv')
Aug18.columns = ['CountryID','Country', 'Quantity(KGM)', 'Value(Baht)', 'Cumulative Quantity(KGM)', 'Cumulative Value(Baht)']
Aug18.insert(Aug18.shape[1], "Date", "2018/08/01")

# 2018 09
Sep18 = pandas.read_csv(r'C:\Users\jiaxi\OneDrive\Desktop\RBAC 2022\Local\Thailand\Raw\2018 09.csv')
Sep18.columns = ['CountryID','Country', 'Quantity(KGM)', 'Value(Baht)', 'Cumulative Quantity(KGM)', 'Cumulative Value(Baht)']
Sep18.insert(Sep18.shape[1], "Date", "2018/09/01")

# 2018 10
Oct18 = pandas.read_csv(r'C:\Users\jiaxi\OneDrive\Desktop\RBAC 2022\Local\Thailand\Raw\2018 10.csv')
Oct18.columns = ['CountryID','Country', 'Quantity(KGM)', 'Value(Baht)', 'Cumulative Quantity(KGM)', 'Cumulative Value(Baht)']
Oct18.insert(Oct18.shape[1], "Date", "2018/10/01")

# 2018 11
Nov18 = pandas.read_csv(r'C:\Users\jiaxi\OneDrive\Desktop\RBAC 2022\Local\Thailand\Raw\2018 11.csv')
Nov18.columns = ['CountryID','Country', 'Quantity(KGM)', 'Value(Baht)', 'Cumulative Quantity(KGM)', 'Cumulative Value(Baht)']
Nov18.insert(Nov18.shape[1], "Date", "2018/11/01")

# 2018 12
Dec18 = pandas.read_csv(r'C:\Users\jiaxi\OneDrive\Desktop\RBAC 2022\Local\Thailand\Raw\2018 12.csv')
Dec18.columns = ['CountryID','Country', 'Quantity(KGM)', 'Value(Baht)', 'Cumulative Quantity(KGM)', 'Cumulative Value(Baht)']
Dec18.insert(Dec18.shape[1], "Date", "2018/12/01")


##2017
# 2017 01
Jan17 = pandas.read_csv(r'C:\Users\jiaxi\OneDrive\Desktop\RBAC 2022\Local\Thailand\Raw\2017 01.csv')
Jan17.columns = ['CountryID','Country', 'Quantity(KGM)', 'Value(Baht)', 'Cumulative Quantity(KGM)', 'Cumulative Value(Baht)']
Jan17.insert(Jan17.shape[1], "Date", "2017/01/01")

# 2017 02
Feb17 = pandas.read_csv(r'C:\Users\jiaxi\OneDrive\Desktop\RBAC 2022\Local\Thailand\Raw\2017 02.csv')
Feb17.columns = ['CountryID','Country', 'Quantity(KGM)', 'Value(Baht)', 'Cumulative Quantity(KGM)', 'Cumulative Value(Baht)']
Feb17.insert(Feb17.shape[1], "Date", "2017/02/01")

# 2017 03
Mar17 = pandas.read_csv(r'C:\Users\jiaxi\OneDrive\Desktop\RBAC 2022\Local\Thailand\Raw\2017 03.csv')
Mar17.columns = ['CountryID','Country', 'Quantity(KGM)', 'Value(Baht)', 'Cumulative Quantity(KGM)', 'Cumulative Value(Baht)']
Mar17.insert(Mar17.shape[1], "Date", "2017/03/01")

# 2017 04
Apr17 = pandas.read_csv(r'C:\Users\jiaxi\OneDrive\Desktop\RBAC 2022\Local\Thailand\Raw\2017 04.csv')
Apr17.columns = ['CountryID','Country', 'Quantity(KGM)', 'Value(Baht)', 'Cumulative Quantity(KGM)', 'Cumulative Value(Baht)']
Apr17.insert(Apr17.shape[1], "Date", "2017/04/01")

# 2017 05
May17 = pandas.read_csv(r'C:\Users\jiaxi\OneDrive\Desktop\RBAC 2022\Local\Thailand\Raw\2017 05.csv')
May17.columns = ['CountryID','Country', 'Quantity(KGM)', 'Value(Baht)', 'Cumulative Quantity(KGM)', 'Cumulative Value(Baht)']
May17.insert(May17.shape[1], "Date", "2017/05/01")

# 2017 06
Jun17 = pandas.read_csv(r'C:\Users\jiaxi\OneDrive\Desktop\RBAC 2022\Local\Thailand\Raw\2017 06.csv')
Jun17.columns = ['CountryID','Country', 'Quantity(KGM)', 'Value(Baht)', 'Cumulative Quantity(KGM)', 'Cumulative Value(Baht)']
Jun17.insert(Jun17.shape[1], "Date", "2017/06/01")

# 2017 07
Jul17 = pandas.read_csv(r'C:\Users\jiaxi\OneDrive\Desktop\RBAC 2022\Local\Thailand\Raw\2017 07.csv')
Jul17.columns = ['CountryID','Country', 'Quantity(KGM)', 'Value(Baht)', 'Cumulative Quantity(KGM)', 'Cumulative Value(Baht)']
Jul17.insert(Jul17.shape[1], "Date", "2017/07/01")

# 2017 08
Aug17 = pandas.read_csv(r'C:\Users\jiaxi\OneDrive\Desktop\RBAC 2022\Local\Thailand\Raw\2017 08.csv')
Aug17.columns = ['CountryID','Country', 'Quantity(KGM)', 'Value(Baht)', 'Cumulative Quantity(KGM)', 'Cumulative Value(Baht)']
Aug17.insert(Aug17.shape[1], "Date", "2017/08/01")

# 2017 09
Sep17 = pandas.read_csv(r'C:\Users\jiaxi\OneDrive\Desktop\RBAC 2022\Local\Thailand\Raw\2017 09.csv')
Sep17.columns = ['CountryID','Country', 'Quantity(KGM)', 'Value(Baht)', 'Cumulative Quantity(KGM)', 'Cumulative Value(Baht)']
Sep17.insert(Sep17.shape[1], "Date", "2017/09/01")

# 2017 10
Oct17 = pandas.read_csv(r'C:\Users\jiaxi\OneDrive\Desktop\RBAC 2022\Local\Thailand\Raw\2017 10.csv')
Oct17.columns = ['CountryID','Country', 'Quantity(KGM)', 'Value(Baht)', 'Cumulative Quantity(KGM)', 'Cumulative Value(Baht)']
Oct17.insert(Oct17.shape[1], "Date", "2017/10/01")

# 2017 11
Nov17 = pandas.read_csv(r'C:\Users\jiaxi\OneDrive\Desktop\RBAC 2022\Local\Thailand\Raw\2017 11.csv')
Nov17.columns = ['CountryID','Country', 'Quantity(KGM)', 'Value(Baht)', 'Cumulative Quantity(KGM)', 'Cumulative Value(Baht)']
Nov17.insert(Nov17.shape[1], "Date", "2017/11/01")

# 2017 12
Dec17 = pandas.read_csv(r'C:\Users\jiaxi\OneDrive\Desktop\RBAC 2022\Local\Thailand\Raw\2017 12.csv')
Dec17.columns = ['CountryID','Country', 'Quantity(KGM)', 'Value(Baht)', 'Cumulative Quantity(KGM)', 'Cumulative Value(Baht)']
Dec17.insert(Dec17.shape[1], "Date", "2017/12/01")



##2016
# 2016 01
Jan16 = pandas.read_csv(r'C:\Users\jiaxi\OneDrive\Desktop\RBAC 2022\Local\Thailand\Raw\2016 01.csv')
Jan16.columns = ['CountryID','Country', 'Quantity(KGM)', 'Value(Baht)', 'Cumulative Quantity(KGM)', 'Cumulative Value(Baht)']
Jan16.insert(Jan16.shape[1], "Date", "2016/01/01")

# 2016 02
Feb16 = pandas.read_csv(r'C:\Users\jiaxi\OneDrive\Desktop\RBAC 2022\Local\Thailand\Raw\2016 02.csv')
Feb16.columns = ['CountryID','Country', 'Quantity(KGM)', 'Value(Baht)', 'Cumulative Quantity(KGM)', 'Cumulative Value(Baht)']
Feb16.insert(Feb16.shape[1], "Date", "2016/02/01")

# 2016 03
Mar16 = pandas.read_csv(r'C:\Users\jiaxi\OneDrive\Desktop\RBAC 2022\Local\Thailand\Raw\2016 03.csv')
Mar16.columns = ['CountryID','Country', 'Quantity(KGM)', 'Value(Baht)', 'Cumulative Quantity(KGM)', 'Cumulative Value(Baht)']
Mar16.insert(Mar16.shape[1], "Date", "2016/03/01")

# 2016 04
Apr16 = pandas.read_csv(r'C:\Users\jiaxi\OneDrive\Desktop\RBAC 2022\Local\Thailand\Raw\2016 04.csv')
Apr16.columns = ['CountryID','Country', 'Quantity(KGM)', 'Value(Baht)', 'Cumulative Quantity(KGM)', 'Cumulative Value(Baht)']
Apr16.insert(Apr16.shape[1], "Date", "2016/04/01")

# 2016 05
May16 = pandas.read_csv(r'C:\Users\jiaxi\OneDrive\Desktop\RBAC 2022\Local\Thailand\Raw\2016 05.csv')
May16.columns = ['CountryID','Country', 'Quantity(KGM)', 'Value(Baht)', 'Cumulative Quantity(KGM)', 'Cumulative Value(Baht)']
May16.insert(May16.shape[1], "Date", "2016/05/01")

# 2016 06
Jun16 = pandas.read_csv(r'C:\Users\jiaxi\OneDrive\Desktop\RBAC 2022\Local\Thailand\Raw\2016 06.csv')
Jun16.columns = ['CountryID','Country', 'Quantity(KGM)', 'Value(Baht)', 'Cumulative Quantity(KGM)', 'Cumulative Value(Baht)']
Jun16.insert(Jun16.shape[1], "Date", "2016/06/01")

# 2016 07
Jul16 = pandas.read_csv(r'C:\Users\jiaxi\OneDrive\Desktop\RBAC 2022\Local\Thailand\Raw\2016 07.csv')
Jul16.columns = ['CountryID','Country', 'Quantity(KGM)', 'Value(Baht)', 'Cumulative Quantity(KGM)', 'Cumulative Value(Baht)']
Jul16.insert(Jul16.shape[1], "Date", "2016/07/01")

# 2016 08
Aug16 = pandas.read_csv(r'C:\Users\jiaxi\OneDrive\Desktop\RBAC 2022\Local\Thailand\Raw\2016 08.csv')
Aug16.columns = ['CountryID','Country', 'Quantity(KGM)', 'Value(Baht)', 'Cumulative Quantity(KGM)', 'Cumulative Value(Baht)']
Aug16.insert(Aug16.shape[1], "Date", "2016/08/01")

# 2016 09
Sep16 = pandas.read_csv(r'C:\Users\jiaxi\OneDrive\Desktop\RBAC 2022\Local\Thailand\Raw\2016 09.csv')
Sep16.columns = ['CountryID','Country', 'Quantity(KGM)', 'Value(Baht)', 'Cumulative Quantity(KGM)', 'Cumulative Value(Baht)']
Sep16.insert(Sep16.shape[1], "Date", "2016/09/01")

# 2016 10
Oct16 = pandas.read_csv(r'C:\Users\jiaxi\OneDrive\Desktop\RBAC 2022\Local\Thailand\Raw\2016 10.csv')
Oct16.columns = ['CountryID','Country', 'Quantity(KGM)', 'Value(Baht)', 'Cumulative Quantity(KGM)', 'Cumulative Value(Baht)']
Oct16.insert(Oct16.shape[1], "Date", "2016/10/01")

# 2016 11
Nov16 = pandas.read_csv(r'C:\Users\jiaxi\OneDrive\Desktop\RBAC 2022\Local\Thailand\Raw\2016 11.csv')
Nov16.columns = ['CountryID','Country', 'Quantity(KGM)', 'Value(Baht)', 'Cumulative Quantity(KGM)', 'Cumulative Value(Baht)']
Nov16.insert(Nov16.shape[1], "Date", "2016/11/01")

# 2016 12
Dec16 = pandas.read_csv(r'C:\Users\jiaxi\OneDrive\Desktop\RBAC 2022\Local\Thailand\Raw\2016 12.csv')
Dec16.columns = ['CountryID','Country', 'Quantity(KGM)', 'Value(Baht)', 'Cumulative Quantity(KGM)', 'Cumulative Value(Baht)']
Dec16.insert(Dec16.shape[1], "Date", "2016/12/01")



##2015
# 2015 01
Jan15 = pandas.read_csv(r'C:\Users\jiaxi\OneDrive\Desktop\RBAC 2022\Local\Thailand\Raw\2015 01.csv')
Jan15.columns = ['CountryID','Country', 'Quantity(KGM)', 'Value(Baht)', 'Cumulative Quantity(KGM)', 'Cumulative Value(Baht)']
Jan15.insert(Jan15.shape[1], "Date", "2015/01/01")

# 2015 02
Feb15 = pandas.read_csv(r'C:\Users\jiaxi\OneDrive\Desktop\RBAC 2022\Local\Thailand\Raw\2015 02.csv')
Feb15.columns = ['CountryID','Country', 'Quantity(KGM)', 'Value(Baht)', 'Cumulative Quantity(KGM)', 'Cumulative Value(Baht)']
Feb15.insert(Feb15.shape[1], "Date", "2015/02/01")

# 2015 03
Mar15 = pandas.read_csv(r'C:\Users\jiaxi\OneDrive\Desktop\RBAC 2022\Local\Thailand\Raw\2015 03.csv')
Mar15.columns = ['CountryID','Country', 'Quantity(KGM)', 'Value(Baht)', 'Cumulative Quantity(KGM)', 'Cumulative Value(Baht)']
Mar15.insert(Mar15.shape[1], "Date", "2015/03/01")

# 2015 04
Apr15 = pandas.read_csv(r'C:\Users\jiaxi\OneDrive\Desktop\RBAC 2022\Local\Thailand\Raw\2015 04.csv')
Apr15.columns = ['CountryID','Country', 'Quantity(KGM)', 'Value(Baht)', 'Cumulative Quantity(KGM)', 'Cumulative Value(Baht)']
Apr15.insert(Apr15.shape[1], "Date", "2015/04/01")

# 2015 05
May15 = pandas.read_csv(r'C:\Users\jiaxi\OneDrive\Desktop\RBAC 2022\Local\Thailand\Raw\2015 05.csv')
May15.columns = ['CountryID','Country', 'Quantity(KGM)', 'Value(Baht)', 'Cumulative Quantity(KGM)', 'Cumulative Value(Baht)']
May15.insert(May15.shape[1], "Date", "2015/05/01")

# 2015 06
Jun15 = pandas.read_csv(r'C:\Users\jiaxi\OneDrive\Desktop\RBAC 2022\Local\Thailand\Raw\2015 06.csv')
Jun15.columns = ['CountryID','Country', 'Quantity(KGM)', 'Value(Baht)', 'Cumulative Quantity(KGM)', 'Cumulative Value(Baht)']
Jun15.insert(Jun15.shape[1], "Date", "2015/06/01")

# 2015 07
Jul15 = pandas.read_csv(r'C:\Users\jiaxi\OneDrive\Desktop\RBAC 2022\Local\Thailand\Raw\2015 07.csv')
Jul15.columns = ['CountryID','Country', 'Quantity(KGM)', 'Value(Baht)', 'Cumulative Quantity(KGM)', 'Cumulative Value(Baht)']
Jul15.insert(Jul15.shape[1], "Date", "2015/07/01")

# 2015 08
Aug15 = pandas.read_csv(r'C:\Users\jiaxi\OneDrive\Desktop\RBAC 2022\Local\Thailand\Raw\2015 08.csv')
Aug15.columns = ['CountryID','Country', 'Quantity(KGM)', 'Value(Baht)', 'Cumulative Quantity(KGM)', 'Cumulative Value(Baht)']
Aug15.insert(Aug15.shape[1], "Date", "2015/08/01")

# 2015 09
Sep15 = pandas.read_csv(r'C:\Users\jiaxi\OneDrive\Desktop\RBAC 2022\Local\Thailand\Raw\2015 09.csv')
Sep15.columns = ['CountryID','Country', 'Quantity(KGM)', 'Value(Baht)', 'Cumulative Quantity(KGM)', 'Cumulative Value(Baht)']
Sep15.insert(Sep15.shape[1], "Date", "2015/09/01")

# 2015 10
Oct15 = pandas.read_csv(r'C:\Users\jiaxi\OneDrive\Desktop\RBAC 2022\Local\Thailand\Raw\2015 10.csv')
Oct15.columns = ['CountryID','Country', 'Quantity(KGM)', 'Value(Baht)', 'Cumulative Quantity(KGM)', 'Cumulative Value(Baht)']
Oct15.insert(Oct15.shape[1], "Date", "2015/10/01")

# 2015 11
Nov15 = pandas.read_csv(r'C:\Users\jiaxi\OneDrive\Desktop\RBAC 2022\Local\Thailand\Raw\2015 11.csv')
Nov15.columns = ['CountryID','Country', 'Quantity(KGM)', 'Value(Baht)', 'Cumulative Quantity(KGM)', 'Cumulative Value(Baht)']
Nov15.insert(Nov15.shape[1], "Date", "2015/11/01")

# 2015 12
Dec15 = pandas.read_csv(r'C:\Users\jiaxi\OneDrive\Desktop\RBAC 2022\Local\Thailand\Raw\2015 12.csv')
Dec15.columns = ['CountryID','Country', 'Quantity(KGM)', 'Value(Baht)', 'Cumulative Quantity(KGM)', 'Cumulative Value(Baht)']
Dec15.insert(Dec15.shape[1], "Date", "2015/12/01")




##2014
# 2014 01
Jan14 = pandas.read_csv(r'C:\Users\jiaxi\OneDrive\Desktop\RBAC 2022\Local\Thailand\Raw\2014 01.csv')
Jan14.columns = ['CountryID','Country', 'Quantity(KGM)', 'Value(Baht)', 'Cumulative Quantity(KGM)', 'Cumulative Value(Baht)']
Jan14.insert(Jan14.shape[1], "Date", "2014/01/01")

# 2014 02
Feb14 = pandas.read_csv(r'C:\Users\jiaxi\OneDrive\Desktop\RBAC 2022\Local\Thailand\Raw\2014 02.csv')
Feb14.columns = ['CountryID','Country', 'Quantity(KGM)', 'Value(Baht)', 'Cumulative Quantity(KGM)', 'Cumulative Value(Baht)']
Feb14.insert(Feb14.shape[1], "Date", "2014/02/01")

# 2014 03
Mar14 = pandas.read_csv(r'C:\Users\jiaxi\OneDrive\Desktop\RBAC 2022\Local\Thailand\Raw\2014 03.csv')
Mar14.columns = ['CountryID','Country', 'Quantity(KGM)', 'Value(Baht)', 'Cumulative Quantity(KGM)', 'Cumulative Value(Baht)']
Mar14.insert(Mar14.shape[1], "Date", "2014/03/01")

# 2014 04
Apr14 = pandas.read_csv(r'C:\Users\jiaxi\OneDrive\Desktop\RBAC 2022\Local\Thailand\Raw\2014 04.csv')
Apr14.columns = ['CountryID','Country', 'Quantity(KGM)', 'Value(Baht)', 'Cumulative Quantity(KGM)', 'Cumulative Value(Baht)']
Apr14.insert(Apr14.shape[1], "Date", "2014/04/01")

# 2014 05
May14 = pandas.read_csv(r'C:\Users\jiaxi\OneDrive\Desktop\RBAC 2022\Local\Thailand\Raw\2014 05.csv')
May14.columns = ['CountryID','Country', 'Quantity(KGM)', 'Value(Baht)', 'Cumulative Quantity(KGM)', 'Cumulative Value(Baht)']
May14.insert(May14.shape[1], "Date", "2014/05/01")

# 2014 06
Jun14 = pandas.read_csv(r'C:\Users\jiaxi\OneDrive\Desktop\RBAC 2022\Local\Thailand\Raw\2014 06.csv')
Jun14.columns = ['CountryID','Country', 'Quantity(KGM)', 'Value(Baht)', 'Cumulative Quantity(KGM)', 'Cumulative Value(Baht)']
Jun14.insert(Jun14.shape[1], "Date", "2014/06/01")

# 2014 07
Jul14 = pandas.read_csv(r'C:\Users\jiaxi\OneDrive\Desktop\RBAC 2022\Local\Thailand\Raw\2014 07.csv')
Jul14.columns = ['CountryID','Country', 'Quantity(KGM)', 'Value(Baht)', 'Cumulative Quantity(KGM)', 'Cumulative Value(Baht)']
Jul14.insert(Jul14.shape[1], "Date", "2014/07/01")

# 2014 08
Aug14 = pandas.read_csv(r'C:\Users\jiaxi\OneDrive\Desktop\RBAC 2022\Local\Thailand\Raw\2014 08.csv')
Aug14.columns = ['CountryID','Country', 'Quantity(KGM)', 'Value(Baht)', 'Cumulative Quantity(KGM)', 'Cumulative Value(Baht)']
Aug14.insert(Aug14.shape[1], "Date", "2014/08/01")

# 2014 09
Sep14 = pandas.read_csv(r'C:\Users\jiaxi\OneDrive\Desktop\RBAC 2022\Local\Thailand\Raw\2014 09.csv')
Sep14.columns = ['CountryID','Country', 'Quantity(KGM)', 'Value(Baht)', 'Cumulative Quantity(KGM)', 'Cumulative Value(Baht)']
Sep14.insert(Sep14.shape[1], "Date", "2014/09/01")

# 2014 10
Oct14 = pandas.read_csv(r'C:\Users\jiaxi\OneDrive\Desktop\RBAC 2022\Local\Thailand\Raw\2014 10.csv')
Oct14.columns = ['CountryID','Country', 'Quantity(KGM)', 'Value(Baht)', 'Cumulative Quantity(KGM)', 'Cumulative Value(Baht)']
Oct14.insert(Oct14.shape[1], "Date", "2014/10/01")

# 2014 11
Nov14 = pandas.read_csv(r'C:\Users\jiaxi\OneDrive\Desktop\RBAC 2022\Local\Thailand\Raw\2014 11.csv')
Nov14.columns = ['CountryID','Country', 'Quantity(KGM)', 'Value(Baht)', 'Cumulative Quantity(KGM)', 'Cumulative Value(Baht)']
Nov14.insert(Nov14.shape[1], "Date", "2014/11/01")

# 2014 12
Dec14 = pandas.read_csv(r'C:\Users\jiaxi\OneDrive\Desktop\RBAC 2022\Local\Thailand\Raw\2014 12.csv')
Dec14.columns = ['CountryID','Country', 'Quantity(KGM)', 'Value(Baht)', 'Cumulative Quantity(KGM)', 'Cumulative Value(Baht)']
Dec14.insert(Dec14.shape[1], "Date", "2014/12/01")



##2013
# 2013 01
Jan13 = pandas.read_csv(r'C:\Users\jiaxi\OneDrive\Desktop\RBAC 2022\Local\Thailand\Raw\2013 01.csv')
Jan13.columns = ['CountryID','Country', 'Quantity(KGM)', 'Value(Baht)', 'Cumulative Quantity(KGM)', 'Cumulative Value(Baht)']
Jan13.insert(Jan13.shape[1], "Date", "2013/01/01")

# 2013 02
Feb13 = pandas.read_csv(r'C:\Users\jiaxi\OneDrive\Desktop\RBAC 2022\Local\Thailand\Raw\2013 02.csv')
Feb13.columns = ['CountryID','Country', 'Quantity(KGM)', 'Value(Baht)', 'Cumulative Quantity(KGM)', 'Cumulative Value(Baht)']
Feb13.insert(Feb13.shape[1], "Date", "2013/02/01")

# 2013 03
Mar13 = pandas.read_csv(r'C:\Users\jiaxi\OneDrive\Desktop\RBAC 2022\Local\Thailand\Raw\2013 03.csv')
Mar13.columns = ['CountryID','Country', 'Quantity(KGM)', 'Value(Baht)', 'Cumulative Quantity(KGM)', 'Cumulative Value(Baht)']
Mar13.insert(Mar13.shape[1], "Date", "2013/03/01")

# 2013 04
Apr13 = pandas.read_csv(r'C:\Users\jiaxi\OneDrive\Desktop\RBAC 2022\Local\Thailand\Raw\2013 04.csv')
Apr13.columns = ['CountryID','Country', 'Quantity(KGM)', 'Value(Baht)', 'Cumulative Quantity(KGM)', 'Cumulative Value(Baht)']
Apr13.insert(Apr13.shape[1], "Date", "2013/04/01")

# 2013 05
May13 = pandas.read_csv(r'C:\Users\jiaxi\OneDrive\Desktop\RBAC 2022\Local\Thailand\Raw\2013 05.csv')
May13.columns = ['CountryID','Country', 'Quantity(KGM)', 'Value(Baht)', 'Cumulative Quantity(KGM)', 'Cumulative Value(Baht)']
May13.insert(May13.shape[1], "Date", "2013/05/01")

# 2013 06
Jun13 = pandas.read_csv(r'C:\Users\jiaxi\OneDrive\Desktop\RBAC 2022\Local\Thailand\Raw\2013 06.csv')
Jun13.columns = ['CountryID','Country', 'Quantity(KGM)', 'Value(Baht)', 'Cumulative Quantity(KGM)', 'Cumulative Value(Baht)']
Jun13.insert(Jun13.shape[1], "Date", "2013/06/01")

# 2013 07
Jul13 = pandas.read_csv(r'C:\Users\jiaxi\OneDrive\Desktop\RBAC 2022\Local\Thailand\Raw\2013 07.csv')
Jul13.columns = ['CountryID','Country', 'Quantity(KGM)', 'Value(Baht)', 'Cumulative Quantity(KGM)', 'Cumulative Value(Baht)']
Jul13.insert(Jul13.shape[1], "Date", "2013/07/01")

# 2013 08
Aug13 = pandas.read_csv(r'C:\Users\jiaxi\OneDrive\Desktop\RBAC 2022\Local\Thailand\Raw\2013 08.csv')
Aug13.columns = ['CountryID','Country', 'Quantity(KGM)', 'Value(Baht)', 'Cumulative Quantity(KGM)', 'Cumulative Value(Baht)']
Aug13.insert(Aug13.shape[1], "Date", "2013/08/01")

# 2013 09
Sep13 = pandas.read_csv(r'C:\Users\jiaxi\OneDrive\Desktop\RBAC 2022\Local\Thailand\Raw\2013 09.csv')
Sep13.columns = ['CountryID','Country', 'Quantity(KGM)', 'Value(Baht)', 'Cumulative Quantity(KGM)', 'Cumulative Value(Baht)']
Sep13.insert(Sep13.shape[1], "Date", "2013/09/01")

# 2013 10
Oct13 = pandas.read_csv(r'C:\Users\jiaxi\OneDrive\Desktop\RBAC 2022\Local\Thailand\Raw\2013 10.csv')
Oct13.columns = ['CountryID','Country', 'Quantity(KGM)', 'Value(Baht)', 'Cumulative Quantity(KGM)', 'Cumulative Value(Baht)']
Oct13.insert(Oct13.shape[1], "Date", "2013/10/01")

# 2013 11
Nov13 = pandas.read_csv(r'C:\Users\jiaxi\OneDrive\Desktop\RBAC 2022\Local\Thailand\Raw\2013 11.csv')
Nov13.columns = ['CountryID','Country', 'Quantity(KGM)', 'Value(Baht)', 'Cumulative Quantity(KGM)', 'Cumulative Value(Baht)']
Nov13.insert(Nov13.shape[1], "Date", "2013/11/01")

# 2013 12
Dec13 = pandas.read_csv(r'C:\Users\jiaxi\OneDrive\Desktop\RBAC 2022\Local\Thailand\Raw\2013 12.csv')
Dec13.columns = ['CountryID','Country', 'Quantity(KGM)', 'Value(Baht)', 'Cumulative Quantity(KGM)', 'Cumulative Value(Baht)']
Dec13.insert(Dec13.shape[1], "Date", "2013/12/01")


##2012
# 2012 01
Jan12 = pandas.read_csv(r'C:\Users\jiaxi\OneDrive\Desktop\RBAC 2022\Local\Thailand\Raw\2012 01.csv')
Jan12.columns = ['CountryID','Country', 'Quantity(KGM)', 'Value(Baht)', 'Cumulative Quantity(KGM)', 'Cumulative Value(Baht)']
Jan12.insert(Jan12.shape[1], "Date", "2012/01/01")

# 2012 02
Feb12 = pandas.read_csv(r'C:\Users\jiaxi\OneDrive\Desktop\RBAC 2022\Local\Thailand\Raw\2012 02.csv')
Feb12.columns = ['CountryID','Country', 'Quantity(KGM)', 'Value(Baht)', 'Cumulative Quantity(KGM)', 'Cumulative Value(Baht)']
Feb12.insert(Feb12.shape[1], "Date", "2012/02/01")

# 2012 03
Mar12 = pandas.read_csv(r'C:\Users\jiaxi\OneDrive\Desktop\RBAC 2022\Local\Thailand\Raw\2012 03.csv')
Mar12.columns = ['CountryID','Country', 'Quantity(KGM)', 'Value(Baht)', 'Cumulative Quantity(KGM)', 'Cumulative Value(Baht)']
Mar12.insert(Mar12.shape[1], "Date", "2012/03/01")

# 2012 04
Apr12 = pandas.read_csv(r'C:\Users\jiaxi\OneDrive\Desktop\RBAC 2022\Local\Thailand\Raw\2012 04.csv')
Apr12.columns = ['CountryID','Country', 'Quantity(KGM)', 'Value(Baht)', 'Cumulative Quantity(KGM)', 'Cumulative Value(Baht)']
Apr12.insert(Apr12.shape[1], "Date", "2012/04/01")

# 2012 05
May12 = pandas.read_csv(r'C:\Users\jiaxi\OneDrive\Desktop\RBAC 2022\Local\Thailand\Raw\2012 05.csv')
May12.columns = ['CountryID','Country', 'Quantity(KGM)', 'Value(Baht)', 'Cumulative Quantity(KGM)', 'Cumulative Value(Baht)']
May12.insert(May12.shape[1], "Date", "2012/05/01")

# 2012 06
Jun12 = pandas.read_csv(r'C:\Users\jiaxi\OneDrive\Desktop\RBAC 2022\Local\Thailand\Raw\2012 06.csv')
Jun12.columns = ['CountryID','Country', 'Quantity(KGM)', 'Value(Baht)', 'Cumulative Quantity(KGM)', 'Cumulative Value(Baht)']
Jun12.insert(Jun12.shape[1], "Date", "2012/06/01")

# 2012 07
Jul12 = pandas.read_csv(r'C:\Users\jiaxi\OneDrive\Desktop\RBAC 2022\Local\Thailand\Raw\2012 07.csv')
Jul12.columns = ['CountryID','Country', 'Quantity(KGM)', 'Value(Baht)', 'Cumulative Quantity(KGM)', 'Cumulative Value(Baht)']
Jul12.insert(Jul12.shape[1], "Date", "2012/07/01")

# 2012 08
Aug12 = pandas.read_csv(r'C:\Users\jiaxi\OneDrive\Desktop\RBAC 2022\Local\Thailand\Raw\2012 08.csv')
Aug12.columns = ['CountryID','Country', 'Quantity(KGM)', 'Value(Baht)', 'Cumulative Quantity(KGM)', 'Cumulative Value(Baht)']
Aug12.insert(Aug12.shape[1], "Date", "2012/08/01")

# 2012 09
Sep12 = pandas.read_csv(r'C:\Users\jiaxi\OneDrive\Desktop\RBAC 2022\Local\Thailand\Raw\2012 09.csv')
Sep12.columns = ['CountryID','Country', 'Quantity(KGM)', 'Value(Baht)', 'Cumulative Quantity(KGM)', 'Cumulative Value(Baht)']
Sep12.insert(Sep12.shape[1], "Date", "2012/09/01")

# 2012 10
Oct12 = pandas.read_csv(r'C:\Users\jiaxi\OneDrive\Desktop\RBAC 2022\Local\Thailand\Raw\2012 10.csv')
Oct12.columns = ['CountryID','Country', 'Quantity(KGM)', 'Value(Baht)', 'Cumulative Quantity(KGM)', 'Cumulative Value(Baht)']
Oct12.insert(Oct12.shape[1], "Date", "2012/10/01")

# 2012 11
Nov12 = pandas.read_csv(r'C:\Users\jiaxi\OneDrive\Desktop\RBAC 2022\Local\Thailand\Raw\2012 11.csv')
Nov12.columns = ['CountryID','Country', 'Quantity(KGM)', 'Value(Baht)', 'Cumulative Quantity(KGM)', 'Cumulative Value(Baht)']
Nov12.insert(Nov12.shape[1], "Date", "2012/11/01")

# 2012 12
Dec12 = pandas.read_csv(r'C:\Users\jiaxi\OneDrive\Desktop\RBAC 2022\Local\Thailand\Raw\2012 12.csv')
Dec12.columns = ['CountryID','Country', 'Quantity(KGM)', 'Value(Baht)', 'Cumulative Quantity(KGM)', 'Cumulative Value(Baht)']
Dec12.insert(Dec12.shape[1], "Date", "2012/12/01")



##2011
# 2011 01
Jan11 = pandas.read_csv(r'C:\Users\jiaxi\OneDrive\Desktop\RBAC 2022\Local\Thailand\Raw\2011 01.csv')
Jan11.columns = ['CountryID','Country', 'Quantity(KGM)', 'Value(Baht)', 'Cumulative Quantity(KGM)', 'Cumulative Value(Baht)']
Jan11.insert(Jan11.shape[1], "Date", "2011/01/01")

# 2011 02
Feb11 = pandas.read_csv(r'C:\Users\jiaxi\OneDrive\Desktop\RBAC 2022\Local\Thailand\Raw\2011 02.csv')
Feb11.columns = ['CountryID','Country', 'Quantity(KGM)', 'Value(Baht)', 'Cumulative Quantity(KGM)', 'Cumulative Value(Baht)']
Feb11.insert(Feb11.shape[1], "Date", "2011/02/01")

# 2011 03
Mar11 = pandas.read_csv(r'C:\Users\jiaxi\OneDrive\Desktop\RBAC 2022\Local\Thailand\Raw\2011 03.csv')
Mar11.columns = ['CountryID','Country', 'Quantity(KGM)', 'Value(Baht)', 'Cumulative Quantity(KGM)', 'Cumulative Value(Baht)']
Mar11.insert(Mar11.shape[1], "Date", "2011/03/01")

# 2011 04
Apr11 = pandas.read_csv(r'C:\Users\jiaxi\OneDrive\Desktop\RBAC 2022\Local\Thailand\Raw\2011 04.csv')
Apr11.columns = ['CountryID','Country', 'Quantity(KGM)', 'Value(Baht)', 'Cumulative Quantity(KGM)', 'Cumulative Value(Baht)']
Apr11.insert(Apr11.shape[1], "Date", "2011/04/01")

# 2011 05
May11 = pandas.read_csv(r'C:\Users\jiaxi\OneDrive\Desktop\RBAC 2022\Local\Thailand\Raw\2011 05.csv')
May11.columns = ['CountryID','Country', 'Quantity(KGM)', 'Value(Baht)', 'Cumulative Quantity(KGM)', 'Cumulative Value(Baht)']
May11.insert(May11.shape[1], "Date", "2011/05/01")

# 2011 06
Jun11 = pandas.read_csv(r'C:\Users\jiaxi\OneDrive\Desktop\RBAC 2022\Local\Thailand\Raw\2011 06.csv')
Jun11.columns = ['CountryID','Country', 'Quantity(KGM)', 'Value(Baht)', 'Cumulative Quantity(KGM)', 'Cumulative Value(Baht)']
Jun11.insert(Jun11.shape[1], "Date", "2011/06/01")

# 2011 07
Jul11 = pandas.read_csv(r'C:\Users\jiaxi\OneDrive\Desktop\RBAC 2022\Local\Thailand\Raw\2011 07.csv')
Jul11.columns = ['CountryID','Country', 'Quantity(KGM)', 'Value(Baht)', 'Cumulative Quantity(KGM)', 'Cumulative Value(Baht)']
Jul11.insert(Jul11.shape[1], "Date", "2011/07/01")

# 2011 08
Aug11 = pandas.read_csv(r'C:\Users\jiaxi\OneDrive\Desktop\RBAC 2022\Local\Thailand\Raw\2011 08.csv')
Aug11.columns = ['CountryID','Country', 'Quantity(KGM)', 'Value(Baht)', 'Cumulative Quantity(KGM)', 'Cumulative Value(Baht)']
Aug11.insert(Aug11.shape[1], "Date", "2011/08/01")

# 2011 09
Sep11 = pandas.read_csv(r'C:\Users\jiaxi\OneDrive\Desktop\RBAC 2022\Local\Thailand\Raw\2011 09.csv')
Sep11.columns = ['CountryID','Country', 'Quantity(KGM)', 'Value(Baht)', 'Cumulative Quantity(KGM)', 'Cumulative Value(Baht)']
Sep11.insert(Sep11.shape[1], "Date", "2011/09/01")

# 2011 10
Oct11 = pandas.read_csv(r'C:\Users\jiaxi\OneDrive\Desktop\RBAC 2022\Local\Thailand\Raw\2011 10.csv')
Oct11.columns = ['CountryID','Country', 'Quantity(KGM)', 'Value(Baht)', 'Cumulative Quantity(KGM)', 'Cumulative Value(Baht)']
Oct11.insert(Oct11.shape[1], "Date", "2011/10/01")

# 2011 11
Nov11 = pandas.read_csv(r'C:\Users\jiaxi\OneDrive\Desktop\RBAC 2022\Local\Thailand\Raw\2011 11.csv')
Nov11.columns = ['CountryID','Country', 'Quantity(KGM)', 'Value(Baht)', 'Cumulative Quantity(KGM)', 'Cumulative Value(Baht)']
Nov11.insert(Nov11.shape[1], "Date", "2011/11/01")

# 2011 12
Dec11 = pandas.read_csv(r'C:\Users\jiaxi\OneDrive\Desktop\RBAC 2022\Local\Thailand\Raw\2011 12.csv')
Dec11.columns = ['CountryID','Country', 'Quantity(KGM)', 'Value(Baht)', 'Cumulative Quantity(KGM)', 'Cumulative Value(Baht)']
Dec11.insert(Dec11.shape[1], "Date", "2011/12/01")




#####

Output1 = [Jan22, Feb22, Mar22, Apr22, \
           Jan21, Feb21, Mar21, Apr21, May21, Jun21, Jul21, Aug21, Sep21, Oct21, Nov21, Dec21, \
           Jan20, Feb20, Mar20, Apr20, May20, Jun20, Jul20, Aug20, Sep20, Oct20, Nov20, Dec20, \
           Jan19, Feb19, Mar19, Apr19, May19, Jun19, Jul19, Aug19, Sep19, Oct19, Nov19, Dec19, \
           Jan18, Feb18, Mar18, Apr18, May18, Jun18, Jul18, Aug18, Sep18, Oct18, Nov18, Dec18, \
           Jan17, Feb17, Mar17, Apr17, May17, Jun17, Jul17, Aug17, Sep17, Oct17, Nov17, Dec17, \
           Jan16, Feb16, Mar16, Apr16, May16, Jun16, Jul16, Aug16, Sep16, Oct16, Nov16, Dec16, \
           Jan15, Feb15, Mar15, Apr15, May15, Jun15, Jul15, Aug15, Sep15, Oct15, Nov15, Dec15, \
           Jan14, Feb14, Mar14, Apr14, May14, Jun14, Jul14, Aug14, Sep14, Oct14, Nov14, Dec14, \
           Jan13, Feb13, Mar13, Apr13, May13, Jun13, Jul13, Aug13, Sep13, Oct13, Nov13, Dec13, \
           Jan12, Feb12, Mar12, Apr12, May12, Jun12, Jul12, Aug12, Sep12, Oct12, Nov12, Dec12, \
           Jan11, Feb11, Mar11, Apr11, May11, Jun11, Jul11, Aug11, Sep11, Oct11, Nov11, Dec11]
Output2 = pd.concat(Output1)

Output2.to_csv("C:\\Users\\jiaxi\\OneDrive\Desktop\RBAC 2022\Local\Thailand\Thailand LNG Imports by Origin.csv",index=None)


##############

endtime = datetime.datetime.now()
print ("duration：", endtime - starttime)

print("Congradutions! Finished :)")

