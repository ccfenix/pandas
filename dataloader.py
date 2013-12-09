#read csv files into data frame
from pandas import *
import numpy as np
import math

set_option('max_rows',200)
set_option('max_columns', 100)

def loadSpy(tdatetime):
  full_date=datetime.strftime( tdatetime,  "/home/ubuntu/uds/taq/%Y/%m/%d/%Y%m%d.spy.csv");
  print full_date

def loadUniv(tdatetime):
  full_path=datetime.strftime( tdatetime,  "/home/ubuntu/uds/univ/%Y/%m/%d/index.html");
  return read_csv(full_path, skiprows=1);

def loadEodCrossingPrice(tdatetime):
  return 0

univ = loadUniv(datetime(2013, 11, 15))
univ= univ[univ.bats_prev_close>1.0][univ.reuters_exchange_code.isin(['L', 'DE'])].set_index(['bats_name'])
print univ.head(5)[['company_name','isin','currency','reuters_exchange_code', 'bats_prev_close','reference_price']]

#print univ[['company_name','bats_name','isin','currency','reuters_exchange_code']].groupby('reuters_exchange_code').count().sort('bats_name', ascending=0).head()
#print value_counts(univ.bats_name)
#print univ.groupby('reuters_exchange_code').count().sort('bats_name', ascending=0).head()
# print spy['Date']

# spy['Date']+np.timedelta64(1,'ns')

# spy['Close2']=spy['Close']
# spy['Close2']=[ 0.5*math.floor(x/0.5) for x in spy['Close']]

# byclose=spy.groupby(['Close2']).mean()
# print byclose

