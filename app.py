from flask import Flask, render_template, request, jsonify
from database import *

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/patients')
def patients():
    patients = get_all_patients()
    return render_template('patients.html', patients=patients)

@app.route('/add_patient', methods=['POST'])
def add_patient():
    name = request.form['name']
    age = request.form['age']
    gender = request.form['gender']
    add_new_patient(name, age, gender)
    return jsonify({'message': 'Patient added successfully'})

if __name__ == '__main__':
    app.run(debug=True)
