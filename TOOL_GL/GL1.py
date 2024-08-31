import requests
import os
from colorama import Fore
from tabulate import tabulate
from termcolor import colored
import itertools
import os
import sys
import requests
import time
from termcolor import colored
import itertools
def rainbow_text(text):
    colors = ['red', 'yellow', 'green', 'cyan', 'blue', 'magenta']
    colored_text = ''

    for char, color in zip(text, itertools.cycle(colors)):
        colored_text += colored(char, color)

    return colored_text
# def banner_Tool():
    banner = f"""
\033[1;34m ██╗░░██╗██╗███████╗██╗░░░██╗  ████████╗░█████╗░░█████╗░██╗░░░░░
\033[1;37m ██║░░██║██║██╔════╝██║░░░██║  ╚══██╔══╝██╔══██╗██╔══██╗██║░░░░░
\033[1;34m ███████║██║█████╗░░██║░░░██║  ░░░██║░░░██║░░██║██║░░██║██║░░░░░
\033[1;37m ██╔══██║██║██╔══╝░░██║░░░██║  ░░░██║░░░██║░░██║██║░░██║██║░░░░░
\033[1;34m ██║░░██║██║███████╗╚██████╔╝  ░░░██║░░░╚█████╔╝╚█████╔╝███████╗
\033[1;37m ╚═╝░░╚═╝╚═╝╚══════╝░╚═════╝░  ░░░╚═╝░░░░╚════╝░░╚════╝░╚══════╝
\033[1;34m                                   by ADMIN HIẾU + ADMIN TRUNG
\033[1;31m────────────────────────────────────────────────────────────
\033[1;31m[\033[1;37m=.=\033[1;31m] \033[1;37m=> \033[1;33mTOOL GOLIKE YOTUBE
\033[1;31m[\033[1;37m=.=\033[1;31m] \033[1;37m=> \033[1;35mADMIN: \033[1;36mHIEU TOOL
\033[1;31m[\033[1;37m=.=\033[1;31m] \033[1;37m=> \033[1;32mZALO: \033[1;37m 84939271874
\033[1;31m[\033[1;37m=.=\033[1;31m] \033[1;37m=> \033[1;34mYOUTUBE: \033[1;37mhttps://www.youtube.com/@hieutool248
\033[1;31m────────────────────────────────────────────────────────────
"""
    for X in banner:
        sys.stdout.write(X)
        sys.stdout.flush()
        time.sleep(0.00125)


