from ubluetooth import BLE, UUID, FLAG_NOTIFY, FLAG_READ, FLAG_WRITE
import time
from machine import Pin
import ubinascii

led = Pin(15, Pin.OUT)

led.off()

# UUIDs for the service and characteristic (as byte strings)
SERVICE_UUID = b'\x12\x34\x56\x78\x12\x34\x56\x78\x12\x34\x56\x78\x9a\xbc\xde\xf0'
CHAR_UUID = b'\x12\x34\x56\x78\x12\x34\x56\x78\x12\x34\x56\x78\x9a\xbc\xde\xf1'


# BLE event handler
def ble_irq(event, data):
    if event == 1:
        led.on()
    elif event == 2:
        led.off()
    elif event == 4:  # Characteristic read event
        print("Read request received")
        conn_handle, attr_handle = data
        response = "Hello from Pico!"
        byte_response = bytes(response, 'utf-8')
        # Send a response to the read request (e.g., a dummy value)
        ble.gatts_write(attr_handle, byte_response)
    elif event == 3:  # Characteristic write event
        try:
            conn_handle, attr_handle, value = data
            # Handle the received value (e.g., print it)
            print("Received value:", bytes(value))
        except:
            conn_handle, attr_handle = data
            # Normally, you would handle the received value here, but it seems not to be provided in this case
            print("Write event received for attribute handle:", attr_handle)


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
ble.gap_advertise(100, b'\x02\x01\x06' + bytes([len(name_bytes) + 1, 0x09]) + name_bytes)

print("BLE advertising...")

while True:
    time.sleep(1)
