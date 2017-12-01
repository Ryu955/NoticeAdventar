# coding: UTF-8
import twitter
import settings
from requests_oauthlib import OAuth1Session

twitter = OAuth1Session(settings.CK, settings.CS, settings.AK, settings.AS)

def tweet(id, url):
    status= "@" + id + " 今日はアドベントカレンダーの担当日です．" + url
    params = {"status":status}
    req = twitter.post("https://api.twitter.com/1.1/statuses/update.json", params = params)
