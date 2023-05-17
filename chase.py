import chase_parser as chp
from contraintes import *
from database import *



def isTGD(df : DF) :             # TODO it is more logical to place this function into DF class
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

        if (isTGD(output)):
            instructions = instructions + output.create_instructions_TGD()

        elif(output.is_EGD()) :
            instructions = instructions + [output.create_instructions_EGD()]

    return instructions


def apply_TGD(list_instr, database: DataBase):

    makeMerge = False
    for instr in list_instr:
        if (len(instr) == 1):

            print('Instruction : ' + str(instr[0]))
            tableFrom = database.find_table_by_relation(instr[0].fromRel)
            tableTo = database.find_table_by_relation(instr[0].toRel)
            columnFrom = instr[0].fromAttr        
            columnTo = instr[0].toAttr

            for i in range(1, len(tableFrom.table) + 1):
                isFound = False
                for j in range(1, len(tableTo.table) + 1):
                    if ( tableFrom.table[i][columnFrom] == tableTo.table[j][columnTo] ):                   
                        isFound = True
                        break

                if not isFound:
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

        
        else: # list of instructions on the same relations  -> need to merge results
            resInstructions = []

            for inst in instr:
                print('Instruction : ' + str(inst))
                tableFrom = database.find_table_by_relation(inst.fromRel)
                tableTo = database.find_table_by_relation(inst.toRel)
                columnFrom = inst.fromAttr        
                columnTo = inst.toAttr

                for i in range(1, len(tableFrom.table) + 1):
                    isFound = False
                    for j in range(1, len(tableTo.table) + 1):
                        if ( tableFrom.table[i][columnFrom] == tableTo.table[j][columnTo] ):                   
                            isFound = True
                            break

                    if not isFound:
                        nbCol = tableTo.nb_columns
                        newItem = []              

                        for k in range(0, nbCol):
                            if columnTo == k:                        
                                newItem.append(tableFrom.table[i][columnFrom])

                            else:
                                newItem.append(None)
                        
                        resInstructions.append(newItem)
                       

            chunks = [resInstructions[i:i + len(instr)] for i in range(0, len(resInstructions), len(instr))]
            
            for i in range(len(chunks[0])):
                toInsert = [None]*len(chunks[0][0])
                for j in range(len(chunks)):                    
                    for k in range(len(resInstructions[0])):
                        if chunks[j][i][k] != None:                
                            toInsert[k] = chunks[j][i][k]
                
                tableTo.insert(toInsert)
            print('Modified table :')
            print(tableTo)



def apply_EGD(instr_EGD: InstructionEGD, database: DataBase):
    
    print('\nInstruction EGD : ' + str(instr_EGD[0]) + '\n\n')
