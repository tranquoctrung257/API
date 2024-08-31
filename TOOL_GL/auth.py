import requests
import os
from colorama import Fore
from tabulate import tabulate
from termcolor import colored
import itertools
import os
import sys
import requests
import time
from termcolor import colored
import itertools
def rainbow_text(text):
    colors = ['red', 'yellow', 'green', 'cyan', 'blue', 'magenta']
    colored_text = ''

    for char, color in zip(text, itertools.cycle(colors)):
        colored_text += colored(char, color)

    return colored_text
def main():
    checkfile = os.path.isfile('auth_gl.txt')
    if checkfile == False:
            os.system('cls' if os.name== 'nt' else 'clear')
            # banner_Tool()
            auth_gl = input(rainbow_text('nhập auth_gl : '))
            createfile = open('auth_gl.txt','w')
            createfile.write(auth_gl)
            createfile.close()
            readfile = open('auth_gl.txt','r')
            auth_gl = readfile.read()
            readfile.close()
    else:
            readfile = open('auth_gl.txt','r')
            auth_gl = readfile.read()
            readfile.close()
    os.system('cls' if os.name== 'nt' else 'clear')
    # banner_Tool()
    print(rainbow_text("Nhập 1 Để Vào Tool!"))
    print(rainbow_text("Nhập 2 Để Xóa TK Golike Cũ!"))
    print("\033[1;31m────────────────────────────────────────────────────────────")
    chon = int(input(rainbow_text('Vui Lòng Nhập Lựa Chọn Của Bạn: ')))
    if chon == 1:
         YOUTUBE(auth_gl)
    if chon == 2:
        os.remove('auth_gl.txt')
        main()
    os.system('cls' if os.name== 'nt' else 'clear')
main()