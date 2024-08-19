import time
import colorama
import os

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

# def color(dl):
#     print(f"{den}T{luc}R{trang}Ầ{red}N {vang}Q{tim}U{lamd}Ố{lam}C {hong}T{den}{luc}R{trang}{red}U{tim}N{lamd}G{dong_mau}",end="\r");time.sleep(2/6)
#     print(f"{luc}T{trang}R{red}Ầ{vang}N {tim}Q{lamd}U{lam}Ố{hong}C {den}T{luc}{trang}R{red}{tim}U{lamd}N{lam}G{dong_mau}",end="\r");time.sleep(2/6)
#     print(f"{trang}T{red}R{vang}Ầ{tim}N {lamd}Q{lam}U{hong}Ố{den}C {luc}T{trang}{red}R{tim}{lamd}U{lam}N{hong}G{dong_mau}",end="\r");time.sleep(2/6)
#     print(f"{red}T{hong}R{tim}Ầ{lamd}N {lam}Q{hong}U{den}Ố{luc}C {trang}T{red}{tim}R{lamd}{lam}U{hong}N{den}G{dong_mau}",end="\r");time.sleep(2/6)
#     print(f"{hong}T{tim}R{lamd}Ầ{lam}N {hong}Q{den}U{luc}Ố{trang}C {red}T{tim}{lamd}R{lam}{hong}U{den}N{tim}G{dong_mau}",end="\r");time.sleep(2/6)
#     print(f"{tim}T{lamd}R{lam}Ầ{hong}N {den}Q{luc}U{trang}Ố{red}C {tim}T{lamd}{lam}R{hong}{den}U{tim}N{lamd}G{dong_mau}",end="\r");time.sleep(2/6)
# color(1)

def banner_HT(dl):
    for i in range(dl,0,-1):
        print(f"{luc}H{trang}i{red}ế{vang}u{tim}-{lamd}T{lam}o{hong}o{den}l{dong_mau} {red}[{i}]{dong_mau}",end="\r");time.sleep(1/6)
        print(f"{den}H{luc}i{trang}ế{red}u{vang}-{tim}T{lamd}o{lam}o{hong}l{dong_mau} {red}[{i}]{dong_mau}",end="\r");time.sleep(1/6)
        print(f"{trang}H{red}i{vang}ế{tim}u{lamd}-{lam}T{hong}o{den}o{luc}l{dong_mau} {red}[{i}]{dong_mau}",end="\r");time.sleep(1/6)
        print(f"{red}H{vang}i{tim}ế{lamd}u{lam}-{hong}T{den}o{luc}o{trang}l{dong_mau} {red}[{i}]{dong_mau}",end="\r");time.sleep(1/6)
        print(f"{vang}H{tim}i{lamd}ế{lam}u{hong}-{den}T{luc}o{trang}o{red}l{dong_mau} {red}[{i}]{dong_mau}",end="\r");time.sleep(1/6)
        print(f"{tim}H{lamd}i{lam}ế{hong}u{den}-{luc}T{trang}o{red}o{vang}l{dong_mau} {red}[{i}]{dong_mau}",end="\r");time.sleep(1/6)
        print(f"{lamd}H{lam}i{hong}ế{den}u{luc}-{trang}T{red}o{vang}o{tim}l{dong_mau} {red}[{i}]{dong_mau}",end="\r");time.sleep(1/6)
        print(f"{lam}H{hong}i{den}ế{luc}u{trang}-{red}T{vang}o{tim}o{lamd}l{dong_mau} {red}[{i}]{dong_mau}",end="\r");time.sleep(1/6)
        print(f"{hong}H{den}i{luc}ế{trang}u{red}-{vang}T{tim}o{lamd}o{lam}l{dong_mau} {red}[{i}]{dong_mau}",end="\r");time.sleep(1/6)
    print(f"\r\r{red}   ⚡Hiếu_Tool⚡                      {dong_mau}\r", end='')

    time.sleep(0.5)

from time import sleep
def nghingoi(delay):
	for x in range(delay,-1,-1):
		print("\r\033[1;93m   Hiếu_Tool \033[1;91m ~>       \033[1;92m LO      \033[1;91m | "+str(x)+" | \r ", end='')
		sleep(0.14)
		print("\r\033[1;91m   Hiếu_Tool \033[1;91m   ~>     \033[1;92m LOA     \033[0;31m | "+str(x)+" | \r ", end='')
		sleep(0.14)
		print("\r\033[1;92m   Hiếu_Tool \033[1;91m     ~>   \033[1;92m LOAD    \033[0;31m | "+str(x)+" | \r", end='')
		sleep(0.14)
		print("\r\033[1;94m   Hiếu_Tool \033[1;91m       ~> \033[1;92m LOADI   \033[0;31m | "+str(x)+" | \r", end='')
		sleep(0.14)
		print("\r\033[1;95m   Hiếu_Tool \033[1;91m        ~>\033[1;92m LOADIN  \033[0;31m | "+str(x)+" | \r", end='')
		sleep(0.14)
		print("\r\033[1;96m   Hiếu_Tool \033[1;91m        ~>\033[1;92m LOADING \033[0;31m | "+str(x)+" | \r", end='')
		sleep(0.14)
		print("\r\033[1;93m  Hiếu_Tool \033[1;91m        ~>\033[1;92m LOADING.\033[0;31m | "+str(x)+" | \r", end='')
		sleep(0.14)
	print(f"\r\r{red}   ⚡Hiếu_Tool⚡                      {dong_mau}\r", end='')
	sleep(1)
nghingoi(2)