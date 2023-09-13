# USB-Button-Selector
Send keystrokes on USB-connected button from selection using rotary encoder. Current ready-to-use setup is for launching Steam games.

The implementation works by using the Adafruit board running as a HID (human interface devices, e.g. keyboard), while taking input from the connected button and rotary encoder. An LCD screen displays the current selection, and the button actives the script.

## Hardware
The Adafruit shopping list can be found here: [https://www.adafruit.com/wishlists/579808](https://www.adafruit.com/wishlists/579808)
* Large Arcade Button with LED-60mm red (PID: 1190, ~$6)
* Rotary Encoder (PID: 377, ~$5)
* USB A/Micro Cable (PID: 2185, ~$5)
* Standard LCD 16x2 display (PID: 181, ~$10)
* Adafruit ItsyBitsy M0 Express (PID: 3727, ~$12)
Total: ~$37 (as of Sept. 2023)

Housing is also highly recommended. 3D models with corresponding FreeCAD files are provided in the `model` directory. The below screws are used to connect the base with the top and the LCD screen to the top.
* M3 (x4)
* M5 (x4)

### Assembly
Please refer to guide in the 'docs' directory.

## Software
The ItsyBitsy M0 Express board is an HID-compatible board that runs CircuitPython. The install is summarized in the `docs` directory, and the full process is explained by Adafruit at [https://learn.adafruit.com/introducing-itsy-bitsy-m0/circuitpython](https://learn.adafruit.com/introducing-itsy-bitsy-m0/circuitpython).

For an as-is setup, simply drag the contents of the `src/all-in-one/` directory to the `CIRCUITPY` drive and wire the connections on the board according to the wiring diagram in the `docs` directory.

### Libraries
The default CircuitPython install comes with all but two of the necessary libraries: `charlcd` and `hid`. The full libraries in their original zip are in `src/lib-full`. However, to save space on the device (and be able to load the code), abbreviated libraries are used and found in `src/lib`.

### Updating Game List
The 'as-is' implementation has five games loaded into an array of names and another array of corresponding Application ID's. To add a game, simply add the name as you want it displayed to the `gameList` array, and add the Application ID to the same index (position) in the `gameNums` array. Application ID's can be found on Steam by right-clicking a game, selecting properties, and navigating to 'Updates'. The App ID is at the bottom of the page.