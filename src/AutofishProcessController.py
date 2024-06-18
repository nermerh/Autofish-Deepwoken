import time
import pyautogui
import SimulInput

# Process function that gets called
def autofish_process(bait, chest_sound, rod_slot):
    time.sleep(0.5)

    equip_rod(rod_slot)

    time.sleep(0.5)

    # Chum
    if bait == 1:
        print("dealing with bait")
    
    cast_rod()

    while True:
        print("waiting for fishy wishy")
        time.sleep(0.3)

# Breaking down the process
def equip_rod(rod_slot):
    print("equip rod")
    press_key(11)

def cast_rod():
    pyautogui.click()
    print("shouldve clicked")

# Simulate Input
def press_key(keyNum):
    SimulInput.PressKey(keyNum)
    time.sleep(0.1)
    SimulInput.ReleaseKey(keyNum)

