# Import the ADXL345 module.
import Adafruit_ADXL345
import requests
import time
import datetime

accel = Adafruit_ADXL345.ADXL345()


def getserial():
    # Extract serial from cpuinfo file
    cpuserial = "0000000000000000"
    try:
        f = open('/proc/cpuinfo', 'r')
        for line in f:
            if line[0:6] == 'Serial':
                cpuserial = line[10:26]
        f.close()
    except:
        cpuserial = "ERROR000000000"

    return cpuserial


while True:
    x,y,z=accel.read()
    print('X={0}, Y={1}, Z={2}'.format(x, y, z))
    ts=datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')
    myserial = getserial()
    aData={'serial-number': myserial, 'timestamp': ts,  'x': x, 'y': y, 'z': z}
    print(aData)
    r=requests.post('http://megan-pi-iot.cfapps.io/test',data=aData)