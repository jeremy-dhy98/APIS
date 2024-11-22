import mss
import cv2
import numpy as np
import time

screen_size = (1920, 1080)
fourcc = cv2.VideoWriter_fourcc(*"XVID")
out = cv2.VideoWriter("screen_recording.avi", fourcc, 20.0, screen_size)

sct = mss.mss()
start_time = time.time()
duration = 10  # seconds
print(f"About to start a screen recording...for: {duration} seconds.")
print(f"Timing for 15 seconds...")
time.sleep(15)
print("Screen recording started...")

while time.time() - start_time < duration:
    # Capture screen
    screenshot = sct.grab(sct.monitors[1])  # Select primary monitor
    frame = np.array(screenshot)
    frame = cv2.cvtColor(frame, cv2.COLOR_BGRA2BGR)  # Remove alpha channel
    out.write(frame)

out.release()
print("Screen recording ended...")
