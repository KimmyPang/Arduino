import serial
import time
import mysql.connector
from flask import Flask, render_template, request

app = Flask(__name__)

conn = mysql.connector.connect(
  host="localhost",
  user="pi",
  password="kimmy",
  database="assignment_db"
)

serialcom = serial.Serial('/dev/ttyACM0', 9600, timeout=1)

def pumpMax():
    serialcom.write(str('MAX').encode())

def pumpMin():
    serialcom.write(str('MIN').encode()) 

def pumpOff():
    serialcom.write(str('OFF').encode())

@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if 'MAX' in request.form:
            pumpMax()
        if 'MIN' in request.form:
            pumpMin()
        if 'OFF' in request.form:
            pumpOff()

    return render_template('index.html')

@app.route('/data')
def get_data():
    cur = conn.cursor()
    cur.execute('SELECT * FROM pressureRecord')
    data = cur.fetchall()
    return render_template('index.html', data=data)

if __name__ == "__main__":
    serialcom = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
    serialcom.flush()
    app.run(host='0.0.0.0',port=8080,debug=False)