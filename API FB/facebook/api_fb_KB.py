    # fb_dtsg = requests.get("https://mbasic.facebook.com/",headers=headers,cookies=cookies).text.split('name="fb_dtsg" value="')[1].split('"')[0]
    # print(fb_dtsg)

import requests,pprint
def API_FB_KET_BAN(id,cookie):
    cookies = {
        'sb': cookie.split("sb=")[1].split(';')[0],
        'datr': cookie.split("datr=")[1].split(';')[0],
        'c_user': cookie.split("c_user=")[1].split(';')[0],
        # 'm_page_voice': cookie.split("m_page_voice=")[1].split(';')[0],
        'xs': cookie.split("xs=")[1].split(';')[0],
        'fr': cookie.split("fr=")[1].split(';')[0],
        'presence': cookie.split("presence=")[1].split(';')[0]
    }
    headers = {
        'accept': '*/*',
        'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
        'content-type': 'application/x-www-form-urlencoded',
        'origin': 'https://www.facebook.com',
        'priority': 'u=1, i',
        'referer': 'https://www.facebook.com/profile.php?id=100054518530464',
        'sec-ch-prefers-color-scheme': 'dark',
        'sec-ch-ua': '"Chromium";v="128", "Not;A=Brand";v="24", "Google Chrome";v="128"',
        'sec-ch-ua-full-version-list': '"Chromium";v="128.0.6613.85", "Not;A=Brand";v="24.0.0.0", "Google Chrome";v="128.0.6613.85"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-model': '""',
        'sec-ch-ua-platform': '"Windows"',
        'sec-ch-ua-platform-version': '"15.0.0"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36',
        'x-asbd-id': '129477',
        'x-fb-friendly-name': 'FriendingCometFriendRequestSendMutation',
        'x-fb-lsd': 'CK-sMyTGf2RFBtfFwQjVXb',
    }
    fb_dtsg = requests.get("https://mbasic.facebook.com/",headers=headers,cookies=cookies).text.split('name="fb_dtsg" value="')[1].split('"')[0]
    id_friend = requests.get(f"https://www.facebook.com/{id}/",headers=headers,cookies=cookies).text.split(',"userID":"')[1].split('"')[0]
    av = cookie.split("c_user=")[1].split(';')[0]
    data = {
        'av': av,
        'fb_dtsg': fb_dtsg,
        'variables': '{"input":{"attribution_id_v2":"ProfileCometTimelineListViewRoot.react,comet.profile.timeline.list,via_cold_start,1724856492524,6360,250100865708545,,","friend_requestee_ids":["'+id_friend+'"],"friending_channel":"PROFILE_BUTTON","warn_ack_for_ids":[],"actor_id":"'+av+'","client_mutation_id":"1"},"scale":1}',
        'doc_id': '7607575099364225',
    }

    response = requests.post('https://www.facebook.com/api/graphql/', cookies=cookies, headers=headers, data=data)
    

API_FB_KET_BAN("61556583153961","sb=RHGvZp-dhN2fBYN7gWkcv1Hm;datr=RHGvZiKYmHXNSoEA7ABQRE4t;ps_l=1;ps_n=1;c_user=100076933605337;xs=18%3AxwMYDh-ZD_1vjQ%3A2%3A1724044358%3A-1%3A6275%3A%3AAcUjahpEeLXtDwCq4o0M_z-2-FUsTT8GyevrtJnebA;fr=1crPWPNIZqA6ZOS4z.AWVGCZfyEa3ka0uKomr6mIOpvs8.Bm0DTO..AAA.0.0.Bm0DVM.AWX3wMNcw7k;wd=1920x911;presence=C%7B%22t3%22%3A%5B%5D%2C%22utc3%22%3A1724921846877%2C%22v%22%3A1%7D;")
