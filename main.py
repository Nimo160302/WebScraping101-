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
# print(text)

for row in rows:

    columns = row.find_all('td')
    # rank = columns[-1]
    # name =  columns[0]
    # score = columns[-2]
    print(columns)
    print('\n')

    # if len(columns) >= 6:  # Ensuring the row has enough columns
    #     institute_id = columns[0].text.strip()
    #     institute_name = columns[1].text.strip()
    #     city = columns[2].text.strip()
    #     state = columns[3].text.strip()
    #     score = columns[4].text.strip()
    #     rank = columns[5].text.strip()
    #
    # print(f"{rank}, {name}  - Score: {score}")
# table = jobs.find('tr', role =  'row')
# print(table)