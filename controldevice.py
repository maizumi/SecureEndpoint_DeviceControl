
https://visibility.apjc.amp.cisco.com/iroh/oauth2/index.html#/


import requests
import json

base_url = "https://api.apjc.amp.cisco.com/v3/"
url = "https://visibility.apjc.amp.cisco.com/iroh/oauth2/token"

payload = "grant_type=client_credentials"
headers = {
    'content-type': "application/x-www-form-urlencoded",
    'accept': "application/json",
    'authorization': "Basic Y2xpZW50LWYwYmNiNWRiLWE5OWUtNGJkYy04YTQ3LWQwOGE1ZDhlOGFiYTpKdjZjakZZTlFuaTJPRzlzcjdJRkhxeFoyX2lINmNlUENOTkVCV3gycG1zVjZBbTZaeHpUWFE=",
    'cache-control': "no-cache",
    'postman-token': "4e200843-4f90-2f44-962e-5a3b6fe455f8"
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


url5 = base_url+"organizations/"+orgID+"/device_control/configurations"


payload2 = {
  "configuration": {
    "name": "New Configuration",
    "baseRule": {
      "controlType": "block",
      "notificationType": "never"
    },
    "exceptionRules": [
      {
        "order": 1,
        "controlType": "read_only",
        "notificationType": "inherit_from_base_rule",
        "quantifier": "any",
        "ruleExpressions": [
          {
            "identifier": "product_name",
            "operator": "not_equals",
            "value": "SDX"
          },
          {
            "identifier": "instance_id",
            "operator": "equals",
            "value": "USB\\VID_1C4F&PID_0002\\5&2eab04ab&0&1"
          }
        ]
      }
    ]
  }
}
    
json_object = json.dumps(payload2)
    
header4device = {
    "Authorization": "Bearer " + EndpointAccessToken,
    'content-type': "application/json",
    'accept': "application/json"
    }

response_devices = requests.request("POST", url5, data=json_object, headers=header4device)

print(response_devices.text)

url6 = base_url+"organizations/"+orgID+"/device_control/configurations/"+configGuid+"/rules"

payload3 = {
  "controlType": "block",
  "notificationType": "always",
  "order": 1,
  "quantifier": "all",
  "displayName": "string",
  "ruleExpressions": [
    {
      "identifier": "instance_id",
      "operator": "equals",
      "value": "string"
    }
  ]
}

json_object3 = json.dumps(payload3)
json3 = json.loads(json_object3)


response_rules = requests.request("POST", url6, data=json3, headers=header4device)
