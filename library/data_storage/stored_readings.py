# TODO write method for get number of readings
# TODO write list with a n variable to control how much is returned? or with a filter for times?
# get_next method?
import pandas as pd
from datetime import datetime
import numpy as np
import xlsxwriter
import sqlite3


class StoredReadings:
    def __init__(self):
        #empty dataframe
        self.df = pd.DataFrame(columns=['serial_no', 'timestamp', 'x', 'y', 'z'])
        self.i = 0
        self.fileNumber = 0

    def add_readings(self, serial_no, timestamp, x, y, z):
        self.df = self.df.append({'serial_no': serial_no, 'timestamp': datetime.now(), 'x': x, 'y': y, 'z': z}, ignore_index=True)
        self.save_all_data()

    def add_readings_withLoc(self, serial_no, timestamp, x, y, z):
        self.df.loc[self.df.shape[0]] = {'serial_no': serial_no, 'timestamp': datetime.now(), 'x': x, 'y': y, 'z': z}

    def get_number_of_readings(self):
        n = self.df.shape[0]
        # n = self.df.index.max()+1
        return n

    # TODO: get rid of console log (how to make a print for html?)
    def list_readings(self):
        return self.df

    def get_first_reading(self):
        sizeOfDataFrame = self.df.shape[0]
        if sizeOfDataFrame > 0:
            self.i = i = 0
            d = {'serial_no': self.df.serial_no[i], 'timestamp': self.df.timestamp[i], 'x': self.df.x[i],
                 'y': self.df.y[i], 'z': self.df.z[i]}

        else:
            d = {'serial_no': "None", 'timestamp': "None", 'x': 0, 'y': 0, 'z': 0}

        return d

    def get_next_reading(self):
        self.i = self.i + 1
        d = {
            'serial_no': self.df.serial_no[self.i],
            'timestamp': self.df.timestamp[self.i],
            'x': self.df.x[self.i],
            'y': self.df.y[self.i],
            'z': self.df.z[self.i]
        }
        return d

    def get_all_data_as_list(self):
        dataList = []
        one = self.get_first_reading()
        dataList.append(one)
        while True:
            try:
                nextReading = self.get_next_reading()
                dataList.append(nextReading)
            except Exception as ex:
                # print("We got an unexpected error {}.".format(ex))
                return dataList

    def get_readings_by_serial(self, serial):
        return self.df.query('serial_no == {}'.format(serial))

    def save_all_data(self):
        n = self.get_number_of_readings()
        if n >= 1000:
            self.fileNumber = self.fileNumber + 1
            filename = 'Saved Readings' + str(self.fileNumber) + '.xlsx'
            print('Saving the last 1000 readings to {}'.format(filename))
            writer = pd.ExcelWriter(filename, engine='xlsxwriter')

            self.df.to_excel(writer, sheet_name='accelData')
            writer.save()
            self.df = []
            self.df = pd.DataFrame(columns=['serial_no', 'timestamp', 'x', 'y', 'z'])

#     add a funtion to add readings to a database instead of saving locally
    def add_readings_to_db(self, serial_no, ts, x, y, z):
        conn = sqlite3.connect('data\\readings.db')
        cur = conn.cursor()
        sql_string = "INSERT INTO readings (x,y,z, serial_no, timestamp) VALUES ('{0}','{1}','{2}','{3}','{4}');".format(x, y, z, serial_no, ts)
        cur.execute(sql_string)
        conn.commit()
        conn.close()

    def get_number_readings_from_db(self):
        conn = sqlite3.connect('data\\readings.db')
        cur = conn.cursor()
        cur.execute("SELECT COUNT(*) FROM readings")
        result = cur.fetchall()
        conn.commit()
        conn.close()
        count = result[0][0]
        return count


if __name__ == '__main__':
    print("running Stored Readings")
