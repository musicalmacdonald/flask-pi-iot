# Add a reading
# List readings
# Get readings for a given serial number
# Get readings for a given date/time range
#etc

import unittest
import datetime
import time
import random
from pathlib import Path
from .stored_readings import StoredReadings


class TestStoredReadings(unittest.TestCase):
    def setUp(self):
        pass

    def test_add_readings(self):
        starttime=time.time()
        aSR = StoredReadings()

        # Create data to send
        for i in range(0, 3):
            x = random.randint(0, 358)
            y = random.randint(0, 358)
            z = random.randint(0, 358)
            aSR.add_readings("46406064", datetime, x, y, z)

        n = aSR.get_number_of_readings()
        self.assertTrue(n == 3)
        endtime=time.time()

        elapsedtime= endtime - starttime
        print("test time: {}".format(elapsedtime))

    def test_add_readings_withLoc(self):
        starttime=time.time()

        aSR = StoredReadings()

        # Create data to send
        for i in range(0, 3):
            x = random.randint(0, 358)
            y = random.randint(0, 358)
            z = random.randint(0, 358)
            date = datetime.datetime
            aSR.add_readings_withLoc("46406064", 'date', x, y, z)

        n = aSR.get_number_of_readings()
        print(n)
        self.assertTrue(n == 3)

        endtime = time.time()
        elapsedtime = endtime - starttime
        print("Loc test time is: {}".format(elapsedtime))

    def test_list_readings(self):

        aSR = StoredReadings()

        # Create data to send
        for i in range(0, 3):
            x = random.randint(0, 358)
            y = random.randint(0, 358)
            z = random.randint(0, 358)
            date = datetime.datetime
            aSR.add_readings("46406064", 'date', x, y, z)

        print(aSR.list_readings())

    def test_get_first_reading(self):
        aSR = StoredReadings()
        serialNo = ['MEGAN0000000', 'SHANE0000000', 250]

        for i in range(0, 3):
            x = random.randint(0, 358)
            y = random.randint(0, 358)
            z = random.randint(0, 358)
            serialNumber = serialNo[i]
            date = datetime.datetime
            aSR.add_readings(serialNumber, 'date', x, y, z)

        fr = aSR.get_first_reading()

        self.assertTrue(type(fr) == dict)
        self.assertTrue(len(fr) == 5)
        self.assertTrue(fr['serial_no'] == 'MEGAN0000000')

    def test_get_next_reading(self):
        print("Start Get Next Reading Test")
        aSR = StoredReadings()
        serialNo = ['MEGAN0000000', 'SHANE0000000', 250]

        for i in range(0, 3):
            x = random.randint(0, 358)
            y = random.randint(0, 358)
            z = random.randint(0, 358)
            serialNumber = serialNo[i]
            date = datetime.datetime
            aSR.add_readings(serialNumber, 'date', x, y, z)

        nr = aSR.get_next_reading()

        self.assertTrue(type(nr) == dict)
        self.assertTrue(len(nr) == 5)
        self.assertTrue(nr['serial_no'] == 'SHANE0000000')

    def test_get_all_data_as_list(self):
        print("Starting get all data as list test")
        aSR = StoredReadings()
        serialNo = ['MEGAN0000000', 'SHANE0000000', 250]
        for i in range(0, 3):
            x = random.randint(0, 358)
            y = random.randint(0, 358)
            z = random.randint(0, 358)
            serialNumber = serialNo[i]
            aSR.add_readings(serialNumber, datetime.datetime.now(), x, y, z)

        dataList = aSR.get_all_data_as_list()
        n = aSR.get_number_of_readings()

        self.assertTrue(type(dataList) == list)
        self.assertTrue(len(dataList) == n)

    def test_save_all_data(self):
        print("Starting save all data test")
        aSR = StoredReadings()
        serialNo = ['MEGAN0000000', 'SHANE0000000', 250]
        for i in range(0, 1001):
            x = random.randint(0, 358)
            y = random.randint(0, 358)
            z = random.randint(0, 358)
            serialNumber = serialNo[0]
            aSR.add_readings(serialNumber, datetime.datetime.now(), x, y, z)

        aSR.save_all_data()
        my_file = Path('./Saved Readings1.xlsx')

        self.assertTrue(my_file.exists())


    # def test_get_readings_by_serial(self):
    #
    #     aSR = StoredReadings()
    #     serialNo=['MEGAN0000000', 'SHANE0000000', 250]
    #
    #     for i in range(0, 3):
    #         x = random.randint(0, 358)
    #         y = random.randint(0, 358)
    #         z = random.randint(0, 358)
    #         serialNumber = serialNo[i]
    #         date = datetime.datetime
    #         aSR.add_readings(serialNumber, 'date', x, y, z)
    #
    #     print(aSR.list_readings())
    #     serialList = aSR.get_readings_by_serial('250')
    #     print(serialList)
    #     print(len(serialList))
    #     #n = serialList.get_number_of_readings()
    #     print('n is: {}'.format(n))
    #     self.assertTrue(n == 1)








if __name__ == '__main__':
    print("starting tests")
    unittest.main()
