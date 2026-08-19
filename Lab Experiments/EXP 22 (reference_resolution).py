"""Heuristic reference resolution for pronouns using recent compatible noun phrases."""
import re
def resolve(text):
 tokens=text.split(); antecedents=[]; results=[]
 for tok in tokens:
  word=tok.strip(',.!?'); low=word.lower()
  if low not in ('he','she','it','they','him','her','them') and (word[:1].isupper() or low in ('cat','dog','book','car')):
   antecedents.append(word)
  if low in ('he','she','it','they','him','her','them'):
   results.append((word, antecedents[-1] if antecedents else None))
 return results
if __name__=='__main__': print(resolve('Alice gave Bob a book. He thanked her.'))
