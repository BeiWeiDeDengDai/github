import requests



url = "https://github.com/favicon.ico"

resp = requests.get(url)
with open("github.ico", mode="wb") as f:
    f.write(resp.content)