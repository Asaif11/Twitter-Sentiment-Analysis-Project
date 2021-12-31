
import tweepy
import re
import numpy as np
#import pandas as pd
#import requests




from textblob import TextBlob
import matplotlib.pyplot as plt

def percentage(part: object, whole: object) -> object:
    return 100*float(part)/float(whole)
consumerKey = "M3BxbtE1rjKVs4Vx1e2Er9FHI"
consumerSecret = "0Jl6uvPvIj6NqJzCi7HHQ2Ik0DOcTmmPWa0TAwevVDQr2FPbVW"
accessToken = "1217873425051447296-rLv1enomdkh0wPRhM2N8WwX8ddBfuA"
accessTokenSecret = "5LB6WmmnBCIo1q3rI6u5Og9IFX8qWEIxRkfQWSF08C0Kf"
auth = tweepy.OAuthHandler(consumer_key=consumerKey, consumer_secret=consumerSecret)
auth.set_access_token(accessToken, accessTokenSecret)
api = tweepy.API(auth,wait_on_rate_limit=True)
searchTerm=input("enter keyword/hashtag to search about:")
date="2019-01-01"
noOfSearchTerms=int(input("enter how many tweets to analyze:"))
tweets=tweepy.Cursor(api.search,q=searchTerm,lang="en").items(noOfSearchTerms)
    #users_locs = [tweet.user.screen_name, tweet.user.location]
positive =0
negative =0
neutral =0
polarity =0

def clean_tweets(text):
    text=re.sub("RT @[\w]*:","",text)
    text=re.sub("@[\w]*","",text)
    text=re.sub("https?://[A-Za-z0-9./]*","",text)
    text=re.sub("\n","",text)
    text=re.sub("#","",text)
    return text


for tweet in tweets:
     users_name = [tweet.user.screen_name]
     users_loc = [[tweet.user.screen_name, tweet.user.location]]
     tweet.text = clean_tweets(tweet.text)
     print(tweet.text)

     print(users_loc)


     analysis =TextBlob(tweet.text)
     polarity += analysis.sentiment.polarity

     if(analysis.sentiment.polarity == 0):
         neutral += 1
     elif(analysis.sentiment.polarity <0.00):
        negative +=1
     elif(analysis.sentiment.polarity >0.00):
        positive +=1



positive=percentage(positive,noOfSearchTerms)
neutral=percentage(neutral,noOfSearchTerms)
negative=percentage(negative,noOfSearchTerms)

positive=format(positive,'.2f')
neutral=format(neutral,'.2f')
negative=format(negative,'.2f')


print("how many people are reacting on" +searchTerm+ "by analyzing" + str(noOfSearchTerms)+ "Tweets.")

if(polarity == 0):
    print("neutral")
elif(polarity<0):
    print("negative")
elif(polarity>0):
     print("positive")

labels = ['positive['+str(positive)+'%]','negative['+str(negative)+'%]','neutral['+str(neutral)+'%]']
sizes =[positive,negative,neutral]
colors=['yellowgreen','gold','red']
patches,texts = plt.pie(sizes,colors=colors,startangle=90)
plt.legend(patches,labels,loc="best")
plt.title('how people are reacting on ' + searchTerm+' by analyzing '+str(noOfSearchTerms)+'Tweets.')
plt.axis('equal')
plt.tight_layout()
plt.show()












