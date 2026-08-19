"""Feature-based subject-verb agreement checker."""
LEXICON={'birds':('N','PL'),'bird':('N','SG'),'sing':('V','PL'),'sings':('V','SG'),'dogs':('N','PL'),'dog':('N','SG'),'runs':('V','SG'),'run':('V','PL')}
def check(sentence):
    w=sentence.lower().split()
    if len(w)!=3 or w[1] != 'the': return False, 'Expected: subject the verb'
    subject, verb = LEXICON.get(w[0]), LEXICON.get(w[2])
    if not subject or not verb or subject[0]!='N' or verb[0]!='V': return False, 'Unknown lexical item'
    ok=subject[1]==verb[1]
    return ok, 'agreement' if ok else 'subject-verb disagreement'
if __name__=='__main__':
    for s in ['birds the sing','bird the sing','dogs the runs']: print(s, '->', check(s))
