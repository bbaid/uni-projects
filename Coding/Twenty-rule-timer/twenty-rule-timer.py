# A timer which promts the user to take a break every 20 minutes. After 20 seconds the timer will start again.

import time

print(time.time())

while True:
    time.sleep(20*60)  # 20 minutes
    print("Time to take a break!")
    time.sleep(20)
    print("Time to get back to work!")

# This script will run indefinitely until the user stops it.

# To stop the script, press Ctrl + C in the terminal. This will send a KeyboardInterrupt signal to the script, which will cause it to stop running.
# If you are using an IDE, you may need to press a different key combination to stop the script. Check the documentation for your IDE to find out how to stop a running script.
# If you are running the script in a terminal window, you can also close the terminal window to stop the script.
