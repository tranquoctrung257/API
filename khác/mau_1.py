from colorama import *

# định dạng văn bản
# print(Style.DIM + 'This text is bright')
# print(Style.NORMAL + 'This text is bright')
# print(Style.BRIGHT + 'This text is bright')
# print(Style.RESET_ALL + 'This text is bright')

# màu nền 
# BLACK
# RED
# GREEN
# YELLOW
# BLUE
# MAGENTA
# CYAN
# WHITE
# RESET
# print(Back.RESET + 'This background is yellow')


# màu chữ
# BLACK
# 
# GREEN
# YELLOW
# BLUE
# MAGENTA
# CYAN
# WHITE
# RESET
# print(Fore.MAGENTA + 'This is a text')

from rich.console import Console
from rich.text import Text

console = Console()

text = Text("This is a rainbow text!")
text.stylize("bold red", 0, 5)
text.stylize("bold orange3", 5, 8)
text.stylize("bold yellow", 8, 11)
text.stylize("bold green", 11, 13)
text.stylize("bold blue", 13, 16)
text.stylize("bold purple", 16, 21)

# console.print(text)

from termcolor import colored
import itertools

def rainbow_text(text):
    colors = ['red', 'yellow', 'green', 'cyan', 'blue', 'magenta']
    colored_text = ''

    for char, color in zip(text, itertools.cycle(colors)):
        colored_text += colored(char, color)

    return colored_text

# print(rainbow_text("This is a rainbow text!"))

import time
import sys
from colorama import Fore, Style, init

init(autoreset=True)

colors = [Fore.RED, Fore.YELLOW, Fore.GREEN, Fore.CYAN, Fore.BLUE, Fore.MAGENTA]

# def moving_rainbow_text(text, delay=0.1):
#     for _ in range(len(text) * 5):  # Lặp đủ số lần để tạo hiệu ứng chạy
#         for i, char in enumerate(text):
#             sys.stdout.write(colors[(i + _) % len(colors)] + char)
#         sys.stdout.flush()
#         time.sleep(delay)
#         sys.stdout.write('\r')  # Quay lại đầu dòng để ghi đè
#     print(Style.RESET_ALL)  # Đảm bảo màu sắc được đặt lại

# moving_rainbow_text("This is a moving rainbow text!")

# print(" xin chào ")
trang='[1;37m'
from time import sleep
def lthd_delay(delay):
    #while(o>0):
    for o in range(delay,-1,-1):
        #o=o-1
        print(f'{trang}[\033[1;31mH\033[1;33mĐ\033[1;36m~\033[1;35mT\033[1;34mO\033[1;32mO\033[1;35mL\033[1;37m]\033[1;37m[\033[1;36m|\033[1;37m]\033[1;37m[.....]\033[1;37m[{o}]','     ',end='\r');sleep(1/6)
        print(f'{trang}[\033[1;35mH\033[1;32mĐ\033[1;34m~\033[1;35mT\033[1;36mO\033[1;33mO\033[1;31mL\033[1;37m]\033[1;37m[\033[1;31m/\033[1;37m]\033[1;37m[\033[1;32m>\033[1;37m....]\033[1;37m[{o}]','     ',end='\r');sleep(1/6)
        print(f'{trang}[\033[1;31mH\033[1;33mĐ\033[1;36m~\033[1;35mT\033[1;34mO\033[1;32mO\033[1;35mL\033[1;37m]\033[1;37m[\033[1;32m-\033[1;37m]\033[1;37m[\033[1;32m>\033[1;31m>\033[1;37m...]\033[1;37m[{o}]','     ',end='\r');sleep(1/6)
        print(f'{trang}[\033[1;35mH\033[1;32mĐ\033[1;34m~\033[1;35mT\033[1;36mO\033[1;33mO\033[1;31mL\033[1;37m]\033[1;37m[\033[1;33m+\033[1;37m]\033[1;37m[\033[1;32m>\033[1;31m>\033[1;36m>\033[1;37m..]\033[1;37m[{o}]','     ',end='\r');sleep(1/6)
        print(f'{trang}[\033[1;31mH\033[1;33mĐ\033[1;36m~\033[1;35mT\033[1;34mO\033[1;32mO\033[1;35mL\033[1;37m]\033[1;37m[\033[1;34m\{trang}]\033[1;37m[\033[1;32m>\033[1;31m>\033[1;36m>\033[1;33m>\033[1;37m.]\033[1;37m[{o}]','     ',end='\r');sleep(1/6)
        print(f'{trang}[\033[1;35mH\033[1;32mĐ\033[1;34m~\033[1;35mT\033[1;36mO\033[1;33mO\033[1;31mL\033[1;37m]\033[1;37m[\033[1;35m|\033[1;37m]\033[1;37m[\033[1;32m>\033[1;31m>\033[1;36m>\033[1;33m>\033[1;35m>\033[1;37m]\033[1;37m[{o}]','     ',end='\r');sleep(1/6)
# lthd_delay(3)
print(trang)
