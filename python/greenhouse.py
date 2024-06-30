import serial
import random
import time

# Configure the serial connection (adjust 'COM3' and baudrate as needed)
ser = serial.Serial('COM3', 9600, timeout=1)

try:
    while True:
        # Generate a random float between 0 and 1
        random_number = random.random()
        
        # Write the random number to the serial port
        ser.write(f"{random_number}\n".encode('utf-8'))
        
        # Print the random number to the console (for debugging purposes)
        print(f"Sent: {random_number}")
        
        # Wait for 5 seconds
        time.sleep(5)

except KeyboardInterrupt:
    print("Interrupted by user")

finally:
    # Close the serial connection
    ser.close()
    print("Serial connection closed")
