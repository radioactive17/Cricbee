from bs4 import BeautifulSoup
import requests
import time

def test_team():
    source = requests.get('https://www.icc-cricket.com/rankings/mens/team-rankings/test').text
    soup = BeautifulSoup(source, 'lxml')
    test_team_rankings = [[] for _ in range(10)]
    main_div = soup.find('div', class_ = 'rankings-block__container full rankings-table')
    #First Rank team
    first = main_div.find('tr', class_ = 'rankings-block__banner')
    f_rank = first.find('td', class_ = 'rankings-block__banner--pos').text
    f_team = first.find('td', class_ = 'rankings-block__banner--team-name').find('span', class_ = 'u-hide-phablet').text
    f_matches = first.find('td', class_ = 'rankings-block__banner--matches').text
    f_points = first.find('td', class_ = 'rankings-block__banner--points').text
    f_rating = first.find('td', class_ = 'rankings-block__banner--rating u-text-right').text.replace('\n', '')
    f_rating = f_rating.replace(' ', '')
    test_team_rankings[0].extend([f_rank, f_team, f_matches, f_points, f_rating])
    i = 1
    for other in main_div.find_all('tr', class_ = 'table-body'):
        rank = other.find('td', class_ = 'table-body__cell table-body__cell--position u-text-right').text
        team = other.find('td', class_ = 'table-body__cell rankings-table__team').find('span', class_ = 'u-hide-phablet').text
        j = 0
        for x in other.find_all('td', class_ = 'table-body__cell u-center-text'):
            if j == 0:
                matches = x.text
            else:
                points = x.text
            j += 1
        rating = other.find('td', class_ = 'table-body__cell u-text-right rating').text
        test_team_rankings[i].extend([rank, team, matches, points, rating])
        i += 1

    for rank in test_team_rankings:
        print(rank)
    #return test_team_rankings


if __name__ == '__main__':
    while True:
        test_team()
        wait_time = 1
        print(f'\nWaiting {wait_time} minute before fetching Mens Test Team Rankings again...\n')
        time.sleep(wait_time * 60)
