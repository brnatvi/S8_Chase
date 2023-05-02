from parsimonious.grammar import Grammar
from parsimonious.nodes import NodeVisitor
from contraintes import *
from database import *

grammar = Grammar(
    r"""
    relAtom = relation tuples
    relation = ~"[A-Z]+[a-z]*"
    tuples = "(" variableList+ ")"
    variableList = (variable comma) / (comma? variable)

    variable = ~"[a-z]+[0-9]*"
    comma = ","
    """
)

def parcours_liste(l, type, ret) :
    for i in l :
        if isinstance(i, list) :
            parcours_liste(i, type, ret)
        if isinstance(i, type) :
            ret.append(i)
    return ret
    

class DFParser(NodeVisitor) :        
        
    def visit_variable(self, node, vc) :
        return Variable(node.text)
    
    def visit_variableList(self, node, vc) :
        ret = []
        for child in vc :
            parcours_liste(child, Variable, ret)
        return ret

    def visit_relation(self, node, vc) :
        return Relation(node.text)

    def visit_tuples(self, node, vc) :
        ret = []
        for child in vc :
            if isinstance(child, list):
                ret.append([item for sublist in child for item in sublist])
        return ret

    
    def visit_relAtom(self, node, vc) :
        relation, tuples = vc
        return RelAtom(relation, tuples)

    def generic_visit(self, node, visited_children) :
        return visited_children or node

   

text = str("R(x1,x2,x3,x4,x5)")

tree = grammar.match(text)
res = DFParser()
output = res.visit(tree)
print(output)

    
    