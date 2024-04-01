import numpy as np
import matplotlib.pyplot as plt
import scipy
from scipy.optimize import curve_fit, differential_evolution, Bounds, minimize

def xi2(x,y,sy,func,param):
    N = len(y)
    m = len(param)
    return (1/(N-m))*sum((y-func(x,*param))**2/(sy**2))




def fit(x,y,sy,func,init_param):
    def opt_func(param):
        return xi2(x,y,sy,func,param)
    # bound = [(-100000,100000) for i in range(len(init_param))]
    # result = differential_evolution(opt_func, bounds = bound, x0 = init_param, strategy='best1bin', maxiter=15000, popsize=4*len(init_param), tol=1e-12, disp = True)
    # result = minimize(opt_func, init_param, method='SLSQP', tol=1e-12)
    popt, pcov = curve_fit(func,x,y,sigma=sy, p0=init_param, method = 'dogbox')
    return popt, opt_func(popt), pcov
    