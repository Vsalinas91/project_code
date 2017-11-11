import numpy as np

def wind_speed(u, v, w):
    '''
    Calculates wind speed from u, v and w componants.
    '''
    w = 0.
    wind = np.sqrt(u*u + v*v + w*w)
    return(wind)

#print(wind_speed(10,-23,2))

def get_wind_direction(u,v):
    return (90. - np.atan2(u,v))
