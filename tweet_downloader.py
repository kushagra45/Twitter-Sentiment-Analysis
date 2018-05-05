import sys
import csv
import time

#http://www.tweepy.org/
import tweepy
import json

#Get your Twitter API credentials and enter them here
consumer_key = ""
consumer_secret = ""
access_key = "3333114852-"
access_secret = ""

#method to get a user's last 100 tweets
#def get_tweets(username):

#http://tweepy.readthedocs.org/en/v3.1.0/getting_started.html#api
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)
api = tweepy.API(auth,parser=tweepy.parsers.JSONParser())

data = api.search(q = '"TakeTheKnee" -filter:retweets' , granularity = 'country' , lang = 'en',result_type='mixed',count = 100)
data_all = data.values()[1]

while (len(data_all) <= 20000):
    time.sleep(0.05)
    #print type(data_all)
    #[x.encode(UTF-8) for x in data_all] 
    last = data_all[-1]["id"]
    #print last
    data = api.search(q = '"#TakeTheKnee" -filter:retweets' , granularity = 'country' , lang = 'en',result_type='mixed', max_id =last  ,count = 100)
    data_all += data["statuses"]
    with open("Tweets_taketheknee.txt","wb") as outfile:
        json.dump(data_all,outfile)
    print "length ",len(data_all)
