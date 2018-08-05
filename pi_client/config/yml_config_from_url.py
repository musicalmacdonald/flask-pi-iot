import yaml
import requests

class YamlConfig:
    def yml_config_from_url(self, url):
        response = requests.get(url)
        if response.status_code == 200:
            config = yaml.load(response.text)

        return config


if __name__ == '__main__':
    aYC = YAMLConfig()
    aYC.yml_config_from_url(url heere)