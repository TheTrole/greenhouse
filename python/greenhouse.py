import serial
import random
import time


ser = serial.Serial('COM2', 9600, timeout=1)

try:
    while True:
        random_number = random.randint(0, 1)

        if random_number == 0:
            ser.write(f"T".encode())
        else:
            ser.write(f"F".encode())
        
        print(f"Sent: {random_number}")
        
        # Wait for 5 seconds
        time.sleep(5)

except KeyboardInterrupt:
    print("Interrupted by user")

finally:
    ser.close()
    print("Serial connection closed")
