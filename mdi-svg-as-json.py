import requests
import json

URL = 'https://pictogrammers.com/data/mdi-7.4.47.json'

response = requests.get(URL)
response_json = json.loads(response.text)
icon_dict = response_json.get("i")

icons = {}

for icon_obj in icon_dict:
    title = icon_obj.get("n")
    path = icon_obj.get("p")

    icons[title] = path

with open('mdi-svg.json', 'w') as file:
    file.write(json.dumps(icons, indent=2))
