import requests
import csv
import json
import time

base_url = "https://api.apjc.amp.cisco.com/v3/"
url = "https://visibility.apjc.amp.cisco.com/iroh/oauth2/token"

payload = "grant_type=client_credentials"
#authorization : Basic の後ろにはSecureXで発行したAPI Client IDとPasswordをBase64に変換して記入（例：Client IDがclient-d3sd4dg5-3f9e-4hds-8adw-d08a5d8e8hds, Client passwordがJv6cjPQDQni2KD9sr7IFHqxZ2_iH6ceDLSSEBWx6pmsL5Am6ZxzTXQの場合はIDとPasswordをコロン(:)で繋いで"client-d3sd4dg5-3f9e-4hds-8adw-d08a5d8e8hds:Jv6cjPQDQni2KD9sr7IFHqxZ2_iH6ceDLSSEBWx6pmsL5Am6ZxzTXQ"の形にした後にBase64に変換して＞”Y2xpZW50LWQzc2Q0ZGc1LTNmOWUtNGhkcy04YWR3LWQwOGE1ZDhlOGhkczpKdjZjalBRRFFuaTJLRDlzcjdJRkhxeFoyX2lINmNlRExTU0VCV3g2cG1zTDVBbTZaeHpUWFE=”とし、それを'authorization': "Basicの後に貼り付ける
headers = {
    'content-type': "application/x-www-form-urlencoded",
    'accept': "application/json",
    'authorization': "Basic Y2xpZW50LWQzc2Q0ZGc1LTNmOWUtNGhkcy04YWR3LWQwOGE1ZDhlOGhkczpKdjZjalBRRFFuaTJLRDlzcjdJRkhxeFoyX2lINmNlRExTU0VCV3g2cG1zTDVBbTZaeHpUWFE=", 
    'cache-control': "no-cache",
    }

response = requests.request("POST", url, data=payload, headers=headers)
#print(response.text)
time.sleep(0.2)

#SecureX API アクセストークン
accesstoken = response.json()["access_token"]
#print(accesstoken)

url2 = base_url+"access_tokens"
header4endpoint = {
    "Authorization": "Bearer " + accesstoken
    }
response_accesstoken = requests.request("POST", url2, headers=header4endpoint)
#print(response_accesstoken.json())

#Secure Endpoint API アクセストークン
EndpointAccessToken = response_accesstoken.json()["access_token"]
#print(EndpointAccessToken)

time.sleep(0.2)

url3 = base_url+"organizations?size=10"

header4org = {
    "Authorization": "Bearer " + EndpointAccessToken
    }

response_org = requests.request("GET", url3, headers=header4org)
#print(response_org.json())

orgData = response_org.json() 

#print(orgData["data"][0]["organizationIdentifier"])

#Secure Endpointの管理画面で”Accounts > Organization Settings > SecureX”にある”SecureXのOrganization”がここでいうOrgIDに格納される（自身のログインIDに紐付いてる組織が複数ある場合はここで一旦Printして表示をみて何番目の組織のSecureXni紐付いてるSecure Endpointかを確認してから["0"]の番号を変更）
#print(orgData["data"][0]["organizationIdentifier"])
orgID = orgData["data"][0]["organizationIdentifier"]

url4 = base_url+"organizations/"+orgID+"/device_control/configurations?size=10"
response_devices = requests.request("GET", url4, headers=header4org)

#print(response_devices.text)
configGuidData = response_devices.json() 
#Management > Device Control のNameでアルファベット順で上記[data]と[guid]番号が変わるので、予め追加したいDeviceControl Config画面で何番目のconfigに追加したいか確認してから番号を変更・入力
configGuid = configGuidData["data"][0]["guid"]

url6 = base_url+"organizations/"+orgID+"/device_control/configurations/"+configGuid+"/rules"

header4device = {
    "Authorization": "Bearer " + EndpointAccessToken,
    'content-type': "application/json",
    'accept': "application/json"
    }

result = []
rulecount = 1

#with open("")にcsvファイルのpathを記入
with open('/Users/xxx/rules.csv', encoding='utf-8-sig') as f:
	reader = csv.DictReader(f)
	for r in reader:
		orderNum = int(r['order'])
		result.append({
			"controlType": r["controlType"],
			"notificationType": r["notificationType"],
			"order": orderNum,
			"quantifier": r["quantifier"],
			"displayName": r["displayName"],
			"ruleExpressions": [
			  {
			    "identifier": r["identifier"],
			    "operator": r["operator"],
			    "value": r["value"]
			    }
			]
		})
		json_result = json.dumps(result)
		lst_str = str(json_result)[1:-1]
		response_rules = requests.request("POST", url6, data=lst_str, headers=header4device)
		#print(response_rules)
		if response_rules.status_code == 200 or response_rules.status_code == 201:
			print("row number "+str(rulecount)+" has added successfully")
		else:
			print("row number "+str(rulecount)+" has something wrong with value in CSV file")
		time.sleep(0.1)
		result.clear()
		rulecount += 1
	
