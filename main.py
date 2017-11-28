# coding: UTF-8

import getAdvent as ga
import tweet as tw

if __name__ == '__main__':
    dates,userids = ga.getData()

    print dates
    print userids

    tw.tweet("krkrkgr","a")
