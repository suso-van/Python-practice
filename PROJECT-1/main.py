import time
import os

DELAY = 0.06      
LINE_DELAY = 1.2   

os.system("cls" if os.name == "nt" else "clear")

with open("lyrics.txt", "r", encoding="utf-8") as file:
    for line in file:
        for ch in line.rstrip("\n"):
            print(ch, end="", flush=True)
            time.sleep(DELAY)
        print()
        time.sleep(LINE_DELAY)

print("\n✨ End of lyrics ✨")