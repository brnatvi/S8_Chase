import csv
from database import *

def read_table(filename, table_name) :
    try :
        with open(filename, 'r') as file:
            csvreader = csv.reader(file, delimiter=',')
            attributs = next(csvreader)
            attrList = []
            for a in attributs :
                attrList.append(Attribut(a))
            relation = Relation(table_name)
            table = Table(relation, len(attrList), attrList)
            # TODO check for NULL and empty values 
            for row in csvreader :
                table.insert(row)
            return table
                
            
    except :
        print("Could not read file")

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


if __name__ == "__main__" :
    main()

