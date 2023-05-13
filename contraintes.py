
from database import *


class Variable :
    def __init__(self, val) :
        self.val = val

    def __str__(self) :        
        return self.val

    def __eq__(self, another) :
        if isinstance(another, Variable) :
            return self.val == another.val
        return False




class RelAtom:
    ''' R[A, B] R(x1, x2)'''
    rel_name : Relation


    def __init__(self, relation, list_vars):
        self.rel_name = relation
        self.list_vars = list_vars
        self.list_attr = list()             #TODO make assert nb vars = nb attributes
        

    def __str__(self):
        
        ret = str(self.rel_name) + '['

        for el in self.list_attr:
            ret += str(el) + ', '        
        #ret = ret[:-2]
        ret += '] '

        
        ret += str(self.rel_name) + '('        
   
        for el in self.list_vars:       #TODO do we really need list of list ?
            for v in el:
                ret += str(v) + ', '        
            ret = ret[:-2]
            ret += ')'

        return ret
    
    def __iter__(self) :
        self.index = 0
        return self
    
    def __next__(self) :
        if self.index < len(self.list_vars) :
            result = self.list_vars[self.index]
            self.index += 1
            return result
        else :
            raise StopIteration

    def takeAttributeOfVariable(self, var):
        index = -1
        try:
            index = self.list_vars.index(el)
        except Exception as e:
            print('variable ' + str(el) + ' is not in relation atom ' + self.rel_name)
            return None 
        if (index >= len(self.list_attr)):
            print('nb of variables != nb of attributes')
            return None
        return self.list_attr[index]

    def addAttribute(self, att):
        self.list_attr.append(att)
    

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

    def __iter__(self) :
        self.index = 0
        return self

    def __next__(self) :
        if self.index < len(self.list_atom) :
            result = self.list_atom[self.index]
            self.index += 1
            return result
        else :
            raise StopIteration
    
    def __str__(self):
        ret = ''
        for el in self.list_atom:
            ret += str(el)
        return ret


class DF :
    left : AtomConj # corps
    right : AtomConj # tete

    def __init__(self, left, right) :
        self.left = left
        self.right = right

    def __str__(self):        
        return 'left: '+ str(self.left) + '  rigth: '+ str(self.right)

    