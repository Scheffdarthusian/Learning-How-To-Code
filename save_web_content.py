import requests


def save_web_content(url):
    response = requests.get(url)
    if response.status_code == 200:
        with open('source.html', 'wb') as f:
            f.write(response.content)
            f.close()
            print('Content saved')
    else:
        print(f'The URL returned {response.status_code}')


url_input: str = input('Input the URL:\n')
save_web_content(url_input)
