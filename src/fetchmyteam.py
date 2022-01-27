import os
import json
import urllib.request
import pprint

pp = pprint.PrettyPrinter(indent=4)

headers = {
    "User-Agent": "Python pulling team time report",
    "Authorization": "Bearer " + os.environ.get("HARVEST_TOKEN"),
    "Harvest-Account-Id": os.environ.get("ACCOUNT_ID")
}

def fetchTeam(role_id, headers):
    url = "https://api.harvestapp.com/v2/roles/" + role_id
    request = urllib.request.Request(url=url, headers=headers)
    response = urllib.request.urlopen(request, timeout=5)
    responseBody = response.read().decode("utf-8")
    jsonResponse = json.loads(responseBody)
    resp = jsonResponse['user_ids']
    pp.pprint(resp)
    return(resp)
    

url = "https://api.harvestapp.com/v2/reports/time/team?from=20220123&to=20220129"

role_id = os.environ.get("HARVEST_ROLE")
user_ids = fetchTeam(role_id, headers)
request = urllib.request.Request(url=url, headers=headers)
response = urllib.request.urlopen(request, timeout=5)
responseBody = response.read().decode("utf-8")
jsonResponse = json.loads(responseBody)

data = jsonResponse["results"]
for user in user_ids:
    pp.pprint(list(filter(lambda x:x["user_id"]==user, data)))

