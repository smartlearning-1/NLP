from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

example_sentence = "This is an example showing off stopwords filtration."

stop_words = set(stopwords.words("english"))
words=word_tokenize(example_sentence)
filter_sentance=[]
print(stop_words)
for w in words:
    if w not in stop_words:
        filter_sentance.append(w)
print(filter_sentance)

