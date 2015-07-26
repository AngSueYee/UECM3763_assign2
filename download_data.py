from pandas.io.data import DataReader as DR
from datetime import datetime as dt
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Download Data From 1/1/2011 TO 1/5/2015 For Public Bank Berhad(pbb)
start = dt(2011, 1, 1)
end = dt(2015, 5, 1)
data = DR("1295.KL", 'yahoo', start, end)

 # Calculate Moving Average
pbb = data['Close']
moving_average = pd.rolling_mean(pbb,5) 
       
#Plot 5-day Moving Average For pbb
MA = len(moving_average)
x_axis = np.arange(MA) + 5
y_axis = moving_average
plt.xlabel('Days $n$')
plt.ylabel('5-day Moving Average')
plt.plot(x_axis,y_axis)
plt.title('Public Bank Berhad 5-day Moving Average')
plt.show()

# Download Data For KLCI Index For Same Duration
KLSE_Data = DR("^KLSE", 'yahoo', start, end)

# Download The Closing Data Of Public Bank Berhad and KLCI
pbb_klci = ['1295.KL', '^KLSE']
pbe_klse_closing = DR(pbb_klci, 'yahoo', start, end)['Close']

# Calculate The Correlation Of Public Bank Berhad and KLCI
correlation = pbe_klse_closing.corr()
print ('Correlation between Public Bank Berhad and KLCI Index =')
print(correlation)