# TODO write method for get number of readings

import pandas as pd
import numpy as np

class StoredReadings():
    def __init__(self):
        #empty dataframe
        df = pd.DataFrame(columns=['serial-no','timestamp', 'x', 'y', 'z'])


    def add_readings(self, serial_no, timestamp, x, y, z):
        self.df.append({'serial-no': serial_no,'timestamp':timestamp, 'x': x, 'y':y, 'z':z}, ignore_index=True)