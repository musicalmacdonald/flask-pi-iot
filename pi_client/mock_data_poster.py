# Mock Pi file

import requests
import time
import datetime
import random



class DataPoster():

    def __init__(self):
        self._valid_servers = []
        self._invalid_servers = []
        self._server_list = ['http://megan-pi-iot.cfapps.io/index.html',
                     'http://katie-pi-iot.cfapps.io/index.html',
                    'http://david-pi-iot.cfapps.io/index.html',
                    'http://jpf-flask-pi-iot.cfapps.io/index.html',
                    'http://shane-pi-iot.cfapps.io/index.html']

    def getserial(self):
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

    def get_ServerList(self):
        return self._server_list

    def get_valid_servers(self):
        sl = self.get_ServerList()
        for server in sl:
            r = requests.get(server)
            if r.status_code != 200:
                self._invalid_servers.append(server)
                print('Added {} to INVALID server list' .format(server))
            else:
                self._valid_servers.append(server)
                print('Added {} to VALID server list'.format(server))
        return(self._valid_servers)

    def accel_read(self):
        x = random.randrange(0, 10, 1)
        y = random.randrange(0, 10, 1)
        z = random.randrange(0, 10, 1)
        return (x, y, z)

if __name__ == '__main__':
    dP = DataPoster()
    while True:
        x,y,z=dP.accel_read()
        print('X={0}, Y={1}, Z={2}'.format(x, y, z))
        ts=datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')
        myserial = dP.getserial()
        aData={'serial-number': myserial, 'timestamp': ts,  'x': x, 'y': y, 'z': z}
        print(aData)
        r=requests.post('http://megan-pi-iot.cfapps.io/test',data=aData)