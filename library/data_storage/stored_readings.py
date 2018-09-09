# TODO write method for get number of readings
# TODO write list with a n variable to control how much is returned? or with a filter for times?
# get_next method?
import pandas as pd
from datetime import datetime
import numpy as np


class StoredReadings:
    def __init__(self):
        #empty dataframe
        self.df = pd.DataFrame(columns=['serial_no', 'timestamp', 'x', 'y', 'z'])

    def add_readings(self, serial_no, timestamp, x, y, z):
        self.df = self.df.append({'serial_no': serial_no, 'timestamp': datetime.now(), 'x': x, 'y': y, 'z': z}, ignore_index=True)

    def add_readings_withLoc(self, serial_no, timestamp, x, y, z):
        self.df.loc[self.df.shape[0]] = {'serial_no': serial_no, 'timestamp': datetime.now(), 'x': x, 'y': y, 'z': z}

    def get_number_of_readings(self):
        #n = self.df.shape[0]
        n = self.df.index.max()+1
        return n

    def list_readings(self):
        return self.df

    def get_first_reading(self):
        i = 0
        d = {'serial_no': self.df.serial_no[i], 'timestamp': self.df.timestamp[i], 'x': self.df.x[i], 'y': self.df.y[i], 'z': self.df.z[i]}
        return d

    def get_readings_by_serial(self, serial):
        return self.df.query('serial_no == {}'.format(serial))




if __name__ == '__main__':
    print("running Stored Readings")
