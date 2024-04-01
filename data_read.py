import csv
import numpy as np

def data_read(file_name):
    data_raw = []
    NCh = 8192
    live_time = None
    with open(file_name, newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        for row in spamreader:
            for item in row:
                if item == 'LIVE_TIME':
                    live_time = int(row[2])
            data_raw.append(', '.join(row))
    data = []
    for i in range(data_raw.index('<<DATA>>')+1,data_raw.index('<<DATA>>')+NCh+1):     
        data.append(int(data_raw[i]))
    return np.array(data), live_time
    