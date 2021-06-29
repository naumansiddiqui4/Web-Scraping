import csv
import requests
from dateutil.parser import parse
from bs4 import BeautifulSoup
def _date(word):
    word = str(word)
    date = word.split('on')[1].lstrip().split(')')[0]
    date = str(parse(date))
    return date
def csvfunc(x):
    cnst = ''
    name = ''
    party = ''
    c = 0
    length = len(x)
    nm = [] #list for name
    cn = [] #list for constituency
    pt = [] #list for party
    st = [] #list for start
    ed = [] #list for end
    for n in range(0, length, 5):
        cn.append(n)
        nm.append((n + 1))
        pt.append((n + 2))
        st.append((n + 3))
        ed.append((n + 4))

    with open('store.csv', 'w', newline='') as csvfile:
        fieldnames = ['S.N','Constituency','Name','Party','State', 'Term_Start', 'Term_End','Twitter', 'Politwoops']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for j in range(0, length):
                if j in cn:
                    cnst = x[j]
                elif j in nm:
                    name = x[j]
                elif j in pt:
                    party = x[j]
                elif j in st:
                    start = x[j]
                else:
                    end = x[j]
                    c += 1
                    writer.writerow({'S.N':c,'Constituency':cnst,'Name':name, 'Party':party, 'State':'Andhra Pradesh', 'Term_Start':start, 'Term_End':end, 'Twitter':False, 'Politwoops':False})
def scrape():
    str_lst = []
    end_lst = []
    for n in range(3, 1000000, 5):
        str_lst.append(n)
    y = []
    k = []
    val = ''
    url = 'https://en.m.wikipedia.org/wiki/List_of_members_of_the_17th_Lok_Sabha'
    r = requests.get(url)
    if r.status_code == 200:  #checks the status code
        soup = BeautifulSoup(r.text, 'html.parser')
        table_ = soup.find('table', class_ = 'wikitable').next
        row = table_.find_all('tr') #finds the body of the table
        for team in range(0,len(row)):
            head = row[team].find_all('td')
            for i in head:
                if '' != i.text.strip():
                    y.append(i.text.strip())
        for i in range(0,len(y)):
            if '(Elected on' in y[i]:
                val = y[i-3]
                y.insert(i,val)
                break
        while ("" in y):
            y.remove("")
        y.append('')
        y.append('')
        k.append(y[0])
        for i in range(1,len(y)):
            if i%3 == 0:
                k.append('2019-05-01')
                k.append('Still in Parliament')
                k.append(y[i])
            else:
                k.append(y[i])
        pos = ''
        ele = ''
        for i in range(0,len(k)):
            if 'died on' in k[i] and 'Vacant' in k[i+5]:
                k.insert((i+6),'Vacant')
                k.pop(i+7)
                k.pop(i+7)
                k.insert((i + 6), 'Vacant')
                k.insert((i + 6), 'Vacant')

            if 'died on' in k[i]:
                k[i+3] = _date(k[i])
                ele = _date(k[i+5])
                pos = (i+7)
                k.insert(pos,ele)
                k.pop(i+8)
        print(k)
        csvfunc(k)
if __name__ == "__main__":
    scrape()