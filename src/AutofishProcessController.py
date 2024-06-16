from queue import Queue
import time

def autofish_process():
    count = 0
    while True:
        print(f"Run -> {count}")
        time.sleep(1)