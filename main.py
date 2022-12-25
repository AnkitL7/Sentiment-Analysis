import requests
import json
import pprint
url = ('https://newsapi.org/v2/top-headlines?'
       'q=apple&'
       'domains=techcrunch.com&'
       'from=2022-12-1&'
       'pageSize=3&'
       'sortBy=popularity&'
       'apiKey=2e478eac63534dfc9b8b7c2b0cd5e33b')

response = requests.get(url).text
response = json.loads(response)["articles"]
# pprint.pprint(response)

with open("sample.json", "w") as outfile:
    json.dump(response, outfile)