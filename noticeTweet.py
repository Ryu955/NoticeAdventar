# coding: UTF-8
import twitter
import settings

def tweet(id, url):
    auth = twitter.OAuth(consumer_key=settings.CK,
    consumer_secret=settings.CS,
    token=settings.AK,
    token_secret=settings.AS)

    status= "@" + id + u" 今日はアドベントカレンダーの担当日です．" + url

    t = twitter.Twitter(auth=auth)

    t.statuses.update(status=status) #Twitterに投稿
