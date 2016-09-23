
# coding: utf-8

# In[ ]:

import numpy as np    
import pandas as pd    

currentDate = '2013-05-30 00:00:00' #defaul current date   
inactivityPeriod = 14 #defaul current date   
k = dateForCurrentDate[dateForCurrentDate[u'id пользователя'] == 170698870].index #default user index   
i = k[0]    

dateForCurrentDate = data[data[u'Дата последней сессии'] == currentDate] #making sample for current date   
DAU = len(dateForCurrentDate) #DAU calculation    
ARPU = float(sum(dateForCurrentDate.values[:, 10]) / DAU) # APRU calculation    

delta = (data.values[i, 2] - data.values[i, 1])   
deltaWithInactityPeriod = delta.days + inactivityPeriod   
LTV = deltaWithInactityPeriod * ARPU #LVT calculation

print 'LTV для указанного пользователя:', LTV

