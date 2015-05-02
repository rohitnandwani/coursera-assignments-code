import sys
import json



def main():

    
    tweet_file = open(sys.argv[1])
	
    word_occur = {}
    word_frequency = {}
    total_words = 0

    for line in tweet_file:
        pyresponse = json.loads(line)
        if "text" in pyresponse.keys():
            tweet = (pyresponse["text"]).encode("utf-8")
            tweet = tweet.replace('\n','')			
            tweet_split = []
            tweet_split = tweet.split(" ")
            for i in range(len(tweet_split)):
                total_words = total_words + 1
                if tweet_split[i] in word_occur:
                    word_key = tweet_split[i]
                    word_occur[word_key] = word_occur[word_key] + 1
                if tweet_split[i] not in word_occur:
                    word_key = tweet_split[i]
                    word_occur[word_key] = 1

    for k,v in word_occur.items():
        word_frequency[k] = word_occur[k]/float(total_words)
    for k,v in word_frequency.items():
        if len(k)>0:
            sys.stdout.write(k + " " + str(v) + '\n')
			

if __name__ == '__main__':
    main()
