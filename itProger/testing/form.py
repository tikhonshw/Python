import requests

class Form:
    def __init__(self, login, pwd, email = '', url = ''):
        self.login = login
        self.pwd = pwd
        self.email = email
        self.url = url

    def url(self, url):
        headers = {
            'accept': '*/*',
            'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36'
        }
        session = requests.Session()
        try:
            req = session.get(url, headers=headers)
            if req.status_code == 200:
                self.url = url
                return True
            else:
                return False
        except Exception:
            return False


# print(url('https://google.com')) ## для проверки как показано к коментарию на выполнения домашнего задания!

