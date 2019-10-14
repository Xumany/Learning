
import json

def josnencode(data):
	return json.loads(data)

def md5decode(data):
	md5 = hashlib.md5()
	for v in data:
		md5.update(v)
		str = md5.hexdigest()
		if str == '4faa8662c59590c6f43ae9fe5b002b42':
			print(v)


if __name__ == "__main__":
			data = '{"weburl":"http://home.yd.chaoxing.com/home/getcxHomePage?incode=cx&ttt=1570881465100","dwtype":1,"hometype":1}},"boundaccount":2,"loginId":0,"codeInfo":{},"invitecode":"3071","pic":"http://photo.chaoxing.com/p/104352589_80?flag=1&psize=100_100c&ext=jpg&t=1567647790593","source":"login_sync","type":2,"ranknum":"40450104","isCertify":1,"uname":"1730663","copyRight":600,"unitConfig":{},"schoolname":"咸宁职业技术学院","unitConfigInfo":{},"unitConfigInfos":[{"fid":3071,"uname":"1730663"}],"phone":"17671314203","bindFanya":true,"updateWay":"passport登录：完善绑定用户","name":"徐多","fullpinyin":"xu duo","status":1,"roleid":"3","industry":6,"nick":"徐多","uid":72814370,"acttime2":"2019-09-05 09:16:53","dxfid":"1981","puid":104352589,"rights":1,"needIntruction":0,"bindOpac":false,"ppfid":"3071","accountInfo":{"cx_opac":{"loginId":1,"tiptitle":"此功能需要绑定借阅证账号/一卡通账号进行认证，如有疑问，请联系图书馆管理员","loginUrl":"http://mc.m.5read.com/ssoLogin.do","boundUrl":"http://mc.m.5read.com/ssoLogin.do?name=${uname}&pwd=${pwd}&fid=${dxfid}&boundUrl=http%3A%2F%2Fsso.chaoxing.com%2Fapis%2Flogin%2FuserBound.do&uid=72814370","tippwd":"借阅证密码","tipuname":"借阅证账号/一卡通账号"},"imAccount":{"uid":72814370,"password":"03CE51068A322A6E","created":1566960662621,"modified":1566960662621,"type":"user","uuid":"ac3af0d0-c93e-11e9-a24c-41e3bab154a9","activated":1,"username":"72814370"}'
			data = josnencode(data)
