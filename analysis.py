import tweepy
import csv
from textblob import TextBlob

#tokens initialized
consumer_key = 'IUK4LzRRBjNZSPse0Yrh0ASzs'
consumer_secret = 'R7wgP61StMDNKtSN71hWTj7ROjIa15m8643bfm9Cy8XsUG6BSR'
access_token = '1226323598144458754-gAWJFxK7fzoioaPomxaUS7PemHhDIl'
access_token_secret = 'MtMZOPHtFyTmAu14zwRRrgJNUZx8gDZUuItwXIz8VFMHv'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth,wait_on_rate_limit=True)

query=str(input("Enter query you wish to search for: "))
number=int(input("Enter the number of tweets you want to query. 1-100,000"))

csvFile = open('tweets.csv', 'w')
csvWriter = csv.writer(csvFile)

csvWriter.writerow(['User screen name', 'Tweet text', 'Tweet sentiment', 'Tweet subjectivity'])#initializes row headings

for item in tweepy.Cursor(api.search,q=query).items(number):
    sentiment_overall=TextBlob(item.text)
    #print(item.user.screen_name, item.text, sentiment_overall.sentiment.polarity, sentiment_overall.sentiment.subjectivity)
    print("Hey, I'm collecting the data right now, click on the file icon on the left panel. Open twitter analysis folder. Download the CSV file!")
    csvWriter.writerow([item.user.screen_name, item.text, sentiment_overall.sentiment.polarity, sentiment_overall.sentiment.subjectivity])
