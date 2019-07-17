from nltk.corpus import stopwords
#CLEANING DATA - REMOVING PUNTUATION, HHTP, WWW, LOWER-CASE CONVERSRION, STOPWORDS
def Cleaner(tweet):
    Distinct_Words =[]
    whitelist = set('abcdefghijklmnopqrstuvwxyz ABCDEFGHIJKLMNOPQRSTUVWXYZ 1234567890')
    tweet = ''.join(filter(whitelist.__contains__, tweet))
    tweet = tweet.lower().split()
    stop_words = set(stopwords.words('english')) 
    for i in tweet: 
        if not i in stop_words: 
            Distinct_Words.append(i)
    for j in Distinct_Words:
        x = j.startswith("http")
        if x == True:
            Distinct_Words.remove(j)
        y = j.startswith("www")
        if y == True:
            Distinct_Words.remove(j)
    tweet = ' '.join(Distinct_Words)
    #print (tweet + "\n")
    return tweet