import chase_parser as chp
from contraintes import *
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

def create_instructions(str_dfs, database):
    instructions = []

    for text in str_dfs.splitlines() :
        tree = chp.get_grammar().match(text)
        res = chp.DFParser()
        output = res.visit(tree) 
        output.complete_attributes(database)        
        print(output)
        instructions = instructions + output.create_instructions_TGD()

    return instructions


def apply_TGD(list_instr, database: DataBase):
    for instr in list_instr:
        print('Instruction : ' + str(instr))

        tableFrom = database.find_table_by_relation(instr.fromRel)
        tableTo = database.find_table_by_relation(instr.toRel)
        columnFrom = instr.fromAttr        
        columnTo = instr.toAttr

        for i in range(1, len(tableFrom.table) + 1):
            isFound = False
            for j in range(1, len(tableTo.table) + 1):
                if ( tableFrom.table[i][columnFrom] == tableTo.table[j][columnTo] ):                   
                    isFound = True
                    break

            if not isFound:                

                print('\n\nNot found ' + str(tableFrom.table[i][columnFrom]) + ' last was ' + str(tableTo.table[j][columnTo]))
                
                if ( None == tableFrom.table[i][columnFrom] ):
                    print('TODO need to try to find fields = None?')


                nbCol = tableTo.nb_columns
                newItem = []              

                for k in range(0, nbCol):
                    if columnTo == k:                        
                        newItem.append(tableFrom.table[i][columnFrom])

                    else:
                        newItem.append(None)

                tableTo.insert(newItem)

                print('Modified table :')
                print(tableTo)

