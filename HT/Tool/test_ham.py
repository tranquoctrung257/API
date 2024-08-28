import requests
import re

headers = {'authority': 'mbasic.facebook.com','cache-control': 'max-age=0','sec-ch-ua': '"Google Chrome";v="93", " Not;A Brand";v="99", "Chromium";v="93"','sec-ch-ua-mobile': '?0','sec-ch-ua-platform': '"Windows"','upgrade-insecure-requests': '1','origin': 'https://mbasic.facebook.com','content-type': 'application/x-www-form-urlencoded','user-agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36','accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site': 'same-origin','sec-fetch-mode': 'navigate','sec-fetch-user': '?1','sec-fetch-dest': 'document','referer': 'https://mbasic.facebook.com/','accept-language': 'en-US,en;q=0.9','cookie': 'sb=tSbIZXr0G2tGnZIpSlNdSWge;datr=tSbIZRcfBccxMakloKJajZ3F;ps_l=1;ps_n=1;c_user=100084175577269;wd=1920x945;fr=11DOikHSmnloq4F0o.AWWnQXW4z9flVPRo3Q1cEbZlTA0.BmyqCZ..AAA.0.0.BmyqCZ.AWVaPAyq4J4;xs=26%3Awna4SwqsZwHRVg%3A2%3A1724061914%3A-1%3A6281%3A%3AAcWVqrvpMV7bVDlo3xrwomAElk9TPVs1aff1BsxlFQ;'}
def reac_cmt( id, type_react):
		access = ""
		url = requests.get("https://mbasic.facebook.com/"+id, headers=headers, proxies="").url
		if id in url:
			return False
		index = 1 if type_react == "LIKE" else 2 if type_react == "LOVE" else 3 if type_react == "CARE" else 4 if type_react == "HAHA" else 5 if type_react == "WOW" else 6 if type_react == "SAD" else 7
		access = requests.get(url, headers=headers).text
		while True:
			if id in access:
				find_cmt = access.split(id)[1].split('</a></span></span>')[0].split('/reactions/picker/?')[1].split('"')[0].replace("amp;", "")
				access = requests.get("https://mbasic.facebook.com/reactions/picker/?"+find_cmt, headers=headers).text
				ufi = access.split('/ufi/reaction/?')
				hoan_thanh = requests.get("https://mbasic.facebook.com/ufi/reaction/?"+ufi[index].split('"')[0].replace("amp;", ""), headers=headers).text
				print(hoan_thanh)
			else:
				if "/comment/replies/" in url:
					xemthemcmt = access.split('/comment/replies/?')[1].split('"')[0].replace("amp;", "")
					access = requests.get("https://mbasic.facebook.com/comment/replies/?"+xemthemcmt, headers=headers).text
				else:
					xemthemcmt = access.split('/story.php?')[1].split('</a></div></div>')[0].replace("amp;", "").split('"')[0]
					access = requests.get("https://mbasic.facebook.com/story.php?"+xemthemcmt, headers=headers).text
reac_cmt("872506561479716","LOVE")