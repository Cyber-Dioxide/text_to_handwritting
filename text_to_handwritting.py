import random
import sys
import time

from pywhatkit import text_to_handwriting
from colorama import Fore
import fontstyle

from pyfiglet import figlet_format
col = ["cyan","purple","yellow","blue","red"]
r = random.choice(col)

t = figlet_format("Text")
to = figlet_format("to")
h = figlet_format("hand")
w = figlet_format("writting")
print(fontstyle.apply(t , r))
m = random.choice(col)
print(fontstyle.apply(to , m))
n = random.choice(col)
print(fontstyle.apply(h , n))
o = random.choice(col)
print(fontstyle.apply(w , o))

print("------------------------------------------------------------------------------------")
print(fontstyle.apply("Saad Khan \nFollow me on instagram @saadkhan041","bold/underline/cyan"))
print()
print("---------- Auther = Saad Khan --------------")
comf = " "
while comf != "n" and "no":
    def sprint(str):
        for i in str + '\n':
            sys.stdout.write(i)
            sys.stdout.flush()
            time.sleep(5 / 90)


    text = input(f"{Fore.LIGHTYELLOW_EX}Type the data you want to convert to hand writting: ")
    r = int(input(f"{Fore.LIGHTRED_EX}Type range of red color from 0~255: "))
    g = int(input(f"{Fore.LIGHTGREEN_EX}Type range of green color from 0~255: "))
    b = int(input(f"{Fore.LIGHTBLUE_EX}Type range of blue color from 0~255: "))
    sprint(f"{Fore.LIGHTMAGENTA_EX}Wait for few seconds__________________________")

    try:
        text_to_handwriting(text, rgb=(r, g, b))
        sprint(f"{Fore.LIGHTWHITE_EX}Done \nNow type cd and then cd angain\nselect this directory and type ls\ncopy .png or .jpg file to "
              "phone storage\nNow download an app from playstore that converts\ntext from image into pdf\nsend that pdf to your teacher\n")
    except ValueError:
        print("Type numerical data while selecting range of colors")

    comf = input(f"{Fore.LIGHTCYAN_EX}Do you want to continue? [y/n]:").lower()




