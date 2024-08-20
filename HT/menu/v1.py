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

print(rainbow_text("* * * * * * * * * * * * * * * * * * * *"))
print(rainbow_text("*         Tool Trao đổi sub           *"))
print(rainbow_text("* 1:Tool TDS TikTok & TDS TIKTOK NOW  *"))
print(rainbow_text("* 2.Tool TDS FB FULL JOD              *"))
print(rainbow_text("* ---------------------               *"))
time.sleep(0.5)
print(rainbow_text("*      Tool Golike                    *"))
print(rainbow_text("*3.Tool Golike Tiktok                 *"))
print(rainbow_text("* ---------------------               *"))
time.sleep(0.5)
print(rainbow_text("*    Tool spam sms                    *"))
print(rainbow_text("* ---------------------               *"))
time.sleep(0.5)
print(rainbow_text("* 4: Hỗ Trợ                           *"))
time.sleep(0.5)
print(rainbow_text("* * * * * * * * * * * * * * * * * * * *"))





# def Ho_tro():
#     while True:
#         clear()
#         banner_Tool()
#         print("\033[1;31m────────────────────────────────────────────────────────────")
#         print("\033[1;37m╔══════════╗")
#         print("\033[1;37m║  Hỗ Trợ  ║")
#         print("\033[1;37m╚══════════╝")
#         print("\033[1;31m[\033[1;37m=.=\033[1;31m] \033[1;37m=> \033[1;32mNhập Số \033[1;31m[\033[1;33m1\033[1;31m] \033[1;32mĐể support qua zalo ngay ")
#         print("\033[1;31m[\033[1;37m=.=\033[1;31m] \033[1;37m=> \033[1;32mNhập Số \033[1;31m[\033[1;33m2\033[1;31m] \033[1;32mĐể vào nhóm zalo cập nhật tool ")
#         print("\033[1;31m[\033[1;37m=.=\033[1;31m] \033[1;37m=> \033[1;32mNhập Số \033[1;31m[\033[1;33m3\033[1;31m] \033[1;32mĐể vào kênh yotube của tôi ")
#         print("\033[1;31m────────────────────────────────────────────────────────────")
#         print("\033[1;31m────────────────────────────────────────────────────────────")
#         nhap  = int(input(rainbow_text("vui lòng chọn: ")))
#         if nhap == 1:
#             if os.name == "nt":
#                 os.system("cmd /c start https://zalo.me/84925736962")
#                 break
#             else : 
#                 os.system("termux-open-url https://zalo.me/84925736962")
#                 break
#         elif nhap == 2:
#             if os.name == "nt":
#                 os.system("cmd /c start https://zalo.me/g/wfakde942")
#                 break
#             else: 
#                 os.system("termux-open-url https://zalo.me/g/wfakde942")
#                 break
#         elif nhap == 3:
#             if os.name == "nt":
#                 os.system("cmd /c start https://www.youtube.com/@hieutool248")
#                 break
#             else :
#                 os.system("termux-open-url https://www.youtube.com/@hieutool248") 
#                 break
