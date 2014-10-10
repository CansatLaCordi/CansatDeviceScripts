#include "DHT.h"
#define DHTPIN 2     // what pin we're connected to
#define DHTTYPE DHT22 
DHT dht(DHTPIN, DHTTYPE);

//TODO: Agregar los numeros de pines correctos
int heatState=0, 
  servoState = 0, 
  speakerState = 0,
  pinHeat, 
  pinMq7, 
  pinDht22, 
  pinSpeaker, 
  pinServo;
  
unsigned long time,
  lowtime=90000,
  hightime = 60000,
  lastChange,
  senseTime=1000, 
  lastSense;
  
double mq7,
  humidity, 
  temperature;

double readMQ7(){
  int m = analogRead(pinMq7);
  return m;
}
double readHumidity(){
  float h = dht.readHumidity();
  if (isnan(h)) {
    return -1;
  }
  return h;
}
double readTemp(){ 
  float t = dht.readTemperature();
  // Check if any reads failed and exit early (to try again).
  if (isnan(t)) {
    return -1;
  }
  return t;
}
void heater(){
  if(heatState){
     digitalWrite(pinHeat, HIGH);   // turn the LED on (HIGH is the voltage level)
     if(time-lastChange > hightime){
       heatState = !heatState;
       lastChange = time;
     }
   }
   else{
     digitalWrite(pinHeat, LOW);
     if(time-lastChange > lowtime){
       heatState = !heatState;
       lastChange = time;
     }
   }
}

void writeValues(){
    Serial.print("mq7=");
    Serial.print(mq7);
    Serial.print("&temp=");
    Serial.print(temperature);
    Serial.print("&hum=");
    Serial.println(humidity);
}

void readSensors(){
   if(time-lastSense > senseTime){
       lastSense = time;
       mq7 = readMQ7();
       humidity = readHumidity();
       temperature = readTemp();       
       digitalWrite(pinSpeaker,speakerState?HIGH:LOW);
       writeValues();
   }
}

void activateServo(){
   if (Serial.available() > 0) {
      // read the incoming byte:
      servoState = Serial.read();
      if(servoState != 0)
        digitalWrite(pinServo,HIGH);
      else
        digitalWrite(pinServo, LOW);

   }
}

// the setup routine runs once when you press reset:
void setup() {                
   // initialize the digital pin as an output.
   Serial.begin(9600);  //Inicializar el puerto COM  
   pinMode(pinSpeaker, OUTPUT);   
   pinMode(pinHeat, OUTPUT);
   pinMode(pinMq7,INPUT);
   pinMode(pinDht22,INPUT);
   pinMode(pinServo,OUTPUT);   
   lastChange = millis();  
   lastSense = lastChange; //uso la misma fecha
   dht.begin();
}

void loop() {
  time = millis();
  heater();
  readSensors();
  activateServo();
}
