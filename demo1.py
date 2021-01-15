import requests,json,sys

username=sys.argv[1]
password=sys.argv[2]
#登录抓包
url1="http://xuegong.qfnu.edu.cn:8080/authentication/login"
header1 = {
	'Host': 'xuegong.qfnu.edu.cn:8080',
	'User-Agent': 'Dart/2.10(dart:io)',
	'Accept-Encoding': 'gzip',
	'Content-Type': 'application/json',
	'Content-Length': '66'
}
data1={"username":username,"password":password,"type":"student"}
r1=requests.request("post",url1,json=data1,headers=header1)
r1=json.loads(r1.text)
uuid=r1['data']


# 获取个人信息
url2="http://xuegong.qfnu.edu.cn:8080/student/healthInfo/todayInfo"
header2 = {
	'Host': 'xuegong.qfnu.edu.cn:8080',
	'User-Agent': 'Dart/2.10(dart:io)',
	'Accept-Encoding': 'gzip',
	'cookie': 'syt.sessionId=' + uuid,
	'authorization': uuid
}
r2=requests.post(url=url2,headers=header2)
complexinfo=json.loads(r2.text)['data']
address=complexinfo['address']
location=complexinfo['location']
home=complexinfo['home']
selfinfo = {
	"home": home,
	"address": address,
	"keepInHome": "否",
	"keepInHomeDate": 'null',
	"keepInHomeReasonSite": "",
	"contact": "否",
	"contactType": "",
	"infect": "否",
	"infectType": "",
	"infectDate": "",
	"familyNCP": "否",
	"familyNCPType": "",
	"familyNCPDate": "",
	"familyNCPRelation": "",
	"cold": "否",
	"fever": "否",
	"feverValue": "",
	"cough": "否",
	"diarrhea": "否",
	"homeInHubei": "否",
	"arriveHubei": "无",
	"travel": "无",
	"remark": "无",
	"submitCount": 1,
	"contactDetail": "",
	"location": location,
	"naDetection": "否",
	"areaInfect": "否",
	"areaInfectType": "",
	"areaInfectDate": "",
	"areaInfectNumber": "",
	"contactAH": "否",
	"contactAHDetail": "",
	"outProvinceBack14": "未出省",
	"naDetectionDate": "",
	"pharynxResult": "阴性",
	"anusResult": "阴性",
	"saDetection": "否",
	"lgMResult": "阴性",
	"lgGResult": "阴性",
	"saDetectionDate": ""
}
selfinfo=json.dumps(selfinfo)

#提交健康信息

url3="http://xuegong.qfnu.edu.cn:8080/student/healthInfo/save"
header3 = {
	'Host': 'xuegong.qfnu.edu.cn:8080',
	'User-Agent': 'Dart/2.10(dart:io)',
	'Accept-Encoding': 'gzip',
	'Content-Type': 'application/json',
	'cookie': 'syt.sessionId=' + uuid,
	'authorization': uuid
}
r3=requests.post(url3,headers=header3,data=selfinfo)
print(r3.text)