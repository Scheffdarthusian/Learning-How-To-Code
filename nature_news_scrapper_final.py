import os
from typing import Tuple, List
import requests
from bs4 import BeautifulSoup
import string
from requests import Response

BASE_URL = 'https://www.nature.com/nature/articles?sort=PubDate&year=2020&page='
ARTICLE_SELECTOR = 'article'
ARTICLE_TYPE_SELECTOR = {'data-test': 'article.type'}
VIEW_ARTICLE_SELECTOR = {'data-track-action': 'view article'}
TITLE_SELECTOR = {'class': 'c-article-magazine-title'}
CONTENT_SELECTOR = {'class': 'article__teaser'}


def get_website(url: str) -> Response:
    """
    Sends an HTTP request to retrieve the page content.

    Args:
        url (str): The URL of the website to scrape.

    Returns:
        Response: The response object containing the page content.
    """
    return requests.get(url, headers={'Accept-Language': 'en-US,en;q=0.5'})


def extract_article_links(soup: BeautifulSoup, article_type_filter: str) -> List[str]:
    """
    Extracts article links of a specific type from the parsed HTML.

    Args:
        soup (BeautifulSoup): The parsed HTML content.
        article_type_filter (str): The type of articles to filter.

    Returns:
        List[str]: A list of filtered article URLs.
    """
    filtered_article_links = []

    all_articles = soup.find_all(ARTICLE_SELECTOR)
    for article in all_articles:
        article_span = article.find('span', ARTICLE_TYPE_SELECTOR)
        if article_span and article_span.find('span').text == article_type_filter:
            article_link = article.find('a', VIEW_ARTICLE_SELECTOR).get('href')
            complete_link = 'https://www.nature.com' + article_link
            filtered_article_links.append(complete_link)

    return filtered_article_links


def get_news_article_links(url: str, article_type_filter: str) -> Tuple[int, List[str]]:
    """
    Fetches and parses the website, then extracts article links of a specific type.

    Args:
        url (str): The URL of the page to scrape.
        article_type_filter (str): The type of articles to filter.

    Returns:
        Tuple[int, List[str]]: HTTP status code and a list of filtered article URLs.
    """
    response = get_website(url)
    if response.status_code != 200:
        return response.status_code, []

    soup = BeautifulSoup(response.content, 'html.parser')
    filtered_article_links = extract_article_links(soup, article_type_filter)
    return response.status_code, filtered_article_links


def clean_article_title(raw_title: str) -> str:
    """
    Cleans and formats the article title for use as a filename.

    Args:
        raw_title (str): The raw title string.

    Returns:
        str: The cleaned title formatted as a filename.
    """
    translator = str.maketrans('', '', string.punctuation + '’')
    cleaned_title = raw_title.translate(translator).strip().replace(' ', '_')
    return cleaned_title


def get_article_title(article_link: str) -> str:
    """
    Retrieves and cleans the title of an article.

    Args:
        article_link (str): The URL of the article.

    Returns:
        str: The cleaned title of the article.
    """
    soup = BeautifulSoup(get_website(article_link).content, 'html.parser')
    raw_title = soup.find('h1', TITLE_SELECTOR).text
    return clean_article_title(raw_title)


def get_article_content(article_link: str) -> str:
    """
    Retrieves the content of an article.

    Args:
        article_link (str): The URL of the article.

    Returns:
        str: The text content of the article.
    """
    soup = BeautifulSoup(get_website(article_link).content, 'html.parser')
    article_content_element = soup.find('p', CONTENT_SELECTOR)
    return article_content_element.get_text().strip() if article_content_element else "Content not found."


def save_article(article_link: str, page_number: int) -> str:
    """
    Saves the article content to a file in the specified page directory.

    Args:
        article_link (str): The URL of the article.
        page_number (int): The page number for directory creation.

    Returns:
        str: The filename of the saved article.
    """
    article_title = get_article_title(article_link)
    article_content = get_article_content(article_link)

    # Create directory for the page if it doesn't exist
    directory_name = f"Page_{page_number}"
    os.makedirs(directory_name, exist_ok=True)

    # Save article in the corresponding directory
    file_name = f"{directory_name}/{article_title}.txt"
    with open(file_name, 'wb') as f:
        f.write(article_content.encode('utf-8'))

    return article_title


def main():
    """
    Main function to execute the script.
    Downloads and saves all filtered articles page by page based on user input.
    """
    num_pages = int(input("Enter the number of pages to scrape: "))
    article_type = input("Enter the type of articles to filter (e.g., 'News', 'Nature Briefing'): ")

    for page_number in range(1, num_pages + 1):
        url = f"{BASE_URL}{page_number}"
        website_code, filtered_article_links = get_news_article_links(url, article_type)

        if website_code == 200:
            for link in filtered_article_links:
                save_article(link, page_number)

            if filtered_article_links:
                print(f"Page {page_number}: Articles saved.")
            else:
                print(f"Page {page_number}: No articles found.")
        else:
            print(f"Failed to retrieve articles from Page {page_number}. Status code: {website_code}")


if __name__ == '__main__':
    main()
