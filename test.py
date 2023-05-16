from read_tables import *
from contraintes import *
import chase_parser as chp
import chase as ch

def main() :
    list = []

    tableR = read_table('csv/R.csv', 'R')
    tableP = read_table('csv/P.csv', 'P')
    tableQ = read_table('csv/Q.csv', 'Q')
    
    list.append(tableR)
    list.append(tableP)
    list.append(tableQ)
    

   # livre = read_table('csv/Livre.csv' , 'Livre')
   # auteur = read_table('csv/Auteur.csv' , 'Auteur')
   # emprunt = read_table('csv/Emprunt.csv' , 'Emprunt')
   # lecteur = read_table('csv/Lecteur.csv' , 'Lecteur')



   # list.append(livre)
   # list.append(auteur)
   # list.append(emprunt)
   # list.append(lecteur)
    
    database = DataBase(list)
    print(database)

    
   # contr1 = str("Emprunt(x1,x2) -> Livre(x2,y1,z1) and Lecteur(x1)\n")
   # contr2 = str("Livre(x1,x2,x3) -> Auteur(x2,y,z)\n")



   # contr3 = str("Livre(x1,y1,z1) and Livre(x2,y2,z2) and x1=x2 -> y1=y2\n")
   # list_instr3 = ch.create_instructions(contr3, database)
        
   
  #  DFs = []
  #
  #  for text in data.splitlines() :
  #      tree = chp.get_grammar().match(text)
  #      res = chp.DFParser()
  #      output = res.visit(tree) 
  #      DFs.append(output)
  #  
  #  for df in DFs :
  #      print(ch.isTGD(df))
  #



    contr1 = str("R(x1,x2) -> Q(x2,x1,x3)\n")  
    contr2 = str("Q(y1,x1,y2) -> P(x1,z1)\n")
    list_instr1 = ch.create_instructions(contr1, database)
    list_instr2 = ch.create_instructions(contr2, database)

    ch.apply_TGD(list_instr1, database)
    ch.apply_TGD(list_instr2, database)
    


if __name__ == "__main__" :
    main()

