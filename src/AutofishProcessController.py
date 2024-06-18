import time
import pyautogui
from SimulInput import PressKey, ReleaseKey

def autofish_process(bait, chest_sound, rod_slot):
    time.sleep(0.5)
    equip_rod(rod_slot)

def equip_rod(rod_slot):
    print("equip rod")
    PressKey(11)
    time.sleep(0.1)
    ReleaseKey(11)

def cast_rod():
    ...

