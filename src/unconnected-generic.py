# Nathaniel Furman
# 2023
#
# Code credit:
# SPDX-FileCopyrightText: 2018 Kattni Rembor for Adafruit Industries
# SPDX-License-Identifier: MIT
# SPDX-FileCopyrightText: 2022 Ruiz Bros for Adafruit Industries
# SPDX-License-Identifier: MIT

import board
import digitalio
import rotaryio
import time
import usb_hid
import adafruit_character_lcd.character_lcd as characterlcd
from adafruit_hid.keycode  import Keycode
from adafruit_hid.keyboard import Keyboard

lcd_columns = 16
lcd_rows    = 2

# Run when button is pressed
def doSomething(inputVar=0):
    print('button pressed')
    # keyboard.send(Keycode.SHIFT)
    # time.sleep(0.01)

# Initialize button
button = digitalio.DigitalInOut(board.D2)
button.direction = digitalio.Direction.INPUT
button.pull      = digitalio.Pull.UP

# Initialize rotary encoder and keyboard
encoder  = rotaryio.IncrementalEncoder(board.D0, board.D1)
keyboard = Keyboard(usb_hid.devices)

# Initialise the lcd class
lcd = characterlcd.Character_LCD_Mono(
        digitalio.DigitalInOut(board.D7),
        digitalio.DigitalInOut(board.D9),
        digitalio.DigitalInOut(board.D10),
        digitalio.DigitalInOut(board.D11),
        digitalio.DigitalInOut(board.D12),
        digitalio.DigitalInOut(board.D13),
        lcd_columns, lcd_rows,
        digitalio.DigitalInOut(board.D5))

# Set up starting states
button_state = None
last_position = encoder.position
lcd.clear()
lcd.backlight = True

# Main loop
lcd.message = 'test message'
runCounter = 10
while runCounter > 0:
    # If running un-connected to encoder/button, get input from user
    current_position = int(input('Current position: '))
    
    # Read status of the encoder
    #current_position = encoder.position
    position_change = current_position - last_position
    if position_change > 0:
        # Increase counter
        print('Positive position')
    elif position_change < 0:
        # Decrease counter
        print('Decrease position')
    last_position = current_position
    print(f'Curr pos: {current_position}')

    # Display message based on counter
    lcd.message = 'new message'
    print(lcd.message)

    # Read status of the button
    if not button.value and button_state is None:
        button_state = "pressed"
    if button.value and button_state == "pressed":
        print("Button pressed.")
        doSomething()
        button_state = None
    time.sleep(0.01)
    
    buttonQuery = input('Button pressed (y/n)? ')
    if buttonQuery.lower() in ['yes', 'y']:
        print('Button pressed.')
        doSomething()
    elif buttonQuery.lower() in ['no', 'n']:
        print('Button not pressed.')
    else:
        print('Unrecognized input, skipping.')
    

    print(runCounter)
    runCounter -= 1

