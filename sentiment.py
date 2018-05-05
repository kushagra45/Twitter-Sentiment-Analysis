import json
from textblob import TextBlob 


with open('Tweets_taketheknee.txt') as data_file:
    data = json.load(data_file)

a = ["CA","TX","AL","AS","AK","CO","CT","DE",
        "IL","IN","KS","LA","MI","MN","NY","OH","OK",
        "OR","FL","GA","GU","HI","ID","AZ","AR","DC","IA","KY","MD","MA"
        ,"MS","MO","MT","NE","NV","NH","NJ","NM","NC","ND","PA","RI","SC","SD","TN","UT"
        ,"VT","VA","WA","WV","WI","WY"]


corpus = [[] for x in xrange(len(a))]


for words in data:
    for x in a:
        if x in words['user']['location']:
            word = words['text']
            word = word.lower()
            ind_tweet = a.index(x)
            corpus[ind_tweet].append(word)


sum = 0
average = 0


for i in range(len(a)):
    #print 'State Number ',i+1
    for x in corpus[i]:
        text = TextBlob(x)
        pol = text.polarity
        average += pol  
        sum += 1        /*sum is number of count.. */                 
    result = average/sum
    print a[i],result
