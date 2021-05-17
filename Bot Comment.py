import requests
import re
import os
import time
from time import sleep

done = 0
# - -
error = 0

r = requests.session()

banner1 = '''
.______     ______   .___________.                 
|   _  \   /  __  \  |           |                 
|  |_)  | |  |  |  | `---|  |----`                 
|   _  <  |  |  |  |     |  |                      
|  |_)  | |  `--'  |     |  |                      
|______/   \______/      |__|                      
                                                   
      ______   ______   .___  ___. .___  ___. 
     /      | /  __  \  |   \/   | |   \/   | 
    |  ,----'|  |  |  | |  \  /  | |  \  /  | 
    |  |     |  |  |  | |  |\/|  | |  |\/|  | 
    |  `----.|  `--'  | |  |  |  | |  |  |  | 
     \______| \______/  |__|  |__| |__|  |__| 
          
                  
'''

print(banner1)

print("by @TweakPY in Telegram\n\n")


user = input('Enter Username :')
pess = input('Enter Password :')
url1 = 'https://www.instagram.com/accounts/login/ajax/'
head1 = {
	'accept': '*/*',
	'accept-encoding': 'gzip, deflate, br',
	'accept-language': 'en-US,en;q=0.9',
	'content-length': '269',
	'content-type': 'application/x-www-form-urlencoded',
	'cookie': 'ig_did=CBE027FC-62A2-4383-85BB-63843B14C94F; ig_nrcb=1; mid=X85qiQALAAFugGOZjugz_zBUZQHx; datr=SD8HYG1W7e-ghmx_vRH1TB7V; fbm_124024574287414=base_domain=.instagram.com; shbid=3563; shbts=1612115664.6497803; rur=VLL; csrftoken=y3yTqqHa0mjqe3ytTy9IBMXw23Z5TT3G',
	'origin': 'https://www.instagram.com',
	'referer': 'https://www.instagram.com/',
	'sec-ch-ua-mobile': '?1',
	'sec-fetch-dest': 'empty',
	'sec-fetch-mode': 'cors',
	'sec-fetch-site': 'same-origin',
	'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Mobile Safari/537.36',
	'x-csrftoken': 'y3yTqqHa0mjqe3ytTy9IBMXw23Z5TT3G',
	'x-ig-app-id': '936619743392459',
	'x-ig-www-claim': 'hmac.AR2kUU6QD4ZMYLZ-anFcEb7SWiyQTfkx3NQ_KuXrhuCHqUhr',
	'x-instagram-ajax': '7a3a3e64fa87',
	'x-requested-with': 'XMLHttpRequest'
}
data1 = {
	'username': f'{user}',
	'enc_password': f'#PWD_INSTAGRAM_BROWSER:0:&:{pess}'
}
log = r.post(url1, headers=head1, data=data1)
if '"authenticated":true' in log.text:
	print(f"Done Login {user}")
else:
	print(f'Error Login {user} Try again later ')
	print(" ")
	input("Press Enter To Close Program ...")
sessi = log.cookies['sessionid']
post_url = input("Post Url :")
post_id_url = post_url+'?__a=1'
try_to_get_post_id = r.get(post_id_url).text
pst = re.findall('"GraphImage","id":"(.*?)"', try_to_get_post_id)
post_id = " ".join(pst)
url2 = f'https://www.instagram.com/web/comments/{post_id}/add/'
head2 = {
    'accept': '*/*',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'en-US,en;q=0.9',
    'content-length': '40',
    'content-type': 'application/x-www-form-urlencoded',
    'cookie': 'ig_did=CBE027FC-62A2-4383-85BB-63843B14C94F; ig_nrcb=1; mid=X85qiQALAAFugGOZjugz_zBUZQHx; datr=SD8HYG1W7e-ghmx_vRH1TB7V; fbm_124024574287414=base_domain=.instagram.com; shbid=3563; shbts=1612115664.6497803; rur=VLL; csrftoken=wAMF4pT7fjbq9ewLB8bmf8cQNZUa3VlX; ds_user_id=45286827132; sessionid='+sessi,
    'origin': 'https://www.instagram.com',
    'referer': 'https://www.instagram.com/p/CKuC44sLbBI/comments/',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Mobile Safari/537.36',
    'x-csrftoken': 'wAMF4pT7fjbq9ewLB8bmf8cQNZUa3VlX',
    'x-ig-app-id': '1217981644879628',
    'x-ig-www-claim': 'hmac.AR2kUU6QD4ZMYLZ-anFcEb7SWiyQTfkx3NQ_KuXrhuCHqUhr',
    'x-instagram-ajax': '7a3a3e64fa87',
    'x-requested-with': 'XMLHttpRequest'
}
com = input('Enter Comment :')
slp = int(input('Enter Sleep :'))
data2 = {
    'comment_text': f'{com}',
    'replied_to_comment_id': ''
}
while True:
	pcom = r.post(url2, headers=head2, data=data2)
	if ('"status":"ok"') in pcom.text:
                done +=1
                os.system('cls' if os.name == 'nt' else 'clear')
                print(f'{banner1}\n- BOT COMMENT STARTING by @TweakPY -\n\n=============================\n\n[-] Done Send Comment : {done}\n\n[-] Error Send Comment : {error}\n\n=============================')
                sleep(slp)
                
	else:
                error +=1
                os.system('cls' if os.name == 'nt' else 'clear')
                print(f'{banner1}\n- BOT COMMENT STARTING by @TweakPY -\n\n=============================\n\n[-] Done Send Comment : {done}\n\n[-] Error Send Comment : {error}\n\n=============================')
                sleep(slp)
