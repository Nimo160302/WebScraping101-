from bs4 import BeautifulSoup
import requests
import lxml
import pdfplumber
import io
url = 'https://www.nirfindia.org/Rankings/2024/EngineeringRanking.html'
href= requests.get(url).text
soup = BeautifulSoup(href, 'lxml')
# print(soup.prettify())
table = soup.find('tbody')
# print(jobs)
rows = table.find_all('tr')

for row in rows:
    columns = row.find_all('td')
    if len(columns) > 6:
        college_data  =[]
        rank = int(columns[-1].text)
        name = columns[1].text.split('More')[0]
        score = columns[-2].text
        stats_link = row.find_all('a', target='_blank')[0]['href']
        college_data.append([rank, name, score, stats_link])
        print(college_data)
        print('\n')
        # ... (your existing code to extract rank, name, score, stats_link)

        # Download the PDF content
        response = requests.get(stats_link)
        pdf_content = io.BytesIO(response.content)

        with pdfplumber.open(pdf_content) as pdf:
            page1_tables = []
            page2_tables = []
            page3_tables = []

            # Uncomment and fix indentation for this part
            for page_num, page in enumerate(pdf.pages, start=1):
                tables = page.extract_tables()
                if page_num == 1:
                    page1_tables.extend(tables)
                elif page_num == 2:
                    page2_tables.extend(tables)
                elif page_num == 3:
                    page3_tables.extend(tables)

            # Move this inside the 'with' block
            print(f'PAGE 1 TABLES')
            for i in range(0, len(page1_tables)):
                print(f'{page1_tables[i]}\n')
            print(f'PAGE 2 TABLES')
            for i in range(0, len(page2_tables)):
                print(f'{page2_tables[i]}\n')
            print(f'PAGE 3 TABLES')
            for i in range(0, len(page3_tables)):
                print(f'{page3_tables[i]}\n')


        print(f"Number of tables on Page 1: {len(page1_tables)}")
        print(f"Number of tables on Page 2: {len(page2_tables)}")
        print(f"Number of tables on Page 3: {len(page3_tables)}")

