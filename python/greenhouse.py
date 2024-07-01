import serial
import random
import time

# Configure the serial connection (adjust 'COM3' and baudrate as needed)
ser = serial.Serial('COM2', 9600, timeout=1)

try:
    while True:
        # Generate a random integer between 0 and 1
        random_number = random.randint(0, 1)
        
        # Write the random number to the serial port
        if random_number == 0:
            ser.write(f"T".encode())
        else:
            ser.write(f"F".encode())
        
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
