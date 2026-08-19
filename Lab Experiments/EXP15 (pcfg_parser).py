"""Probabilistic CFG (inside-style recursive chart parser)."""
G={'S':[(0.9,['NP','VP'])], 'NP':[(0.5,['Det','N']),(0.5,['N'])], 'VP':[(0.8,['V','NP']),(0.2,['V'])], 'Det':[(1.0,['the'])], 'N':[(0.6,['cat']),(0.4,['dog'])], 'V':[(1.0,['sees'])]}
def best(sym, words, i, j, memo):
    key=(sym,i,j)
    if key in memo:return memo[key]
    bestv=None
    for prob,rhs in G.get(sym,[]):
        if len(rhs)==1 and rhs[0] not in G:
            val=prob if j==i+1 and words[i]==rhs[0] else None
            if val is not None and (bestv is None or val>bestv[0]): bestv=(val,(sym,[rhs[0]]))
        elif len(rhs)==1:
            val=best(rhs[0],words,i,j,memo)
            if val and (bestv is None or prob*val[0]>bestv[0]): bestv=(prob*val[0],(sym,[val[1]]))
        elif len(rhs)==2:
            for k in range(i+1,j):
                a,b=best(rhs[0],words,i,k,memo),best(rhs[1],words,k,j,memo)
                if a and b and (bestv is None or prob*a[0]*b[0]>bestv[0]): bestv=(prob*a[0]*b[0],(sym,[a[1],b[1]]))
    memo[key]=bestv; return bestv
if __name__=='__main__':
    w='the cat sees the dog'.split(); r=best('S',w,0,len(w),{}); print('Sentence:', ' '.join(w)); print('Best probability:', r[0] if r else 0); print('Best tree:', r[1] if r else None)
