import webbrowser

import requests as requests

url = 'https://github.com/'
dates = [20100101, 20150101, 20200101]

for date in dates:
    response = requests.get(url)
    archiveUrl ='http://archive.org/wayback/available?url=' + url + '&timestamp=' + str(date)
    response = requests.get(archiveUrl)
    responseJson = response.json()
    page = responseJson["archived_snapshots"]["closest"]["url"]
    webbrowser.open(page)
