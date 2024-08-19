import requests

def golike():
    while True:
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
        else:
            exit()
