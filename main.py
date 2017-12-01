# coding: UTF-8

import getAdvent as ga
import tweet as tw
import comparisonDate as cd

if __name__ == '__main__':
    adventURL = "https://adventar.org/calendars/2359"
    userdata = ga.getData(adventURL)

    for date in userdata:
        if(cd.run(date)):
            print date
            print userdata[date]
            tw.tweet("krkrkgr",adventURL)



