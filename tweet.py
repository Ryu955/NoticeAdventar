# coding: UTF-8
import twitter
import settings
from requests_oauthlib import OAuth1Session

twitter = OAuth1Session(settings.CK, settings.CS, settings.AK, settings.AS)

# t = twitter.Twitter(auth=auth)

#ツイートのみ
status="今日はアドベントカレンダーの担当日です．" #投稿するツイート
#t.statuses.update(status=status) #Twitterに投稿
params = {"status":status}
req = twitter.post("https://api.twitter.com/1.1/statuses/update.json", params = params)
