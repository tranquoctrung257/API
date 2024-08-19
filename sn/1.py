import time
import colorama
import os
import sys
from colorama import Fore, Style, init

den = "\033[1;90m"
luc = "\033[1;32m"
trang = "\033[1;37m"
red = "\033[1;31m"
vang = "\033[1;33m"
tim = "\033[1;35m"
lamd = "\033[1;34m"
lam = "\033[1;36m"
hong = "\033[1;95m"
dong_mau = "\033[0m"
def chuc():
    s = f"""
    {den}⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣶⣦⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    {luc}⠀⠀⠀⠀⠀⠀⠀⠀ ⣴⡿⣿⣿⠿⣿⣿⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    {trang}⠀⠀⠀⠀⠀⠀⠀⠀⣾⣿⣿⡟⠁⢀⣾⣿⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    {red}⠀⠀⠀⠀⠀⠀⠀⣼⣿⣿⡏⣀⣴⣿⡿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    {vang}⠀⠀⠀⠀⠀⠀⣸⣿⣿⣿⣿⠿⠛⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    {tim}⠀⠀⠀⠀⠀⠘⣿⣿⣿⣧⣴⣶⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    {lamd}⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⠟⣻⣿⣿⠦⠀⠀⠀⣠⣤⣤⣄⣀⠀⠀⠀⠀⣀⡀⠀⠀⢀⣀⣀⡀⠀⠀⣄⣀⡀⠀⣠⣤⣤⡄⠀⠀⣾⣶⠀⠀⣿⣟⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    {lam}⠀⠀⠀⠀⠀⢸⣿⣿⣿⠃⢠⣿⣿⠃⠀⠀⢠⣾⣿⡿⠿⢿⣿⡄⠀⠀⠀⢹⣿⣿⣴⣿⣿⣿⣧⠀⠀⢹⣿⣿⣾⡿⠿⣿⣷⡀⠀⣿⣿⡆⠀⢻⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    {den}⠀⠀⠀⠀⠀⠈⠻⠿⠃⢠⣿⣿⠏⠀⢀⣤⣿⣿⠏⠀⠀⣸⣿⡄⠀⠀⠀⢸⣿⣿⣿⠃⠈⣿⣿⡆⠀⢸⣿⣿⡿⠀⠀⣿⣿⡇⣠⣿⣿⣇⠀⣾⣿⣿⣿⣧⠀⠀⢀⡀⠀⠀⠀⠀⠀
    {luc}⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⣿⠏⣠⣴⣿⠏⣿⣿⡄⠀⣠⣿⣿⡇⠀⣦⡄⢸⣿⣿⡇⠀⢠⣿⣿⣷⡾⠃⣿⣿⡇⠀⢠⣿⣿⣿⠟⠉⠿⣿⣿⡿⠇⢿⣿⣿⣠⣾⣿⠇⠀⠀⠀⠀⠀
    {trang}⠀⠀⠀⠀⠀⠀⠀⠀⠀⠻⣿⣿⣿⠟⠁⠀⠘⢿⣿⣿⣿⣿⣿⣇⣼⣿⣩⣿⣿⣿⡇⣠⣿⡿⠟⠉⢠⣾⣿⣿⣇⣴⣿⠿⠋⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⡟⠁⠀⠀⠀⠀⠀⠀
    {red}⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⠀⠀⠀⠀⠀⠀⠉⠉⠀⠻⣿⡿⠟⣽⣿⠛⣿⣿⡟⠛⠉⠀⠀⢀⣿⡏⢿⣿⣯⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣾⣿⣿⡏⠀⠀⠀⠀⠀⠀⠀⠀
    {vang}⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⡟⠀⣿⣿⡇⠀⠀⠀⠀⣸⣿⠃⢸⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⣿⡿⢹⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀
    {tim}⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⡇⠀⣿⣿⠇⠀⠀⠀⠀⢿⣿⡄⢸⣿⣿⠀⠀⠀⠀⠀⠀⠀⠄⢰⣿⡿⠁⣼⣿⣿⠁⠀⠀⠀⠀⠀⠀⠀⠀
    {lamd}⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣿⣷⣴⣿⣿⠀⠀⠀⠀⠀⠸⣿⣷⣼⣿⡟⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣧⣴⣿⣿⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀
    {lam}⠀⠀⠀⠀⠀⠀⣠⣾⣿⣿⣿⣿⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠻⠿⠛⠁⠀⠀⠀⠀⠀⠀⠈⠛⠛⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠘⣿⣿⣿⡿⠋⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀
    {hong}⠀⢀⡀⠀⢠⣾⣿⣿⠟⠁⣸⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠀⠀⠀⡈⠀⠀⠀⠀⠀⠀⠀⠀
    {den}⠀⢼⣧⣠⣿⣿⡿⠁⣀⣼⣿⠟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⡀⠀⠀⠀⠀⢰⣿⣿⣿⣷⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀
    {luc}⠀⠈⣿⣿⣿⣿⣶⣿⠿⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡀⠀⠀⢀⣴⣿⣿⢿⣿⣆⠀⠀⠀⢸⣿⡏⠈⣿⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠕⠀⠀⠀⠀⠀⠀⠀⠀⠀
    {trang}⠀⣼⣿⣿⡿⣄⣀⡀⠀⠀⠀⣿⣿⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣿⠀⠀⣼⣿⣿⠃⢠⣿⡟⠀⠀⠀⢸⣿⣇⠀⣿⡿⠀⠀⠀⠀⠀⠀⠀⠀⣀⠀⠈⢺⣿⣶⣄⠀⠀⠂⠀⠀⠀
    {red}⢰⣿⣿⣿⣿⠿⢿⣿⣶⢶⣾⣿⠛⠁⠀⣠⣶⡄⠀⠀⠀⣤⣤⣾⣿⡏⠀⢰⣿⣿⢃⣴⣿⠟⠁⠀⠀⠀⠸⣿⣿⣼⣿⠃⠀⠀⠀⣀⣠⣄⠀⠀⢿⣿⡄⠀⢻⣿⣿⣷⡀⠀⠀⠀⠀
    {vang}⢿⣿⡿⠉⠀⠀⠀⣿⣿⣾⣿⣿⠉⠁⠙⢿⣿⣇⣀⣀⡀⢉⣿⣿⣿⢿⡇⣸⣿⣿⠟⠋⠁⠀⠀⠀⠀⠀⠀⢻⣿⣿⠁⠀⠀⢠⣿⡿⠛⢿⣇⠀⠘⣿⣷⡀⠈⣿⣿⣿⣿⡄⢀⣾⡷
    {tim}⣿⣿⣦⣀⣀⣠⣾⣿⣿⣿⣿⠇⢀⣀⠀⣾⡿⢻⣿⡿⠀⢠⣿⣿⠋⠀⠘⣿⣿⣿⣾⣿⣿⣶⠄⠀⠀⣠⣤⣭⣿⣿⡄⠀⢠⣿⣿⠁⠀⢸⣿⡆⠀⣿⣿⣷⣾⡿⠠⢻⣿⣿⣾⡿⠁
    {lamd}⠀⠈⠛⠿⠿⠿⠟⠋⣿⣿⣏⣴⣿⣟⣼⠟⠀⣼⣿⠃⠀⢸⣿⣿⠀⠀⠀⢹⣿⣿⡟⢠⣿⡟⠀⠀⣾⣿⠟⠙⠻⣿⣿⣄⣾⡿⣿⣧⣠⣼⣿⣷⣽⣿⠀⠉⠉⠀⠀⠈⣿⣿⣿⠀⠀
    {lam}⠀⠀⠀⠀⠀⠀⠀⠀⢿⣿⣿⡿⣿⣿⠏⠀⢠⣿⡿⠀⣴⣾⣿⡿⠀⣀⣴⣿⣿⣿⠡⣸⣿⠇⢀⣴⣿⣿⡀⡀⢠⣿⡿⣿⡟⠀⠊⠛⡛⠛⠙⠛⠛⠃⠀⠀⠀⠀⢠⣿⣿⣿⣿⡄⠀
    {hong}⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠀⠀⠙⠃⠀⠀⢸⣿⣧⣾⡿⢹⣿⣿⣶⣿⡿⠁⠀⠀⠀⣿⣿⣠⣿⠟⠈⠻⠿⠿⠿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⠀⠀⠀⠀⣀⣿⣿⠈⣿⣿⡇⠀
    {den}⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⠿⠋⠁⠀⠻⠿⠟⠁⠀⠀⠀⠀⠀⠙⠿⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⢀⣿⣿⡇⠀
    {luc}⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡄⠀⠘⣿⣿⣿⣿⡿⠀⠀
    {trang}⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠀⠀⠄⢀⠀⠈⠛⠛⠛⠁⠀⠀
    """
    os.system('cls')  
    for h in s:
       sys.stdout.write(h)
       sys.stdout.flush()
       time.sleep(0.00001)
