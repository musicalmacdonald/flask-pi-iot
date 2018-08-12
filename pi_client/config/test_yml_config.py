#Test the yaml config

import unittest
from pi_client.config import yml_config_from_url as y


class test_yaml_cofig(unittest.TestCase):

    def setUp(self):
        return

    def test_yml_config_from_url(self):

        url = 'https://raw.githubusercontent.com/musicalmacdonald/flask-pi-iot/master/pi_client/config/config.yml'
        y2 = y.YamlConfig()
        result = y2.yml_config_from_url(url)
        # print(result)
        self.assertTrue(len(result) != 0)




#
# mysql:
#     host: localhost
#     user: root
#     passwd: my secret password
#     db: write-math

if __name__ == '__main__':
    unittest.main()