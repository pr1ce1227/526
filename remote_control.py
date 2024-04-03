from bluepy.btle import Peripheral

# The MAC address of your Pico W (replace with the actual address)
pico_w_address = "d8:3a:dd:8c:14:9d"

# The UUID of the service on the Pico W (must match the one used in the Pico W code)
# Convert the UUID string to a byte string format
service_uuid = b'\x12\x34\x56\x78\x12\x34\x56\x78\x12\x34\x56\x78\x9a\xbc\xde\xf0'
service_uuid = service_uuid[::-1]

# Connect to the Pico W
p = Peripheral(pico_w_address)

# Discover services
services = p.getServices()

# Find the service by UUID
service = None
for svc in services:
    print(str(svc.uuid))
    print()
    if  str(svc.uuid).find(str(service_uuid)) != -1:
        service = svc
        break

if service is None:
    print("Service not found")
    exit()

# Find the characteristic (replace with the actual UUID of the characteristic)
# Convert the UUID string to a byte string format
char_uuid = b'\x12\x34\x56\x78\x12\x34\x56\x78\x12\x34\x56\x78\x9a\xbc\xde\xf1'

# Get the characteristic
char = None
for characteristic in service.getCharacteristics():
    if characteristic.uuid.bin == char_uuid:
        char = characteristic
        break

if char is None:
    print("Characteristic not found")
    exit()

# Write a message to the characteristic
char.write(b"Hello from Raspberry Pi 4B!")

# Disconnect
p.disconnect()
