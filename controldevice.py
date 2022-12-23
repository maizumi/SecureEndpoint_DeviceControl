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

print(response_devices)
    
