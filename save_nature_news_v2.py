from typing import Tuple, List, Any

import requests
from bs4 import BeautifulSoup
import string

from requests import Response


def get_website(url: str) -> Response:
    # Send the HTTP request to get the page content
    return requests.get(url, headers={'Accept-Language': 'en-US,en;q=0.5'})


def get_news_article_link(url: str) -> tuple[int, list[str | Any]]:
    # storage for the links scrapped
    news_article_link = []
    response = get_website(url)

    if response.status_code != 200:
        return response.status_code, news_article_link

    soup = BeautifulSoup(response.content, 'html.parser')
    # find all articles on the page
    all_articles = soup.find_all('article')

    # iterate through all articles
    for article in all_articles:
        article_span = article.find('span', {'data-test': 'article.type'})
        # This can be any type of article
        article_type = article_span.find('span').text
        if article_type == 'News':
            main_link = 'https://www.nature.com'
            # grab all "a" tags with the "view article" string and grab the "href" of this selection
            article_link = article.find('a', {'data-track-action': 'view article'}).get('href')
            complete_link = main_link + article_link
            news_article_link.append(complete_link)

    return response.status_code, news_article_link


def get_article_title(article_link: str) -> str:
    soup = BeautifulSoup(get_website(article_link).content, 'html.parser')

    raw_title = soup.find('h1', {'class': 'c-article-magazine-title'}).text
    translator = raw_title.maketrans('', '', string.punctuation + '’')
    # Translating the mapped object back into a string
    cleaned_title = raw_title.translate(translator).strip().replace(' ', '_')
    return cleaned_title


def get_article_content(article_link: str) -> str:
    soup = BeautifulSoup(get_website(article_link).content, 'html.parser')
    article_content = soup.find('p', class_='article__teaser').get_text().strip()

    return article_content


def save_article(article_link: str) -> str:
    article_title = get_article_title(article_link)
    article_content = get_article_content(article_link)

    file_name = article_title + '.txt'
    with open(file_name, 'wb') as f:
        f.write(article_content.encode('utf-8'))

    return article_title


def main():
    url = 'https://www.nature.com/nature/articles?sort=PubDate&year=2020&page=3'
    website_code, news_article_link = get_news_article_link(url)

    if website_code == 200:
        saved_article = []

        for link in news_article_link:
            saved_title = save_article(link)
            saved_article.append(saved_title)
            print("Article downloaded:", saved_title)

        print("\nDownloaded article: ")
        for i in range(len(saved_article)):
            print(str(i + 1) + ". " + saved_article[i])
    else:
        print("Invalid URL. Status code:", website_code)


if __name__ == '__main__':
    main()
    
