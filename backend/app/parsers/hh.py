import requests
from bs4 import BeautifulSoup

headers = {
    'Host': 'hh.ru',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36',
    'Accept': '*/*',
    'Accept-Encoding': 'qzip, deflate, br',
    'Connection': 'keep-alive'
}


def parse_hh_vacancy(url: str) -> tuple:
    hh_request = requests.get(url, headers=headers)
    hh_soup = BeautifulSoup(hh_request.text, 'html.parser')
    try:
        title = hh_soup.title.get_text()
    except AttributeError:
        title = ''

    try:
        description = hh_soup.find('div', {'data-qa': "vacancy-description"}).get_text()
    except AttributeError:
        description = ''

    try:
        keywords = (hh_soup
                    .find('div', {'class': "bloko-tag-list"})
                    .get_text(separator='</span>')
                    .replace("</span>", ", "))
    except AttributeError:
        keywords = ''

    return title, description, keywords


def is_hh_link(text: str) -> bool:
    return 'hh.ru/vacancy' in text
