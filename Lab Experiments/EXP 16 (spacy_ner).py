"""Named Entity Recognition with spaCy; uses a blank fallback if a model is unavailable."""
text='Apple was founded by Steve Jobs in California in 1976.'
try:
 import spacy
 try: nlp=spacy.load('en_core_web_sm')
 except OSError: print('Install model: python -m spacy download en_core_web_sm'); nlp=None
 if nlp:
  for ent in nlp(text).ents: print(ent.text, '->', ent.label_)
except ImportError: print('spaCy is not installed. Run: pip install spacy && python -m spacy download en_core_web_sm')
