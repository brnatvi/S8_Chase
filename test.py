from read_tables import *
from contraintes import *

def main() :
    list = []

    '''tableR = read_table('csv/R.csv', 'R')
    tableP = read_table('csv/P.csv', 'P')
    tableQ = read_table('csv/Q.csv', 'Q')
    
    list.append(tableR)
    list.append(tableP)
    list.append(tableQ)
    '''

    livre = read_table('csv/Livre.csv' , 'Livre')
    auteur = read_table('csv/Auteur.csv' , 'Auteur')
    emprunt = read_table('csv/Emprunt.csv' , 'Emprunt')
    lecteur = read_table('csv/Lecteur.csv' , 'Lecteur')

    list.append(livre)
    list.append(auteur)
    list.append(emprunt)
    list.append(lecteur)
    
    database = DataBase(list)
    print(database)

    print('')

    test = RelAtom(Relation('R'), [Attribut('A'), Attribut('B'), Attribut('C')], [Variable('x'), Variable('y'), Variable('z')])
    print(test)

    print('')

    test2 = EqAtom(Variable('x1'), Variable('x2'))
    print(test2)

    print(test.strVars())



if __name__ == "__main__" :
    main()

