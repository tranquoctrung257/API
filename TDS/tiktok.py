import requests
import time 
import os
class API_TIKTOK:
    def __init__(self,Token:str,ID_nick:str,Type:int) -> None:
        self.Token = Token
        self.ID_nick = ID_nick
        self.Type = "tiktok_like" if type == 1 else "tiktok_follow"
    def Info_Acc_TDS(self):
        try:
            res = requests.get(f"https://traodoisub.com/api/?fields=profile&access_token={self.Token}")
            if "success" in res.text:
                ueser = res.json()["data"]["user"]
                xu = res.json()["data"]["xu"]
                xu_die =res.json()["data"]["xudie"]
                return f"Tài Khoản: {ueser} | Hiện có {xu} | [xu die{xu_die}]"
            elif "error" in res.text:
                return res.json()["error"]
        except:
            return False  
    # cấu hình tài khoản tiktok chạy    
    def CauHinh(self):
        try: 
            res = requests.get(f"https://traodoisub.com/api/?fields=tiktok_run&id={self.ID_nick}&access_token={self.Token}")
            try:
                id = res.json()["data"]["uniqueID"]
                msg = res.json()["data"]["msg"]
                return f"Tài Khoản: {id} | {msg}"
            except:
                return "Nick chưa được thêm vào tài khoản TDS này!"
        except:
            return False
    # nhận nhiệm vụ
    def get_nv(self):
        try: 
            res = requests.get(f"https://traodoisub.com/api/?fields={self.Type}&access_token={self.Token}")
            nv = res.json()["data"]
            return nv
        except:
            return False
    def gui_duyet_nv(self,id="7391477984353993736_U8C8QGON3C1K90NOHI78"):
        Type_nv = "TIKTOK_LIKE_CACHE" if self.Type == "tiktok_like" else "TIKTOK_FOLLOW_CACHE"
        gui_nv = requests.get(f"https://traodoisub.com/api/coin/?type={Type_nv}&id={id}&access_token={self.Token}")
        return gui_nv.json()["cache"]
    # nhận xu
    def nhan_xu(self):
        fields = "TIKTOK_LIKE_API" if self.Type == 1 else "TIKTOK_FOLLOW_API"
        nhan_xu = requests.get(f"https://traodoisub.com/api/coin/?type={self.Type.upper()}&id={fields}&access_token={self.Token}")
        return nhan_xu.json()



