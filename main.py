import pandas as pd
import requests
from bs4 import BeautifulSoup
# dfs = pd.read_html('https://en.m.wikipedia.org/wiki/List_of_members_of_the_17th_Lok_Sabha')
# for df in dfs:
#     print(df)
url = 'https://en.m.wikipedia.org/wiki/List_of_members_of_the_17th_Lok_Sabha'
r = requests.get(url)
if r.status_code == 200:  #checks the status code
    soup = BeautifulSoup(r.text, 'html.parser')
    table_ = soup.find('table', class_ = 'wikitable sortable')
    # headers = []
    # for i in table_.find_all('tbody'):
    #     title = i.text.strip()
    #     headers.append(title)
    print()
    body = table_.find_all('tbody') #finds the body of the table
    for team in body:
        for i in range(0,3):
            rows = team.find_all('tr')
            # head = team.find_all('th')
            print(rows)