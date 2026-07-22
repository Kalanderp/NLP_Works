import nltk
from nltk.stem import PorterStemmer
ps = PorterStemmer()
words = ["running", "playing", "studies", "happiness",
         "connected", "flying", "easily", "reading"]
print("Original Word -> Stemmed Word")
for word in words:
    print(word, "->", ps.stem(word))