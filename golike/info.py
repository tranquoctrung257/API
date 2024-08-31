import requests

headers = {
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'vi',
    'authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwOlwvXC9nYXRld2F5LmdvbGlrZS5uZXRcL2FwaVwvbG9naW4iLCJpYXQiOjE3MjM5ODYxMzMsImV4cCI6MTc1NTUyMjEzMywibmJmIjoxNzIzOTg2MTMzLCJqdGkiOiI4VVo2aDBCUHBRakl4SnIzIiwic3ViIjoyODI1NDM1LCJwcnYiOiJiOTEyNzk5NzhmMTFhYTdiYzU2NzA0ODdmZmYwMWUyMjgyNTNmZTQ4In0.rFVtzCBUR5Bf7Se9ffm2g08e7kTPSTjYKrB_m0wIQeI',
    'cache-control': 'no-cache',
    'content-type': 'application/json;charset=utf-8',
    'origin': 'https://app.golike.net',
    'pragma': 'no-cache',
    'priority': 'u=1, i',
    'referer': 'https://app.golike.net/',
    'sec-ch-ua': '"Chromium";v="129", "Not=A?Brand";v="8"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    't': 'VFZSamVVNVVRWGxOZWtrd1RtYzlQUT09',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36',
}

response = requests.get('https://gateway.golike.net/api/statistics/report', headers=headers).json()
print(response)