from parsimonious.grammar import Grammar
from parsimonious.nodes import NodeVisitor
from contraintes import *
from database import *

grammar = Grammar(
    r"""
    # and = "and"
    # equals = "="
    # implies = "->"
    # lparen = "("
    # rparen = ")"
    # comma = ","

    df = conjAtom " -> " conjAtom
    conjAtom = (atom (" and " atom)*) +
    atom = (relAtom / eqAtom)

    relAtom = relation tuples 
    relation = ~"[A-Z]+[a-z]*"
    tuples = "(" variableList ")"
    variableList = (variable ("," variable)*) +
    equals = "="
    eqAtom = (variable equals variable)+ / (equals variable)
    variable = ~"[a-z]+[0-9]*"
    ws = ~"[^\S\r\n]"
    
    
    
    # newline = ~"[\r\n]+"
    # listDFs = df +
    """
)

class DFParser(NodeVisitor) :
    entry = {}
    conj_atom = []

    def __init__(self, grammar, text) :
        ast = grammar.match(text)
        self.visit(ast)

    def visit_variable(self, node, vc) :
        return Variable(node.text)
    
    def visit_variableList(self, node, vc) :
        # self.entry.append([node.text])
        return node.text

    def visit_tuples(self, node, vc) :
        # self.entry.append(node.text)
        return node.text

    def visit_relation(self, node, vc) :
        return Relation(node.text)

    def visit_relAtom(self, node, vc) :
        relation, tuples = vc
        return RelAtom(relation, tuples)

    def visit_eqAtom(self, node, vc) :
        # print(node.text)
        print(vc)

    def visit_df(self, node, vc) :
        # print(node.text)
        # print(vc)
        left,_,right = vc
        self.entry['left'] = left
        self.entry['right'] = right
        return node.text

    def visit_conjAtom(self, node, vc):
        # print(node.text)        
        return node.text

    def visit_atom(self, node, vc) :
        # print(node.text)
        
        return node.text

    

    def generic_visit(self, node, visited_children) :
        pass

    # visit_variable + visit_variableList 

text = str("R(x1,x2,x3) and x1=x2=x3 -> P(x2,x2)")

print(DFParser(grammar, text).entry)

    
    