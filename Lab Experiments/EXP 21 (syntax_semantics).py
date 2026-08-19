"""Syntax-driven semantic analysis: extract noun phrases and assign simple meanings."""
import re
MEANINGS={'cat':'animal','dog':'animal','Alice':'person','park':'location','book':'artifact'}
def analyze(sentence):
 phrases=re.findall(r'(?:(?:the|a|an) )?[A-Z][a-z]+|(?:(?:the|a|an) )?[a-z]+',sentence)
 return [(p, MEANINGS.get(p.split()[-1].strip('.,'),'unknown')) for p in phrases if p.split()[-1].strip('.,') in MEANINGS]
if __name__=='__main__': print(analyze('Alice reads the book in the park.'))
