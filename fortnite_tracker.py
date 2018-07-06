import requests
import json
import token

# TRN-Api-Key from fornitetracker.com
token.APIKEY = 'c4e9e33b-2661-4fe9-9b32-a766f246bff6'
url = 'https://api.fortnitetracker.com/v1/profile/pc/'
user = 'Schmusefant'


def return_all_stats(username):
    response = requests.get(url+username, headers={"TRN-Api-Key": APIKEY})
    try:
        return response.json()['error']
    except KeyError:
        return format_lifetime_stats(response)


def format_lifetime_stats(response):
    msg = "\nEpic Username: " + response.json()["epicUserHandle"] + "\n"
    msg += "\nSolo:\n"
    msg += "\t" + response.json()["lifeTimeStats"][3]["key"] + ":\t" + response.json()["lifeTimeStats"][3]["value"] + "\n"
    msg += "\t" + response.json()["lifeTimeStats"][5]["key"] + ":\t" + response.json()["lifeTimeStats"][5]["value"] + "\n"
    msg += "\nDuo:\n"
    msg += "\t" + response.json()["lifeTimeStats"][0]["key"] + ":\t" + response.json()["lifeTimeStats"][0]["value"] + "\n"
    msg += "\t" + response.json()["lifeTimeStats"][4]["key"] + ":\t" + response.json()["lifeTimeStats"][4]["value"] + "\n"
    msg += "\nSquad:\n"
    msg += "\t" + response.json()["lifeTimeStats"][1]["key"] + ":\t" + response.json()["lifeTimeStats"][1]["value"] + "\n"
    msg += "\t" + response.json()["lifeTimeStats"][2]["key"] + ":\t" + response.json()["lifeTimeStats"][2]["value"] + "\n"
    msg += "\nLifetime:\n"
    for x in range(6, 12):
        msg += "\t" + response.json()["lifeTimeStats"][x]["key"] + ":\t" + response.json()["lifeTimeStats"][x]["value"] + "\n"
    return msg
    '''for item in response.json()["lifeTimeStats"]:
        msg += item["key"]+": "
        msg += item["value"]+"\n"
    return msg
    '''
    '''
    solo: top 10, 25
    duo: 5, 12
    squads: 3, 6
    '''


if __name__ == '__main__':
    r1 = requests.get(url+user, headers={"TRN-Api-Key": APIKEY})
    print(r1)
    print(json.dumps(r1.json(), sort_keys=True, indent=4))