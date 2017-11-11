import numpy as np

def wind_speed(u, v, w):
    '''
    Calculates wind speed from u, v and w componants.
    '''
    return np.sqrt(u*u + v*v + w*w)

print(wind_speed(10,-23,2))

