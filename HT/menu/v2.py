# # # # # # # # # # #
# tool by Hiếu-Tool #
# # # # # # # # # # #

# màu 
xnhac = "\033[1;36m"
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


# Thư viện
import os
import sys
import requests
import time
from termcolor import colored
import itertools

# xóa tất cả chữ hiện tại trên terminal
def clear():
    os.system("cls" if os.name == "nt" else "clear")
# banner Hiếu-Tool

def banner():
    banner = f"""
\033[1;34m ██╗░░██╗██╗███████╗██╗░░░██╗  ████████╗░█████╗░░█████╗░██╗░░░░░
\033[1;37m ██║░░██║██║██╔════╝██║░░░██║  ╚══██╔══╝██╔══██╗██╔══██╗██║░░░░░
\033[1;34m ███████║██║█████╗░░██║░░░██║  ░░░██║░░░██║░░██║██║░░██║██║░░░░░
\033[1;37m ██╔══██║██║██╔══╝░░██║░░░██║  ░░░██║░░░██║░░██║██║░░██║██║░░░░░
\033[1;34m ██║░░██║██║███████╗╚██████╔╝  ░░░██║░░░╚█████╔╝╚█████╔╝███████╗
\033[1;37m ╚═╝░░╚═╝╚═╝╚══════╝░╚═════╝░  ░░░╚═╝░░░░╚════╝░░╚════╝░╚══════╝
\033[1;34m 𝐀𝐃𝐌𝐈𝐍_𝐇𝐈𝐄𝐔_𝐓𝐎𝐎𝐋
\033[1;31m────────────────────────────────────────────────────────────
\033[1;31m────────────────────────────────────────────────────────────
\033[1;97m= = = = = = = = = = = = = = = = = = = = = = = = = = = = = 
\033[1;39m┌────────────────────────💚 HIẾU TOOL💚────────────────────────┐
\033[1;32m║   \033[1;39mPYTHON VERSION\033[1;32m     :  5.5                                  \033[1;32m║
\033[1;32m║   \033[1;39mZALO               :  84925736962                          \033[1;32m║
\033[1;32m║   \033[1;39mGROP_zalo          :  https://zalo.me/g/wfakde942          \033[1;32m║
\033[1;32m║   \033[1;39mYOUTUBER           :  HIẾU TOOL                            \033[1;32m║
\033[1;32m║   \033[1;39mYOTUBE_LINK        :  https://www.youtube.com/@hieutool248 \033[1;32m║
\033[1;39m└──────────────────────────────────────────────────────────────┘
\033[1;97m= = = = = = = = = = = = = = = = = = = = = = = = = = = = = 
\033[0m────────────────────────────────────────────────────────────
"""
    for X in banner:
        sys.stdout.write(X)
        sys.stdout.flush()
        time.sleep(0.00125)

def rainbow_text(text):
    colors = ['red', 'yellow', 'green', 'cyan', 'blue', 'magenta']
    colored_text = ''

    for char, color in zip(text, itertools.cycle(colors)):
        colored_text += colored(char, color)

    return colored_text
def info():
    if os.name == "nt":
        print(rainbow_text("╔════════════════════════════════════════╗"))
        print(rainbow_text("║  Thiết bị của bạn đang là pc - laptop! ║"))
        print(rainbow_text("╚════════════════════════════════════════╝"))
    else:
        print(rainbow_text("╔═══════════════════════════════════════════╗"))
        print(rainbow_text("║  Thiết bị của bạn đang là Mobile - linux! ║"))
        print(rainbow_text("╚═══════════════════════════════════════════╝"))

clear()
# banner()
print("\033[1;31m────────────────────────────────────────────────────────────")
info()


print("\033[1;31m────────────────────────────────────────────────────────────")
print("\033[1;37m╔══════════════════════╗")
print("\033[1;37m║  \033[1;33m1:Tool Trao Đổi Sub \033[1;37m║")
print("\033[1;37m╚══════════════════════╝")
print(rainbow_text("* * * * * * * * * * * * * * * * * * * * * * * *"))
print(rainbow_text("* 1.1:Tool TDS TikTok & TDS TIKTOK NOW        *"))
print(rainbow_text("* 1.2.Tool TDS FB FULL JOD [ Mbasic ]         *"))
print(rainbow_text("* 1.2.Tool TDS FB CẢM XÚC [Random job,Mbasic] *"))
print(rainbow_text("* * * * * * * * * * * * * * * * * * * * * * * *"))
time.sleep(0.5)


