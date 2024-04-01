import numpy as np

def ch_to_ener(ch,detector):
    if detector == 1:
        A = 0.3964
        sA = 0.0033
        B = -33.7
        sB = 5.9
    elif detector == 2:
        A = 0.3974
        sA = 0.0021
        B = -25.7
        sB = 3.5
    else:
        print('Error')
    sch = 1/((12)**(1/2))
    E = A*ch + B
    sE = np.sqrt(sch**2 * A**2 + sA**2 * ch**2 + sB**2)
    return E, sE

    
    