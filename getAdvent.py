# coding: UTF-8
import urllib2
import json
from bs4 import BeautifulSoup

def getData(url):
    # アクセスするURL
    html = urllib2.urlopen(url)

    # htmlをBeautifulSoupで扱う
    soup = BeautifulSoup(html, "html.parser")
    adventDate= soup.find('div', {'data-react-class': 'CalendarContainer'})['data-react-props']
    jsonDate = json.loads(adventDate)
    entries = jsonDate['entries']

    userdata = {}

    for entry in entries:
        userdata[entry['date']] = entry['user']['name']
    return userdata

