from contraintes import *
from parser import *
from database import *


def isTGD(df : DF) :
    corps = df.left
    tete = df.right
    if len(corps.list_atom) != 1 :
        print("corps a plus d'un atome")
        return False
    for atom in corps.list_atom :
        if isinstance(atom, EqAtom) :
            print("contient EqAtom")
            return False
    for atom in tete.list_atom :
        if isinstance(atom, EqAtom) :
            print("contient EqAtom")
            return False
    list_tuples = corps.list_atom[0].list_tuples[0]
    
    same_var = 0
    diff_var = 0
    
    for atom in tete.list_atom :
        for var in atom.list_tuples[0] :
            if var in list_tuples :
                same_var += 1
            else :
                diff_var += 1
        if same_var == 0 or diff_var == 0 :
            return False
    return True

def satisfaitCorps(df, table) : # database au lieu de table
    corps = df.left
    corps_tuples = corps.list_atom
    table_tuples = table.table
    satisfies = True
    for atom in corps_tuples :
        for k in range(0, table.key) :
            if table_tuples[k] == [] :
                return True
            satisfies = True
            if len(table_tuples[k] != len(atom.list_tuples[0])) :
                satisfies = False
            else :
                for i in range(0, len(table_tuples[k])) :
                    for j in range(i+1, len(table_tuples[k])) :
                        if table_tuples[k][i] == table_tuples[k][j] :
                            if atom.list_tuples[0][i] != atom.list_tuples[0][j] :
                                satisfies = False
                        elif table_tuples[k][i] != table_tuples[k][j] :
                            if atom.list_tuples[0][i] == atom.list_tuples[0][j] :
                                satisfies = False
                if satisfies == True : # au moins une ligne qui satisfait
                    return True

    return satisfies


data = str("R(x1,x2) -> Q(x2,x1,z1)\n")

DFs = []
for text in data.splitlines() :
    tree = grammar.match(text)
    res = DFParser()
    output = res.visit(tree)
    DFs.append(output)

for df in DFs :
    print(isTGD(df))





