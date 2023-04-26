#include <Servo.h>

int potPin = A0;      
int servoPin = 9;     
int waterPin = A1;    
int ledPin = 10;      
int threshold = 500;

Servo myservo;              

void setup() {
  
  myservo.attach(servoPin);  
  pinMode(ledPin, OUTPUT);   
  Serial.begin(9600);        

}

void loop() {
  
  int potValue = analogRead(potPin);  
  int waterValue = analogRead(waterPin);
  int pressure = map(potValue, 150, 950, 10, 75);

  if (Serial.available() > 0) {
    String inputString = Serial.readStringUntil('\n');
    if (inputString == "MAX") {
      myservo.write(180);
    } else if (inputString == "MIN") {
      myservo.write(90);
    } else if (inputString == "OFF") {
      myservo.write(0);
    }
  }

  String dataString = "";

  if (waterValue < threshold || potValue < 250) { 
    
    digitalWrite (ledPin, LOW);
    myservo.write(180);
    dataString += "Extremely Low,";
    dataString += String(pressure) + ",";
    dataString += "Max,";
    dataString += "No\n";
    
  }else if (potValue <500) {

    digitalWrite (ledPin, LOW);
    myservo.write(90);
    dataString += "Low,";
    dataString += String(pressure) + ",";
    dataString += "Min,";
    dataString += "No\n";

  } else {
    
    myservo.write(0);      

     if (potValue <750) {
      
      digitalWrite (ledPin, HIGH);
      dataString += "Abnormal,";
      dataString += String(pressure) + ",";
      dataString += "Off,";
      dataString += "Yes\n";
      
    } else {
      
      digitalWrite (ledPin, LOW);
      dataString += "Normal,";
      dataString += String(pressure) + ",";
      dataString += "Off,";
      dataString += "No\n";
      
    }
    
  }

  Serial.println(dataString);

  // add delay to prevent reading the sensor values too frequently
  delay(3000); 
}
