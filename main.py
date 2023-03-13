import webbrowser

import requests

url = 'https://github.com/'
# response = requests.get(url)
dates = [20100101, 20150101, 20200101]




for date in dates:
    # response = requests.get(url.format(date))
    # if response.status_code == 200:

    print(webbrowser.open('http://archive.org/wayback/available?url=' + url + '&timestamp=' + str(date)))


