import yaml
import requests


class YamlConfig():
    def __init__(self):
        pass

    def yml_config_from_url(self, url):
        response = requests.get(url)
        if response.status_code == 200:
            config = yaml.load(response.text)
            l = config['servers']
            print(l)
            for key in config:
                key = config[key]
            print(newConfigDitionary)
        # >> > yaml.load("""
        # ... none: [~, null]
        # ... bool: [true, false, on, off]
        # ... int: 42
        # ... float: 3.14159
        # ... list: [LITE, RES_ACID, SUS_DEXT]
        # ... dict: {hp: 13, sp: 5}
        # ... """)


        return newConfigDitionary


if __name__ == '__main__':
    aYC = YamlConfig()
    aYC.yml_config_from_url("https://raw.githubusercontent.com/musicalmacdonald/flask-pi-iot/master/pi_client/config/config.yml")