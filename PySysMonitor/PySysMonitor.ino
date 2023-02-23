#include <Wire.h> 
#include <LiquidCrystal_I2C.h>

LiquidCrystal_I2C lcd(0x27,16,2);  // set the LCD address to 0x27 for a 16 chars and 2 line display
byte cpuIcon[8] = {
	0b00000,
	0b10101,
	0b11111,
	0b10001,
	0b10111,
	0b10001,
	0b11111,
	0b10101
};
byte ramIcon[8] = {
	0b01110,
	0b11111,
	0b10011,
	0b11111,
	0b10010,
	0b11110,
	0b10011,
	0b11111
};
void setup() {
  // put your setup code here, to run once:
  lcd.init();
  lcd.backlight();
  lcd.createChar(0, cpuIcon);
  lcd.createChar(1, ramIcon);
  Serial.begin(9600);
  lcd.setCursor(0, 0);
  lcd.print("Inited");
}

void loop() {
  // put your main code here, to run repeatedly:
  if(Serial.available()){
    String incmgmsg = Serial.readStringUntil('#');
    String cpu = incmgmsg.substring(3, incmgmsg.indexOf("MEM"));
    String mem = incmgmsg.substring(incmgmsg.indexOf("MEM") + 3, incmgmsg.indexOf("GB") + 1);
    lcd.clear();
    lcd.setCursor(0,0);
    lcd.write((uint8_t)0);
    lcd.setCursor(1, 0);
    lcd.print(cpu + "%");
    lcd.setCursor(0, 1);
    lcd.write((uint8_t)1);
    lcd.setCursor(1, 1);
    lcd.print(mem);
    delay(500);
  }
}
