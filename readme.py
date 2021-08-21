import requests
import json
subs = requests.get("https://api.pubsub-api.dev/onsale/")
sub_data = json.loads(subs.text)
readme_intro = "Hello, my name is Abrahan Nevarez. I'm currently working on various projects, but my favorite is my pubsub site.<br/>"
pubsub_project_heading = "<h1>[Pubsub api site](https://www.pubsub-api.dev/) - [Github Repo](https://github.com/zenith110/pubsub_api)</h1>"
subs = ""
for sub in sub_data:
    if(sub["on_sale"] == "True"):
        subs = f"Currently the sub(s) on sale are: <br/>![{sub['name']}]({sub['image']})<br/>from {sub['last_on_sale']} for {sub['price']}<br/>"
    else:
        continue
final_string = readme_intro + pubsub_project_heading + subs
readme = open('README.md', 'w')
readme.write(final_string)
        
