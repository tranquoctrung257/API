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

cookie = "HSID=A5DRLbnxyqTYwDTIu; SSID=AcnNV-aXFQ-HSWv-R; APISID=x2Oh6Mt_HRxlR-Pq/ANQSzFioK9zDEhewW; SAPISID=Kq9NdFMQCUgGXyiD/A7S3KqIPXSrCHFhz7; __Secure-1PAPISID=Kq9NdFMQCUgGXyiD/A7S3KqIPXSrCHFhz7; __Secure-3PAPISID=Kq9NdFMQCUgGXyiD/A7S3KqIPXSrCHFhz7; VISITOR_INFO1_LIVE=SZujpXAW1Yc; VISITOR_PRIVACY_METADATA=CgJWThIEGgAgFA%3D%3D; LOGIN_INFO=AFmmF2swRQIgc7tpalOQq9YLd2xcudm03FawrdbG4PZAhhkhh1QVQ8sCIQCJRK1XFGzlnG31UxW2u_HwSEeG-ANsnr6KZ7eVhvldnw:QUQ3MjNmd1J6YllMODIySkZjSXlqZWI0UXRNOWtWaDM3cEFEbmhULW40LVBQdURkRDhOM2lGbVc3eE1TOHNXZkdmNDR4U1hnOW5FeFoxQ1QzMFhNREdRdGtkbjVTdzd1RTVIRmpzZ1B5U0UxeG5GbXJVUUJ4ckZzVTdsWEx0ejZLY3RVZXBtN3Qwc2FsdmhqdzJwSDM4dmpmcmYzckRmNU9B; PREF=f6=40000000&tz=Asia.Saigon&f7=100; NID=516=T0ytHDJ7P1NQUcHRbpBevtMqSLp24aT9dCM41TEt6TNIEaAViA2Dc5MOQ1L2fW2Syvh0-q-IYqjD_ruATchB3AUEwxBNmoKAy-GePjSFgEnwCd932d7F0sc8onzL9Jc2q4chozQmHo2rit5hVErxBXA-rtEM83iFXXtos7dyvit3xzN7XCDNo0FjGY6O5mpfNlfjfSdA0_SZJ5PMKQtGG0wPVqvenfq783GAoNgn52q0L6tG; SID=g.a000nAjcna0ehNXob4mq0nv7_YUSNTOMGgjZw82Go36vgiHpDCeo7IgbCnfO4wwbgm6ikARrbwACgYKAZcSARMSFQHGX2MilGDXw1Fe_H3C8WZMCSDhBhoVAUF8yKpdSTgUzUNP-LRhvFiFaLK50076; __Secure-1PSID=g.a000nAjcna0ehNXob4mq0nv7_YUSNTOMGgjZw82Go36vgiHpDCeoAiNyjNTYqlHLq7KbYts16gACgYKAS8SARMSFQHGX2MiAbXwts5zHgZRKZ0yoKwe8BoVAUF8yKqaKBW1y6PUSFnglvk_8GW-0076; __Secure-3PSID=g.a000nAjcna0ehNXob4mq0nv7_YUSNTOMGgjZw82Go36vgiHpDCeoYq_nhYqSQRQ8tLzyQHpC0QACgYKATcSARMSFQHGX2MieIBiIyGvjuX4hWHd53UIhhoVAUF8yKpSfuWg-chmT0gIf-dROjuA0076; YSC=wdD9kj6W9sA; __Secure-1PSIDTS=sidts-CjEBUFGoh2jDWTc0q1JqEr8wZkbuXW62R2jS84vy5MUGVQhFxJFKs7AawKu5kuizoD3oEAA; __Secure-3PSIDTS=sidts-CjEBUFGoh2jDWTc0q1JqEr8wZkbuXW62R2jS84vy5MUGVQhFxJFKs7AawKu5kuizoD3oEAA; SIDCC=AKEyXzWUSOINZ7DO78hPIrvBELizBd-i0ijXrCfYN1cu2B1mCoRM-9ppnOf3MMyLHvYdj5F9N3c; __Secure-1PSIDCC=AKEyXzXqn_Ny2z70kNFfzScUXzFBZgarqph5mxuKwlKpebshF47_Rmhb_Ifbzhr8JxnrwxDCaw; __Secure-3PSIDCC=AKEyXzVExhQhjpDyriYJkMSkeQsrc3pdIrpV04OjSvKdy_ViccglCQHYCm70T7GQ0GGkGektJQ; ST-4n4ru8=session_logininfo=AFmmF2swRQIgc7tpalOQq9YLd2xcudm03FawrdbG4PZAhhkhh1QVQ8sCIQCJRK1XFGzlnG31UxW2u_HwSEeG-ANsnr6KZ7eVhvldnw%3AQUQ3MjNmd1J6YllMODIySkZjSXlqZWI0UXRNOWtWaDM3cEFEbmhULW40LVBQdURkRDhOM2lGbVc3eE1TOHNXZkdmNDR4U1hnOW5FeFoxQ1QzMFhNREdRdGtkbjVTdzd1RTVIRmpzZ1B5U0UxeG5GbXJVUUJ4ckZzVTdsWEx0ejZLY3RVZXBtN3Qwc2FsdmhqdzJwSDM4dmpmcmYzckRmNU9B"
auth = 'SAPISIDHASH 1724045122_f3eee06ef33f888deec1c52ee6b85c86989c20a4'
id_kenh = "UCL9-pEHNBs3N4r2bMoXdLJA"

yt = API_YT(cookies=cookie,auth=auth,channelIds=id_kenh)
yt.api_yt()