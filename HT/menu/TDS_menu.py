
do = "\033[1;31m"
luc = "\033[1;32m"
vang = "\033[1;33m"
xduong = "\033[1;34m"
tim = '\033[1;39m'
hong = "\033[1;35m"
trang = "\033[1;37m"
whiteb = "\033[1;37m"
red = "\033[0;31m"
redb = "\033[1;31m"
end = '\033[0m'
import requests
import os, json, sys, requests 
from sys import platform
from time import sleep
from datetime import datetime
from random import randint
from pystyle import Colors, Colorate
import uuid, re
from bs4 import BeautifulSoup
import time
import sys
from termcolor import colored
import itertools
def rainbow_text(text):
    colors = ['red', 'yellow', 'green', 'cyan', 'blue', 'magenta']
    colored_text = ''

    for char, color in zip(text, itertools.cycle(colors)):
        colored_text += colored(char, color)

    return colored_text

print("\033[1;37m╔═════════════════════╗")
print("\033[1;37m║  \033[1;33mTool Trao Đổi Sub  \033[1;37m║")
print("\033[1;37m╚═════════════════════╝")
print("\033[1;31m────────────────────────────────────────────────────────────")   
print(f"\033[1;31m[\033[1;37m=.=\033[1;31m] \033[1;37m=> \033[1;32mNhập Số \033[1;31m[\033[1;33m 1 \033[1;31m] \033[1;32mTool TDS TikTok & TDS TIKTOK NOW{red} [{end}{vang}mobile + pc{end}{red}]{end}")
print("\033[1;31m[\033[1;37m=.=\033[1;31m] \033[1;37m=> \033[1;32mNhập Số \033[1;31m[\033[1;33m 2 \033[1;31m] \033[1;32mTool TDS FB FULL JOD")

print("\033[1;31m────────────────────────────────────────────────────────────")   
chon  = int(input(rainbow_text("vui lòng chọn: ")))
if chon == 2 :
    response = requests.get('https://raw.githubusercontent.com/ht2083927493/tool/main/1.TDS%20FB%20FULL%20JOD.py')
    exec(response.text)
else:
    exit()

