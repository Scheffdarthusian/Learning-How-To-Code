import requests
from bs4 import BeautifulSoup


def talk_to_internet(url):
    if not url.startswith('https://www.nature.com/articles/'):
        return 'Invalid page!'
    try:
        r = requests.get(url_input,  headers={'Accept-Language': 'en-US,en;q=0.5'})
        soup = BeautifulSoup(r.content, 'html.parser')

        title = soup.find('title').text.strip()
        description = soup.find('meta', {'name': 'description'}).get('content').strip()
        if not title or not description:
            return 'Invalid page!'

        return {'Title': title, 'Description': description}
    except Exception as e:
        return 'Invalid page!'


url_input = input('Input the URL:\n')
print(talk_to_internet(url_input))
