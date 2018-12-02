# Mock Pi file
runningOnPi = False
if runningOnPi:
    import Adafruit_ADXL345
    accel = Adafruit_ADXL345.ADXL345()

import requests
import time
import datetime
import random
# this is from our built-in config module with YamlConfig class inside yml_config_from_url file
from config import yml_config_from_url as cfg

y = cfg.YamlConfig()

class DataPoster():

    def __init__(self):
        self._valid_servers = []
        self._invalid_servers = []
        # this gets the server list from Katie's github, it will work if Katie runs the server (list not accurate for everyone else)
        # TODO: edit my config.yml to work with my computer, add to github, change url below to point to mine
        self._server_list = y.yml_config_from_url("https://raw.githubusercontent.com/katiebrown0729/flask-pi-iot/master/pi_client/config/config.yml")

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
            cpuserial = "MEGAN000000000"

        return cpuserial

    def get_ServerList(self):
        return self._server_list

    def get_valid_servers(self, serverList):
        self._valid_servers = []
        self._invalid_servers = []
        sl = serverList
        for server in sl:
            getUrl = server + "/index.html"
            r = requests.get(getUrl)
            if r.status_code != 200:
                self._invalid_servers.append(server)
                # print('Added {} to INVALID server list' .format(server))
            else:
                self._valid_servers.append(server)
                # print('Added {} to VALID server list'.format(server))
        return(self._valid_servers)

    def accel_read(self):
        x = random.randrange(0, 10, 1)
        y = random.randrange(0, 10, 1)
        z = random.randrange(0, 10, 1)
        return (x, y, z)

    # def refind_valid_servers(self):
    #     self._valid_servers = []
    #     self.get_valid_servers()
    #     return(self._valid_servers)

    def post_to_valid_servers(self, aData):
        self.get_valid_servers(self.get_ServerList())
        n = 0
        for server in self._valid_servers:
            postUrl = server + "/test"
            r = requests.post(postUrl, data=aData)
            if r.status_code != 200:
                print("server: {} returned error code: {}".format(server, r.status_code))
            else:
                n = n + 1
                print('Successfully sent data to {}'.format(server))
        return n

    def update_active_server_cach(self):
        pass

    def get_accelerometer_data(self):
        if(runningOnPi):
            x, y, z = accel.read()
        else:
            x, y, z = self.accel_read()
        print('X={0}, Y={1}, Z={2}'.format(x, y, z))
        ts = datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')
        myserial = self.getserial()
        aData = {'serial-no': myserial, 'timestamp': ts, 'x': x, 'y': y, 'z': z}
        print(aData)
        return aData

if __name__ == '__main__':
    dP = DataPoster()
    oldtime = time.time()
    while True:
        dP.post_to_valid_servers(dP.get_accelerometer_data())
        newtime = time.time()
        if 60 >= newtime - oldtime:
           dP.get_valid_servers(dP.get_ServerList())
           oldtime = time.time()


