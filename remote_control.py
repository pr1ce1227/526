from bluepy.btle import Peripheral, UUID
import time
import struct
import tkinter as tk
from threading import Thread
import time

# The MAC address of your Pico W (replace with the actual address)
pico_w_address = "d8:3a:dd:8c:14:9d"

# The UUID of the service on the Pico W (in standard string format)
service_uuid = UUID("f0debc9a-7856-3412-7856-341278563412")

# Initialize the peripheral object
p = None

# Attempt to connect to the peripheral
while True:
    try:
        p = Peripheral(pico_w_address)
        print("Connected to", pico_w_address)
        break  # Exit the loop once connected
    except Exception as e:
        print("Connection failed, retrying...")
     # Wait for a short period before retrying

# Give some time for the connection to stabilize
time.sleep(2)

# Discover services
services = p.getServices()

# Find the service by UUID
service = None
for svc in services:
    if svc.uuid == service_uuid:
        print("Service found:", svc.uuid)
        service = svc
        break

if service is None:
    print("Service not found")
    print("Expected: ", service_uuid)
    exit()

# The UUID of the characteristic (in standard string format)
char_uuid = UUID("f1debc9a-7856-3412-7856-341278563412")

# Get the characteristic
char = None
for characteristic in service.getCharacteristics():
    if characteristic.uuid == char_uuid:
        print("Characteristic found:", characteristic.uuid)
        char = characteristic
        break

if char is None:
    print("Characteristic not found")
    exit()

# Write a message to the characteristic
char.write(b"Left", withResponse=True)


def arrow_pressed(direction):
    if direction == "Up":
        print("Up pressed")
        char.write(b"Up pressed", withResponse=True)
    elif direction == "Down":
        print("Down pressed")
        char.write(b"Down pressed", withResponse=True)
    elif direction == "Left":
        print("Left pressed")
        char.write(b"Left pressed", withResponse=True)
    elif direction == "Right":
        print("Right pressed")
        char.write(b"Right pressed", withResponse=True)

def arrow_released(direction):
    if direction == "Up":
        print("Up released")
        char.write(b"Up released", withResponse=True)
    elif direction == "Down":
        print("Down released")
        char.write(b"Down released", withResponse=True)
    elif direction == "Left":
        print("Left released")
        char.write(b"Left released", withResponse=True)
    elif direction == "Right":
        print("Right released")
        char.write(b"Right released", withResponse=True)

def on_press(event, direction):
    arrow_pressed(direction)

def on_release(event, direction):
    arrow_released(direction)

root = tk.Tk()
root.title("Arrow Buttons")

# Create buttons with larger font and padding
btn_up = tk.Button(root, text="↑", font=("Arial", 60), padx=40, pady=40)
btn_down = tk.Button(root, text="↓", font=("Arial", 60), padx=40, pady=40)
btn_left = tk.Button(root, text="←", font=("Arial", 60), padx=40, pady=40)
btn_right = tk.Button(root, text="→", font=("Arial", 60), padx=40, pady=40)

# Bind mouse events to buttons
btn_up.bind("<ButtonPress-1>", lambda event: on_press(event, "Up"))
btn_up.bind("<ButtonRelease-1>", lambda event: on_release(event, "Up"))
btn_down.bind("<ButtonPress-1>", lambda event: on_press(event, "Down"))
btn_down.bind("<ButtonRelease-1>", lambda event: on_release(event, "Down"))
btn_left.bind("<ButtonPress-1>", lambda event: on_press(event, "Left"))
btn_left.bind("<ButtonRelease-1>", lambda event: on_release(event, "Left"))
btn_right.bind("<ButtonPress-1>", lambda event: on_press(event, "Right"))
btn_right.bind("<ButtonRelease-1>", lambda event: on_release(event, "Right"))

# Position buttons in a grid
btn_up.grid(row=0, column=1)
btn_left.grid(row=1, column=0)
btn_down.grid(row=2, column=1)
btn_right.grid(row=1, column=2)

root.mainloop()
