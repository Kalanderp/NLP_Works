"""Compact Earley recognizer for a context-free grammar."""
def earley(grammar, start, words):
    augmented = "@START"; rules = {**grammar, augmented:[[start]]}; chart=[set() for _ in range(len(words)+1)]
    chart[0].add((augmented, tuple([start]), 0, 0))
    for i in range(len(words)+1):
        changed=True
        while changed:
            changed=False
            for lhs,rhs,dot,origin in list(chart[i]):
                if dot < len(rhs) and rhs[dot] in rules:
                    for prod in rules[rhs[dot]]:
                        item=(rhs[dot],tuple(prod),0,i)
                        if item not in chart[i]: chart[i].add(item); changed=True
                elif dot == len(rhs) and lhs != augmented:
                    for pl,pr,pd,po in list(chart[origin]):
                        if pd < len(pr) and pr[pd] == lhs:
                            item=(pl,pr,pd+1,po)
                            if item not in chart[i]: chart[i].add(item); changed=True
            if i < len(words):
                for lhs,rhs,dot,origin in list(chart[i]):
                    if dot < len(rhs) and rhs[dot] not in rules and rhs[dot] == words[i]:
                        chart[i+1].add((lhs,rhs,dot+1,origin))
    return (augmented, (start,), 1, 0) in chart[len(words)]

if __name__ == '__main__':
    g={'S':[['NP','VP']], 'NP':[['Det','N']], 'VP':[['V','NP']], 'Det':[['the']], 'N':[['cat'],['dog']], 'V':[['sees']]}
    w='the cat sees the dog'.split(); print('Sentence:', ' '.join(w)); print('Accepted:', earley(g,'S',w))
