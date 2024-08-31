import requests



            
def get_acc(auth):
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
    't': 'VFZSamVVNVVRWGROYW1jMFQwRTlQUT09',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36',
    }

    response = requests.get('https://gateway.golike.net/api/youtube-account', headers=headers)
    try:
        id = response.json()["data"][0]["id"]
        nick_name = response.json()["data"][0]["channel_id"]
        return id,nick_name
    except:
        return False
    

def get_job(auth,account_id):
        
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

    params = {
            'account_id': account_id,
        }

    response = requests.get('https://gateway.golike.net/api/advertising/publishers/youtube/jobs', params=params, headers=headers)
    if response.status_code == 400:
        return response.json()['message']
    else:
        # return response.json()
        if 'comment_run' in response.text:
            message = response.json()["data"]["comment_run"]["message"]
            link = response.json()["data"]["link"]
            # return link,message
            return False
        else:
            return response.json()["data"]["link"],response.json()["data"]["object_id"]
def main():
    auth = "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwOlwvXC9nYXRld2F5LmdvbGlrZS5uZXRcL2FwaVwvbG9naW4iLCJpYXQiOjE3MTQ3MzUxNzgsImV4cCI6MTc0NjI3MTE3OCwibmJmIjoxNzE0NzM1MTc4LCJqdGkiOiJoQ1JFWElzOWViQ3p5eTVGIiwic3ViIjoyMTAyMDY4LCJwcnYiOiJiOTEyNzk5NzhmMTFhYTdiYzU2NzA0ODdmZmYwMWUyMjgyNTNmZTQ4In0.hRTMIYrKXHeWfqTSPZoOiHPgfbGnx5hhBRDLwV6Afrs"
    acc = get_acc(auth)[0]
    print(get_job(auth,acc))
main()