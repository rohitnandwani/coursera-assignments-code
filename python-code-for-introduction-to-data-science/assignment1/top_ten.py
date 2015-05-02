import sys
import json
import operator


def main():

    
    tweet_file = open(sys.argv[1])
	
    hashtag_occur = {}

    for line in tweet_file:
        pyresponse = json.loads(line)
        if "entities" in pyresponse.keys():
            entities = pyresponse["entities"]
            if "hashtags" in entities.keys():
                hashtags = entities["hashtags"]
                for i in range(len(hashtags)):
                    if "text" in hashtags[i].keys():
                        hash_key = hashtags[i]["text"].encode("utf-8")
                        if hash_key in hashtag_occur:
                            hashtag_occur[hash_key] = hashtag_occur[hash_key] + 1.0
                        if hash_key not in hashtag_occur:
                            hashtag_occur[hash_key] = 1.0

    sorted_hashtag_occur = sorted(hashtag_occur.iteritems(), key=operator.itemgetter(1))
    sorted_hashtag_occur.reverse()
    for i in range(10):
        sys.stdout.write(sorted_hashtag_occur[i][0] + " " + str(sorted_hashtag_occur[i][1]) + '\n')
			

if __name__ == '__main__':
    main()
