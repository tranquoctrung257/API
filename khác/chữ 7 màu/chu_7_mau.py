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

res="\033[0m"
BBlack="\033[1;30m" 
BRed="\033[1;31m" 
Bmg="\033[1;32m" 
BYellow="\033[1;33m" 
BBlue="\033[1;34m" 
BPurple="\033[1;35m" 
BCyan="\033[1;36m" 
BWhite="\033[1;37m" 
Blue="\033[0;34m"
lmg="\033[1;32m"
red="\033[1;31m"
xanh="\033[1;32m"
cyan="\033[1;36m"
yellow="\033[1;33m"
mtool="\033[1;34m"
maugi="\033[1;35m"
white= "\033[1;37m"
red="\033[1;31m"
white= "\033[1;37m"
whiteb= "\033[1;37m"
pmtol="\033[1;31m"
green="\033[1;32m"
yellow="\033[1;33m"
cam="\033[1;33m"
test="\033[1;33m"
greenb="\033[1;32m"
blue="\033[1;34m"
lam="\033[1;34m"
tmi="\033[1;34m"
hong="\033[1;35m"
imt="\033[1;35m"
cyan= "\e[1;36m"
syan="\033[1;36m"
xnhac= "\033[1;96m"
den="\033[1;90m"
do="\033[1;91m"
luc="\033[1;92m"
vang="\033[1;93m"
xduong="\033[1;94m"
hong="\033[1;95m"
trang="\033[1;97m"
vang="\033[1;93m"
do="\033[1;91m"
BBlack="\033[1;30m"      
BRed="\033[1;31m"
BGreen="\033[1;32m"
BYellow="\033[1;33m"
BBlue="\033[1;34m"
BPurple="\033[1;35m"
BCyan="\033[1;36m"
BWhite="\033[1;37m"
Blue="\033[0;34m"
lime="\033[1;32m"
red="\033[1;31m"
xanh="\033[1;32m"
cyan="\033[1;36m"
yellow="\033[1;33m"
turquoise="\033[1;34m"
maugi="\033[1;35m"
white= "\033[1;37m"
BCyan="\033[1;36m"
trang="\033[1;37m"
do="\033[1;31m"
luc="\033[1;32m"
vang="\033[1;33m"
luc="\033[1;92m"