import os
import json
import urllib.request

url = "https://api.harvestapp.com/v2/reports/time/team?from=20220123&to=20220129"

headers = {
    "User-Agent": "Python pulling team time report",
    "Authorization": "Bearer " + os.environ.get("HARVEST_TOKEN"),
    "Harvest-Account-Id": os.environ.get("ACCOUNT_ID")
}

request = urllib.request.Request(url=url, headers=headers)
response = urllib.request.urlopen(request, timeout=5)
responseBody = response.read().decode("utf-8")
jsonResponse = json.loads(responseBody)

print(json.dumps(jsonResponse, sort_keys=True, indent=4))
