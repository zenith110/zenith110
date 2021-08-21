import requests
import json
subs = requests.get("https://api.pubsub-api.dev/onsale/")
sub_data = json.loads(subs.text)
readme_intro = "Hello, my name is Abrahan Nevarez. I'm currently working on various projects, but my favorite is my pubsub site.<br/>"
programming_languages = f"![Golang](https://user-images.githubusercontent.com/3613230/41752586-476b0b24-7596-11e8-95fe-8fd3faa21e8a.png)"
f"![Javascript](https://img.icons8.com/color/452/javascript--v1.png)"
pubsub_project_heading = "<h1>[Pubsub api site](https://www.pubsub-api.dev/) - [Github Repo](https://github.com/zenith110/pubsub_api)</h1>"
subs = ""
for sub in sub_data:
    if(sub["on_sale"] == "True"):
        subs = f"Currently the sub(s) on sale are: <br/>![{sub['name']}]({sub['image']})<br/>{sub['name']}<br/>from {sub['last_on_sale']} for {sub['price']}<br/>"
    else:
        continue
final_string = readme_intro + programming_languages + pubsub_project_heading + subs
readme = open('README.md', 'w')
readme.write(final_string)
        
