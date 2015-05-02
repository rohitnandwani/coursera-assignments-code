import QSTK.qstkutil.qsdateutil as du
import QSTK.qstkutil.tsutil as tsu
import QSTK.qstkutil.DataAccess as da

import datetime as dt
import matplotlib.pyplot as plt
import pandas as pd

import numpy as np

ls_symbols =       ['BRCM', 'TXN', 'IBM', 'HNZ'] 
dt_start = dt.datetime(2010, 1, 1)
dt_end = dt.datetime(2010, 12, 31)
dt_timeofday = dt.timedelta(hours=16)
ldt_timestamps = du.getNYSEdays(dt_start, dt_end, dt_timeofday)


c_dataobj = da.DataAccess('Yahoo')
ls_keys = ['open', 'high', 'low', 'close', 'volume', 'actual_close']
ldf_data = c_dataobj.get_data(ldt_timestamps, ls_symbols, ls_keys)
d_data = dict(zip(ls_keys, ldf_data))




na_price = d_data['close'].values
na_normalized_price = na_price / na_price[0, :]

na_rets = na_normalized_price.copy()
daily_returns = tsu.returnize0(na_rets)

wtdr = []
best_sharpe=0
optimal_alloc = []
for i in range(11):
    for j in range(11):
        for k in range(11):
            for l in range(11):
                if(i + j + k + l == 10):
                    wtdr1 = daily_returns[:,0:1]*i/10
                    wtdr2 = daily_returns[:,1:2]*j/10
                    wtdr3 = daily_returns[:,2:3]*k/10
                    wtdr4 = daily_returns[:,3:4]*l/10
                    for m in range(0, len(wtdr1)):
                        wtdr.append(wtdr1[m] + wtdr2[m] + wtdr3[m] + wtdr4[m])
                    wtdr_avg = sum(wtdr)/float(len(wtdr))
                    std_metric = np.std(wtdr)
                    sharpe = 15.8113883008419*wtdr_avg/std_metric
                    if(sharpe > best_sharpe):
                        best_sharpe = sharpe
                        optimal_alloc = [i,j,k,l]

print best_sharpe
print optimal_alloc
                    

    



