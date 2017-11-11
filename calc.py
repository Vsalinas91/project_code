import numpy as np

def wind_speed(u,v):
    '''
    Calculates wind speed from u and v componants.
    '''
    return np.sqrt(u*u + v*v)

print(wind_speed(10,-23))

