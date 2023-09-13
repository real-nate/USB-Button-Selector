# Nathaniel Furman
# 2023
#
# Code credit:
# SPDX-FileCopyrightText: 2018 Kattni Rembor for Adafruit Industries
# SPDX-License-Identifier: MIT
# SPDX-FileCopyrightText: 2022 Ruiz Bros for Adafruit Industries
# SPDX-License-Identifier: MIT

# TODO: maybe add button connection for rotary encoder that switches the order or scroll speed

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

# Game ID's
gameList = ('Valheim', 'Smite', 'Satisfactory', 'Deep Rock Galactic', 'Timberborn')
gameNums = (892970, 386360, 526870, 548430, 1062090)
numGames = len(gameList)

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

# Function to send keyboard strokes to start game
def runGame(index):
    # [WIN+R], 'cmd', 'start steam://rungameid/{ID}/&exit'
    keyboard.send(Keycode.GUI, Keycode.R)
    time.sleep(0.05)
    keyboard.send(Keycode.C)
    keyboard.send(Keycode.M)
    keyboard.send(Keycode.D)
    time.sleep(0.01)
    keyboard.send(Keycode.ENTER)

    time.sleep(0.05)
    keyboard.send(Keycode.S)
    keyboard.send(Keycode.T)
    keyboard.send(Keycode.A)
    keyboard.send(Keycode.R)
    keyboard.send(Keycode.T)
    keyboard.send(Keycode.SPACE)
    keyboard.send(Keycode.S)
    keyboard.send(Keycode.T)
    keyboard.send(Keycode.E)
    keyboard.send(Keycode.A)
    keyboard.send(Keycode.M)
    keyboard.send(Keycode.SHIFT, Keycode.SEMICOLON)
    keyboard.send(Keycode.FORWARD_SLASH)
    keyboard.send(Keycode.FORWARD_SLASH)
    keyboard.send(Keycode.R)
    keyboard.send(Keycode.U)
    keyboard.send(Keycode.N)
    keyboard.send(Keycode.G)
    keyboard.send(Keycode.A)
    keyboard.send(Keycode.M)
    keyboard.send(Keycode.E)
    keyboard.send(Keycode.I)
    keyboard.send(Keycode.D)
    keyboard.send(Keycode.FORWARD_SLASH)
    for digit in map(int, str(gameNums[index])):
        print(digit)
        print(type(digit))
        if digit == 0:
            keyboard.send(digit + 39)
        else:
            keyboard.send(digit + 29)
    keyboard.send(Keycode.SHIFT, Keycode.SEVEN)
    keyboard.send(Keycode.SHIFT, Keycode.SEVEN)
    keyboard.send(Keycode.E)
    keyboard.send(Keycode.X)
    keyboard.send(Keycode.I)
    keyboard.send(Keycode.T)
    time.sleep(0.01)
    keyboard.send(Keycode.ENTER)


# Set up starting states
button_state = None
last_position = encoder.position
lcd.clear()
lcd.backlight = True

# Main loop
gameCounter = 0
# Display first game in list
lcd.message = '>> ' + gameList[gameCounter][0:lcd_columns-3] + '\n' + gameList[gameCounter + 1][0:lcd_columns]
while True:
    # Read status of the encoder
    current_position = encoder.position
    position_change = current_position - last_position
    if position_change > 0:
        if gameCounter == numGames-1:
        # Loop back to the start
            gameCounter = 0
        else:
            gameCounter += 1
        print(f'Game Counter: {gameCounter}; {gameList[gameCounter]}')
    elif position_change < 0:
        if gameCounter == 0:
        # Loop back to the end
            gameCounter = numGames-1
        else:
            gameCounter -= 1
        print(f'Game Counter: {gameCounter}; {gameList[gameCounter]}')
    last_position = current_position
    print(f'Curr pos: {current_position}')

    # Display current and next game on screen
    if gameCounter == numGames-1:
        lcd.message = '>> ' + gameList[gameCounter][0:lcd_columns-3] + '\n' + gameList[0][0:lcd_columns]
    else:
        lcd.message = '>> ' + gameList[gameCounter][0:lcd_columns-3] + '\n' + gameList[gameCounter+1][0:lcd_columns]
    print(lcd.message)

    # Read status of the button
    if not button.value and button_state is None:
        button_state = "pressed"
    if button.value and button_state == "pressed":
        print("Button pressed.")
        runGame(gameCounter)
        button_state = None
    time.sleep(0.01)


