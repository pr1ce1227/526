from ubluetooth import BLE, UUID, FLAG_NOTIFY, FLAG_READ, FLAG_WRITE
import time
from machine import Pin
import ubinascii
from stepper import Stepper

pin0 = Pin(0, Pin.OUT)
pin1 = Pin(1, Pin.OUT)
pin2 = Pin(2, Pin.OUT)
pin3 = Pin(3, Pin.OUT)
pin4 = Pin(4, Pin.OUT)
pin5 = Pin(5, Pin.OUT)
pin6 = Pin(6, Pin.OUT)
pin7 = Pin(7, Pin.OUT)
stepper = Stepper(pin0, pin1, pin2, pin3)


print("Spin stepper motor...")
stepper = Stepper(pin0, pin1, pin2, pin3)

led = Pin(15, Pin.OUT)

led.off()

# UUIDs for the service and characteristic (as byte strings)
SERVICE_UUID = UUID("f0debc9a-7856-3412-7856-341278563412")
CHAR_UUID = UUID("f1debc9a-7856-3412-7856-341278563412")

turn = False
forward = False
backward = False


def ble_irq(event, data):
    global turn
    global forward
    global backward
    print("BLE event:", event)
    print("Data:", data)
    if event == 1:
        led.on()
    elif event == 2:
        led.off()
    elif event == 4:  # Characteristic read event
        print("Read request received")
        conn_handle, attr_handle = data
        response = "Hello from Pico!"
        byte_response = bytes(response, 'utf-8')
        # Send a response to the read request
        ble.gatts_write(attr_handle, byte_response)
    elif event == 3:  # Characteristic write event
        print("Write request received")
        conn_handle, attr_handle = data
        value = ble.gatts_read(attr_handle)
        msg = value.decode( 'utf-8')
        print("Received msg:", msg)
        if msg == "on":
            print("LED ON")
            led.on()
        elif msg == "off":
            print("LED OFF")
            led.off()
        elif msg == "Right pressed": 
            stepper.set_steps(50)
            stepper.set_clockwise(1)
            stepper.run()
            turn = True

        elif msg == "Right released":
            stepper.stop()
            turn = False
         
        elif msg == "Left pressed":
            stepper.set_steps(50)
            stepper.set_clockwise(0)
            stepper.run()
            turn = True
        
        elif msg == "Left released":
            stepper.stop()
            turn = False

        elif msg == "Up pressed":
            if backward:
                pin4.off()
                pin5.off()
                pin6.off()
                pin7.off()
                backward = False
            else:
                pin4.off()
                pin5.on()
                pin6.on()
                pin7.off()
                forward = True
          

        elif msg == "Up released":
            # pin4.off()
            # pin5.off()
            # pin6.off()
            # pin7.off()
            pass


        elif msg == "Down pressed":
            if forward:
                pin4.off()
                pin5.off()
                pin6.off()
                pin7.off()
                forward = False
            else:
                pin4.on()
                pin5.off()
                pin6.off()
                pin7.on()
                backward = True
        
        elif msg == "Down released":
            # pin4.off()
            # pin5.off()
            # pin6.off()
            # pin7.off()
            pass
            



        



# Initialize BLE
ble = BLE()
ble.active(False)
ble.active(True)
ble.irq(ble_irq)


# Get the MAC address
mac_address = ble.config("mac")
mac_address_hex = ubinascii.hexlify(mac_address[1], ':').decode()
print("Bluetooth MAC address:", mac_address_hex)

# Register BLE service and characteristic
service = (
    UUID(SERVICE_UUID),
    ((UUID(CHAR_UUID), FLAG_READ | FLAG_NOTIFY | FLAG_WRITE),),
)
services = (service,)
ble.gatts_register_services(services)

# Set the device name (up to 20 characters)
device_name = "Caleb Pico"
name_bytes = bytes(device_name, 'utf-8')

# Advertise the service with the device name and service UUID
adv_payload = b'\x02\x01\x06'  # Flags (general discoverable, no BR/EDR)
adv_payload += bytes([len(name_bytes) + 1, 0x09]) + name_bytes  # Complete Local Name

# Add the service UUID to the advertising payload
print("Service UUID:", SERVICE_UUID)
print("Char UUID:", CHAR_UUID)
adv_payload += bytes([16 + 1, 0x06]) + SERVICE_UUID  # 0x06 for Complete List of 128-bit Service Class UUIDs



# Start advertising
ble.gap_advertise(100, adv_payload)

print("BLE advertising...")

while True:
    if turn:
        stepper.run()
    else:
        time.sleep(0.1)
