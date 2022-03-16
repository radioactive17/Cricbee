from bs4 import BeautifulSoup
import requests
import time

def wt20_batting():
    source = requests.get('https://www.icc-cricket.com/rankings/womens/player-rankings/t20i/batting').text
    soup = BeautifulSoup(source, 'lxml')
    main_div = soup.find('div', class_ = 'rankings-block__container full')
    wt20_batting = [[] for _ in range(100)]
    first = main_div.find('tr', class_ = 'rankings-block__banner')
    first_rank = first.find('td', class_ = 'rankings-block__position').find('span', class_ = 'rankings-block__pos-number').text.replace(' ', '').replace('\n', '')
    player = first.find('td', class_ = 'rankings-block__top-player-container').find('div', class_ = 'rankings-block__banner--name-large').text
    team = first.find('div', class_ = 'rankings-block__banner--nationality').text.replace(' ', '').replace('\n', '')

    rating = first.find('div', class_ = 'rankings-block__banner--rating').text
    wt20_batting[0].extend([first_rank, player, team, rating])
    i = 1
    for other in main_div.find_all('tr', class_ = 'table-body'):
        rank = other.find('span', class_ = 'rankings-table__pos-number').text.replace(' ', '').replace('\n', '')
        name = other.find('td', class_ = 'table-body__cell rankings-table__name name').text.replace('\n', '')
        team = other.find('span', class_ = 'table-body__logo-text').text
        rating = other.find('td', class_ = 'table-body__cell rating').text
        wt20_batting[i].extend([rank, name, team, rating])
        i += 1

    for batters in wt20_batting:
        print(batters)
    #return wt20_batting

if __name__ == '__main__':
    while True:
        wt20_batting()
        wait_time = 1
        print(f'\nWaiting {wait_time} minute before fetching Womens T20 Batting Rankings again...\n')
        time.sleep(wait_time * 60)
