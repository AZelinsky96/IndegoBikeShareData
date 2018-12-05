#!/home/zeski/anaconda3/bin/python


import re
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime as dt
import os
import time
import numpy as np
#%matplotlib inline
#print('\n\nPlease make sure that your files are combined together by year and in the following format:  Year.csv such as 2018.csv')
#prop = input('Is your file in proper format? Enter yes or no: ')

#if ('y' or 'Y') in prop:
#    print('Great, continuing!\n')
#else:
#    print('Please make sure the files are in proper format.')
#    exit()

#path1 = input('Please enter the path to the files you wish to process: ')
#if len(path1) > 1:
#    print('')
#else:
#    print('Please enter the correct path')
#os.chdir('/home/zeski/Documents/Data_Science/Intro_To_Data_Science_And_Analytics/Indego/Data/DataBody/FinalData')
#os.chdir(path1)
path1 = os.getcwd()
if (os.path.isdir(path1+'/plot') == True):
    pass
else:
    os.mkdir('plot')
print('\n')

file = input('Please input the file you would like to process:  ')
chunksize = 8000
parse_dates = ['start_time', 'end_time']
print('Processing the data file....this may take up to a minute or two!')

textfilereader = pd.read_csv(file, chunksize = chunksize, parse_dates= parse_dates)
  
df5 = pd.concat(textfilereader, ignore_index=True)
n = re.findall('[0-9][0-9][0-9][0-9]', file)

df5_nan = df5[df5.isnull().values]
df5.dropna(inplace = True)
df5['length_of_trip'] = df5['end_time']-df5['start_time']


## Setting the date as the index

df5['Date'] = df5['start_time'].dt.date
df5.set_index('Date', inplace = True)
df5= df5[['trip_id','duration','bike_id','trip_route_category','passholder_type','length_of_trip']]


df=df5.copy()
df.reset_index(inplace=True)
df['Month'] = pd.to_datetime(df['Date'], format= '%Y-%m-%d').apply(lambda x: x.strftime('%Y-%m'))
df['DATE'] = df['Date']
df.set_index('Date',inplace = True)

dfM = df.groupby([df.Month, 'passholder_type'])['trip_id'].count()
dfM = pd.DataFrame(dfM)
dfM.reset_index(inplace=True)
dfM.set_index('passholder_type', inplace = True)
dfM['Month'] = dfM.astype('str')
dfM['Month'] = dfM.Month.str.replace('-','_')

Ind30M             = dfM.loc['Indego30',:]
Ind30M.columns     = ['Month','30']
IndFlexM           = dfM.loc['IndegoFlex',:]
IndFlexM.columns   = ['Month','Flex']
WalkupM            = dfM.loc['Walk-up',:]
WalkupM.columns    = ['Month', 'Walkup']

#Creating a list for the x ticks:
xticks = ['01_'+str(n[0]),'02_'+str(n[0]),'03_'+str(n[0]),'04_'+str(n[0]),'05_'+str(n[0]),'06_'+str(n[0]),'07_'+str(n[0]),'08_'+str(n[0]),'09_'+str(n[0]),'10_'+str(n[0]),'11_'+str(n[0]),'12_'+str(n[0])]

