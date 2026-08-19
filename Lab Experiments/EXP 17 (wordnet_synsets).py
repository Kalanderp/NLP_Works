"""Explore WordNet synsets and definitions using NLTK."""
try:
 from nltk.corpus import wordnet as wn
 word='bank'; synsets=wn.synsets(word)
 if not synsets: raise LookupError
 for s in synsets[:5]: print(s.name(), ':', s.definition(), '| examples:', s.examples())
except (ImportError, LookupError): print('Install/download WordNet: pip install nltk; python -m nltk.downloader wordnet')
