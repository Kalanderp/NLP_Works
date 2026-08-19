"""Simple text coherence score using adjacent sentence vocabulary overlap."""
import re
def score(text):
 s=[set(re.findall(r'[a-z]+',x.lower())) for x in re.split(r'[.!?]+',text) if x.strip()]
 overlaps=[len(a&b)/max(1,len(a|b)) for a,b in zip(s,s[1:])]
 return sum(overlaps)/len(overlaps) if overlaps else 1.0
if __name__=='__main__': print('Coherence:', round(score('Cats are mammals. Mammals need food. Food provides energy.'),3))