# chuc()
init(autoreset=True)

colors = [Fore.RED, Fore.YELLOW, Fore.GREEN, Fore.CYAN, Fore.BLUE, Fore.MAGENTA]



def moving_rainbow_text(text, delay=0.1):
    for _ in range(len(text)):  # Lặp đủ số lần để tạo hiệu ứng chạy
        for i, char in enumerate(text):
            sys.stdout.write(colors[(i + _) % len(colors)] + char)
        sys.stdout.flush()
        time.sleep(delay)
        sys.stdout.write('\r')  # Quay lại đầu dòng để ghi đè
        Style.RESET_ALL  # Đảm bảo màu sắc được đặt lại

# moving_rainbow_text("Chúc mừng sinh nhật! Mong rằng tất cả những ước mơ của bạn đều trở thành hiện thực và mỗi ngày đều ngập tràn niềm vui, hạnh phúc. Chúc bạn luôn mạnh khỏe, thành công và gặp nhiều may mắn trong cuộc sống!")

bsn =f"""
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡏⠉⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠛⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢿⡿⠟⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠁⣸⣇⠈⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡏⠉⣙⠛⢁⡄⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣄⠈⠉⢁⣄⡈⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢯⣿⣇⠀⢿⡿⠀⢹⣿⣽⣻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡄⠙⣿⣿⣧⣀⡉⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⢿⡽⣿⣦⣀⣡⣴⣿⣿⣻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠁⠾⠛⢿⡏⢀⣤⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣄⣈⣿⣿⣿⣿⣿⣿⣿⣿⢿⡿⣿⠋⢉⡉⠉⠉⠉⣿⣟⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⣴⣶⣦⡀⠁⣸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣞⣿⠀⢸⣿⣿⡇⠀⣿⣾⣻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣾⣿⠀⢸⣷⣿⡇⠀⣿⣷⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⢈⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣍⣻⣋⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢿⣟⣯⡿⣽⢯⡽⣿⠀⢸⣿⣿⡇⠀⣿⣧⢯⣽⣯⢿⣻⣿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣇⣀⡀⠀⣻⣿⣿⣿⣿⣿⣿⣿⣿⣩⣿⡙⣿⣿⣿⣿⣿⣿⣿⣿⣟⣯⣟⣿⣯⢷⣻⡽⢾⣽⣿⠀⢸⣿⣿⡇⠀⣿⡾⣽⣺⣽⣻⣯⣟⣿⡿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠙⢿⡿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣇⠈⣉⠈⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣟⣿⣻⣾⡿⢿⣿⡟⣿⣿⣽⡿⢿⣟⣶⣾⣿⣿⣧⣴⣛⡛⢿⣷⣽⡿⢟⣻⡟⢿⣿⣻⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠁⣠⣤⠀⣸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣏⠀⣹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣯⣷⡿⣿⡿⣿⠐⢿⡿⣿⢌⣿⢿⢰⣿⢿⣿⣎⣿⣿⠡⡿⣿⣿⡎⣿⠿⢁⠾⣿⢿⡎⢿⣿⠿⡿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⡄⠘⢉⣀⢹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡏⢾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡶⢹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣳⣿⡇⣽⣿⣿⢿⣿⣿⣻⣿⠿⣿⣽⢯⣿⣿⢿⣿⣽⣿⣽⡿⢿⣽⢯⣟⣿⡿⣿⣟⣿⣿⣿⢿⣿⣟⢸⣿⣯⣿⣿⣿⣿⣿⣟⠻⣿⣿⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣟⣿⡧⣘⣻⣼⣦⣛⠻⣟⣥⣾⣌⡛⣿⣻⣥⣧⣙⠻⡟⣯⣼⣎⡹⠿⣿⣡⣷⣌⡻⢿⣏⣥⣯⣙⣛⣾⣿⢷⣻⣽⣿⣿⣿⣿⡷⣾⣷⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣻⣿⡁⢹⣿⡿⣿⢿⣿⡿⣿⢿⣿⣿⡿⣿⢿⡿⣿⣿⡿⣿⢿⡿⣿⣿⡿⣿⢿⣿⣿⣿⣿⢿⣿⣿⡏⢙⣿⣟⣿⣻⢿⣿⣿⣧⣴⣿⣧⣙⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠻⣿⡿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣯⣷⣻⣿⡇⢸⣿⡿⣭⣟⡾⣽⣏⣿⣻⢾⡽⣏⡿⣽⣳⢯⡿⣽⣫⣟⡷⣯⡽⣯⡿⣞⣳⢯⣞⣯⣟⣿⡇⢀⣿⣟⡾⣽⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣻⡿⠀⣆⠘⠿⣿⣾⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣟⣷⣿⡇⢸⣿⣟⡷⣯⣟⣷⣻⣾⡽⣯⢿⣽⣻⢷⣯⣿⣽⣳⣟⡾⣽⣳⡟⣷⣿⣽⣯⣟⣾⣳⣯⣿⡇⢀⣿⣯⣟⡷⣿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠋⣉⣁⣰⣿⣦⣀⡴⠀⢠⣿⣿⣿⣿⣿⣿⡿⣽⣞⣷⠟⣯⣯⣷⠸⣿⣿⡼⣷⡾⢻⣿⣍⡛⢿⣾⢶⣯⡿⢻⣭⣟⡙⢿⣟⣷⣳⡿⢛⣿⣯⣛⠿⣾⣳⢷⣿⠷⣼⣯⣝⠻⣿⣽⣻⣾⢿⣿⣿⣿⣿⣿⣿⡿⣿⣿⡿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⣄⡈⠻⣿⣯⢿⡟⠁⣶⣿⣿⣿⣿⣿⣿⣷⡿⢿⡿⠇⡺⠿⡿⢿⢷⡸⠿⠿⠟⠸⠿⢿⠿⢿⣎⠿⠿⠿⠰⠿⠿⡿⠿⣖⡻⠿⠿⡱⠿⠿⠿⠿⣶⣽⠿⢿⠃⢿⠿⠿⠿⡷⠹⣿⠿⢿⣿⣿⣿⣿⣿⣿⣷⣄⠈⢻⣿⠋⢋⠉⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⣿⡇⢠⡿⠋⠙⠻⠦⢹⣿⣿⣿⣿⣟⣿⡟⣲⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡦⣹⣿⣯⣿⣿⣿⣿⣿⣧⣀⣁⣱⣿⣧⡀⠉⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣇⢈⣠⣾⣿⣦⣤⣤⣿⣿⣿⣿⣻⣿⡇⣽⣿⣿⣿⣯⢿⡽⣾⠽⣯⣿⡽⣏⡿⣾⢽⣻⣿⣽⣳⢯⣟⡾⣽⣯⣷⢯⣟⡾⣝⣯⣿⣿⣽⣫⢿⣹⢯⣿⣿⣽⣛⡾⣽⢯⣿⣿⣿⣿⡷⢸⣿⣿⣟⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⢾⣿⣿⣋⢿⣿⣽⣾⣿⡿⢋⢿⣿⡽⣯⢿⣿⠟⢻⣯⡿⣾⣽⣷⠟⢻⣿⣾⣽⣻⣾⠟⢹⣷⣯⢿⣽⣿⠟⠹⣷⣯⢿⣽⣿⠟⡹⣿⣿⡿⢸⣿⡿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⣾⣿⣧⣟⣻⣦⣿⣦⣙⣛⢛⣭⣱⣿⣦⣍⣛⣛⢫⣴⣾⣦⣍⣛⡛⣋⣥⣾⣷⣌⣛⡛⣋⣵⣾⣧⣜⣋⢟⣋⣥⣾⣷⣌⣛⢛⣋⣵⣾⣷⣬⣙⣛⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠁⢹⣿⣿⣻⣟⡿⣿⣿⢿⣿⣻⣟⣿⣿⣿⣿⡿⣟⡿⣿⣿⣿⣿⡿⣿⣻⢿⣿⣿⣿⢿⣻⣟⡿⣿⣿⣿⡿⣟⡿⣿⡿⣿⣿⢿⣻⣽⣿⣿⡏⠉⣿⣷⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⣽⣿⠀⢸⣿⣯⡝⣯⣽⣛⣞⠿⣼⣳⣭⣿⣽⣞⡽⣽⢯⣽⡳⣏⢿⣹⣽⣧⣿⣯⣯⡝⣯⣛⠷⣯⣽⢫⣟⣭⣿⣭⣿⣱⢿⣹⣏⡯⢷⣹⢽⣿⡇⢸⣿⣯⢿⣽⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢿⡽⣿⠄⣄⡉⠙⠻⣷⣞⣽⣾⠿⠛⢉⣁⣀⣀⠉⠛⢿⣿⣖⣻⣽⠿⠋⠉⣀⣀⡉⠉⠻⢷⣯⣿⣽⡾⠟⠉⣁⣀⣀⠉⠙⠿⣷⣞⣽⣿⠾⠋⢉⡅⠐⣿⣯⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⣿⢿⣿⠀⢸⣿⣶⣄⣀⡉⠉⢁⣠⣴⣾⢿⠿⣿⢷⣦⣀⣈⡉⠉⣀⣠⣶⣿⢿⡿⢿⣶⣤⣀⡈⠉⢁⣀⣴⣾⡿⢿⡿⣿⣦⣄⣀⡉⠉⣀⣠⣶⢿⡇⠀⣿⡿⣾⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣯⢿⣿⣳⢯⣞⣿⠀⢸⣷⠺⣽⢻⡿⢿⡿⣟⣿⡹⢮⡟⣶⣫⣞⢿⣻⢿⡿⣿⢻⣳⢎⡿⣞⣧⢯⡟⡿⢿⡿⣿⠿⣏⣷⣹⢳⢾⣱⣟⡿⣻⢿⠿⣟⢿⡩⣿⡇⠐⣿⣻⣽⢯⣿⣿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣻⣽⡿⣿⣯⢿⣽⣺⣿⡀⢸⣿⣟⣬⢳⡝⣯⢞⡽⣮⣽⢻⣼⣣⢷⣭⣳⡽⢮⣳⣭⣟⣼⣫⡞⣷⢎⣯⡽⣹⣏⣾⣱⣯⣛⡶⣭⣛⣮⢳⡻⣵⣫⣞⡽⣱⣎⡵⣿⡇⠀⣿⡷⣯⡿⣽⣿⣻⣯⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠻⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⢿⣿⣧⡀⠙⠛⠙⠋⠛⠉⠛⠙⠉⠙⠋⠙⠉⠋⠉⠙⠙⠋⠉⠉⠉⠋⠙⠙⠋⠋⠙⠙⠋⠉⠉⠙⠉⠋⠙⠉⠋⠙⠋⠙⠋⠉⠙⠙⠉⠛⠛⠋⢁⣸⣿⣽⠟⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣾⣿⢿⣿⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣾⣿⡿⢿⣿⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠿⠿⣿⣿⣿⢿⡿⣿⢿⣟⡿⣿⡿⠿⠿⣿⣻⢟⡿⣻⣟⣿⣻⢿⣯⣟⢿⣻⠿⠿⢿⣿⣻⣟⡿⢿⣻⡟⣿⠻⣟⡻⣿⣿⠿⠿⠿⠛⠛⠿⠻⠿⠿⢯⣿⡝⢯⠿⡝⣯⢿⡹⣯⡿⠿⠿⠿⠻⠛⠿⠷⠿⠿⣷⣿⠟⣞⡻⡽⣻⠟⣿⣿⣿⣿⣟⢿⣻⢿⡿⣿⠿⣿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠋⢠⣶⣄⠈⢿⣟⣿⡽⣯⣟⡾⣷⠏⢀⣴⣤⠈⢻⣿⡽⣷⣻⢾⣽⣻⡾⣽⡟⠁⣤⣤⡀⠹⣷⣿⢾⣷⣳⢿⣳⣟⣮⡿⠋⣀⣤⣤⣴⣶⣶⣶⣶⣦⣤⣄⡈⠙⠳⣾⡜⣦⢧⡟⢁⣠⣤⣤⣶⣶⣶⣶⣶⣤⣤⣀⡉⠙⢷⣽⢳⢯⣿⠏⢁⣤⣄⠙⢿⣽⣻⢾⣳⣟⣯⢿⡿⠋⣰⣦⡈⢻⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣟⠀⣻⣿⣿⠀⢸⣿⡷⣿⣽⡾⣽⣿⠀⢸⣿⣿⡇⢸⣿⡿⣽⣯⣟⣷⡿⣽⡟⠁⣼⣿⢿⣷⡀⠹⣿⣻⣾⣯⣟⣷⣻⢾⡇⢰⣿⠿⣽⠷⠿⠾⠷⠿⠾⢽⣿⢿⣷⣄⠘⢿⡼⣿⠀⢸⣿⢯⡿⠷⠿⠶⠿⠾⠯⣿⣟⣿⣦⡀⠹⣯⣟⣿⡀⢸⣿⣿⣦⡀⠻⣯⣟⣷⣻⣾⡏⢁⣴⣿⣿⡇⢈⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⢿⣻⣿⠀⢸⣿⣽⣳⣭⢿⣹⣿⠀⢸⣿⣿⡇⢸⣯⡽⣧⣟⣾⣳⢯⡿⠁⣼⣿⣹⣎⡿⣧⠀⢻⣯⢷⣯⢾⣭⢯⣿⡇⢸⣿⣻⡇⠀⣦⣴⣤⣤⣤⣄⠉⢻⣼⣿⡆⠘⣿⡽⣧⣾⢯⣻⡇⢸⣦⣤⣤⣤⣤⡀⠙⢷⣯⢿⡄⢸⣯⢾⣷⡀⠙⢯⣿⣿⣄⠈⢿⣖⡿⠋⢠⣿⣿⣿⠏⢀⣾⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⣻⣟⣿⠀⢸⣿⣾⣵⣯⣿⣽⣿⡄⢸⣿⣿⡇⢸⣿⣽⣻⣞⡷⣯⡿⠁⣸⣿⣳⡟⠹⣿⣽⣧⠀⢻⣿⣼⣻⡼⣛⣾⡇⢸⣿⣿⣷⣠⣿⣿⡿⣟⡿⣿⡇⠈⣿⣾⣷⠀⣿⣿⡿⢿⣧⢿⡇⢸⣿⣝⣻⣟⣿⣿⡆⢸⣯⢿⡇⠀⣿⣯⢟⣿⣆⠈⠻⣾⣿⣧⡀⠻⢁⣰⣿⣿⡿⠁⣰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡀⣽⣿⢿⣦⣀⣀⣀⣀⣀⣤⣠⣤⣤⣾⣿⣻⡇⢸⣿⢷⡻⣞⠿⣿⠃⣸⣿⢯⡟⢠⡆⠹⣞⡿⣇⠈⢿⣞⡷⣻⢟⣾⡇⢸⣿⣻⣿⠿⠿⠷⠿⠟⠛⢉⣠⣾⣿⣻⡏⢠⣿⣿⡄⢸⣿⣻⡇⢸⣿⢾⠷⠟⠋⢁⣤⣾⡿⣿⠇⢸⣿⣯⡿⣿⢿⣷⣀⢹⣿⣿⣿⣦⣾⡿⣿⠏⢀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣯⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠷⣿⡇⢸⣿⣯⢷⣯⣿⣷⣶⣿⣯⡟⠁⣼⣷⡀⢹⣿⢿⣇⠈⢿⣾⣹⠾⣽⡇⢸⣿⣿⣿⣶⣦⣶⣶⣶⣿⣿⣿⣿⡿⢋⣠⣿⡿⣾⡇⢸⣿⢿⣷⣾⣿⣿⣶⣶⣾⣿⣿⣯⠟⠁⣠⣿⣿⣿⣿⣿⣻⣿⣿⣿⣿⣿⣿⣿⣟⡿⠃⣠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠉⢿⣿⣿⠉⢡⣀⣀⣀⣀⣹⣠⣬⠉⢹⣿⣿⡇⢸⣿⣯⣿⣼⠿⣿⣿⣿⣿⣧⣾⣿⣿⣷⣴⣿⣿⣿⣆⠈⣿⣽⣻⣽⣇⢸⣿⣿⣿⡿⠿⠿⠿⠿⠿⣿⣿⣿⣿⣿⣿⣿⣽⣿⡇⢸⣿⣯⣿⣿⣿⣾⡿⠿⠿⠋⠉⣁⣤⣾⣿⣿⣿⣿⣿⣾⣿⣷⣿⣿⣿⠀⣿⣯⣿⠁⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⠀⣻⣯⣿⠀⢸⣿⣿⡿⣿⡿⣿⣿⡆⢸⣿⣿⣧⣾⠿⠿⢿⣯⣴⣿⣷⣧⡿⠿⠿⠯⠿⢿⢿⡿⣷⣻⣿⡆⠘⣷⣭⢿⣿⣿⣿⣿⣿⣶⣦⣴⣴⣶⠟⣿⣿⡇⣿⣿⣟⣮⢷⣿⡇⢸⣿⣾⣿⢏⣿⡟⣷⣦⣶⣶⣿⣿⣿⣿⣟⣯⣿⣿⣿⣿⣿⣿⣽⣾⣿⠀⣿⣿⣿⠀⢾⣿⣿⣽⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⣽⣿⣿⠀⢸⣿⡷⣟⣷⣻⣽⣿⣷⣟⣿⣿⡟⢻⣿⣷⠟⢿⣿⣭⣹⣿⣦⣤⣤⣤⣴⣼⣤⣷⠈⢿⣿⣿⡌⠸⣿⣻⣏⢹⡟⣼⣟⣻⣿⣿⣿⠏⣼⣿⡿⢰⣿⣟⣿⢺⢿⣿⠃⢸⣿⣿⠇⢸⣿⡇⣿⣿⣟⣿⣻⣿⣽⣿⣿⣿⣿⣿⣿⣿⣿⣯⣿⣿⣿⠀⣿⣿⣿⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⢾⣿⣿⠃⢸⣿⣟⡿⣯⣟⣿⡟⡹⢿⣿⣿⣷⣾⣿⣟⠀⣿⣿⣿⠋⣾⢹⣿⡿⣿⡿⢿⣿⣿⣇⠈⢿⣿⣿⠄⣿⣿⣿⡿⣾⡿⣹⠏⣿⣷⡟⣸⣿⣿⢃⣿⡿⣝⡞⣯⢿⣿⡇⢸⣿⣟⣲⢸⣿⢡⣿⣟⡾⣽⢯⣟⣿⣻⣿⢿⣿⣿⣿⢿⣿⡿⣿⣿⣧⠀⢿⣿⣿⠀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⡈⠙⠋⣠⣿⣿⣿⣽⣷⣿⣿⣶⣧⡈⠙⣿⢰⣿⣿⣿⣦⡈⠋⢃⣴⢇⣾⣿⡝⣿⣷⣾⣿⣿⣿⣦⣈⢉⢿⣴⣿⣿⣿⠍⠛⠑⣟⣴⣿⣿⡇⣾⣿⠇⣾⣿⡻⣵⡻⣞⡽⣿⣧⡈⢻⣿⣿⣾⡏⣼⣿⣻⡼⣏⡿⣾⣽⣳⢿⣻⣿⣿⣿⢿⣻⣿⣿⣿⣿⣧⣀⡙⣁⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢋⣿⣿⣷⡛⠛⠟⢿⣫⣵⣾⣿⡳⣿⡟⢻⣿⡟⣾⡿⢹⣿⣿⣿⣿⣿⣷⣶⠀⣲⣷⣶⣿⣿⣿⢠⣿⢏⣼⣿⣷⢿⣷⡽⣭⢿⣹⣿⠟⣿⢉⣿⡟⣰⣿⣯⠷⣽⡿⢛⣭⣿⣿⣯⠷⣿⡟⣹⣿⡿⣿⡟⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣳⣿⡏⢼⣿⣳⢿⣿⣿⣶⣎⡙⢿⣟⡾⣵⣿⢃⣿⡿⣝⣿⡇⢾⡟⣱⣯⢸⣿⣿⡷⢸⣿⢯⣛⡾⣵⣟⣸⠯⣾⢫⣶⣿⢃⣿⡿⣭⣿⠏⣴⣿⣿⣂⡿⢹⣿⢿⡼⣿⢋⣶⣿⣿⠃⣿⣯⣟⣿⢡⣿⡿⣽⣿⠁⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⢿⣿⣽⣫⣞⠾⣽⣻⣿⡌⣿⣟⣾⡏⣸⣿⣻⡽⣾⣷⠟⣸⣿⣿⣧⣙⣛⣛⢹⣿⣏⣯⣽⣻⣧⢆⢲⣾⣿⣿⠇⣾⣿⣟⣿⡇⣾⣿⢯⣿⡏⣷⣿⣟⣯⣾⢛⣾⣿⣿⡿⢸⣿⣟⣾⡯⣰⣿⢿⣽⡗⡄⣿⣿⣿⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡄⣿⣿⢾⡵⣯⢟⣳⣿⡿⢡⣿⣟⣿⡇⣿⣟⣷⠿⣻⠁⣼⣿⣟⠾⣽⢿⡿⣿⡘⣿⣞⣷⡾⢟⣃⢼⣿⣿⣻⡏⢼⣿⣿⠟⣫⡄⣿⣿⡿⢏⣷⢹⣿⣞⡿⣟⠸⣿⣿⡿⣡⡼⣿⣿⠿⣃⢽⣿⣿⠟⣰⣏⣿⠟⣻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⡙⡛⠿⠿⠿⠿⣛⣩⣴⣿⣿⣽⣻⣧⣜⣭⣵⣾⣿⣸⣿⣟⣾⣻⣽⣾⡽⣿⣷⣌⣯⣱⣮⣿⣯⣼⣿⣳⣟⣿⣮⣵⣦⣿⣿⣷⣬⣫⣵⣿⣿⣦⣙⣭⣽⣿⣧⣽⣩⣶⣿⣧⣭⣵⣿⣿⣬⣯⣼⣿⡿⣭⣗⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣿⣿⣿⣿⣿⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣾⣷⣿⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣿⣿⣿⣿⡿⣿⣯⣿⣿⣿⣿⡿⣽⣿⣿⣿⣿⣿⢿⣿⣿⣿⣻⡿⣿⣿⢿⣟⣿⣿⠟⣩⡧⣽⣿⣿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣽⣿⣿⣿⣿⣷⣿⣾⣷⣿⣿⣽⣷⣿⣽⣷⣿⣳⣿⣾⣿⣾⣿⢿⣾⣿⣶⣯⣽⣳⢯⣾⣽⠟⣡⣾⣿⢃⣿⣿⣻⣿⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣯⣿⡃⣿⣿⣿⢋⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣬⣭⣥⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿

"""
