import keyboard
import time
import mouse 

# Configuration
activation_key = 'c'  # You can change these key to whatever is most comfortable for you
exit_key = 'f1'       # Key to stop the program
click_speed = 0.05    # Time between clicks in seconds

def send_click():
    mouse.click('left')
    time.sleep(0.01)  
    mouse.click('left')

print(f"Script started. Hold '{activation_key}' key to auto-click.")
print(f"Press '{exit_key}' to stop the program.")

while True:
    if keyboard.is_pressed(exit_key):
        print("Program stopped.")
        break
    
    if keyboard.is_pressed(activation_key):
        send_click()
        time.sleep(click_speed)
    else:
        time.sleep(0.01)  # Small pause to avoid high CPU usage
