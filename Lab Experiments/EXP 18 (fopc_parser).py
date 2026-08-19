"""Basic parser for FOPC expressions: predicates, variables, constants, and connectives."""
import re
TOKEN=re.compile(r'\s*(forall|exists|and|or|not|implies|[A-Za-z_]\w*|[(),.])')
def parse(text):
    toks=[m.group(1) for m in TOKEN.finditer(text)]; i=0
    def expr():
        nonlocal i
        if toks[i] in ('forall','exists'):
            q=toks[i]; i+=1; var=toks[i]; i+=1
            if toks[i]=='.': i+=1
            return (q,var,expr())
        if toks[i]=='not': i+=1; return ('not',expr())
        name=toks[i]; i+=1; args=[]
        if i<len(toks) and toks[i]=='(':
            i+=1
            while toks[i]!=')':
                args.append(toks[i]); i+=1
                if toks[i]==',': i+=1
            i+=1
        node=(name,args)
        if i<len(toks) and toks[i] in ('and','or','implies'):
            op=toks[i]; i+=1; return (op,node,expr())
        return node
    return expr()
if __name__=='__main__': print(parse('forall x. human(x) implies mortal(x)'))
