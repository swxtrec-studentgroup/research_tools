
def orb_avg(den_in, lat_in, time_in):
    """
    This function takes density, latitude, longitude, and time
    as input and returns the orbit averaged density and time.

    This function may only work for satellites in a polar orbit.

    The time needs to be in pandas datetime format
    """

    import numpy as np
    import pandas as pd

    lat = np.asarray(lat_in)
    time_pd = pd.to_datetime(time_in)
    den = den_in

    i = np.nonzero(lat[1:] * lat[0:-1] < np.logical_and(0, lat[1:] > lat[0:-1]))
    i = i[0]
    d_avg = np.zeros(np.size(i))
    height_avg = np.zeros(np.size(i))
    time_avg = []

    for j in range(np.size(i) - 1):
        #     print(j+1)
        d_avg[j] = np.mean(den[i[j]: i[j + 1] - 1])
        height_avg[j] = np.mean(den[i[j]: i[j + 1] - 1])
        mean_time = time_pd[i[j]: i[j + 1] - 1].mean()
        time_avg.append(mean_time)


    return(time_avg, d_avg)

