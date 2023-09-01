# import requests
# import json

# pdata ={"ahaha" : '123'}

# response = requests.request("POST",'https://click.mmolovers.com/administrator/api/post_keyword', data = pdata )
# print(response)
# import requests
# import json

# final = []
# id = 1
# keyword = 'xe máy'
# price = {"Giá thấp": "19.55", "Giá cao": "17.88"}

# pdata = {"id": id, "keyword": keyword, "Price": price}

# final.append(pdata)

# response = requests.request("POST", 'https://click.mmolovers.com/administrator/api/post_keyword', data=json.dumps(final))
# print(pdata)
# print(response)
# import requests
# import json

# final = []
# id = 1
# keyword = 'loto66'
# price = {"123": "19.55", "142": "17.88"}

# pdata = {"id": id, "keys": keyword, "data": price}

# final.append(pdata)

# response = requests.post('https://click.mmolovers.com/administrator/api/post_keyword', json=final)
# print(final)
# print(response.text)


import requests
import json

id = 1
keyword = 'loto66'
price = {"123": "19.55", "142": "17.88"}

data = {"id": id, "keys": keyword, "data": price}

response = requests.post('https://click.mmolovers.com/administrator/api/post_keyword', json=data)
print(data)
print(response.text)



