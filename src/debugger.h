#pragma once

#define DEBUG true
#define DEBUG_RATE_MILLIS 500
#define RED_LED_PIN 31
#define GREEN_LED_PIN 30

void debugger_print();
void debugger_leds();
void debugger_leds_init();
void debugger_indicate_emergency(const char *reason);
