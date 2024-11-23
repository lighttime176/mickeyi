import random,time
import imaplib
import email
import re
from DrissionPage import ChromiumPage
from DrissionPage import ChromiumOptions

# 创建页面对象
co = ChromiumOptions().auto_port()  # 指定程序每次使用空闲的端口和临时用户文件夹创建浏览器
co.headless(True)   # 无头模式
co.set_argument('--no-sandbox')  # 无沙盒模式
co.set_argument('--headless=new')  # 无界面系统添加
co.set_paths(browser_path="/opt/google/chrome/google-chrome")  # 设置浏览器路径
co.set_argument('--disable-gpu')    # 禁用gpu，提高加载速度
co.set_user_agent("Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:65.0) Gecko/20100101 Firefox/65.0") 
browser = ChromiumPage(co)
tab = browser.latest_tab
url = "https://business.mickey.business/#/register?code=VVIJFE2q"
tab.get(url)
tab.wait(2)
print(tab.user_agent)

account = ''
randomlength = 10
base_str = '0123456789'
length = len(base_str) - 1
for i in range(randomlength):
    account += base_str[random.randint(0, length)]
email = f"{account}@176468.xyz"
print(email)
ele = tab.ele('css=#app > div > div > div > div > div.p-24 > div:nth-child(3) > div > div > div.n-input-wrapper > div > input')
print(ele)
ele.clear()
ele.input(email)
time.sleep(1)
ele = tab.ele('css=#app > div > div > div > div > div.p-24 > div:nth-child(4) > div > button > span')
print(ele)
ele.click()
print('等待邮件验证码：')
for itime in range(20):
    time.sleep(1)
    print(itime)
EMAIL_ADDRESS = 'luo1764682172@163.com'
EMAIL_PASSWORD = 'ZHQgy35wE28LqzTU'
server = imaplib.IMAP4_SSL(host='imap.163.com', port=993)
#网易邮箱需要发送额外的Command验证后才能登录
#https://blog.csdn.net/jony_online/article/details/108638571
imaplib.Commands ['ID'] = ('NONAUTH', 'AUTH', 'SELECTED')
args = ("name", "imaplib", "version", "1.0.0")
typ, dat = server._simple_command('ID', '("' + '" "'.join(args) + '")')
server.login (EMAIL_ADDRESS, EMAIL_PASSWORD)
#print(server.list())
server.select("INBOX")
typ,data = server.search(None,'ALL')#'ALL',or 'SEEN'
data[0].split()
fetch_data_lst = []
for num in data[0].split():
    typ,fetch_data = server.fetch(num,'(RFC822)')
    fetch_data_lst.append(fetch_data)
# for fetch_data in fetch_data_lst:
#     msg = email.message_from_bytes(fetch_data[0][1])
#     for part in msg.walk():
#         print(part.get_content_type())
#         if part.get_content_maintype() == 'text':
#             body = part.get_payload(decode=True)
#             text = body.decode('utf8')
#             print(text)
fetch_data = fetch_data_lst[-1]
msg = email.message_from_bytes(fetch_data[0][1])
#print(msg)
print((msg['subject']))
# result = msg['subject'].find('Mickey')
# print('result:',result)
if msg['subject'] == 'MickeyEmail verification code':
    for part in msg.walk():
        #print(part.get_content_type())
        if part.get_content_maintype() == 'text':
            body = part.get_payload(decode=True)
            text = body.decode('utf8')
            #print(text)
    match = re.search(r"验证码是：(\d+)", text)
    if match:
        verification_code = match.group(1)
        print("验证码:", verification_code)
    else:
        print("未找到验证码")
vcode = verification_code

#print(vcode)
ele = tab.ele('css=#app > div > div > div > div > div.p-24 > div:nth-child(4) > div > div > div.n-input-wrapper > div > input')
ele.input(vcode)
ele = tab.ele('css=#app > div > div > div > div > div.p-24 > div:nth-child(5) > div > div.n-input-wrapper > div.n-input__input > input')
ele.input('12345678')
ele = tab.ele('css=#app > div > div > div > div > div.p-24 > div:nth-child(6) > div > div.n-input-wrapper > div.n-input__input > input')
ele.input('12345678')
ele = tab.ele('css=#app > div > div > div > div > div.p-24 > div:nth-child(9) > button')
tab.listen.start(targets='/register')  # 开始监听，指定获取包含该文本的数据包
ele.click()
res = tab.listen.wait().response
res = res.body
print(res)
token = res['data']['token']
v2_url = f"https://sub.mickeyi.lol/api/v1/client/subscribe?token={token}"
print(v2_url)
tab.get_screenshot(path=r"./test_browser_page.png", full_page=True)
with open(r"./test_browser.html", "w", encoding="utf-8") as f:
    f.write(tab.html)


browser.quit()
 
