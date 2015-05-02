import sys
import json



def main():
    afinnfile = open(sys.argv[1])
    scores = {}
    for line in afinnfile:
        term, score  = line.split("\t")
        scores[term] = int(score)
    
    tweet_file = open(sys.argv[2])

    for line in tweet_file:
        pyresponse = json.loads(line)
        if "text" in pyresponse.keys():
            #language = pyresponse["lang"]
            #if language == "en":
                tweet = (pyresponse["text"]).encode("utf-8")	
                sentiment_count=0
                tweet_split = []
                tweet_split = tweet.split(" ")
                for i in range(len(tweet_split)):
                    if tweet_split[i] in scores:
                        sentiment_key = tweet_split[i]
                        sentiment_count = sentiment_count +  scores[sentiment_key]
                sys.stdout.write(str(sentiment_count) + '\n')

if __name__ == '__main__':
    main()
