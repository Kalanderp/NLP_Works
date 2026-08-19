"""Generate and pretty-print a parse tree using recursive CFG parsing."""
from pprint import pprint
from importlib.util import spec_from_file_location, module_from_spec
spec=spec_from_file_location('td','01_top_down_parser.py'); td=module_from_spec(spec); spec.loader.exec_module(td)

def pretty(tree, indent=0):
    label, kids=tree; print(' '*indent + label)
    for kid in kids:
        if isinstance(kid, tuple): pretty(kid, indent+2)
        else: print(' '*(indent+2)+kid)

if __name__=='__main__':
    words='the cat sees a dog'.split(); trees=[t for t,p in td.parse('S',words) if p==len(words)]
    print('Parse tree for:', ' '.join(words)); pretty(trees[0])
