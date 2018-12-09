from flask import Flask
from flask import render_template
from flask import request
from flask import jsonify
import requests
from library.data_storage import stored_readings as sR

app = Flask(__name__)

dataStore = sR.StoredReadings()

# TODO: check that the methods on dataStore match up with StoredReadings


@app.route('/test', methods=['POST', 'GET'])
def my_test():
    if request.method == "POST":
        print("/test")
        print("This is what is in the request object: ")
        print(request)
        print("Here's what's in the request.form:  ")
        print(request.form)
        d = request.form
        dataStore.add_readings(d["serial_no"], d["timestamp"], d["x"], d["y"], d["z"])
        print(dataStore.get_number_of_readings())
        print("Data Added")
        return "Data added"
    return "Test page"


@app.route('/yaml')
def my_yaml_microservice():
    pass
    #return ymlify({'Hello':'World'})


@app.route('/')
@app.route('/index.html')
def main_page():
    print("rendering index.html")
    return render_template('index.html')


@app.route('/alldata.html',methods=['POST', 'GET'])
def alldata_page():
    if request.method == 'POST':
        pass
    print("All Data got a GET")
    print(request.form)
    d = dataStore.get_all_data_as_list()
    print(d)
    return render_template('alldata.html', data=d)


@app.route('/johnpi.html', methods=['POST', 'GET'])
def john_page():
    if request.method == 'POST':
        print("JohnPi got a post")
        print(request.form)
    return render_template('johnpi.html')


@app.route('/meganpi.html', methods=['POST', 'GET'])
def megan_page():
    if request.method == 'POST':
        print("MeganPi got a post")
        print(request.form)
    return render_template('meganpi.html')


@app.route('/katiepi.html', methods=['POST', 'GET'])
def katie_page():
    if request.method == 'POST':
        print("KatiePi got a post")
        print(request.form)
    return render_template('katiepi.html')


@app.route('/davidpi.html', methods=['POST', 'GET'])
def david_page():
    if request.method == 'POST':
        print("DavidPi got a post")
        print(request.form)
    return render_template('davidpi.html')


@app.route('/shanepi.html', methods=['POST', 'GET'])
def shane_page():
    if request.method == 'POST':
        print("ShanePi got a post")
        print(request.form)
    return render_template('shanepi.html')



