#!/usr/bin/python2.7
#-*- coding: utf-8 -*-

import pandas as pd
import matplotlib


file_csv = '/home/pi/Documents/work_hh_search/work_hhapi_php_2017-11-05.txt.csv'
reviews = pd.read_csv(file_csv, sep=';', encoding='utf-8')
print reviews.head()
#print reviews.shape
#print reviews.iloc[0:5,:] # the first 5 rows, and all of the columns for those rows
#print reviews.iloc[:,:] # the entire DataFrame
#print reviews.iloc[5:,5:] #  rows from position 5 onwards, and columns from position 5 onwards
#print reviews.iloc[5:,2:4] #  rows from position 5 onwards, and columns from position 5 onwards
#print reviews.iloc[:,0]  #  the first column, and all of the rows for the column
#print reviews.iloc[:,1]  #  the second column, and all of the rows for the column
#print reviews.iloc[9,:]
#print reviews.loc[0:5,:]
#print reviews.loc[:5,"vac_money_to"] # распечатать 5 строк, отображая только поле с названием vac_money_to
#print reviews.loc[:5, ["vac_money_to", "vac_name"]] # распечатать 5 строк, отображая только поле с названием vac_money_to  
#print reviews["vac_money_from"]
#print reviews[["vac_money_from", "vac_money_to"]]

# Remove first column
#reviews = reviews.iloc[:,1:]
#print reviews.head()


# SERIES
#s1 = type(reviews["vac_money_from"])
#print s1


#print reviews["vac_money_from"].head()
#print reviews["vac_money_from"].mean() # среднее значение для столбца vac_money_from
#print reviews.mean() # среднее значение по всем числовым столбцам
#print reviews.corr() # вычисляет как одно колелирует относительно другого
#print reviews["vac_money_from"] / 2 # можно посмотреть значения столбца, разделенные на 2

# boolean
#score_filter = reviews["vac_money_from"] > 70000
#print score_filter                  


#reviews["vac_money_from"].plot()
