import sys
import json



def main():
    afinnfile = open(sys.argv[1])
    scores = {}
    new_words = {}
    new_words_occur = {}
    for line in afinnfile:
        term, score  = line.split("\t")
        scores[term] = float(score)
    
    tweet_file = open(sys.argv[2])

    for line in tweet_file:
        pyresponse = json.loads(line)
        if "text" in pyresponse.keys():
            #language = pyresponse["lang"]
            #if language == "en":
                tweet = (pyresponse["text"]).encode("utf-8")	
                sentiment_count=0.0
                sentiment_ratio=0.0
                positive_count=0.0
                negative_count=0.0
                tweet_split = []
                tweet_split = tweet.split(" ")
                for i in range(len(tweet_split)):
                    if tweet_split[i] in scores or tweet_split[i] in new_words:
                        sentiment_key = tweet_split[i]
                        if tweet_split[i] in scores:
                            sentiment_count = sentiment_count +  scores[sentiment_key]
                            if scores[sentiment_key] > 0:
                                positive_count = positive_count + scores[sentiment_key]
                            if scores[sentiment_key] < 0:
                                negative_count = negative_count - scores[sentiment_key]
                        if tweet_split[i] in new_words:
                            sentiment_count = sentiment_count +  new_words[sentiment_key]
                            if new_words[sentiment_key] > 0:
                                positive_count = positive_count + new_words[sentiment_key]
                            if new_words[sentiment_key] < 0:
                                negative_count = negative_count - new_words[sentiment_key]
                        if negative_count != 0:
                            sentiment_ratio = (positive_count / negative_count)/len(tweet_split)
                        if negative_count == 0:
                            sentiment_ratio = (positive_count * 2)/len(tweet_split)
                        if negative_count > positive_count:
                            sentiment_ratio = (sentiment_ratio * -1.0)/len(tweet_split)
                #print positive_count
                for i in range(len(tweet_split)):
                    if tweet_split[i] not in scores and tweet_split[i] not in new_words:
                        word_key = tweet_split[i]
                        new_words[word_key] = sentiment_ratio
                        new_words_occur[word_key] = 1
                    if tweet_split[i] not in scores and tweet_split[i] in new_words:
                        word_key = tweet_split[i]
                        temp = new_words_occur[word_key] + 1
                        new_words[word_key] = ((new_words[word_key] * new_words_occur[word_key])+sentiment_ratio)/float(temp)
                        new_words_occur[word_key] = new_words_occur[word_key] + 1
    for k,v in new_words.items():
        sys.stdout.write(k + " " + str(v) + '\n')

if __name__ == '__main__':
    main()
