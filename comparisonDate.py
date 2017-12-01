import datetime

def comparison(opinionDate):

    calday = opinionDate
    today = datetime.date.today()
    return calday == today

def strToDate(strDate):
    date = datetime.datetime.strptime(strDate, '%Y-%m-%d')
    return date.date()

def run(strDate):
    return comparison(strToDate(strDate))

