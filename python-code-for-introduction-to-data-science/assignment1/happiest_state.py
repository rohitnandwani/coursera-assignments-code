import sys
import json
import operator


def main():
    afinnfile = open(sys.argv[1])
    scores = {}
    for line in afinnfile:
        term, score  = line.split("\t")
        scores[term] = int(score)

    
    tweet_file = open(sys.argv[2])
	
    state_sentiment = {}
    state_no_of_tweets = {}

    for line in tweet_file:
        pyresponse = json.loads(line)
        if "place" in pyresponse.keys():
            place = pyresponse["place"]
            if type(place) == dict and "country_code" in place.keys():
                country_code = place["country_code"]
                if country_code == "US":
                    if "full_name" in place.keys():
                        state = place["full_name"].encode("utf-8")
                        state = state[-2:]
                        if state not in state_sentiment:
                            state_sentiment[state] = 0
                            state_no_of_tweets[state] = 0
                            if "text" in pyresponse.keys():
                                if "lang" in pyresponse.keys():
                                    language = pyresponse["lang"]
                                    if language == "en":
                                        tweet = (pyresponse["text"]).encode("utf-8")	
                                        sentiment_count=0
                                        tweet_split = []
                                        tweet_split = tweet.split(" ")
                                        for i in range(len(tweet_split)):
                                            if tweet_split[i] in scores:
                                                sentiment_key = tweet_split[i]
                                                sentiment_count = sentiment_count +  scores[sentiment_key]
                                                temp = state_no_of_tweets[state] + 1
                                                state_sentiment[state] = ((state_sentiment[state] * state_no_of_tweets[state]) + sentiment_count)/float(temp)
                                                state_no_of_tweets[state] = state_no_of_tweets[state] + 1

    sorted_state_sentiment = sorted(state_sentiment.iteritems(), key=operator.itemgetter(1))
    sorted_state_sentiment.reverse()
    for i in range(1):
        sys.stdout.write(sorted_state_sentiment[i][0])

			

if __name__ == '__main__':
    main()
