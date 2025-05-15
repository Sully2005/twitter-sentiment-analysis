import tweepy
from textblob import TextBlob
import csv

consumer_key = 'consumer_key'
consumer_secret = 'consumer_secret'


access_token = 'acess_token'
access_secret = 'access_secret'

basketball_players = ['Lebron', 'Giannis', 'Durant', 'Curry','Harden', 'Kyrie']

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token,access_secret)

api = tweepy.API(auth)




total_sentiment = 0

# Get label for whether opinion is positive or negative
def get_label(polarity):
    threshold = 0

    if analysis.sentiment.polarity > threshold:
        return 'Positive'
    else:
        return 'Negative'

#Iterate through each basketball player in the list 
for basketball_player in basketball_players:
    #Reset each time
    total_sentiment = 0
    public_tweet = api.search_tweets(q=basketball_player, count=50, tweet_mode = 'extended', lang='en')
    with open('%s_tweets.csv' % basketball_player, 'w', newline='', encoding='utf-8') as basketball_player_opinions:

        writer = csv.writer(basketball_player_opinions)

        writer.writerow(["Tweet", "Sentiment", "Polarity"])

        for tweet in public_tweet:

            analysis = TextBlob(tweet.full_text)

            polarity  = analysis.sentiment.polarity

            sentiment_label = get_label(polarity)

            writer.writerow([tweet.full_text, sentiment_label, polarity])

            total_sentiment += analysis.sentiment.polarity
    
        #Get the average sentiment for the tweets
        average_sentiment = total_sentiment/len(public_tweet)
        writer.writerow([])
        #Better for formatting since data is in three columns
        writer.writerow(['Average sentiment: ', '',  round(average_sentiment, 3)])

