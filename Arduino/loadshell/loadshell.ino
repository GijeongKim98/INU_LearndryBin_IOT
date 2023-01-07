#include "HX711.h"

// HX711 circuit wiring
const int LOADCELL_DOUT_PIN = 2;
const int LOADCELL_SCK_PIN = 3;

HX711 scale;

void setup() {
  Serial.begin(57600);
  scale.begin(LOADCELL_DOUT_PIN, LOADCELL_SCK_PIN);
}

void loop() {

  if (scale.is_ready()) {
    long reading = scale.read();
    double read1 = double(reading + 26200) / 229200;
    read1 = read1 - 0.66;
    // Serial.print("HX711 reading: ");
    Serial.println(read1);
  } else {
    Serial.println(-1000);
  }

  delay(1000);
  
}
