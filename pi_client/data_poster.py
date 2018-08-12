# Import the ADXL345 module.
import Adafruit_ADXL345
import requests
import time
import datetime
from pi_client.config import yml_config_from_url as cfg

y = cfg.YamlConfig()

accel = Adafruit_ADXL345.ADXL345()

class DataPoster():

    def __init__(self):
        self._valid_servers = []
        self._invalid_servers = []
        self._server_list = y.yml_cofig_from_url(
            "https://raw.githubusercontent.com/musicalmacdonald/flask-pi-iot/master/pi_client/config/config.yml")

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

    def get_valid_servers(self, serverList):
        self._valid_servers = []
        self._invalid_servers = []
        sl = serverList
        for server in sl:
            r = requests.get(server)
            if r.status_code != 200:
                self._invalid_servers.append(server)
                # print('Added {} to INVALID server list' .format(server))
            else:
                self._valid_servers.append(server)
                # print('Added {} to VALID server list'.format(server))
        return (self._valid_servers)

    def post_to_valid_servers(self, aData):
        self.get_valid_servers(self.get_ServerList())
        n = 0
        for server in self._valid_servers:
            r = requests.post(server, data=aData)
            if r.status_code != 200:
                print("server: {} returned error code: {}".format(server, r.status_code))
            else:
                n = n + 1
        return n

    def get_accelerometer_data(self):
        x, y, z = accel.read()
        print('X={0}, Y={1}, Z={2}'.format(x, y, z))
        ts = datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')
        myserial = self.getserial()
        aData = {'serial-number': myserial, 'timestamp': ts, 'x': x, 'y': y, 'z': z}
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
