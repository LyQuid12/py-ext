import sys
from time import sleep


class slowprint:
    def __init__(self, text, delay:int=0.5):
        r"""
        A class that implements the server side
        -----
        Parameters :
        - text: :class:`str` | Text you wanna print
        - delay: :class:`int` | How long does it take for the text to print. The bigger the number, the longer the text will print (Default : 0.5)
        """
        for letter in text:
            sys.stdout.write(letter)
            sys.stdout.flush()
            sleep(delay)
