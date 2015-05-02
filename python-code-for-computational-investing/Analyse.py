import QSTK.qstkutil.qsdateutil as du
import QSTK.qstkutil.tsutil as tsu
import QSTK.qstkutil.DataAccess as da

import datetime as dt
import matplotlib.pyplot as plt
import pandas as pd

import numpy as np
import csv

reader = csv.reader(open('orders2.csv', 'rU'), delimiter=',')
ls_symbols = []
cash = [1000000]
ryear = []
rmonth = []
rday = []
rdo = []
rquantity = []
rdt = []
count = 0

for row in reader:
    ls_symbols.append(row[3])
    ryear.append(row[0])
    rmonth.append(row[1])
    rday.append(row[2])
    rdo.append(row[4])
    rquantity.append(row[5])
    count = count + 1

ls_symbols2 = list(set(ls_symbols))


dt_start = dt.datetime(2011, 1, 13)
dt_end = dt.datetime(2011, 7, 21)
dt_timeofday = dt.timedelta(hours=16)
ldt_timestamps = du.getNYSEdays(dt_start, dt_end, dt_timeofday)


c_dataobj = da.DataAccess('Yahoo')
ls_keys = ['open', 'high', 'low', 'close', 'volume', 'actual_close']
ldf_data = c_dataobj.get_data(ldt_timestamps, ls_symbols2, ls_keys)
d_data = dict(zip(ls_keys, ldf_data))
exp_dict = {}
count3 = 0
for i in ls_symbols2:
    exp_dict[i] = count3
    count3 = count3 + 1
print exp_dict



for dt_date in ldt_timestamps[0:]:
    for row in range(count):
        if int(rday[row]) == dt_date.day and int(rmonth[row]) == dt_date.month and int(ryear[row]) == dt_date.year:
            if rdo[row] == 'Buy':
                cash.append(cash[-1] - (int(d_data['close'].loc[dt_date][exp_dict[ls_symbols[row]]]) * int(rquantity[row])))
                #print cash[-1]
                print 'buy'
                print ls_symbols[row]
            if rdo[row] == 'Sell':
                cash.append(cash[-1] + (int(d_data['close'].loc[dt_date][exp_dict[ls_symbols[row]]]) * int(rquantity[row])))
                #print cash[-1]
                print 'sell'
                print ls_symbols[row]
        else:
            cash.append(cash[-1])
    if dt_date == ldt_timestamps[-1]:
        print ldt_timestamps[-1]
        print (cash[-1] + (int(d_data['close'].loc[dt_date][1])) * 1200)
print cash[-1]








                
            
        