def YOUTUBE(auth):
    headers = {
            'accept': 'application/json, text/plain, */*',
            'accept-language': 'vi,en;q=0.9,vi-VN;q=0.8',
            'authorization': auth,
            'cache-control': 'no-cache',
            'content-type': 'application/json;charset=utf-8',
            'origin': 'https://app.golike.net',
            'pragma': 'no-cache',
            'priority': 'u=1, i',
            'referer': 'https://app.golike.net/',
            'sec-ch-ua': '"Chromium";v="128", "Not;A=Brand";v="24", "Google Chrome";v="128"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-site',
            't': 'VFZSamVVNVVRWGROYWxFeVRVRTlQUT09',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36',
        }
    checkaccount = requests.get('https://gateway.golike.net/api/youtube-account',headers=headers).json()
    user_YTB = []
    account_id1 = []
    STT = []
    STATUS =[]

    i=1
    head = ["STT", "  ACCOUNT"]
    for data in checkaccount['data'] :
            usernametk = data['name']
            # print(str(i)+'.'+usernametk)
            user_YTB.append(data['name'])
            account_id1.append(data['id'])
            STT.append(i)
            i=i+1
    table = zip(STT,user_YTB)
    LIST=tabulate(table, headers=head, tablefmt="grid") 
    os.system('cls' if os.name== 'nt' else 'clear')  
    # banner_Tool()
    print(rainbow_text('Các Tài Khoản Hiện Tại Của Bạn'))
    print(rainbow_text(LIST))
    choose = int(input(rainbow_text('Vui Lòng Nhập Tk: ')))
    os.system('cls' if os.name== 'nt' else 'clear')
    if choose >=1 or choose <= len(user_YTB) :
        user_YTB = user_YTB[choose-1:choose]
        account_id1 = account_id1[choose-1:choose]
        user_tiktok = user_YTB[0] 
        account_id = account_id1[0]
        checkfile = os.path.isfile('AUTHYTB'+str(account_id)+'.txt')
        if checkfile == False:
            AUTHYTB = input(rainbow_text('nhập AUTHYTB : '))
            createfile = open('AUTHYTB'+str(account_id)+'.txt','w')
            createfile.write(AUTHYTB)
            createfile.close()
            readfile = open('AUTHYTB'+str(account_id)+'.txt','r')
            AUTHYTB = readfile.read()
            readfile.close()
        else:
            readfile = open('AUTHYTB'+str(account_id)+'.txt','r')
            AUTHYTB = readfile.read()
            readfile.close()
        checkfile2 = os.path.isfile('COOKIEYTB'+str(account_id)+'.txt')
        if checkfile2 == False:
            cookieYTB = input(rainbow_text('nhập COOKIEYTB : '))
            createfile = open('COOKIEYTB'+str(account_id)+'.txt','w')
            createfile.write(cookieYTB)
            createfile.close()
            readfile = open('COOKIEYTB'+str(account_id)+'.txt','r')
            cookieYTB = readfile.read()
            readfile.close()
        else:
            readfile = open('COOKIEYTB'+str(account_id)+'.txt','r')
            cookieYTB = readfile.read()
            readfile.close()
        
        os.system('cls' if os.name== 'nt' else 'clear')
        # banner_Tool()
        print(rainbow_text('1: Sử Dụng Dữ Liệu Tài Khoản YT Cũ!'))
        print(rainbow_text('2: Xóa Dữ Liệu Tài Khoản YT Cũ!'))
        chon = int(input(rainbow_text('Vui Lòng Nhập Lựa Chọn Của Bạn: ')))
        if chon == 2:
             os.remove('AUTHYTB'+str(account_id)+'.txt')
             os.remove('COOKIEYTB'+str(account_id)+'.txt')
             return 0
        os.system('cls' if os.name== 'nt' else 'clear')
        # banner_Tool()
        param = {
             'account_id':str(account_id)
        }
        for i in range(100000000):
            job = 'https://gateway.golike.net/api/advertising/publishers/youtube/jobs?account_id='+str(account_id)
            nos = requests.get(job,headers=headers,params=param).json()
            print("đã vào")
            if nos['status'] ==200:
                ads_id = nos['data']['id']
                object_id = nos['data']['object_id']
                type = nos['data']['type']
                link = nos['data']['link']
                if type == 'subscribe':
                    headersYTB = {
                            'accept': '*/*',
                            'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
                            'authorization': AUTHYTB,
                            'content-type': 'application/json',
                            'cookie': cookieYTB,
                            'origin': 'https://www.youtube.com',
                            'priority': 'u=1, i',
                            'referer': 'https://www.youtube.com/watch?v=_tRfOmytgek',
                            'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
                            'sec-ch-ua-arch': '"x86"',
                            'sec-ch-ua-bitness': '"64"',
                            'sec-ch-ua-form-factors': '"Desktop"',
                            'sec-ch-ua-full-version': '"126.0.6478.182"',
                            'sec-ch-ua-full-version-list': '"Not/A)Brand";v="8.0.0.0", "Chromium";v="126.0.6478.182", "Google Chrome";v="126.0.6478.182"',
                            'sec-ch-ua-mobile': '?0',
                            'sec-ch-ua-model': '""',
                            'sec-ch-ua-platform': '"Windows"',
                            'sec-ch-ua-platform-version': '"15.0.0"',
                            'sec-ch-ua-wow64': '?0',
                            'sec-fetch-dest': 'empty',
                            'sec-fetch-mode': 'same-origin',
                            'sec-fetch-site': 'same-origin',
                            'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Mobile/15E148 Safari/604.1,gzip(gfe)',
                            'x-client-data': 'CJW2yQEIpbbJAQipncoBCLyKywEIlaHLAQiFoM0BCLvIzQEIvJ3OAQiyns4BCNunzgEIg6zOAQifrM4BCPCszgEIpq7OAQjlr84BGI/OzQEYoJ3OAQ==',
                            'x-goog-authuser': '0',
                            'x-goog-visitor-id': 'CgtmVGlWcWxVcE1PdyjI3Pq0BjIKCgJWThIEGgAgMA%3D%3D',
                            'x-origin': 'https://www.youtube.com',
                            'x-youtube-bootstrap-logged-in': 'true',
                            'x-youtube-client-name': '1',
                            'x-youtube-client-version': '2.20240722.00.00',
                        }
                    
                    try:
                            paramYTB = {
                                    'prettyPrint': 'false',
                                    }
                            json_dataYTB = {
                                    'context': {
                                        'client': {
                                            'hl': 'en',
                                            'gl': 'VN',
                                            'remoteHost': '2401:d800:b0e1:b88c:f190:bb5b:1413:52c4',
                                            'deviceMake': 'Apple',
                                            'deviceModel': 'iPhone',
                                            'visitorData': 'Cgs3NnhVUlFzSkdXRSiPyIO1BjIKCgJWThIEGgAgSA%3D%3D',
                                            'userAgent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Mobile/15E148 Safari/604.1,gzip(gfe)',
                                            'clientName': 'MWEB',
                                            'clientVersion': '2.20240722.07.00',
                                            'osName': 'iPhone',
                                            'osVersion': '16_6',
                                            'originalUrl': 'https://m.youtube.com/',
                                            'playerType': 'UNIPLAYER',
                                            'screenPixelDensity': 2,
                                            'platform': 'MOBILE',
                                            'clientFormFactor': 'SMALL_FORM_FACTOR',
                                            'configInfo': {
                                                'appInstallData': 'CI_Ig7UGEOX0sAUQ9quwBRCe0LAFEJmYsQUQ0PqwBRD68LAFELDusAUQk9KwBRCUlbEFEJCSsQUQvZmwBRDPqLAFEMn3rwUQiOOvBRCq2LAFELfvrwUQo-2wBRDK-bAFENv-tyIQ2N2wBRCk9a4FENCNsAUQ6-j-EhDrmbEFEL22rgUQj8awBRC2sf8SEIiHsAUQqJOxBRDh7LAFENPhrwUQ052xBRCa8K8FENWIsAUQ3Y6xBRD8hbAFEOrDrwUQqoCxBRCMlLEFEN3o_hIQqJqwBRCUibEFEO_NsAUQ9KuwBRCokrEFEL6KsAUQlP6wBRCWlbAFELXksAUQ4bz_EhDG9a4FEKaSsQUQ_4ixBRDZya8FEPGOsQUQpcL-EhCO2rAFEJeDsQUQt-r-EhCAi7EFENWLsQUQooGwBRCDuf8SEI3MsAUQ0Z2xBRDOr68FEKe3sAUQj5SxBRD3sf8SEIfUrwUQyIGxBRCinbEFEMnmsAUQzN-uBRDW3bAFEKaTsQUQh6ivBRDj0bAFEPmRsQUqHENBTVNFUlVLb0wyd0ROSGtCcUc2LWd2VEdoMEg%3D',
                                            },
                                            'screenDensityFloat': 2.0000000298023224,
                                            'userInterfaceTheme': 'USER_INTERFACE_THEME_DARK',
                                            'timeZone': 'Asia/Bangkok',
                                            'browserName': 'Safari Mobile',
                                            'browserVersion': '16.6.15E148',
                                            'acceptHeader': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                                            'deviceExperimentId': 'ChxOek01TlRFMk1UTTBNVEkzTXpVeE56QXhNQT09EI_Ig7UGGI_Ig7UG',
                                            'screenWidthPoints': 667,
                                            'screenHeightPoints': 375,
                                            'utcOffsetMinutes': 420,
                                            'connectionType': 'CONN_CELLULAR_4G',
                                            'memoryTotalKbytes': '8000000',
                                            'mainAppWebInfo': {
                                                'graftUrl': 'https://m.youtube.com/@SangVlog9',
                                                'webDisplayMode': 'WEB_DISPLAY_MODE_BROWSER',
                                                'isWebNativeShareAvailable': True,
                                            },
                                        },
                                        'user': {
                                            'lockedSafetyMode': False,
                                        },
                                        'request': {
                                            'useSsl': True,
                                            'consistencyTokenJars': [
                                                {
                                                    'encryptedTokenJarContents': 'AKreu9vlJw-IxsS5kklSYhcRVj6L6Od-dq4N02h47nZp1bDUC4zDUngqU4rGhxUn96yFfcPbbrtEpci-TyBMl5FPJXjRZKoatcDNkkPK0HS-vSdYiL_-QvIew9C7oN48uuKFayQ7f-b-Z4gtXCt2zuvW',
                                                },
                                            ],
                                            'internalExperimentFlags': [],
                                        },
                                        'clientScreenNonce': 'IGVAGYPEX5XI0kz6',
                                        'clickTracking': {
                                            'clickTrackingParams': 'CBMQmysYASITCJKxqoLIv4cDFTNSnQkd6Ks75zIJY2hhbm5lbHM0',
                                        },
                                        'adSignalsInfo': {
                                            'params': [
                                                {
                                                    'key': 'dt',
                                                    'value': '1721820176714',
                                                },
                                                {
                                                    'key': 'flash',
                                                    'value': '0',
                                                },
                                                {
                                                    'key': 'frm',
                                                    'value': '0',
                                                },
                                                {
                                                    'key': 'u_tz',
                                                    'value': '420',
                                                },
                                                {
                                                    'key': 'u_his',
                                                    'value': '8',
                                                },
                                                {
                                                    'key': 'u_h',
                                                    'value': '375',
                                                },
                                                {
                                                    'key': 'u_w',
                                                    'value': '667',
                                                },
                                                {
                                                    'key': 'u_ah',
                                                    'value': '375',
                                                },
                                                {
                                                    'key': 'u_aw',
                                                    'value': '667',
                                                },
                                                {
                                                    'key': 'u_cd',
                                                    'value': '24',
                                                },
                                                {
                                                    'key': 'bc',
                                                    'value': '31',
                                                },
                                                {
                                                    'key': 'bih',
                                                    'value': '375',
                                                },
                                                {
                                                    'key': 'biw',
                                                    'value': '667',
                                                },
                                                {
                                                    'key': 'brdim',
                                                    'value': '0,0,0,0,667,0,667,375,667,375',
                                                },
                                                {
                                                    'key': 'vis',
                                                    'value': '1',
                                                },
                                                {
                                                    'key': 'wgl',
                                                    'value': 'true',
                                                },
                                                {
                                                    'key': 'ca_type',
                                                    'value': 'image',
                                                },
                                            ],
                                        },
                                    },
                                    'channelIds': [
                                        object_id,
                                    ],
                                    'params': 'EgIIAhgA',
                                }

                            response = requests.post(
                                    'https://www.youtube.com/youtubei/v1/subscription/subscribe',
                                    params=paramYTB,
                                    headers=headersYTB,
                                    json=json_dataYTB,
                                ).json()
                            if 'Request contains an invalid argument' in str(response) :
                                print('Cookies Yotube Của Bạn Đã Bị Die!')
                                os.remove('AUTHYTB'+str(account_id)+'.txt')
                                os.remove('COOKIEYTB'+str(account_id)+'.txt')
                                return 0
                            elif "'subscribed': True" in str(response):
                                url = 'https://gateway.golike.net/api/advertising/publishers/youtube/complete-jobs'
                                json_data = {
                                    'account_id': account_id,
                                    'ads_id': ads_id,
                                    }
                                response = requests.post(
                                    'https://gateway.golike.net/api/advertising/publishers/youtube/complete-jobs',
                                    headers=headers,
                                    json=json_data,
                                    ).json()
                                if response['success']==True:
                                    prices =response['data']['prices']
                                    print(Fore.CYAN+'['+str(i)+']'+'|'+Fore.WHITE+type+'|'+Fore.GREEN+str(ads_id)+' | '+Fore.YELLOW+str(prices)+'VND'+'|'+Fore.BLUE+"SUCCESS")
                                else:
                                    skipjob = 'https://gateway.golike.net/api/advertising/publishers/youtube/skip-jobs'
                                    PARAMS = {
                                        'ads_id' : ads_id,
                                        'account_id' : account_id,
                                        'object_id' : object_id ,
                                        'async': 'true',
                                        'data': 'null',
                                        'type': type,
                                        }
                                    checkskipjob = requests.post(skipjob,params=PARAMS).json()
                                    if checkskipjob['status'] == 200:
                                        message = checkskipjob['message']
                                        print(Fore.RED+str(message))
                                        PARAMSr = {
                                            'ads_id' : ads_id,
                                            'account_id' : account_id,
                                            'object_id' : object_id ,
                                            'async': 'true',
                                            'data': 'null',
                                            'type': type,
                                            }
                            else :
                                skipjob = 'https://gateway.golike.net/api/advertising/publishers/youtube/skip-jobs'
                                PARAMS = {
                                    'ads_id' : ads_id,
                                    'account_id' : account_id,
                                    'object_id' : object_id ,
                                    'async': 'true',
                                    'data': 'null',
                                    'type': type,
                                    }
                                checkskipjob = requests.post(skipjob,params=PARAMS).json()
                                if checkskipjob['status'] == 200:
                                        message = checkskipjob['message']
                                        print(Fore.RED+str(message))
                                        PARAMSr = {
                                        'ads_id' : ads_id,
                                        'account_id' : account_id,
                                        'object_id' : object_id ,
                                        'async': 'true',
                                        'data': 'null',
                                        'type': type,
                                        }
                    except IndexError:
                        print('COOKIE DIE')
                        os.remove('AUTHYTB'+str(account_id)+'.txt')
                        os.remove('COOKIEYTB'+str(account_id)+'.txt')
                        return 0
                else :
                    skipjob = 'https://gateway.golike.net/api/advertising/publishers/youtube/skip-jobs'
                    PARAMS = {
                        'ads_id' : ads_id,
                        'account_id' : account_id,
                        'object_id' : object_id ,
                        'async': 'true',
                        'data': 'null',
                        'type': type,
                        }
                    checkskipjob = requests.post(skipjob,params=PARAMS).json()
                    if checkskipjob['status'] == 200:
                        message = checkskipjob['message']
                        print(Fore.RED+str(message))
                        PARAMSr = {
                            'ads_id' : ads_id,
                            'account_id' : account_id,
                            'object_id' : object_id ,
                            'async': 'true',
                            'data': 'null',
                            'type': type,
                            }
            else: 
                print(nos['message'])
