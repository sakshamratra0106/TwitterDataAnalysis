import fileinput
import json
import csv
from textblob import TextBlob ## For Sentiment Analysis
import datetime
from email.utils import mktime_tz, parsedate_tz

##Parsing Date From Twitter DateTime Stamp Wed Nov 14 04:12:21 +0000 2018 to 
##System DateTime Stamp 11/14/2018  12:01:35 AM
def parse_datetime(value):
     time_tuple = parsedate_tz(value)
     timestamp = mktime_tz(time_tuple)
     return datetime.datetime.fromtimestamp(timestamp)
 
##To Read the tweets.txt Log File from where it left if the Counter File exits
line_number=0
try:
    with fileinput.FileInput("counter.csv") as counter_line:
            line=list(counter_line)
            temp=line[0].split(",")
            c=int(temp[0])
            line_number=c
			

##To create CounterFile if it does not exits
except IOError:
    file = open("counter.csv", 'w')
    file.close()
	

##Reading tweets.txt, Processing/Parsing and Saving Record by Record in output.csv
f=fileinput.FileInput("tweets.txt")
for line in f:
    try:
        if line_number < f.filelineno():
            
            tweet_dict = json.loads(line)
            record = []
            date=tweet_dict['created_at']
            record.append(parse_datetime(date))
            record.append(tweet_dict['id'])
            record.append(tweet_dict['truncated'])
            record.append(tweet_dict['user']['id'])
            record.append(tweet_dict['user']['name'])
            record.append(tweet_dict['user']['screen_name'])
            loc=str(tweet_dict['user']['location'])
            record.append(loc.replace("\n"," ").replace("\n"," "))
            desc=str(tweet_dict['user']['description'])
            record.append(desc.replace("\n"," ").replace("\n"," "))
            record.append(tweet_dict['user']['friends_count'])
            record.append(tweet_dict['user']['followers_count'])
            record.append(tweet_dict['user']['listed_count'])
            record.append(tweet_dict['user']['favourites_count'])
            record.append(tweet_dict['user']['statuses_count'])
            date=tweet_dict['user']['created_at']
            record.append(parse_datetime(date))
            record.append(tweet_dict['user']['lang'])
            record.append(tweet_dict['quote_count'])
            record.append(tweet_dict['reply_count'])
            record.append(tweet_dict['retweet_count'])
            record.append(tweet_dict['favorite_count'])
            record.append(tweet_dict['lang'])
            record.append(tweet_dict['timestamp_ms'])
             
            if tweet_dict['truncated']:
                analysis = TextBlob(tweet_dict['extended_tweet']['full_text'])
                record.append(analysis.sentiment.subjectivity)
                record.append(analysis.sentiment.polarity)
                record.append(tweet_dict['extended_tweet']['full_text'].replace('\n',' '))
                
            else :
                analysis = TextBlob(tweet_dict['text'])
                record.append(analysis.sentiment.subjectivity)
                record.append(analysis.sentiment.polarity)
                record.append(tweet_dict['text'].replace('\n',' ')) 
        
            print(record)
        
            with open("output.csv", "a",newline='',encoding='utf-8') as fp:
                wr = csv.writer(fp, dialect='excel')
                wr.writerow(record)
                
            counter=[]
            counter.append(f.filelineno())
            counter.append(f.filename())
            with open("counter.csv", "w",newline='',encoding='utf-8') as c:
                wr = csv.writer(c, dialect='excel')
                wr.writerow(counter)
             
    except (json.JSONDecodeError):
        pass
 