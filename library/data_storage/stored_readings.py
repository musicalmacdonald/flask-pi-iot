# TODO write method for get number of readings

import pandas as pd
import numpy as np


class StoredReadings():
    def __init__(self):
        #empty dataframe
        self.df = pd.DataFrame(columns=['serial-no','timestamp', 'x', 'y', 'z'])

    def add_readings(self, serial_no, timestamp, x, y, z):
        self.df = self.df.append({'serial-no': serial_no, 'timestamp' :timestamp, 'x': x, 'y':y, 'z':z}, ignore_index=True)

    def add_readings_withLoc(self, serial_no, timestamp, x, y, z):
        self.df.loc[self.df.shape[0]] = {'serial-no': serial_no, 'timestamp': timestamp, 'x': x, 'y': y, 'z': z}

    def get_number_of_readings(self):
        n = self.df.shape[0]
        return n


if __name__ == '__main__':
    print("running Stored Readings")
