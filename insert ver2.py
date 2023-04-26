import mysql.connector
import serial

device = '/dev/ttyACM0'
arduino = serial.Serial(device, 9600)

while 1:
    mydb = mysql.connector.connect(
        host = "localhost",
        user = "pi",
        password = "kimmy",
        database = "assignment_db"
    )

    print(mydb)

    while(arduino.in_waiting == 0):
        pass

    line = arduino.readline().decode().strip()
    data = line.split(',')
    if len(data) == 4:
        degreeOfWaterPressure = data[0]
        pressure = int(data[1]
        speedOfPump = data[2]
        pipeLeakage = data[3]
        print("Degree of Water Pressure: " + str(degreeOfWaterPressure) + " Pressure: " + str(int(pressure)) + " Speed of Pump: " + str(speedOfPump) + " Pipe Leakage: " + str(pipeLeakage))    

    with mydb:
        mycursor = mydb.cursor()
        sql = "INSERT INTO pressureRecord (degreeOfWaterPressure, pressure, speedOfPump, pipeLeakage) VALUES (%s, %s, %s, %s)"
        val = (degreeOfWaterPressure, int(pressure), speedOfPump, pipeLeakage)
        mycursor.execute(sql, val)
        mydb.commit()
        mycursor.close()