if 'Indego365' in dfM.index:
    Ind365M        = dfM.loc['Indego365',:]
    Ind365M.columns= ['Month','365']
    plt.figure(figsize = (12,8))
    plt.plot(Ind30M['Month'], Ind30M['30'],c='b', alpha = 0.35, linestyle='-', marker = 'o')
    plt.plot(IndFlexM['Month'],IndFlexM['Flex'],c='g', alpha = 0.35,linestyle='-', marker = 'o')
    plt.plot(WalkupM['Month'], WalkupM['Walkup'],c='r', alpha = 0.35, linestyle ='-', marker ='o')
    plt.plot(Ind365M['Month'], Ind365M['365'],c='c', alpha = 0.35, linestyle='-', marker = 'o')
    plt.xticks(rotation= 90)
    plt.title('Number of trips by all User types for '+str(n[0]))
    plt.xlabel('Month and year')
    plt.ylabel('# of trips')  
    plt.legend()
    plt.tight_layout()
    plt.savefig('Combined'+str(n[0])+'.png')
    plt.savefig('zCombined.png')
   # plt.show()
    #plt.clf()
    
    plt.figure(figsize = (12,8))
    x= []
    y= []

    for a,b in Ind30M.itertuples(index = False):
        num=re.findall('[0-9][0-9][0-9][0-9]_[0-9][0-9]', a)
    #print(num)
        x.append(a)
        y.append(b)
        plt.plot(x,y, marker ='o', c='b',markersize = 10, linestyle='-' )
        plt.xticks(np.arange(12),Ind30M['Month'],rotation = 90)
        plt.ylim((0,max(Ind30M['30']+5000)))
        plt.title('Amount of Trips by Indego 30 members each month for '+str(n[0]))
        plt.ylabel('# of trips')
        plt.xlabel('Month and year')
    #plt.show()
        plt.savefig('Ind30M'+str(num[0])+'.png')
    #plt.show()
    #plt.clf()
    
    plt.figure(figsize=(12,8))
    x= []
    y= []
    for a,b in IndFlexM.itertuples(index = False):
        num=re.findall('[0-9][0-9][0-9][0-9]_[0-9][0-9]', a)
    #print(num)
        x.append(a)
        y.append(b)
        plt.plot(x,y, marker ='o', c='g',markersize = 10, linestyle = '-')
        plt.xticks(np.arange(12),IndFlexM['Month'],rotation = 90)
        plt.ylim((0,max(IndFlexM['Flex']+500)))
        plt.title('Amount of Trips by Indego Flex Members each month for '+str(n[0]))
        plt.ylabel('# of trips')
        plt.xlabel('Month and year')
    #plt.show()
    #time.sleep(0.5)
        plt.savefig('IndFlexM'+str(num[0])+'.png')
    #plt.show()
   # plt.clf()
    
    
    plt.figure(figsize = (12,8))
    x= []
    y= []
    for a,b in WalkupM.itertuples(index = False):
        num=re.findall('[0-9][0-9][0-9][0-9]_[0-9][0-9]', a)
        #print(num)
        x.append(a)
        y.append(b)
        plt.plot(x,y, marker ='o', c='r',markersize = 10, linestyle = '-')
        plt.xticks(np.arange(12),WalkupM['Month'],rotation = 90)
        plt.ylim((0,max(WalkupM['Walkup']+1000)))
        plt.title('Amount of Trips by Walkups each month for '+str(n[0]))
        plt.ylabel('# of trips')
        plt.xlabel('Month and year')
    #plt.show()
    #time.sleep(0.5)
        plt.savefig('WalkupM'+str(num[0])+'.png')
    #plt.show()
    #plt.clf()
    
    #Indego
    plt.figure(figsize = (12,8))
    x= []
    y= []
    for a,b in Ind365M.itertuples(index = False):
        num=re.findall('[0-9][0-9][0-9][0-9]_[0-9][0-9]', a)
    #print(num)
        x.append(a)
        y.append(b)
        plt.plot(x,y, marker ='o', c='c',markersize = 10, linestyle='-')
        plt.xticks(np.arange(12),Ind365M['Month'],rotation = 90)
        plt.ylim((0,max(Ind365M['365'])+1000))
        plt.title('Amount of Trips by Indego 365 members each month for '+str(n[0]))
        plt.ylabel('# of trips')
        plt.xlabel('Month and year')
    #plt.show()
    #time.sleep(0.5)
        plt.savefig('Ind365M'+str(num[0])+'.png')
    #plt.show()
    #plt.clf()
    os.chdir(path1+'/plot')

    if (os.path.isdir(path1+'/plot/CombinedPlots') == True):
        pass    
    else:
        os.mkdir('Outputcsvs')
        os.mkdir('CombinedPlots')
    
    os.chdir(path1+'/plot/Outputcsvs')
    Ind30M.to_csv('Ind30M'+str(n[0])+'.csv')
    IndFlexM.to_csv('IndFlexM'+str(n[0])+'.csv')
    WalkupM.to_csv('WalkupM'+str(n[0])+'.csv')
    Ind365M.to_csv('Ind365M'+str(n[0])+'.csv')
    os.chdir(path1)

