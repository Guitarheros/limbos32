from shutil import which
from os import system
from _thread import start_new_thread
from time import sleep

w1 = which("python")
w2 = which("python3")
cmd = "python" if (w2==None or (w1!=None and ("WindowsApps" in w2))) else "python3"

counted = 0


def threadeded():
    global counted
    system(cmd+" main.py")
    counted -= 1


for _ in range(8):
    counted += 1
    start_new_thread(threadeded, ())
    sleep(0.23)

while counted:
    sleep(0.1)
