import requests
import json

#TRN-Api-Key from fornitetracker.com
APIKEY = 'c4e9e33b-2661-4fe9-9b32-a766f246bff6'
url = 'https://api.fortnitetracker.com/v1/profile/pc/'
user = 'InfPowerTower'
if __name__ == '__main__':
    r1 = requests.get(url+user, headers={"TRN-Api-Key": APIKEY})
    print(r1)
    print(json.dumps(r1.json(), sort_keys=True, indent=4))