import nltk

nltk.download('punkt')
nltk.download('averaged_perceptron_tagger_eng')

text = input("Enter a sentence: ")

words = nltk.word_tokenize(text)
tags = nltk.pos_tag(words)

print("\nPOS Tags:")
for word, tag in tags:
    print(word, "->", tag)