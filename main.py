import random
import requests
from bs4 import BeautifulSoup

url = 'https://www.imdb.com/chart/toptv'

def main():
    response = requests.get(url)
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    series_tags = soup.select('td.titleColumn')
    inner_series_tags = soup.select('td.titleColumn a')
    rating_tags = soup.select('td.posterColumn span[name=ir]')

    def get_year(series_tag):
        series_split = series_tag.text.split()
        year = series_split[-1]
        return year

    years = [get_year(tag) for tag in series_tags]  
    actors_list  = [tag['title'] for tag in inner_series_tags]
    titles = [tag.text for tag in inner_series_tags]
    ratings = [float(tag['data-value']) for tag in rating_tags]

    n_series = len(titles)
    while True:
        index = random.randrange(0, n_series)
        print(f"{titles[index]} {years[index]}, rating: {ratings[index]:.1f}, starring: {actors_list[index]}")
        user_input = input("Do you want another suggestion? (y/n) ")
        if user_input != 'y':
            break

if __name__ == '__main__':
    main()
    