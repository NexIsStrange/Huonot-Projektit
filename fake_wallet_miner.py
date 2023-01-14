"""Fake Bitcoin Wallet Generator by ctih#3462"""

import random
import string
import time

class color:
    green = "\u001b[32m"
    red = "\u001b[31m"
    reset = "\u001b[0m"

def random_address(lenght):
    letters = (string.ascii_letters + string.digits)
    address = "".join(random.choice(letters)for i in range(lenght))
    return address

speed_index = round(random.uniform(0.5,4), 4)

def fake_login():
    global speedindex
    print("Starting...")
    time.sleep(random.uniform(1,4))
    print("Looking for an infected computer...")
    time.sleep(random.uniform(20,120))
    print("Found an infected computer!")
    time.sleep(random.uniform(1,2))
    print("Testing SI...")
    time.sleep(random.uniform(10,12))
    print(f"SI:{speed_index}")
    print("Starting Wallet Mining...")
    time.sleep(random.uniform(9,11))


fake_login()
for i in range(random.randint(1000,5000)):
    print(f"{color.red}[-]{color.reset} {random_address(random.randint(26,35))} -> {color.red}0.000BTC{color.reset}")
    time.sleep(speed_index)

final = f"{color.green}[+]{color.reset} {random_address(random.randint(26,35))} -> {color.green}{round(random.uniform(0.2, 0.8),3)}BTC"
print(f"{final}")
