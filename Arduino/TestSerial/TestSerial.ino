int n;
int led =13;

void setup(){
  n = 0;
  Serial.begin(9600);
  //pinMode(led, OUTPUT);
}

void loop(){
  Serial.print(++n%10);
  //delay(1000);
  //digitalWrite(led,(n%2==0?HIGH:LOW));
}
