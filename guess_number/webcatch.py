import requests
from bs4 import BeautifulSoup
from datetime import datetime

all_dates = []
#Get the content by using Packages from the link:
r = requests.get('http://old-releases.ubuntu.com/releases/')

soup = BeautifulSoup(r.text,'html.parser')

tables = soup.findAll('table')

for table in tables:
    rows = table.findAll('tr')

    for tds in rows:
        td = tds.findAll('td') 
        #previously I put td = rows.findAll('td')
        if len(td) >= 3:
            # current_time = datetime.strptime(td[2].text, "%Y-%m-%d %H:%M  ")
            # current_time = parser.parse(td[2].text)
            # print(current_time)
            try:
                current_date = datetime.strptime(td[2].text, '%Y-%m-%d %H:%M  ')
                all_dates.append(current_date)
            except Exception:
                # In case we are unable to parse the text into a date.
                # to prevent the app to crash.
                pass

    print('the latest date is {}'.format(max(all_dates)))