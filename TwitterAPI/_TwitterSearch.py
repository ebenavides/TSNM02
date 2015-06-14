from TwitterSearch import *

try:
    tso = TwitterSearchOrder() # create a TwitterSearchOrder object
    tso.set_keywords(['PelonArmy', 'LeagueOfLegends', 'Lindsan']) # let's define all words we would like to have a look for
    tso.set_language('es') # we want to see German tweets only
    tso.set_include_entities(False) # and don't give us all those entity information

    # it's about time to create a TwitterSearch object with our secret tokens
    ts = TwitterSearch(
        consumer_key = '1uQQd0wTVH76kCPCqNVnm15Lk',
        consumer_secret = 'XNTLr9Y2S1ThRYlGQyKxoOkIVUuheAMrHFmpyFwIQZiyBKU8hT',
        access_token = '898572810-btveERSAL1n5BflyJL54ZzylIKFeV4xA14vXPcaq',
        access_token_secret = '5bO2B8PsxiPiQeGaUL0ESGoZSCTMa4n2tvNkaZ39J1tYZ'
     )

     # this is where the fun actually starts :)
    for tweet in ts.search_tweets_iterable(tso):
        print( '@%s tweeted: %s' % ( tweet['user']['screen_name'], tweet['text'] ) )

except TwitterSearchException as e: # take care of all those ugly errors if there are some
    print(e)
