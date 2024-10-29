import time
import csv
from pynput import mouse

# Initialize the list to store the mouse coordinates
mouse_data = []

# Define the callback for mouse movement
def on_move(x, y):
    timestamp = time.time()  # Record the timestamp
    mouse_data.append((timestamp, x, y))  # Append timestamp and coordinates

# Small delay before listeting
print("Starting listening in 5 seconds...")
time.sleep(5)

# Start listening to the mouse movements
print("Started Listening")
listener = mouse.Listener(on_move=on_move)
listener.start()

# Define the interval and duration
interval = 0.2  # 200ms interval
duration = 5  # Record for 5 seconds

# Run for a specific time duration
start_time = time.time()
while time.time() - start_time < duration:
    time.sleep(interval)

# Stop listener and write to a file
listener.stop()

# Save to CSV
with open("mouse_movement_data.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(mouse_data)  # Data
