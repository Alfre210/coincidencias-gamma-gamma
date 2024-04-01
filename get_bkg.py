import numpy as np
import csv
from data_read import data_read
from rebinning import rebinning

def get_bkg():
    Stime = 1/np.sqrt(12)
    counts_bkg, time_bkg = data_read('./Data/Gamma data/Fondo.mca')
    spam, rb_counts_bkg = rebinning(counts_bkg)
    
    Srb_counts_bkg = np.sqrt(rb_counts_bkg)
    rb_rate_bkg = rb_counts_bkg/time_bkg
    Srb_rate_bkg = np.sqrt((Srb_counts_bkg**2)*((1/time_bkg)**2)+(Stime**2)*((rb_counts_bkg/(time_bkg**2))**2))
    

    return rb_rate_bkg, Srb_rate_bkg
    
