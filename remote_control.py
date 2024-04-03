from bluepy.btle import Peripheral, UUID
import time
import struct
import tkinter as tk

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
        time.sleep(1)  # Wait for a short period before retrying

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

root = tk.Tk()
root.title("Arrow Buttons")

def arrow_pressed(direction):
    print(f"{direction} arrow pressed")

# Create buttons with arrow symbols
btn_up = tk.Button(root, text="↑", command=lambda: arrow_pressed("Up"))
btn_down = tk.Button(root, text="↓", command=lambda: arrow_pressed("Down"))
btn_left = tk.Button(root, text="←", command=lambda: arrow_pressed("Left"))
btn_right = tk.Button(root, text="→", command=lambda: arrow_pressed("Right"))

# Position buttons in a grid
btn_up.grid(row=0, column=1)
btn_left.grid(row=1, column=0)
btn_down.grid(row=2, column=1)
btn_right.grid(row=1, column=2)

# Start the Tkinter event loop
root.mainloop()

