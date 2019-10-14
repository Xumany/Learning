import requests
import hashlib
import json
def w_json(data):
	'''当数据存储到文件中'''
	with open('json_test.json', 'w') as w:
		json.dump(data,w)
	print('ok')

def login():
	uname = input("请输入账号:")
	passworld = input("请输入密码:")
	url = 'https://passport2-api.chaoxing.com/v11/loginregister?uname='+ str(uname)+'&code='+ str(passworld)+'&cx_xxt_passport=json&loginType=1&roleSelect=true'
	r = requests.get(url)
	cookies = requests.utils.dict_from_cookiejar(r.cookies)
	return cookies

if __name__ == '__main__':
	login_url = 'https://sso.chaoxing.com/apis/login/userLogin4Uname.do'
	headers = {"User-Agent":"Mozilla/5.0 (iPhone; CPU iPhone OS 12_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/16A366 ChaoXingStudy/ChaoXingStudy_3_4.3.1_ios_phone_201909191720_27 (@Kalimdor)_4233108647765227054",
}
	re = requests.get(login_url,headers = headers, cookies = login())
	print(re.json()['msg']['name'])
	
