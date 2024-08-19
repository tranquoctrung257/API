import time

# Định nghĩa các màu sắc (mã escape ANSI)
luc = "\033[1;32m"
trang = "\033[1;37m"
red = "\033[1;31m"
vang = "\033[1;33m"
tim = "\033[1;35m"
lamd = "\033[1;36m"
lam = "\033[1;34m"
hong = "\033[1;95m"
den = "\033[1;90m"
dong_mau = "\033[0m"

def banner(dl):
    for i in range(dl, -1, -1):
        print(f"{luc}H{trang}i{red}ế{vang}u{tim}-{lamd}T{lam}o{hong}o{den}l{dong_mau} {red}[{i}]{dong_mau}", end="\r")
        time.sleep(1/6)
        print(f"{den}H{luc}i{trang}ế{red}u{vang}-{tim}T{lamd}o{lam}o{hong}l{dong_mau} {red}[{i}]{dong_mau}", end="\r")
        time.sleep(1/6)
        print(f"{trang}H{red}i{vang}ế{tim}u{lamd}-{lam}T{hong}o{den}o{luc}l{dong_mau} {red}[{i}]{dong_mau}", end="\r")
        time.sleep(1/6)
        print(f"{red}H{vang}i{tim}ế{lamd}u{lam}-{hong}T{den}o{luc}o{trang}l{dong_mau} {red}[{i}]{dong_mau}", end="\r")
        time.sleep(1/6)
        print(f"{vang}H{tim}i{lamd}ế{lam}u{hong}-{den}T{luc}o{trang}o{red}l{dong_mau} {red}[{i}]{dong_mau}", end="\r")
        time.sleep(1/6)
        print(f"{tim}H{lamd}i{lam}ế{hong}u{den}-{luc}T{trang}o{red}o{vang}l{dong_mau} {red}[{i}]{dong_mau}", end="\r")
        time.sleep(1/6)
        print(f"{lamd}H{lam}i{hong}ế{den}u{luc}-{trang}T{red}o{vang}o{tim}l{dong_mau} {red}[{i}]{dong_mau}", end="\r")
        time.sleep(1/6)
        print(f"{lam}H{hong}i{den}ế{luc}u{trang}-{red}T{vang}o{tim}o{lamd}l{dong_mau} {red}[{i}]{dong_mau}", end="\r")
        time.sleep(1/6)
        print(f"{hong}H{den}i{luc}ế{trang}u{red}-{vang}T{tim}o{lamd}o{lam}l{dong_mau} {red}[{i}]{dong_mau}", end="\r")
        time.sleep(1/6)
    
    # In dòng cuối cùng mà không có carriage return (\r)
    print(f"{hong}H{den}i{luc}ế{trang}u{red}-{vang}T{tim}o{lamd}o{lam}l{dong_mau}")

# Gọi hàm
banner(2)
