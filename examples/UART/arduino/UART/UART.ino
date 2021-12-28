/*
  UART example

  Print debug data via the programmer boards USB port and other content on the
  4x2 pinheader repeatedly every second.
*/

// the setup function runs once when you press reset or power the board
void setup() {
  Serial.begin(115200);

  Serial.println("Setting up the alternative UART on D25 (TX) and D26 (RX)");
  // Note the format for setting a serial port is as follows:
  // Serial2.begin(baud-rate, protocol, RX pin, TX pin);
  Serial2.begin(115200, SERIAL_8N1, 26, 25);
}

// the loop function runs over and over again forever
void loop() {
	// print current timestamp via programmer board on USB C
	Serial.print("Debug message on programmer USB at ");
	Serial.println(millis());

	// print "Hello World" on the 4x2 pinheader TX pin
	Serial2.print("Hello World from 4x2 pinheader at ");
	Serial2.println(millis());

	// wait for a second
	delay(1000);
}
