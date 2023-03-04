import requests
import json

URL = 'https://pictogrammers.com/_next/static/chunks/981.4f0849cd440234f9.js'

response = requests.get(URL)
response_json = json.loads(response.text.split("'")[1])
icon_dict = response_json.get("i")

icons = {}

for icon_obj in icon_dict:
    title = icon_obj.get("n")
    path = icon_obj.get("p")

    icons[title] = f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><title>{title}</title><path d="{path}" /></svg>'

with open('mdi-svg.json', 'w') as file:
    file.write(json.dumps(icons))
