import pandas as pd
import random as ran

def isNaN(num):
    return num != num

def importLog():
    #data_file = 'input-logs/Hospital Billing - Event Log.csv'
    #data_file = 'input-logs/Road_Traffic_Fine_Management_Process.csv'
    #data_file = 'input-logs/Sepsis Cases - Event Log.csv'
    data_file = 'input-logs/BPI_Challenge_2013_closed_problems.csv'
    data = pd.read_csv(data_file, sep=';')
    data2 = data.groupby('Case ID')['Activity'].apply(list).apply(pd.Series).reset_index()
    print('Number of cases in raw log: ', len(data2))
    data2.drop('Case ID', axis=1, inplace=True)
    data2.drop_duplicates(keep='first', inplace=True)
    data2.to_csv('input-logs/log_without_duplicates.csv')
    list1 = data2.values.tolist()
    list2 = []
    for line in list1:
        list2_partial = []
        for col in line:
            if not isNaN(col):
                list2_partial.append(col)
        list2.append(list2_partial)
    list3 = []
    for line in list2:
        list3_partial = []
        list3_partial.append(line[0])
        if (len(line) > 1):
            list3_partial.append(line[1])
        for col in range(2, len(line)):
            if (line[col] != line[col - 1]) or (line[col] != line[col - 2]):
                list3_partial.append(line[col])
        list3.append(list3_partial)
    list4 = []
    for num in list3:
        if num not in list4:
            list4.append(num)
    log = list4
    print('Number of cases in pre-processed log: ', len(list4))
    return log

def sampleLog(sampledLog, fullLog):
    sublogsize = 10
    iter = len(fullLog)
    if iter > sublogsize:
        iter = sublogsize
    for i in range(iter):
        pos = ran.randrange(0, len(fullLog))
        sampledLog.append(fullLog[pos])
        fullLog.pop(pos)
    return (sampledLog, fullLog)