else:
    plt.figure(figsize = (12,8))
    plt.plot(Ind30M['Month'], Ind30M['30'], alpha = 0.35, linestyle='-', marker = 'o')
    plt.plot(IndFlexM['Month'],IndFlexM['Flex'], alpha = 0.35,linestyle='-', marker = 'o')
    plt.plot(WalkupM['Month'], WalkupM['Walkup'], alpha = 0.35, linestyle ='-', marker = 'o')
    plt.xticks(rotation= 90)
    plt.title('Number of trips by all User types for '+str(n[0]))
    plt.xlabel('Month and year')
    plt.ylabel('# of trips') 
    plt.legend()
    plt.tight_layout()
    plt.savefig('zCombined.png')
    plt.savefig('Combined'+str(n[0])+'.png')
    #plt.show()
    #plt.clf()
    
    plt.figure(figsize = (12,8))
    x= []
    y= []

    for a,b in Ind30M.itertuples(index = False):
        num=re.findall('[0-9][0-9][0-9][0-9]_[0-9][0-9]', a)
    #print(num)
        x.append(a)
        y.append(b)
        plt.plot(x,y, marker ='o', c='b', markersize= 10, linestyle='-')
        plt.xticks(np.arange(12),Ind30M['Month'],rotation = 90)
        plt.ylim((0,max(Ind30M['30']+5000)))
        plt.title('Amount of Trips by Indego 30 members each month for '+str(n[0]))
        plt.ylabel('# of trips')
        plt.xlabel('Month and year')
    #plt.show()
        plt.savefig('Ind30M'+str(num[0])+'.png')
    #plt.show()
    #plt.clf()
    
    
    plt.figure(figsize = (12,8))
    x= []
    y= []
    for a,b in IndFlexM.itertuples(index = False):
        num=re.findall('[0-9][0-9][0-9][0-9]_[0-9][0-9]', a)
    #print(num)
        x.append(a)
        y.append(b)
        plt.plot(x,y, marker ='o', c='g', markersize = 10, linestyle ='-')
        plt.xticks(np.arange(12),IndFlexM['Month'],rotation = 90)
        plt.ylim((0,max(IndFlexM['Flex']+500)))
        plt.title('Amount of Trips by Indego Flex Members each month for '+str(n[0]))
        plt.ylabel('# of trips')
        plt.xlabel('Month and year')
    #plt.show()
    #time.sleep(0.5)
        plt.savefig('IndFlexM'+str(num[0])+'.png')
    #plt.show()
    #plt.clf()
    
    plt.figure(figsize = (12,8))
    x= []
    y= []
    for a,b in WalkupM.itertuples(index = False):
        num=re.findall('[0-9][0-9][0-9][0-9]_[0-9][0-9]', a)
        #print(num)
        x.append(a)
        y.append(b)
        plt.plot(x,y, marker ='o', c='r',markersize = 10, linestyle='-')
        plt.xticks(np.arange(12),WalkupM['Month'],rotation = 90)
        plt.ylim((0,max(WalkupM['Walkup']+1000)))
        plt.title('Amount of Trips by Walkups each month for '+str(n[0]))
        plt.ylabel('# of trips')
        plt.xlabel('Month and year')
    #plt.show()
    #time.sleep(0.5)
        plt.savefig('WalkupM'+str(num[0])+'.png')
    #plt.show()
    #plt.clf()
	

    os.chdir(path1+'/plot')

    if (os.path.isdir(path1+'/plot/CombinedPlots') == True):
        pass    
    else:
        os.mkdir('Outputcsvs')
        os.mkdir('CombinedPlots')
    os.chdir(path1+'/plot/Outputcsvs')
    Ind30M.to_csv('Ind30M'+str(n[0])+'.csv')
    IndFlexM.to_csv('IndFlexM'+str(n[0])+'.csv')
    WalkupM.to_csv('WalkupM'+str(n[0])+'.csv')
    os.chdir(path1)
print('\nI have created several sub directories.\nA directory called plot, a directory called combined and a directory call OutputCsvs.\nThe plot folder will contain the animated file for your selected year.\nThe Combined directory contains the still image for all user types for your selected year.\nThe Outputcsvs directory contains all of the csv files used to create the plots for your selected year.\n') 
print('Thank you and all done processing! Please wait for the images to generate!\n')
time.sleep(3)





