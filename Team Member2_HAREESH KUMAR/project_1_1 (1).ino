// C++ code
//
#include<Servo.h>
Servo s;
int buzz = 8;
void setup()
{
  Serial.begin(9600);
  pinMode(13, OUTPUT);
  pinMode(2, INPUT);
  pinMode(3, INPUT);
  pinMode(buzz,OUTPUT);
  s.attach(3);
  
}


void loop()
{

  int a=digitalRead(2);
  Serial.println(a);
  digitalWrite(13, LOW);
  
  if(a==1){
	Serial.println("MOTION DETECTED");
    digitalWrite(13, HIGH);
    for(int i=0;i<=180;i++){
	s.write(i);
    delay(10);
 }
   	tone(buzz, 131);
    delay(300);
    noTone(buzz);
    delay(300);
    

}
  
}