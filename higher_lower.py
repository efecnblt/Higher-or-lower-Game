import random
import os
from data import data

class bcolors:
    FAIL = '\033[91m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    OKBLUE = '\033[94m'
    HEADER = '\033[95m'
    OKCYAN = '\033[96m'
    ENDC = '\033[0m'
    UNDERLINE = '\033[4m'
    BLINK = '\033[05m'

logo = """
    __  ___       __             
   / / / (_)___ _/ /_  ___  _____
  / /_/ / / __ `/ __ \/ _ \/ ___/
 / __  / / /_/ / / / /  __/ /    
/_/ ///_/\__, /_/ /_/\___/_/     
   / /  /____/_      _____  _____
  / /   / __ \ | /| / / _ \/ ___/
 / /___/ /_/ / |/ |/ /  __/ /    
/_____/\____/|__/|__/\___/_/     
"""

vs = """
 _    __    
| |  / /____
| | / / ___/
| |/ (__  ) 
|___/____(_)
"""


os.system("clear")

print(bcolors.OKBLUE + logo + bcolors.ENDC)


def compare(comp_name):
    if comp_name == compare_a:
        print(bcolors.HEADER + f"Compare A: {comp_name['name']}, {comp_name['description']}, {comp_name['country']}" + bcolors.ENDC)
    else:
        print(bcolors.HEADER + f"Against B: {comp_name['name']}, {comp_name['description']}, {comp_name['country']}" + bcolors.ENDC)


def compare_score(score_a, score_b, choose):

    if score_a > score_b and choose == "a":
        return True
    elif score_a < score_b and choose == "b":
        return True
    else:
        return False


score = 0


while True:
    while True:
        compare_a = random.choice(data)
        compare_b = random.choice(data)
        if compare_a == compare_b:
            compare_a = random.choice(data)
        else:
            break
    compare(compare_a)
    print(vs)
    compare(compare_b)
    a_or_b = input("Who has more followers? Type 'A' or 'B': ").lower()
    if a_or_b != "a" and a_or_b != "b":
        os.system("clear")
        print(bcolors.FAIL + "Enter valid value. 'A' or 'B'!" + bcolors.ENDC)
    elif compare_score(compare_a["follower_count"], compare_b["follower_count"], a_or_b):
        score += 1
        print(bcolors.OKGREEN + f"You are right! Current score {score}" + bcolors.ENDC)
    else:
        print(bcolors.WARNING + f"Sorry that is wrong. Final score {score}" + bcolors.ENDC)
        break

