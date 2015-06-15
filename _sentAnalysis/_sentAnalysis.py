import nltk
import urllib

try:
    import urllib.request as urllib2
except ImportError:
    import urllib2
    
def filter_words(tweets_list):
    res=[]
    for words in tweets_list:
        words_filtered = [e.lower() for e in words.split() if len(e) >= 3]
        res.append(words_filtered)
    return res

def get_words_in_tweets(tweets):
    all_words = []
    for (words, sentiment) in tweets:
      all_words.extend(words)
    return all_words

def get_word_features(wordlist):
    wordlist = nltk.FreqDist(wordlist)
    word_features = wordlist.keys()
    return word_features

tweets = ['I love this car','This view is amazing','I am so excited about the concert','This view is amazing','He is my best friend',
          'I do not like this car','This view is horrible','I feel tired this morning','I am not looking forward to the concert','He is my enemy']


print(filter_words(tweets))



url = 'http://text-processing.com/api/sentiment/'
values = {'text' : 'Michael Foord'}

data = urllib.parse.urlencode(values)
binary_data = data.encode('utf-8')
req = urllib2.Request(url, binary_data)
response = urllib2.urlopen(req)
the_page = response.read()
print(the_page)

#word_features = get_word_features(get_words_in_tweets(tweets))





    


