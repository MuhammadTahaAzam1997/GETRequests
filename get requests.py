import requests
import json

url =  "https://malshare.com/api.php?api_key=96c9ac0cb0d33971669c624e118199b432dc9dbc9604aeb8436136c3d5a53702&action=getlist"

payload={}
headers = {
  'Authorization': 'Basic 96c9ac0cb0d33971669c624e118199b432dc9dbc9604aeb8436136c3d5a53702'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)