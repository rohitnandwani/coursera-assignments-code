import QSTK.qstkutil.qsdateutil as du
import QSTK.qstkutil.tsutil as tsu
import QSTK.qstkutil.DataAccess as da

import datetime as dt
import matplotlib.pyplot as plt
import pandas as pd

import numpy as np

ls_symbols = ["MSFT"]
dt_start = dt.datetime(2010, 1, 1)
dt_end = dt.datetime(2010, 5, 12)
dt_timeofday = dt.timedelta(hours=16)
ldt_timestamps = du.getNYSEdays(dt_start, dt_end, dt_timeofday)


c_dataobj = da.DataAccess('Yahoo')
ls_keys = ['open', 'high', 'low', 'close', 'volume', 'actual_close']
ldf_data = c_dataobj.get_data(ldt_timestamps, ls_symbols, ls_keys)
d_data = dict(zip(ls_keys, ldf_data))



sum = 0
stdarr = []
for i in range(20):
    sum = sum + d_data['close'].values[-i]
    stdarr.append(d_data['close'].values[-i])
    
sum = sum/20
stdarr.reverse()
stdev = np.std(stdarr)

print((d_data['close'].values[-i]-sum)/stdev)


