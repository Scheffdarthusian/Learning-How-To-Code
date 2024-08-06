import requests
from bs4 import BeautifulSoup


def fetch_nature_article(url):
    #Check if the URL is a valid nature.com article link
    if not url.startswith('https://www.nature.com/articles/'):
        return 'Invalid page'

    try:
        #Send the HTTP request with the required headers
        headers = {'Accept-Language': 'en-US,en;q=0.5'}
        response = requests.get(url, headers=headers)
        response.raise_for_status()

        #Parse the webpage content
        soup = BeautifulSoup(response.text, 'html.parser')

        #Extract the title and description
        title = soup.find('title').text.strip()
        description_tag = soup.find('meta', {'name': 'description'})

        if not title or not description_tag:
            return 'Invalid page'

        description = description_tag.get('content').strip()
        return {'title': title, 'description': description}

    except requests.exceptions.RequestException as e:
        return f'Http Error: {e}'
    except Exception as e:
        return f'Error: {e}'


def main():
    url_input: str = input('Input the URl:\n')
    print(fetch_nature_article(url_input))


if __name__ == '__main__':
    main()



