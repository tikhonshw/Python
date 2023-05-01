import requests
from bs4 import BeautifulSoup as bs4

headers = {
    'accept': '*/*',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36'
}

url = "https://itproger.com/"
session = requests.Session()

try:
    req = session.get(url, headers=headers)
    if req.status_code == 200:
        soup = bs4(req.content, 'html.parser')
        divs = soup.find_all('div', attrs={'class': 'article'})
        for div in divs:
            title = div.find('a').text
            href = div.find('a')['href']
            print("{} - https://itproger.com/{}".format(title, href))
    else:
        print("Ошибка")
except Exception:
    print("Ошибка в самом URL адресе")