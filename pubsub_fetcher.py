import requests
import json
subs = requests.get("https://api.pubsub-api.dev/onsale/")
sub_data = json.loads(subs.text)
for sub in sub_data:
    if(sub["on_sale"] == "True"):
        with open('pubsubs.json', 'w') as outfile:
            json.dump(sub, outfile)
    else:
        continue