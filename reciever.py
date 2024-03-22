from ubluetooth import BLE, UUID, FLAG_NOTIFY, FLAG_READ, FLAG_WRITE
import time
from machine import Pin

led = Pin(25, Pin.OUT)

# UUIDs for the service and characteristic (as byte strings)
SERVICE_UUID = b'\x12\x34\x56\x78\x12\x34\x56\x78\x12\x34\x56\x78\x9a\xbc\xde\xf0'
CHAR_UUID = b'\x12\x34\x56\x78\x12\x34\x56\x78\x12\x34\x56\x78\x9a\xbc\xde\xf1'

# BLE event handler
def ble_irq(event, data):
    if event == 1:
        led.on()
    elif event == 2:
        led.off()

# Initialize BLE
ble = BLE()
ble.active(True)
ble.irq(ble_irq)

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
ble.gap_advertise(100, b'\x02\x01\x06' + bytes([len(name_bytes) + 1, 0x09]) + name_bytes + bytes([len(SERVICE_UUID) + 1, 0x03]) + SERVICE_UUID)

print("BLE advertising...")

while True:
    time.sleep(1)
