import requests
import csv
import json
from requests.auth import HTTPBasicAuth
from getpass import getpass
import os
from flask import Flask, render_template, request, redirect, url_for, send_from_directory, session
from werkzeug.utils import secure_filename


base_url = "https://api.apjc.amp.cisco.com/v3/"
url = "https://visibility.apjc.amp.cisco.com/iroh/oauth2/token"

payload = "grant_type=client_credentials"
headers = {
    'content-type': "application/x-www-form-urlencoded",
    'accept': "application/json",
    'authorization': "Basic Y2xpZW50LWYwYmNiNWRiLWE5OWUtNGJkYy04YTQ3LWQwOGE1ZDhlOGFiYTpKdjZjakZZTlFuaTJPRzlzcjdJRkhxeFoyX2lINmNlUENOTkVCV3gycG1zVjZBbTZaeHpUWFE=",
    'cache-control': "no-cache",
    }

response = requests.request("POST", url, data=payload, headers=headers)


print(response.text)

accesstoken = response.json()["access_token"]

print(accesstoken)

url2 = base_url+"access_tokens"

header4endpoint = {
    "Authorization": "Bearer " + accesstoken
    }

response_accesstoken = requests.request("POST", url2, headers=header4endpoint)
print(response_accesstoken.json())

EndpointAccessToken = response_accesstoken.json()["access_token"]
print(EndpointAccessToken)

url3 = base_url+"organizations?size=10"

header4org = {
    "Authorization": "Bearer " + EndpointAccessToken
    }

response_org = requests.request("GET", url3, headers=header4org)
print(response_org.json())

orgData = response_org.json() 

print(orgData["data"][0]["organizationIdentifier"])
orgID = orgData["data"][0]["organizationIdentifier"]

url4 = base_url+"organizations/"+orgID+"/device_control/configurations?size=10"
response_devices = requests.request("GET", url4, headers=header4org)

print(response_devices.text)
configGuidData = response_devices.json() 
configGuid = configGuidData["data"][0]["guid"]
#Management > Device Control のNameでアルファベット順で上記[data]と[guid]番号が変わるので、予め追加したいDeviceControl Config画面で何番目のconfigに追加したいか確認してから番号を変更・入力

url6 = base_url+"organizations/"+orgID+"/device_control/configurations/"+configGuid+"/rules"


header4device = {
    "Authorization": "Bearer " + EndpointAccessToken,
    'content-type': "application/json",
    'accept': "application/json"
    }


result = []
with open('/Users/maizumi/Documents/15.Technology/Programming/SecureEndpoint/rules.csv', encoding='utf-8-sig') as f:
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
		#print(result)
		json_result = json.dumps(result)
		lst_str = str(json_result)[1:-1]
		response_rules = requests.request("POST", url6, data=lst_str, headers=header4device)
		result.clear()
	




