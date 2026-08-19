"""TF-IDF information retrieval and cosine document ranking."""
import math,re

def tokens(s): return re.findall(r'[a-z]+',s.lower())
def rank(query, docs):
 dt=[tokens(d) for d in docs]; q=tokens(query); vocab=set(q)|{x for d in dt for x in d}; n=len(docs)
 def vec(words): return {t:(words.count(t)/len(words))*math.log((1+n)/ (1+sum(t in d for d in dt)))+0.0 for t in vocab}
 qv=vec(q); scores=[]
 for d in dt:
  dv=vec(d); dot=sum(qv[t]*dv[t] for t in vocab); den=(sum(x*x for x in qv.values())**.5)*(sum(x*x for x in dv.values())**.5); scores.append(dot/den if den else 0)
 return sorted(enumerate(scores,1), key=lambda x:x[1], reverse=True)
if __name__=='__main__':
 docs=['cats chase mice','dogs chase balls','machine learning and natural language processing']; print(rank('cats mice',docs))
