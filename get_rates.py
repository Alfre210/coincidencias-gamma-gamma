import numpy as np
import csv
from data_read import data_read
from rebinning import rebinning

def get_rates(file_name,):
    Stime = 1/np.sqrt(12)
    counts, time = data_read(file_name)
    rb_ch, rb_counts = rebinning(counts)
    
    Srb_counts = np.sqrt(rb_counts)
    rb_rate= rb_counts/time
    Srb_rate = np.sqrt((Srb_counts**2)*((1/time)**2)+(Stime**2)*((rb_counts/(time**2))**2))
    
    
    return rb_ch, rb_rate, Srb_rate
    