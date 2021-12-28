/*
  Neopixel example

  Let the WS2812 RGB LED light up in red, green and blue with one second delay

  Based on the NeoPixel Ring simple sketch (c) 2013 Shae Erisson
  Released under the GPLv3 license to match the rest of the Adafruit NeoPixel
  library
*/

#include <Adafruit_NeoPixel.h>

// One single NeoPixels is connected to IO27 on the BE32-01
#define NUMPIXELS  1
#define PIN        27

// When setting up the NeoPixel library, we tell it how many pixels,
// and which pin to use to send signals. Note that for older NeoPixel
// strips you might need to change the third parameter -- see the
// strandtest example for more information on possible values.
Adafruit_NeoPixel pixels(NUMPIXELS, PIN, NEO_GRB + NEO_KHZ800);

// the setup function runs once when you press reset or power the board
void setup() {
  // initialize NeoPixel strip object and turn all pixels off
  pixels.begin();
  pixels.clear();
}

// the loop function runs over and over again forever
void loop() {
  // turn the RGB LED at index 0 red with 10/255 intensity
  pixels.setPixelColor(0, pixels.Color(10, 0, 0));
  pixels.show();   // Send the updated pixel colors to the hardware.

  // wait for a second
  delay(1000);

  // turn the RGB LED at index 0 green with 10/255 intensity
  pixels.setPixelColor(0, pixels.Color(0, 10, 0));
  pixels.show();   // Send the updated pixel colors to the hardware.

  // wait for a second
  delay(1000);

  // turn the RGB LED at index 0 blue with 10/255 intensity
  pixels.setPixelColor(0, pixels.Color(0, 0, 10));
  pixels.show();   // Send the updated pixel colors to the hardware.

  // wait for a second
  delay(1000);
}
