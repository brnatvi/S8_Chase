
from database import *


class Variable :
    def __init__(self, val) :
        self.val = val

    def __str__(self) :
        return f"{self.val}"
    
    def equals(self, another):
        return (self.val == another.val)


class RelAtom:
    ''' R[A, B]'''
    rel_name : Relation
    
    # def __init__(self, relation, list_attr, list_vars):
    #     self.rel_name = relation
    #     self.list_attr = list_attr
    #     self.list_vars = list_vars

    def __init__(self, relation, list_tuples):
        self.rel_name = relation
        self.list_tuples = list_tuples
        

    def __str__(self):
        # print(self.list_tuples)
        ret = str(self.rel_name) + '('
    
        for attr in self.list_tuples:
            ret += str(attr) + ', '
        
        ret = ret[:-2]
        ret += ')'
        return ret
    
    def strVars(self):
        ret = str(self.rel_name) + '('    
        for v in self.list_vars:
            ret += str(v) + ', '        
        ret = ret[:-2]
        ret += ')'
        return ret
    

class EqAtom:
    ''' x1 = x2'''
    whoIsEqual : Variable
    
    def __init__(self, at1, at2):
        self.whoIsEqual = at1
        self.toWhom = at2 # can be variable or EqAtom


    def __str__(self):        
        return str(self.whoIsEqual) + '=' + str(self.toWhom)


#class AtomConjunction :
    ''' R(x1, y1) /\ Q(y2, x2) /\ x1 = y1 '''

class AtomConj :
    list_atom = []

    def __init__(self, list_atom) :
        self.list_atom = list_atom

class DF :
    left : AtomConj
    right : AtomConj

    def __init__(self, left, right) :
        self.left = left
        self.right = right
