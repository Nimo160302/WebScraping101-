from bs4 import BeautifulSoup
import requests
import lxml
url = 'https://www.nirfindia.org/Rankings/2024/EngineeringRanking.html'
href= requests.get(url).text
soup = BeautifulSoup(href, 'lxml')
# print(soup.prettify())
table = soup.find('tbody')
# print(jobs)
rows = table.find_all('tr')

for row in rows:
    columns = row.find_all('td')
# When using find_all(), we can directly access the 'href' attribute using ['href']
    if len(columns)>6:
        rank = int(columns[-1].text)
        name =  columns[1].text.split('More')[0]
        score = columns[-2].text
        stats_link = row.find_all('a', target= '_blank')[0]['href']
        print(f'Rank : {rank}, College: {name}, score = {score} , stats_link ={stats_link}')

