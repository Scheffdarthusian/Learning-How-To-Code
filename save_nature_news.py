import os
import string

import requests
from bs4 import BeautifulSoup


def scrap_nature_news(url: str):
    '''

    Scrapes the Nature News website for articles of type 'News'.
    :param url:Link of the Nature News
    :return: The title and body of the Nature News
    '''
    article_data = []
    # Send the HTTP request to get the page content
    response = requests.get(url, headers={'Accept-Language': 'en-US,en;q=0.5'})
    # Ensure the request was successful
    response.raise_for_status()
    # Parse the HTML content
    soup = BeautifulSoup(response.content, 'html.parser')
    # find all articles on the page
    all_articles = soup.find_all('article')

    for article in all_articles:
        # Find the article type
        article_link = article.find('a', {'data-track-action': 'view article'})
        if article_link:
            full_article_url = 'https://www.nature.com' + article_link['href']

            # Send a request to the full article page
            full_article_response = requests.get(full_article_url,
                                                 headers={'Accept-Language': 'en-US,en;q=0.5'})
            full_article_response.raise_for_status()

            # Parse the article page
            full_article_soup = BeautifulSoup(full_article_response.content, 'html.parser')

            # Find the element with the class 'article-teaser'
            article_teaser = full_article_soup.find('p', class_='article__teaser')
            if article_teaser:
                article_text = article_teaser.text.strip()

                # Get the title for the filename
                article_title = full_article_soup.find('title').text.strip()
                article_data.append((article_title, article_text))

    return article_data


def clean_filename(name: str) -> str:
    '''
    Cleans the article title to create a valid filename.

    :param name: The original article title
    :return: A cleaned filename string
    '''
    # Replace spaces with underscores and remove punctuation
    translator = str.maketrans('', '', string.punctuation)
    clean_name = name.translate(translator).replace(' ', '_')
    return clean_name


def save_article(title: str, text: str):
    '''
    Saves the article text to a file with a title-based filename.

    :param title: The article title
    :param text: The article text
    :return:
    '''
    filename = clean_filename(title.strip()) + '.txt'
    filepath = os.path.join(os.getcwd(), filename)

    # Save the article body to a text file
    with open(filepath, 'wb') as f:
        f.write(text.encode('utf-8'))


def main():
    url_input: str = input('Input the URL:\n')
    save_article_list = []
    articles = scrap_nature_news(url_input)

    if articles:
        for title, text in articles:
            save_article(title, text)
            save_article_list.append(title)
    else:
        print('No articles found.')

    print(f'Saved articles:\n{save_article_list}')


if __name__ == '__main__':
    main()


