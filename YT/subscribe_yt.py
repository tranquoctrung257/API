import requests

class API_YT():
    def __init__(self,cookies,auth,channelIds) -> None:
        self.cookies = cookies
        self.auth = auth
        self.channelIds = channelIds
    def api_yt(self):

        headers = {
            'accept': '*/*',
            'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
            'authorization': f'{self.auth}',
            'cache-control': 'no-cache',
            'content-type': 'application/json',
            'cookie': f'{self.cookies}',
            'origin': 'https://www.youtube.com',
            'pragma': 'no-cache',
            'priority': 'u=1, i',
            'referer': 'https://www.youtube.com/@ThangLongTv',
            'sec-ch-ua': '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
            'sec-ch-ua-arch': '""',
            'sec-ch-ua-bitness': '"64"',
            'sec-ch-ua-form-factors': '',
            'sec-ch-ua-full-version': '"127.0.6533.101"',
            'sec-ch-ua-full-version-list': '"Not)A;Brand";v="99.0.0.0", "Google Chrome";v="127.0.6533.101", "Chromium";v="127.0.6533.101"',
            'sec-ch-ua-mobile': '?1',
            'sec-ch-ua-model': '"SM-G981B"',
            'sec-ch-ua-platform': '"Android"',
            'sec-ch-ua-platform-version': '"13"',
            'sec-ch-ua-wow64': '?0',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'same-origin',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Linux; Android 13; SM-G981B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36',
            'x-client-data': 'CKS1yQEIkrbJAQimtskBCKmdygEI7YjLAQiWocsBCIWgzQEIjafNAQisns4BCOSvzgEIpLLOAQi+ts4BCIa3zgEI2bfOARi/k9Ui',
            'x-goog-authuser': '0',
            'x-goog-visitor-id': 'Cgt5MW5LNW56NEtnayiwkfa1BjIKCgJWThIEGgAgGw%3D%3D',
            'x-origin': 'https://www.youtube.com',
            'x-youtube-bootstrap-logged-in': 'true',
            'x-youtube-client-name': '1',
            'x-youtube-client-version': '2.20240814.00.00',
        }

        params = {
            'prettyPrint': 'false',
        }

        json_data = {
            'context': {
                'client': {
                    'hl': 'vi',
                    'gl': 'VN',
                    'remoteHost': '2402:800:6279:1f64:4dbf:2754:8b2:8858',
                    'deviceMake': '',
                    'deviceModel': '',
                    'visitorData': 'Cgt5MW5LNW56NEtnayiwkfa1BjIKCgJWThIEGgAgGw%3D%3D',
                    'userAgent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36,gzip(gfe)',
                    'clientName': 'WEB',
                    'clientVersion': '2.20240814.00.00',
                    'osName': 'Windows',
                    'osVersion': '10.0',
                    'originalUrl': 'https://www.youtube.com/@ThangLongTv',
                    'platform': 'DESKTOP',
                    'clientFormFactor': 'UNKNOWN_FORM_FACTOR',
                    'configInfo': {
                        'appInstallData': 'CLCR9rUGEJnB_xIQ5fSwBRDW3bAFEN3o_hIQydewBRDrk64FEPirsQUQlP6wBRDj0bAFEL2ZsAUQlpWwBRCJ6K4FEJrwrwUQt-r-EhDvzbAFENnJrwUQ7qKvBRDJ5rAFEKaasAUQt--vBRCNlLEFENCNsAUQxJKxBRDerbEFENqgsQUQkp2xBRComrAFEI_EsAUQxqSxBRCx3LAFEOG8_xIQ4eywBRDviLEFEIWusQUQop2xBRDM364FEKiTsQUQpcL-EhDi1K4FEParsAUQ0-GvBRC9irAFEP-IsQUQntCwBRDbr68FEL22rgUQirCxBRCZjbEFEJGusQUQsO6wBRCmk7EFEPSrsAUQmZixBRDr6P4SEOzD_xIQkJKxBRDJ968FEI3MsAUQ3_WwBRDSsLEFEJ2msAUQooGwBRDwrLEFEKiSsQUQtrH_EhCLz7AFEKCwsQUQ2a-xBRD8hbAFEK-P_xIQzdewBRCUibEFEIiHsAUQtKCxBRDrmbEFEKrYsAUQppKxBRCWo7EFENfprwUQiOOvBRDViLAFEJDGsAUQg7n_EhDqw68FEJytsQUQ4auxBRCKwf8SEOiNsQUQ1-2tBRCBr7EFKixDQU1TSEJVZm9MMndETkhrQnZmcUFOazdvOGZwQzRTb0FQRzBCdThOSFFjPQ%3D%3D',
                    },
                    'userInterfaceTheme': 'USER_INTERFACE_THEME_DARK',
                    'timeZone': 'Asia/Saigon',
                    'browserName': 'Chrome',
                    'browserVersion': '127.0.0.0',
                    'acceptHeader': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                    'deviceExperimentId': 'ChxOelF3TXpJeU16WTFNelEyTkRJek1Ua3dPUT09ELCR9rUGGLCR9rUG',
                    'screenWidthPoints': 981,
                    'screenHeightPoints': 2177,
                    'screenPixelDensity': 4,
                    'screenDensityFloat': 3.5,
                    'utcOffsetMinutes': 420,
                    'connectionType': 'CONN_CELLULAR_4G',
                    'memoryTotalKbytes': '8000000',
                    'mainAppWebInfo': {
                        'graftUrl': 'https://www.youtube.com/@ThangLongTv',
                        'pwaInstallabilityStatus': 'PWA_INSTALLABILITY_STATUS_CAN_BE_INSTALLED',
                        'webDisplayMode': 'WEB_DISPLAY_MODE_BROWSER',
                        'isWebNativeShareAvailable': True,
                    },
                },
                'user': {
                    'lockedSafetyMode': False,
                },
                'request': {
                    'useSsl': True,
                    'internalExperimentFlags': [],
                    'consistencyTokenJars': [
                        {
                            'encryptedTokenJarContents': 'AKreu9sgXYUmkwdBSpvnhHj3YUoJCg325XAmDClIbqNNXCVe6x8P5-ntROpIQkRNn1AEOFydnQgEXvlwbzBO-oQCnsWakBECZ_Pi5IR0UUFZJ2BMMp4g6E3-ZDk',
                            'expirationSeconds': '600',
                        },
                    ],
                },
                'clientScreenNonce': 'vo8eYDm97WL3aTDo',
                'clickTracking': {
                    'clickTrackingParams': 'CCUQmysYASITCPrB-PeY9ocDFZMxewcd7UIUlDIJY2hhbm5lbHM0',
                },
                'adSignalsInfo': {
                    'params': [
                        {
                            'key': 'dt',
                            'value': '1723697329660',
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
                            'value': '5',
                        },
                        {
                            'key': 'u_h',
                            'value': '915',
                        },
                        {
                            'key': 'u_w',
                            'value': '412',
                        },
                        {
                            'key': 'u_ah',
                            'value': '915',
                        },
                        {
                            'key': 'u_aw',
                            'value': '412',
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
                            'value': '2176',
                        },
                        {
                            'key': 'biw',
                            'value': '980',
                        },
                        {
                            'key': 'brdim',
                            'value': '0,0,0,0,412,0,412,915,981,2177',
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
                f'{self.channelIds}',
            ],
            'params': 'EgIIAhgA',
        }

        response = requests.post(
            'https://www.youtube.com/youtubei/v1/subscription/subscribe',
            params=params,
            headers=headers,
            json=json_data,
        ).text
        try: 
            res = response.split('"content":{"runs":[{"text":"')[1].split(".")[0]
            print("cookie đã bị die")
        except Exception as e:
            print(response)

cookie = "HSID=AYrCpZowAx6ZBBsAR; SSID=AgdJaLpF3U6ggLAvA; APISID=DAKq_9eFvoeO2tyD/AyZepS2TrnhXpn1BY; SAPISID=eKIL1Zcu8XJloE_6/AsSwNnxX7TOwn9Twu; __Secure-1PAPISID=eKIL1Zcu8XJloE_6/AsSwNnxX7TOwn9Twu; __Secure-3PAPISID=eKIL1Zcu8XJloE_6/AsSwNnxX7TOwn9Twu; VISITOR_INFO1_LIVE=_iCeZClZ820; VISITOR_PRIVACY_METADATA=CgJWThIEGgAgRw%3D%3D; LOGIN_INFO=AFmmF2swRQIhAJLNYIyFlgpLnS7rWy-JNMFbTe8MGsY8agI-wV0l8VQ7AiB5QSyQ7iG6vZHaQLLFpP_9HgvVo9bsAt3dO7DsCs__Rg:QUQ3MjNmd0pmcVEzNmJweDRyblBhVEFTZDJINlZjME1uLUxJVFFNUDNyc01iOVZzeGVtOWJSa0Z3WXlXVk5vbVlwRzFWZEVfNTFJMzE2LS12cUg1djdtSmFBRGVaa1czakxQRWk4Vmd2Qk11SHZuaFhnSGlWWFZBTnBNdFhSQml0OHBhUjZfZ0RzMzlUS1lKV1I1NGhMYmktUzlIVE1IakdB; PREF=tz=Asia.Saigon&f6=40000000&f5=30000&f7=100; SID=g.a000nAguDeGV_ziPr-EGfOe3jD5q6hgTTsUaJ1kOa8a-_kp0sR-5cohZY0uoKNGfNTa0EP4vKQACgYKAUkSAQ8SFQHGX2MigGGUcalilQ7bjTVz523uUhoVAUF8yKqC7U_qYyigtqqAhpNbJjgl0076; __Secure-1PSID=g.a000nAguDeGV_ziPr-EGfOe3jD5q6hgTTsUaJ1kOa8a-_kp0sR-5APtatQGoUMU0S6A7g_tKxAACgYKATkSAQ8SFQHGX2Miqo1WtwYnk48_830TUpkf2RoVAUF8yKoM0j57Gs7d6tB5YHueiST80076; __Secure-3PSID=g.a000nAguDeGV_ziPr-EGfOe3jD5q6hgTTsUaJ1kOa8a-_kp0sR-5Mx933nU65pDEZzJURK1w2QACgYKAZkSAQ8SFQHGX2MiuIaDMADZMEvGJt2_tSp2TBoVAUF8yKrY3DwUj7ZMQYC3CFTfFGOL0076; YSC=cMuPPM3M1O4; __Secure-1PSIDTS=sidts-CjIBUFGoh2DkqMAuzGYfcgahBZixQx2dN9ozcdz_r_n5ea-aMU9UHFAqEwf71FQbIRqOcBAA; __Secure-3PSIDTS=sidts-CjIBUFGoh2DkqMAuzGYfcgahBZixQx2dN9ozcdz_r_n5ea-aMU9UHFAqEwf71FQbIRqOcBAA; SIDCC=AKEyXzU9XY1eQq-W3WmntgbcfWoaQppVETf-kEyhg2aXxn00CLeOoFCVENZBR292oTdnPO8V8w; __Secure-1PSIDCC=AKEyXzWe1Q9jRKjLru1XcE2az1f0tV-ypdFOcxYaGIEf8gRvBkqnqVZP-2mbAe1ZSiuBIx5emWM; __Secure-3PSIDCC=AKEyXzXKarojfYcjkCcpaDcKyzFWEk1-Ws1QEAg7w2zcRDkKq81WjNtbGfC602_9AZZbxmJTLkU; ST-4n4ru8=session_logininfo=AFmmF2swRQIhAJLNYIyFlgpLnS7rWy-JNMFbTe8MGsY8agI-wV0l8VQ7AiB5QSyQ7iG6vZHaQLLFpP_9HgvVo9bsAt3dO7DsCs__Rg%3AQUQ3MjNmd0pmcVEzNmJweDRyblBhVEFTZDJINlZjME1uLUxJVFFNUDNyc01iOVZzeGVtOWJSa0Z3WXlXVk5vbVlwRzFWZEVfNTFJMzE2LS12cUg1djdtSmFBRGVaa1czakxQRWk4Vmd2Qk11SHZuaFhnSGlWWFZBTnBNdFhSQml0OHBhUjZfZ0RzMzlUS1lKV1I1NGhMYmktUzlIVE1IakdB"
auth = 'SAPISIDHASH 1725002155_bbc499d826c1b9d93a4cc0aa1cee9300c6cb479f'
id_kenh = "UCr3lP3zs_wZZdFBOD_Eiwiw"

yt = API_YT(cookies=cookie,auth=auth,channelIds=id_kenh)
yt.api_yt()