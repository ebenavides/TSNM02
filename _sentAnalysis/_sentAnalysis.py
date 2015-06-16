import nltk
import urllib
from TwitterSearch import *
import time


url = 'http://text-processing.com/api/sentiment/'

k=0
while(k<2):
    c=0
    lan=input("Language: ")
    tags=input("Tag: ")
    tags = tags.split(",")
    tweets=[]

    file = open("tweets.txt", "r+")
    file2 = open("probability.txt", "r+")

    def my_callback_closure(current_ts_instance): 
        queries, tweets_seen = current_ts_instance.get_statistics()
        if queries > 0 and (queries % 5) == 0: 
            time.sleep(20)


    try:
        tso = TwitterSearchOrder() 
        tso.set_keywords(tags) 
        tso.set_language(lan) 
        tso.set_include_entities(False) 

        ts = TwitterSearch(
            consumer_key = '1uQQd0wTVH76kCPCqNVnm15Lk',
            consumer_secret = 'XNTLr9Y2S1ThRYlGQyKxoOkIVUuheAMrHFmpyFwIQZiyBKU8hT',
            access_token = '898572810-btveERSAL1n5BflyJL54ZzylIKFeV4xA14vXPcaq',
            access_token_secret = '5bO2B8PsxiPiQeGaUL0ESGoZSCTMa4n2tvNkaZ39J1tYZ'
         )

        for tweet in ts.search_tweets_iterable(tso, callback=my_callback_closure):
            user=tweet['user']['screen_name'].encode("utf-8")
            text=tweet['text'].encode("utf-8")
            file.write( '%s'% (text))
            tweets.append(text)
            print( '@%s tweeted: %s' % ( user, text ) )
            if(c>2):
                break
            c+=1

    except TwitterSearchException as e: 
        print(e)

    def send_request(tweet):
        value = {'text' : tweet}
        data = urllib.parse.urlencode(value).encode('utf-8')
        req = urllib.request.Request(url, data)
        response = urllib.request.urlopen(req)
        the_page = response.read()
        sample=the_page.decode('utf-8')
        file2.write(sample+"\n")
        print(the_page)

    for i in tweets:
        send_request(i)
    
    k+=1












    


