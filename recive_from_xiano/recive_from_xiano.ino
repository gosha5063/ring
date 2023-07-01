
#include <SoftwareSerial.h>


void setup() {
  Serial.begin(9600);
  Serial1.begin(9600);
  // portOne.begin(9600);
}
void loop() {
  if (Serial1.available()>0){Serial.println((int)Serial1.read());}
}
