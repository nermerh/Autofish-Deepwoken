import time

def autofish_process():
    count = 0
    while True:
        print(f"Run -> {count}")
        count+=1
        time.sleep(1)