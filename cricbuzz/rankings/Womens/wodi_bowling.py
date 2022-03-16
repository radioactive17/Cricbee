from bs4 import BeautifulSoup
import requests
import time

def wodi_bowling():
    source = requests.get('https://www.icc-cricket.com/rankings/womens/player-rankings/odi/bowling').text
    soup = BeautifulSoup(source, 'lxml')
    main_div = soup.find('div', class_ = 'rankings-block__container full')
    wodi_bowling = [[] for _ in range(100)]
    first = main_div.find('tr', class_ = 'rankings-block__banner')
    first_rank = first.find('td', class_ = 'rankings-block__position').find('span', class_ = 'rankings-block__pos-number').text.replace(' ', '').replace('\n', '')
    player = first.find('td', class_ = 'rankings-block__top-player-container').find('div', class_ = 'rankings-block__banner--name-large').text
    team = first.find('div', class_ = 'rankings-block__banner--nationality').text.replace(' ', '').replace('\n', '')

    rating = first.find('div', class_ = 'rankings-block__banner--rating').text
    wodi_bowling[0].extend([first_rank, player, team, rating])
    i = 1
    for other in main_div.find_all('tr', class_ = 'table-body'):
        rank = other.find('span', class_ = 'rankings-table__pos-number').text.replace(' ', '').replace('\n', '')
        name = other.find('td', class_ = 'table-body__cell rankings-table__name name').text.replace('\n', '')
        team = other.find('span', class_ = 'table-body__logo-text').text
        rating = other.find('td', class_ = 'table-body__cell rating').text
        wodi_bowling[i].extend([rank, name, team, rating])
        i += 1

    for bowlers in wodi_bowling:
        print(bowlers)
    #return wodi_bowling

if __name__ == '__main__':
    while True:
        wodi_bowling()
        wait_time = 1
        print(f'\nWaiting {wait_time} minute before fetching Womens ODI Bowling Rankings again...\n')
        time.sleep(wait_time * 60)
