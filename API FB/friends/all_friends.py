import requests

cookies = {
    'sb': 'XpSCZpgqpRaQapzV5d7jAc3W',
    'datr': 'XpSCZvTyL4kWeq5YH0EH905R',
    'ps_n': '1',
    'ps_l': '1',
    'c_user': '100069089687778',
    'm_page_voice': '100069089687778',
    'locale': 'vi_VN',
    'fbl_st': '100438805%3BT%3A28745837',
    'wl_cbv': 'v2%3Bclient_version%3A2603%3Btimestamp%3A1724750243',
    'dpr': '1',
    'xs': '11%3A3autNA0cFlRL-g%3A2%3A1723541647%3A-1%3A6411%3A%3AAcWHsSF8i92aVOl6CGC4us4qg3KBdycjxXnlkjeYFCE',
    'fr': '1LiOCVShxniclXKPG.AWU_b8ow7MT_bpAq_JdqNRwWKpo.Bm0C7E..AAA.0.0.Bm0DyE.AWV27jOcdHI',
    'wd': '1920x911',
    'presence': 'C%7B%22t3%22%3A%5B%5D%2C%22utc3%22%3A1724925423418%2C%22v%22%3A1%7D',
}

headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'vi,en;q=0.9,vi-VN;q=0.8',
    'cache-control': 'no-cache',
    # 'cookie': 'sb=XpSCZpgqpRaQapzV5d7jAc3W; datr=XpSCZvTyL4kWeq5YH0EH905R; ps_n=1; ps_l=1; c_user=100069089687778; m_page_voice=100069089687778; locale=vi_VN; fbl_st=100438805%3BT%3A28745837; wl_cbv=v2%3Bclient_version%3A2603%3Btimestamp%3A1724750243; dpr=1; xs=11%3A3autNA0cFlRL-g%3A2%3A1723541647%3A-1%3A6411%3A%3AAcWHsSF8i92aVOl6CGC4us4qg3KBdycjxXnlkjeYFCE; fr=1LiOCVShxniclXKPG.AWU_b8ow7MT_bpAq_JdqNRwWKpo.Bm0C7E..AAA.0.0.Bm0DyE.AWV27jOcdHI; wd=1920x911; presence=C%7B%22t3%22%3A%5B%5D%2C%22utc3%22%3A1724925423418%2C%22v%22%3A1%7D',
    'dpr': '1',
    'pragma': 'no-cache',
    'priority': 'u=0, i',
    'sec-ch-prefers-color-scheme': 'dark',
    'sec-ch-ua': '"Chromium";v="128", "Not;A=Brand";v="24", "Google Chrome";v="128"',
    'sec-ch-ua-full-version-list': '"Chromium";v="128.0.6613.113", "Not;A=Brand";v="24.0.0.0", "Google Chrome";v="128.0.6613.113"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-model': '""',
    'sec-ch-ua-platform': '"Windows"',
    'sec-ch-ua-platform-version': '"15.0.0"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36',
    'viewport-width': '1288',
}

response = requests.get('https://www.facebook.com/nguyenhongvip2/friends', cookies=cookies, headers=headers)
print(response.text)