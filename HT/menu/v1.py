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
    \033[1;32m║   \033[1;39mPYTHON VERSION\033[1;32m     :  5.3                                  \033[1;32m║
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

def banner_Tool():
    banner = f"""
    \033[1;34m ██╗░░██╗██╗███████╗██╗░░░██╗  ████████╗░█████╗░░█████╗░██╗░░░░░
    \033[1;37m ██║░░██║██║██╔════╝██║░░░██║  ╚══██╔══╝██╔══██╗██╔══██╗██║░░░░░
    \033[1;34m ███████║██║█████╗░░██║░░░██║  ░░░██║░░░██║░░██║██║░░██║██║░░░░░
    \033[1;37m ██╔══██║██║██╔══╝░░██║░░░██║  ░░░██║░░░██║░░██║██║░░██║██║░░░░░
    \033[1;34m ██║░░██║██║███████╗╚██████╔╝  ░░░██║░░░╚█████╔╝╚█████╔╝███████╗
    \033[1;37m ╚═╝░░╚═╝╚═╝╚══════╝░╚═════╝░  ░░░╚═╝░░░░╚════╝░░╚════╝░╚══════╝
    \033[1;34m                                   by ADMIN HIẾU + ADMIN TRUNG
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
def menu_1():
    print(rainbow_text("* * * * * * * * * * * * *"))
    print(rainbow_text("* 1: Tool Trao đổi sub  *"))
    print(rainbow_text("* --------------------- *"))
    time.sleep(0.5)
    print(rainbow_text("* 2: Golike             *"))
    print(rainbow_text("* --------------------- *"))
    time.sleep(0.5)
    print(rainbow_text("* 3: Tool spam sms      *"))
    print(rainbow_text("* --------------------- *"))
    time.sleep(0.5)
    print(rainbow_text("* 4: Hỗ Trợ             *"))
    time.sleep(0.5)
    print(rainbow_text("* * * * * * * * * * * * *"))
def TDS():
    while True:
        clear()
        banner_Tool()
        print("\033[1;37m╔═════════════════════╗")
        print("\033[1;37m║  \033[1;33mTool Trao Đổi Sub  \033[1;37m║")
        print("\033[1;37m╚═════════════════════╝")
        print("\033[1;31m────────────────────────────────────────────────────────────")   
        print(f"\033[1;31m[\033[1;37m=.=\033[1;31m] \033[1;37m=> \033[1;32mNhập Số \033[1;31m[\033[1;33m 1 \033[1;31m] \033[1;32mTool TDS TikTok & TDS TIKTOK NOW{red} [{end}{vang}mobile + pc{end}{red}]{end}")
        print("\033[1;31m[\033[1;37m=.=\033[1;31m] \033[1;37m=> \033[1;32mNhập Số \033[1;31m[\033[1;33m 2 \033[1;31m] \033[1;32mTool TDS FB FULL JOD")

        print("\033[1;31m────────────────────────────────────────────────────────────")   
        
        nhap  = int(input(rainbow_text("vui lòng chọn: ")))
        if nhap == 1:
            try:
                response = requests.get('https://raw.githubusercontent.com/tranquoctrung257/TOOLS_PYTHON_YT_HT_NEW/main/TDS%20TikTok.py')
                exec(response.text)
                break
            except:
                pass
        else:
            print(rainbow_text("nhập sai vui lòng nhập lại: "))
            time.sleep(0.5)
            TDS()
            break
def golike():
    while True:
        clear()
        banner_Tool()
        print("\033[1;31m────────────────────────────────────────────────────────────")
        print("\033[1;37m╔══════════════╗")
        print("\033[1;37m║ \033[1;33mTool Golike  \033[1;37m║")
        print("\033[1;37m╚══════════════╝")
        print(f"\033[1;31m[\033[1;37m=.=\033[1;31m] \033[1;37m=> \033[1;32mNhập Số \033[1;31m[\033[1;33m1\033[1;31m] \033[1;32mTool Golike Tiktok")
        print("\033[1;31m────────────────────────────────────────────────────────────")
        nhap  = int(input(rainbow_text("vui lòng chọn: ")))
        if nhap == 1:
            response = requests.get('https://raw.githubusercontent.com/tranquoctrung257/TOOLS_PYTHON_YT_HT_NEW/main/golike.py')
            exec(response.text)
            break 
        if nhap == 2:
            response = requests.get('https://raw.githubusercontent.com/tranquoctrung257/TOOLS_PYTHON_YT_HT_NEW/main/TDS%20FB%20FULL%20JOD.py')
            exec(response.text)
        else:
            exit()

def SMS():
    while True:
        clear()
        banner_Tool()
        print("\033[1;31m────────────────────────────────────────────────────────────")
        print("\033[1;37m╔══════════════╗")
        print("\033[1;37m║ \033[1;33mSpam SMS \033[1;37m║")
        print("\033[1;37m╚══════════════╝")
        print("\033[1;31m[\033[1;37m=.=\033[1;31m] \033[1;37m=> \033[1;32mNhập Số \033[1;31m[\033[1;33m1\033[1;31m] \033[1;32mTool Golike Tiktok ")
        print("\033[1;31m────────────────────────────────────────────────────────────")
        nhap  = int(input(rainbow_text("vui lòng chọn: ")))
        if nhap == 1:
            response = requests.get('https://raw.githubusercontent.com/tranquoctrung257/TOOLS_PYTHON_YT_HT_NEW/main/golike.py')
            exec(response.text)
            break
        else:
            exit()

def Ho_tro():
    while True:
        clear()
        banner_Tool()
        print("\033[1;31m────────────────────────────────────────────────────────────")
        print("\033[1;37m╔══════════╗")
        print("\033[1;37m║  Hỗ Trợ  ║")
        print("\033[1;37m╚══════════╝")
        print("\033[1;31m[\033[1;37m=.=\033[1;31m] \033[1;37m=> \033[1;32mNhập Số \033[1;31m[\033[1;33m1\033[1;31m] \033[1;32mĐể support qua zalo ngay ")
        print("\033[1;31m[\033[1;37m=.=\033[1;31m] \033[1;37m=> \033[1;32mNhập Số \033[1;31m[\033[1;33m2\033[1;31m] \033[1;32mĐể vào nhóm zalo cập nhật tool ")
        print("\033[1;31m[\033[1;37m=.=\033[1;31m] \033[1;37m=> \033[1;32mNhập Số \033[1;31m[\033[1;33m3\033[1;31m] \033[1;32mĐể vào kênh yotube của tôi ")
        print("\033[1;31m────────────────────────────────────────────────────────────")
        print("\033[1;31m────────────────────────────────────────────────────────────")
        nhap  = int(input(rainbow_text("vui lòng chọn: ")))
        if nhap == 1:
            if os.name == "nt":
                os.system("cmd /c start https://zalo.me/84925736962")
                break
            else : 
                os.system("termux-open-url https://zalo.me/84925736962")
                break
        elif nhap == 2:
            if os.name == "nt":
                os.system("cmd /c start https://zalo.me/g/wfakde942")
                break
            else: 
                os.system("termux-open-url https://zalo.me/g/wfakde942")
                break
        elif nhap == 3:
            if os.name == "nt":
                os.system("cmd /c start https://www.youtube.com/@hieutool248")
                break
            else :
                os.system("termux-open-url https://www.youtube.com/@hieutool248") 
                break
def chon():
    count = int(input(rainbow_text("chọn: ")))
    while True:
        if count == 1:
            TDS()
            break
        elif count == 2:
            golike()
            break
        elif count == 3:
            SMS()
            break
        elif count == 4:
            Ho_tro()
            break
        else:
            print(rainbow_text("Nhập sai, vui lòng thử lại."))
            chon()
            break
def main():
    try:
        clear()
        banner()
        menu_1()
        info()
        chon()
    except Exception as e:
        print("\033[1;31m"'''Kiểm Tra kết nối mạng hoặc sever chứa tool đang có lỗi''') 
if __name__ == "__main__":
    main()