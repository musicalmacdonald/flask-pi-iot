echo removing all the .py files
rm *.py
echo *** getting lastest from master ****
echo pi_accelerometer_IOT_client_test.py
curl -OL https://raw.githubusercontent.com/musicalmacdonald/flask-pi-iot/master/pi_client/accelerometer_post_test.py > accelerometer_post_test.py
echo pi_accelerometer_IOT_client.py
curl -OL https://raw.githubusercontent.com/musicalmacdonald/flask-pi-iot/master/pi_client/accelerometer_post.py > accelerometer_post.py
echo *** running test ***
python accelerometer_post_test.py -v

