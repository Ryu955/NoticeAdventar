# coding: UTF-8
import urllib2
import json
from bs4 import BeautifulSoup

def getData():
    # アクセスするURL
    url = "https://adventar.org/calendars/2359"
    html = urllib2.urlopen(url)

    # htmlをBeautifulSoupで扱う
    soup = BeautifulSoup(html, "html.parser")
    adventDate= soup.find('div', {'data-react-class': 'CalendarContainer'})['data-react-props']
    jsonDate = json.loads(adventDate)
    entries = jsonDate['entries']

    dates = []
    userids = []

    for entry in entries:
        dates.append(entry['date'])
        userids.append(entry['user']['name'])

    return dates,userids

if __name__ == '__main__':
    dates,userids = getData()

    print dates
    print userids
