import time

def countdown(start):
    i = start
    while i > 0:
        print(f"{i} SECOND(S)!")
        i -= 1
    print("HAPPY NEW YEAR!")

def countdown_with_sleep(start):
    i = start
    while i > 0:
        print(f"{i} SECOND(S)!")
        i -= 1
        time.sleep(1)
    print("HAPPY NEW YEAR!")