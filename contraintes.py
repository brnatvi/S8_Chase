
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
    
    def __init__(self, relation, list_attr, list_vars):
        self.rel_name = relation
        self.list_attr = list_attr
        self.list_vars = list_vars

    def __str__(self):
        ret = str(self.rel_name) + '['    
        for attr in self.list_attr:
            ret += str(attr) + ', '        
        ret = ret[:-2]
        ret += ']'
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
    toWhom : Variable
    
    def __init__(self, at1, at2):
        self.whoIsEqual = at1
        self.toWhom = at2

    def __str__(self):        
        return str(self.whoIsEqual) + '=' + str(self.toWhom)


class AtomConjunction :
    ''' R(x1, y1) /\ Q(y2, x2) /\ x1 = y1 '''

    def __init__(self, list_atoms):
        self.list_atoms = list_atoms        

    def compose_transformation(self, database: DataBase):
        for atom in self.list_atoms:
            if isinstance(atom, RelAtom):
                if (database.find_by_relation(atom.rel_name))

class AtomDisjunction :
    ''' R(x1, y1) \/ Q(y2, x2) '''
    def __init__(self, list_atoms):
        self.list_atoms = list_atoms        


class Dependency :
    def __init__(self, corps, head):
        self.corps = corps
        self.head = head 
