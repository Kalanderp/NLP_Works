import nltk
from nltk.stem import PorterStemmer, WordNetLemmatizer
nltk.download("wordnet")
stemmer = PorterStemmer()
lemmatizer = WordNetLemmatizer()
words=["running", "jumps", "easily", "fairly"]
print("Morphological Analysis\n")
for word in words:
    stem = stemmer.stem(word)
    lemma = lemmatizer.lemmatize(word)
    print("Original Word: ", word)
    print("Stem: ", stem)
    print("Lemma: ", lemma)
    print()