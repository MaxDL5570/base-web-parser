from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd


def main():
    driver = webdriver.Chrome()
    pages_count = 1
    df = []
    for x in range(pages_count):
        driver.get('https://www.kinopoisk.ru/lists/top250/' + '?page=' + str(x + 1) + '&tab=all')
        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')
        items = soup.find_all('div', class_='desktop-rating-selection-film-item')
        for item in items:
            rating_position = item.find('span', class_='film-item-rating-position__position').text
            film_name = item.find('p', class_='selection-film-item-meta__name').text
            rating_value = item.find('span', class_='rating__value rating__value_positive').text
            df.append({
                'Rating position': rating_position,
                'Film name': film_name,
                'Rating value': rating_value
            })
    df = pd.DataFrame(df)
    df.to_csv('data.csv', index=False)


if __name__ == '__main__':
    main()
