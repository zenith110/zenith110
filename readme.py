import requests
import json
subs = requests.get("https://api.pubsub-api.dev/onsale/")
sub_data = json.loads(subs.text)
readme_intro = "Hello, my name is Abrahan Nevarez. I'm currently a software engineer, but I like trying new things.<br/>I'm currently experimenting with Kubernetes, Terraform, data driven tools such as Grafana Labs Grafana, Prometheus, Loki, and Tempo.<br/>"
programming_languages = f"<h1>Programming Languages</h1> <div styles='display: inline-block'>![Golang](https://github.com/zenith110/zenith110/blob/main/golang_logo_icon_171073.png)![Javascript](https://github.com/zenith110/zenith110/blob/main/javascript-371774.ico) ![Python](https://github.com/zenith110/zenith110/blob/main/python-452091.ico)</div>"
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
        
