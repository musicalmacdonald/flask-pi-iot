import yaml
import requests


class YamlConfig():
    def __init__(self):
        pass

    def yml_config_from_url(self, url):
        response = requests.get(url)
        if response.status_code == 200:
            config = yaml.load(response.text)
            for key in config:
                newConfigDitionary = config[key]
            for key in newConfigDitionary:


        return newConfigDitionary


if __name__ == '__main__':
    aYC = YamlConfig()
    aYC.yml_config_from_url("https://raw.githubusercontent.com/musicalmacdonald/flask-pi-iot/master/pi_client/config/config.yml")