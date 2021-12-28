/*
  Onboard LED example

  Let the onboard LED blink in an endless loop
*/

// define macro for onboard LED at pin IO4
#define ONBOARD_LED   4

// the setup function runs once when you press reset or power the board
void setup() {
  // initialize pin ONBOARD_LED as an output.
  pinMode(ONBOARD_LED, OUTPUT);
}

// the loop function runs over and over again forever
void loop() {
  digitalWrite(ONBOARD_LED, LOW);    // turn the LED on (soldered from 3.3V to pin)
  delay(1000);                       // wait for a second
  digitalWrite(ONBOARD_LED, HIGH);   // turn the LED off by making the voltage HIGH
  delay(1000);                       // wait for a second
}
