"""Simple recursive top-down parser for a CFG."""
GRAMMAR = {'S': [['NP','VP']], 'NP': [['Det','N']], 'VP': [['V','NP']],
           'Det': [['the'], ['a']], 'N': [['cat'], ['dog']], 'V': [['sees']]}

def parse(symbol, words, pos=0):
    if symbol not in GRAMMAR:
        return [(symbol, pos + 1)] if pos < len(words) and words[pos] == symbol else []
    results=[]
    for rhs in GRAMMAR[symbol]:
        states=[([], pos)]
        for part in rhs:
            nxt=[]
            for children, p in states:
                for tree, q in parse(part, words, p): nxt.append((children+[tree], q))
            states=nxt
        for children, q in states: results.append(((symbol, children), q))
    return results

if __name__ == '__main__':
    sentence='the cat sees a dog'.split()
    trees=[t for t,p in parse('S', sentence) if p == len(sentence)]
    print('Sentence:', ' '.join(sentence)); print('Accepted:', bool(trees)); print('Trees:', trees)
