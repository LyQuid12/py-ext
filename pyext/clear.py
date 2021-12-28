import os
import platform
from time import sleep

class clear:
    def __init__(self, delay:int=None):
        if platform.uname()[0] == "Windows":
            if delay == None:
                pass
            else:
                sleep(delay)
            os.system("cls")
            
        else:
            if delay == None:
                pass
            else:
                sleep(delay)
            os.system("clear")
