from contraintes import *
from database import *
import chase_parser as chp


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
    list_vars = corps.list_atom[0].list_vars[0]
    
    same_var = 0
    diff_var = 0
    
    for atom in tete.list_atom :
        for var in atom.list_vars[0] :
            if var in list_vars :
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
            if len(table_tuples[k] != len(atom.list_vars[0])) :
                satisfies = False
            else :
                for i in range(0, len(table_tuples[k])) :
                    for j in range(i+1, len(table_tuples[k])) :
                        if table_tuples[k][i] == table_tuples[k][j] :
                            if atom.list_vars[0][i] != atom.list_vars[0][j] :
                                satisfies = False
                        elif table_tuples[k][i] != table_tuples[k][j] :
                            if atom.list_vars[0][i] == atom.list_vars[0][j] :
                                satisfies = False
                if satisfies == True : # au moins une ligne qui satisfait
                    return True

    return satisfies


data = str("R(x1,x2) -> Q(x2,x1,z1)\n")     #TODO add attributes parsing an reading from R[A, B]


# return fromRel R attr A copyTo Q attr D
#        fromRel R attr B copyTo Q attr C
#          rel attr rel attr  
# return [[ R,   A,  Q,  D], [R, B, Q, C]]
# 
# return [instr1, instr2]

# find R, Q in DB 
# for i from 0 to end Q:
#   for j from 0 to end R:
#       if ( Q[D[i]] == R[A[j]] ) && ( Q[C[i]] == R[B[i]] ):
#           continue
#   Q.append ( new tuple composed by R[A[i]] and R[B[i]] and NULL in others attributes of Q )  


DFs = []
for text in data.splitlines() :
    tree = chp.get_grammar().match(text)
    res = chp.DFParser()
    output = res.visit(tree)
    
    print(type(output))
    DFs.append(output)

for df in DFs :
    print(isTGD(df))

