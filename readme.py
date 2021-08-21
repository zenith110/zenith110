import requests
import json
subs = requests.get("https://api.pubsub-api.dev/onsale/")
sub_data = json.loads(subs.text)
readme_intro = "Hello, my name is Abrahan Nevarez. I'm currently working on various projects, but my favorite is my pubsub site.<br/>"
programming_languages = f"<h1>Programming Languages</h1>![Golang](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAAAAXNSR0IArs4c6QAAA1xJREFUWEet1k3IZmMYB/DfNe/rI2qIRGEWw0ZpjI2NiFJir3yUsmCjyIbVlGIxdpOQstIUsbEgUT6aFDtN+YiilKKGzEY0xsytc859nuc+93POec6Us3jfp3Ou+7r////1v677DkufQPo/g7uEzV/af032Ypdz2XAQu2ThOiYDyMzKtWN5Vu+2A+0T16LVaYcAeoU3GDUftui/gHhESGmYZxzAiCBLq99XNPI+/Xaj+KIr+vizhdGYlJWLVu5a6xdCWms5CqDNPL57tXyg09SKtnQzZCYVWFDSlXIbsWVvzdZgrgQTPpjsuAnE24hUCmwLL+0yjB129rzsdZaBCc8FwpbO2BM8lPiA+G3dxkMnzbZhOyODqnUnARfg38J9eBFP4sLgVLbDS3g8O/NsC2B26JXf+8CpMddBO45vMvvz8A/uwDH8gOvwMg7j5w5AZrksf+/OUWnexYdoWDbPnfgEO3gb92AvzhBXhHSi41JJ0AJaTY9JujvBwcSJhgmextVZ8r5Ml4s4K6UbG2DBRcUgfgMHBx7oZtBKjl3JviYId+Nm7Bd+knwUfJw6uX/HDfgUV+J84i7SbbglM38Vu8SZTG0Xp3FVs+fFeCFvcg1OCd9Kbc3ew5f4e+j4aNbcK9JeyevCaanZwKN4BUfxcFHex/BakeMP4WvJ7WNdcC1xICO9idgv0gHJ9bi0Gd+Jf/EjnsdTwvtSHFrdKSIda5LjORyKrvP6M+DXYG/qiG8cRg2Lxjj7RByX0vf4s0deWiUj38lgSiJP4AguyWX5Co80JQj+St1pdEGZc2OezA2jai7cjzexJ5M5SjxIuhWf42SEL/IcaTrgJC4rfT8ziOrW2LyTBA8kGjf3jfRLq17bZu3Lw5JnMsPPaMuinIVbJ+H4uB2M02fxHd5pDTw22GYkbTJNnv+V8zv7VTez2heLL879PBsaLOPpd9nIPjODa5YLT7XpEuR+Kxl1Oeczr79WvwbuHX5bK53frz6Xh8PY/Xo1rstiLQXYGbdQoJB3Y+OSeyfNiB02LDPwywSu4l5a3mIWFrAw0sQ9toyoGrCjv7gNVxpsUM8ptkhSN1sp8nirz5qtUGiujec8VLfhBIpOpo32r91aKT2ZrPtQd/dI+LRj2uDJaTOzbmLNf/dDIx1wr2YnAAAAAElFTkSuQmCC)![Javascript](https://www.iconninja.com/files/824/866/459/node-javascript-js-data-icon.png)"
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
        
