#include <LiquidCrystal.h>
#include <Servo.h>

Servo myservo;
LiquidCrystal lcd(9,8,5,4,3,2);
const int pin = A0;
int limit = 100;

void setup()
{
  Serial.begin(9600);
  lcd.begin(16,2);
  myservo.attach(6);
  
  lcd.setCursor(3,0);
  lcd.print("loading...");
  delay(1000);
  lcd.clear();
}

void loop()
{
  int ldrValue = analogRead(pin);
  if(ldrValue > limit)
  {
    myservo.write(180);
    lcd.print("ROOF OPEN");
    delay(1000);
  }    
  else
  {
    myservo.write(0);
    lcd.print("ROOF CLOSED");
    delay(1000);
  }
  lcd.clear();
}












