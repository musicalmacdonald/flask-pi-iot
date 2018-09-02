# Add a reading
# List readings
# Get readings for a given serial number
# Get readings for a given date/time range
#etc

import unittest
import datetime
import time
import random
from .stored_readings import StoredReadings


class TestStoredReadings(unittest.TestCase):
    def setUp(self):
        pass

    def test_add_readings(self):
        starttime=time.time()
        aSR = StoredReadings()

        # Create data to send
        for i in range(0, 1000):
            x = random.randint(0, 358)
            y = random.randint(0, 358)
            z = random.randint(0, 358)
            aSR.add_readings("46406064", datetime, x, y, z)

        n = aSR.get_number_of_readings()
        self.assertTrue(n == 1000)
        endtime=time.time()

        elapsedtime= endtime - starttime
        print("test time: {}".format(elapsedtime))

    def test_add_readings_withLoc(self):
        starttime=time.time()

        aSR = StoredReadings()

        # Create data to send
        for i in range(0, 1000):
            x = random.randint(0, 358)
            y = random.randint(0, 358)
            z = random.randint(0, 358)
            aSR.add_readings_withLoc("46406064", datetime, x, y, z)

        n = aSR.get_number_of_readings()
        print(n)
        self.assertTrue(n == 1000)

        endtime = time.time()
        elapsedtime = endtime - starttime
        print("Loc test time is: {}".format(elapsedtime))



if __name__ == '__main__':
    print("starting tests")
    unittest.main()
