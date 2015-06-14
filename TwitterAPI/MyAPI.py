from TwitterAPI import TwitterAPI

twitter_api = TwitterAPI('1uQQd0wTVH76kCPCqNVnm15Lk',
                         'XNTLr9Y2S1ThRYlGQyKxoOkIVUuheAMrHFmpyFwIQZiyBKU8hT','898572810-btveERSAL1n5BflyJL54ZzylIKFeV4xA14vXPcaq','5bO2B8PsxiPiQeGaUL0ESGoZSCTMa4n2tvNkaZ39J1tYZ')

_request = twitter_api.request('search/tweets', {'q':'PelonArmy'})

for tweet in _request:
        print(tweet['user']['screen_name'],tweet['text'])

