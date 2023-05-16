
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
        ret = ret[:-2]
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

  #  def takeAttributeOfVariable(self, var):
  #      index = -1
  #      try:
  #          index = self.list_vars.index(el)
  #      except Exception as e:
  #          print('variable ' + str(el) + ' is not in relation atom ' + self.rel_name)
  #          return None 
  #      if (index >= len(self.list_attr)):
  #          print('nb of variables != nb of attributes')
  #          return None
  #      return self.list_attr[index]

    

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
            ret += str(el) + ' and '
        ret = ret[:-5]
        return ret


class Instruction :
    fromRel: Relation
    fromAttr: int
    toRel: Relation
    toAttr: int

    def __init__(self, fromR, fromA, toR, toA) :
        self.fromRel = fromR      
        self.fromAttr = fromA    
        self.toRel = toR      
        self.toAttr = toA  

    def __str__(self):
        return '[' + str( self.fromRel) + ', ' + str(self.fromAttr) + ', ' +  str(self.toRel) + ', ' + str(self.toAttr) + ']'

class DF :
    left : AtomConj # corps
    right : AtomConj # tete

    def __init__(self, left, right) :
        self.left = left
        self.right = right
        

    def __str__(self):        
        return str(self.left) + '  -> '+ str(self.right)


    def complete_attributes(self, database):
        for el in self.left.list_atom:
            if isinstance(el, RelAtom):                
                el.list_attr = el.list_attr + database.find_table_by_relation(el.rel_name).attr_list
        
        for el in self.right.list_atom:
            if isinstance(el, RelAtom):                
                el.list_attr = el.list_attr + database.find_table_by_relation(el.rel_name).attr_list

    def create_instructions_TGD(self):
        body = self.left.list_atom
        head = self.right.list_atom
        def make_job(atomTo, atomFrom):
            listInstr = list()
            for i in range(len(atomFrom.list_vars[0])):
                for j in range(len(atomTo.list_vars[0])):
                    if atomFrom.list_vars[0][i] == atomTo.list_vars[0][j]:                                               
                        listInstr.append( Instruction(atomFrom.rel_name, i, atomTo.rel_name, j) )
            return listInstr

        allInstr = []
        for relTo in head:
            for relFrom in body:
                allInstr = allInstr + make_job(relTo, relFrom)
        return allInstr
 
    def create_instructions_EGD(self):
        print('TODO')