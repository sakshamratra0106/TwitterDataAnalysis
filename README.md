# TwitterDataAnalysis
Capture Real Time Tweets on a Topic and Visualize  It

==>Prequisites

Twitter API Keys
https://www.youtube.com/watch?v=KPHC2ygBak4

Python 3.6

There are number of Python libraries you will need for this for starters 7 of them are listed below most of them are default libraries. If you don't have any of them please google for there installation i would prefer PIP for their installation.
1. Tweepy(Streaming API for twitter)
2. fileinput(Accessing Json file line by line)
3. json
4. csv(Creating and Saving Tweets in CSV format)
5. textblob (For Sentiment Analysis)
6. datetime
7. email(For DateTimeZone Conversion)

==> Points To Note
##Keep All Three .Py file in single folder and Run accessing_published_tweets.py.

##Three Files
1. accessing_published_tweets.py(Capturing Real time twitter tweets)
2. twitter_credentials.py(API Keys)
2. tweets_analysis.py(Analysing Tweets.txt to output.csv)


##Polarity is the sentment analsysis of the Text(1 being the most positive and -1 being the most negative tweet)
##Output CSV has the Two extra sheets which has a pivot table to show count of tweets from a particular location/User
