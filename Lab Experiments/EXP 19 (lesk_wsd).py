"""Simplified Lesk word-sense disambiguation using WordNet gloss overlap."""
try:
 from nltk.corpus import wordnet as wn
 def lesk(sentence, target):
  context=set(sentence.lower().split()); best=None
  for syn in wn.synsets(target):
   signature=set(syn.definition().lower().split())
   score=len(context & signature)
   if best is None or score>best[0]: best=(score,syn.name(),syn.definition())
  return best
 print(lesk('I deposited money at the bank', 'bank'))
except (ImportError, LookupError): print('Install/download NLTK WordNet to run this experiment.')
