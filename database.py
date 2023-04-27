class Type :
    def __init__(self, type) :
        self.type = type

    def __str__(self) :
        return f"{self.type}"
    
    def __eq__(self, another):
        return (self.type == another.type)

class Attribut :
    def __init__(self, nom): # param type ?
        self.nom = nom
        # self.type = type

    def __str__(self):
        return f"{self.nom}"
    
    def __eq__(self, att):
        return (self.nom == att.nom)


class Relation :
    def __init__(self, nom):
        self.nom = nom

    def __str__(self) :
        return f"{self.nom}"
    
    def __eq__(self, another):
        return (self.nom == another.nom)

class Table :
    key = 0
    table = dict()

    def __init__(self, relation, nb_columns, attr_list) :
        self.relation = relation
        self.nb_columns = nb_columns
        self.attr_list = attr_list
        self.table = {}
    
    def insert(self, list) :
        keys = self.table.keys()
        i = 1
        while i in keys :
            i += 1
        self.table[i] = list
        if i == self.key + 1:
            self.key += 1

    def __str__(self) :
        s = ""
        s += str(self.relation)
        s += "["
        
        for i in range(0, len(self.attr_list)) :
            s += str(self.attr_list[i])
            if i == (len(self.attr_list) - 1) :
                s += "]\n"
            else :
                s += ","            
        
        for k in self.table :
            s = s + "(" + ",".join(self.table[k]) + ")\n"
            
        return s
    
    def get_relation(self):
        return self.relation
    
    def get_attribute(self, att_str):
        for el in self.attr_list: 
            if (el.nom == att_str): 
                return el
        print('attribute not found')
        return None 



class DataBase :
    tableList = []     
    
    def __init__(self, list):
        self.tableList = list

    def __str__(self) :
        s = ""
        for table in self.tableList :
            s += table.__str__()
        return s
    
    def add_table(self, table):
        self.tableList.append(table)

    def find_by_relation(self, rel):
        for table in self.tableList:
            if (table.relation == rel):
                return table
        print('relation not found')
        return None
    

