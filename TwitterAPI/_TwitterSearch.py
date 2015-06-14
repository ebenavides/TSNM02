from TwitterSearch import *

try:
    tso = TwitterSearchOrder() 
    tso.set_keywords(['PelonArmy', 'LeagueOfLegends', 'Lindsan']) 
    tso.set_language('es') 
    tso.set_include_entities(False) 


    ts = TwitterSearch(
        consumer_key = '1uQQd0wTVH76kCPCqNVnm15Lk',
        consumer_secret = 'XNTLr9Y2S1ThRYlGQyKxoOkIVUuheAMrHFmpyFwIQZiyBKU8hT',
        access_token = '898572810-btveERSAL1n5BflyJL54ZzylIKFeV4xA14vXPcaq',
        access_token_secret = '5bO2B8PsxiPiQeGaUL0ESGoZSCTMa4n2tvNkaZ39J1tYZ'
     )


    for tweet in ts.search_tweets_iterable(tso):
        print( '@%s tweeted: %s' % ( tweet['user']['screen_name'], tweet['text'] ) )

except TwitterSearchException as e: 
    print(e)
