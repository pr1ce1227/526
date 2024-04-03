from ubluetooth import BLE, UUID, FLAG_NOTIFY, FLAG_READ, FLAG_WRITE
import time
from machine import Pin
import ubinascii


led = Pin(15, Pin.OUT)

led.off()

# UUIDs for the service and characteristic (as byte strings)
SERVICE_UUID = UUID("f0debc9a-7856-3412-7856-341278563412")
CHAR_UUID = UUID("f1debc9a-7856-3412-7856-341278563412")


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
adv_payload = b'\x02\x01\x06'  # Flags (general discoverable, no BR/EDR)
adv_payload += bytes([len(name_bytes) + 1, 0x09]) + name_bytes  # Complete Local Name

# Add the service UUID to the advertising payload
service_uuid_length = len(SERVICE_UUID)
adv_payload += bytes([service_uuid_length + 1, 0x03]) + SERVICE_UUID  # Incomplete List of 16-bit Service Class UUIDs

# Start advertising
ble.gap_advertise(100, adv_payload)

print("BLE advertising...")

while True:
    time.sleep(1)
