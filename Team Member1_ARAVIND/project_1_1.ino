// C++ code
//
#include<Servo.h>
Servo s;
int buzz = 9;
void setup()
{
  Serial.begin(9600);
  pinMode(11, OUTPUT);
  pinMode(7, INPUT);
  pinMode(3, INPUT);
  pinMode(buzz,OUTPUT);
  s.attach(3);
  
}


void loop()
{

  int a=digitalRead(7);
  Serial.println(a);
  digitalWrite(11, LOW);
  
  if(a==1){
	Serial.println("MOTION DETECTED");
    digitalWrite(11, HIGH);
    for(int i=0;i<=180;i++){
	s.write(i);
    delay(10);
 }
  for(int i=180;i>=0;i--){
	s.write(i);
    delay(10);
  }
   	tone(buzz, 131);
    delay(300);
    noTone(buzz);
    delay(300);
    

}
  
}