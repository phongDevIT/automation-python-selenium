import requests

url = "https://click.mmolovers.com/administrator/api/get_keyword"
response = requests.get(url)
data = response.json()


keywords = list(data.values())


for keyword in keywords:
    print(keyword)