import requests
import random
import time
headers = {
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'zh-CN,zh;q=0.9',
        'content-language': 'zh-CN',
        # 'cookie': 'p_uv_id=242167a500065d17dcfba99b8a3e4d7c',
        'origin': 'https://business.mickey.business',
        'priority': 'u=1, i',
        'referer': 'https://business.mickey.business/',
        'sec-ch-ua': '"Chromium";v="130", "Google Chrome";v="130", "Not?A_Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36',
}


data = {
    'email': '2121432411341@qq.com',
    'password': '12345678',
    'invite_code': '3guPMWLn',
    'email_code': '',
}
v2_url = ['0','1','2','3','4','5','6','7','8','9']
for i in range(2):
        account = ''
        randomlength = 10
        base_str = '0123456789'
        length = len(base_str) - 1
        for i in range(randomlength):
            account += base_str[random.randint(0, length)]
        print(account)
        data['email'] = f"{account}@qq.com"
        
        response = requests.post('https://business.mickey.business/api/v1/passport/auth/register',
                                 headers=headers, data=data)
        # response = requests.post('http://business.mickey.business/api/v1/passport/auth/register', headers=headers, cookies = cookies,data=data, proxies=proxies)
        print(response)
        print(response.json())
        response = response.json()
        token = response['data']['token']
        print(token)
        #print(f"https://sub.mickeyi.lol/api/v1/client/subscribe?token={token}")
        v2_url[i] = f"https://sub.mickeyi.lol/api/v1/client/subscribe?token={token}|"
        print(v2_url[i])
        #time.sleep(120)
strr = ''
for i in v2_url:
        strr = strr + str(i)
print('strr:')
print(strr)











