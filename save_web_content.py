import requests


def fetch_web_content(url: str) -> str:
    response = requests.get(url)
    if response.status_code == 200:
        save_file(response)
        return 'Content saved.'
    else:
        return f'The URL returned {response.status_code}'


def save_file(response):
    try:
        with open('source.html', 'wb') as f:
            f.write(response.content)
    except Exception as e:
        return e


url_input: str = input('Input the URL:\n')
print(fetch_web_content(url_input))
