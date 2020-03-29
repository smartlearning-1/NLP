from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
# I was taking a ride in the car.
# I was riding in the car.
ps=PorterStemmer()
paragraph = """I was taking a ride in the car. I was riding in the car."""

words=word_tokenize(paragraph)
print(words)
for w in words:
    print(ps.stem(w))