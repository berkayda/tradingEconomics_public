import pandas as pd
import tradingeconomics as te
import numpy as np

pd.set_option('display.max_columns', None) # Shows all columns
pd.set_option('display.max_rows', None) # Shows all rows
pd.set_option('display.max_colwidth', None) # Shows maximum column width
te.login('WRITE YOURS') # WRITE YOURS


mydata = te.getCalendarData(output_type='df')
print(mydata)
print("===============================================================================================================")


# To get all calendar events by importance (1-Low, 2-Medium, 3-High)
mydata = te.getCalendarData(importance='2', output_type='df')
print(mydata)
print("===============================================================================================================")

# To get calendar events by date or by date and importance
mydata = te.getCalendarData(initDate='2023-02-06', endDate='2023-03-31', importance='2', output_type='df')

mydata = te.getCalendarData(initDate='2023-02-06', endDate='2023-03-31', importance='2', output_type='df')
print(mydata)
print("===============================================================================================================")

#!!!FREE ACCOUNTS CAN ACCESS ONLY MEXICO, NEW ZELAND, SWEDEN and THAILAND!!!
