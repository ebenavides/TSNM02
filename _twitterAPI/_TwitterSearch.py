from TwitterSearch import *
import time

class _TwitterSearch:

    def __init__(self, tags, lan):
        self.tags = tags
        self.lan = lan

    def my_callback_closure(current_ts_instance): 
        queries, tweets_seen = current_ts_instance.get_statistics()
        if queries > 0 and (queries % 5) == 0: 
            time.sleep(60)


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
                print( '@%s tweeted: %s' % ( tweet['user']['screen_name'].encode("utf-8", errors='ignore'), tweet['text'].encode("utf-8", errors='ignore') ) )

        except TwitterSearchException as e: 
            print(e)
