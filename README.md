# 526

This repo holds the source code for a BLE controlled car built using a Raspberry PI Pico W as the reciever and a Raspberyy PI 4B as the transiever. I used the MicroPico extension in vscode for programming the pico. 

## File Structure 
blink.py: This can be used just to verify that you are able to program the pico. If succesful will cause the led to blink.<br>

reciever.py: Main script for the pico. This script will hand all bluetooth communication and imports the controls from the stepper.py and steer.py<br>

remote_control.py: This is what was load onto the rasperry pi 4B. Build the graphical interface for the controller and handles forwarding the message to the Pico.<br>

Steer.py: Class that handles the steering and allows the user to turn right or left.<br>

Stepper.py: Class used by the steering class. This handles the sequences needed to turn the stepper motor clockwise or counter clockwise. 
