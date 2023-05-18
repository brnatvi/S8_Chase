from read_tables import *
from contraintes import *
import chase_parser as chp
import chase as ch

def main() :
    list = []

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
 

    contr3 = str("Livre(x1,y1,z1) and Livre(x2,y2,z2) and x1=x2 -> y1=y2\n")
    list_instr3 = ch.create_instructions(contr3, database)
    ch.apply_EGD(list_instr3, database)


    
if __name__ == "__main__" :
    main()
