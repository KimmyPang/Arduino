import serial
import time
import mysql.connector
from flask import Flask, render_template, request, url_for

app = Flask(__name__)

@app.route("/")
def index():
    mydb = mysql.connector.connect(
        host = "localhost",
        user = "pi",
        password = "kimmy",
        database = "assignment_db"
    )

    with mydb:
        cursor = mydb.cursor()

        cursor.execute("SELECT * FROM pressureRecord")
        records = cursor.fetchall()

    return render_template('index.html', )

@app.route("/<action>")
def action(action):
    if (action == "Max"):
        ser.write("Speed of Pump turned to MAX\n".encode('utf-8'))
    return request(url_for('index'))

if __name__ == '__main__':
    ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
    ser.flush()
    app.run(debug=True, host='0.0.0.0', port=8080)