import requests
import json
subs = requests.get("https://api.pubsub-api.dev/onsale/")
sub_data = json.loads(subs.text)
readme_intro = "Hello, my name is Abrahan Nevarez. I'm currently working on various projects, but my favorite is my pubsub site."
subs = ""
for sub in sub_data:
    if(sub["on_sale"] == "True"):
        subs = f"\nCurrently the sub(s) on sale are: ![{sub['name']} picture]({sub['image']}){sub['name']}<br/>from {sub['last_on_sale']}<br/>"
    else:
        continue
final_string = readme_intro + subs
readme = open('README.md', 'w')
readme.write(final_string)
