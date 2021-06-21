import pandas as pd
import csv
import requests
from bs4 import BeautifulSoup
def csvfunc(x):
    c = 0
    length = len(x)
    with open('store.csv', 'w', newline='') as csvfile:
        fieldnames = ['S.N','Name','Constituency','Party']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for j in range(1,length):
            while x != []:
                c = c+1
                writer.writerow({'S.N':c, 'Name':x[j-1], 'Constituency':x[j], 'Party':x[j+1]})
                x =x[3:]
def main():
    y = []
    url = 'https://en.m.wikipedia.org/wiki/List_of_members_of_the_17th_Lok_Sabha'
    r = requests.get(url)
    if r.status_code == 200:  #checks the status code
        soup = BeautifulSoup(r.text, 'html.parser')
        table_ = soup.find('table', class_ = 'wikitable').next
        row = table_.find_all('tr') #finds the body of the table
        for team in range(0,len(row)):
            head = row[team].find_all('td')
            for i in head:
                # print(i.text)
                y.append((i.text.strip()))
        print(y)
        csvfunc(y)
if __name__ == "__main__":
    main()