from datetime import datetime
import datetime as dt
import pandas as pd
import tweepy
import numpy as np
import constants as ct

# ipstr = "covid"


def top_results(ipstr):
    auth = tweepy.OAuth2AppHandler(ct.consumer_key, ct.consumer_secret)
    user = tweepy.API(auth)
    tweets = user.search_tweets(q=ipstr, lang='en')
    df = pd.DataFrame(data=[tweet.text for tweet in tweets])
    df['Date'] = np.array([tweet.created_at for tweet in tweets])
    df.rename(columns={0:'text'},inplace = True)
    return df


# top_results(ipstr)
