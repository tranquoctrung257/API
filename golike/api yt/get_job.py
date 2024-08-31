import requests

class GL():
    def __init__(self,auth,account_id) -> None:
        self.auth = auth
        self.account_id = account_id
    def get_job(self):
        
        print(self.account_id)
        headers = {
            'accept': 'application/json, text/plain, */*',
            'accept-language': 'vi,en;q=0.9,vi-VN;q=0.8',
            'authorization': self.auth,
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
            'account_id': self.account_id,
        }

        response = requests.get('https://gateway.golike.net/api/advertising/publishers/youtube/jobs', params=params, headers=headers)
        if response.status_code == 400:
            return response.json()['message']
        else:
            # return response.json()['data']['link']
            if 'comment_run' in response.text:
                message = response.json()["data"]["comment_run"]["message"]
                link = response.json()["data"]["link"]
                # return link,message
                return False
            else:
                return response.json()["data"]["link"]

            
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
auth = "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwOlwvXC9nYXRld2F5LmdvbGlrZS5uZXRcL2FwaVwvbG9naW4iLCJpYXQiOjE3MjM5ODYxMzMsImV4cCI6MTc1NTUyMjEzMywibmJmIjoxNzIzOTg2MTMzLCJqdGkiOiI4VVo2aDBCUHBRakl4SnIzIiwic3ViIjoyODI1NDM1LCJwcnYiOiJiOTEyNzk5NzhmMTFhYTdiYzU2NzA0ODdmZmYwMWUyMjgyNTNmZTQ4In0.rFVtzCBUR5Bf7Se9ffm2g08e7kTPSTjYKrB_m0wIQeI"
def main():
    id_acc = get_acc(auth)[0]
    gl = GL(auth,id_acc)
    job = gl.get_job()
    print(job)
main()