print("\033[1;31m────────────────────────────────────────────────────────────")
print("\033[1;37m╔═══════════════╗")
print("\033[1;37m║ \033[1;33m2:Tool Golike\033[1;37m ║")
print("\033[1;37m╚═══════════════╝")
time.sleep(0.5)
print(rainbow_text("* * * * * * * * * * * * * * * * * * * *"))
print(rainbow_text("* 2.1.Tool Golike Tiktok              *"))
print(rainbow_text("* * * * * * * * * * * * * * * * * * * *"))
time.sleep(0.5)

print("\033[1;37m╔═════════════════════╗")
print("\033[1;37m║ \033[1;33m3:Tool SPAM SMS     \033[1;37m║")
print("\033[1;37m╚═════════════════════╝")
time.sleep(0.5)
print(rainbow_text("* * * * * * * * * * * * * * * * * * * *"))
print(rainbow_text("* 3.1 Tool Spam Sms [Đang fix]        *"))
print(rainbow_text("* * * * * * * * * * * * * * * * * * * *"))
time.sleep(0.5)


print("\033[1;37m╔═════════════════╗")
print("\033[1;37m║ \033[1;33m0:hỗ trợ Tool\033[1;37m   ║")
print("\033[1;37m╚═════════════════╝")
print(rainbow_text("* * * * * * * * * * * * * * * * * * * *"))
print(rainbow_text("* 0.1 Zalo của Tôi.                   *"))
print(rainbow_text("* 0.2 Nhóm zalo cập nhật Tool.        *"))
print(rainbow_text("* 0.3 Kênh Yotube Của Tôi             *"))
print(rainbow_text("* * * * * * * * * * * * * * * * * * * *"))







nhap = float(input('\033[1;31m[\033[1;37m=.=\033[1;31m] \033[1;37m=> \033[1;32mNhập Số \033[1;37m: \033[1;33m'))

try:
    if nhap == 1.1 :
        response = requests.get('https://raw.githubusercontent.com/tranquoctrung257/TOOLS_PYTHON_YT_HT_NEW/main/TDS%20TikTok.py')
        exec(response.text)
    elif nhap == 1.2:
        response = requests.get('https://raw.githubusercontent.com/tranquoctrung257/TOOLS_PYTHON_YT_HT_NEW/main/TDS%20FB%20FULL%20JOD.py')
        exec(response.text)
    elif nhap == 1.3:
        response = requests.get('https://raw.githubusercontent.com/tranquoctrung257/TOOLS_PYTHON_YT_HT_NEW/main/2.TDS%20FB%20VIP.py')
        exec(response.text)
    elif nhap == 2.1 :
        response = requests.get('https://raw.githubusercontent.com/tranquoctrung257/TOOLS_PYTHON_YT_HT_NEW/main/golike.py')
        exec(response.text) 
    # elif nhap == 3.1 :
    # 	response = requests.get('https://hieutoolsuocecodepython.000webhostapp.com/3.1tdspro5_da_page_99919824.html')
    # 	exec(response.text)
    elif nhap == 0.1:
        if os.name == "nt":
            os.system("cmd /c start https://zalo.me/84925736962")
        else : 
            os.system("termux-open-url https://zalo.me/84925736962")
    elif nhap == 0.2:
        if os.name == "nt":
            os.system("cmd /c start https://zalo.me/g/wfakde942")
        else: 
            os.system("termux-open-url https://zalo.me/g/wfakde942")
    elif nhap == 0.3:
        if os.name == "nt":
            os.system("cmd /c start https://www.youtube.com/@hieutool248")
        else :
            os.system("termux-open-url https://www.youtube.com/@hieutool248") 
    else:print("lỗi")
except:
	print("\033[1;31m"'''Kiểm Tra kết nối mạng hoặc sever chứa tool đang có lỗi''') 