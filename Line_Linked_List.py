from Line_Node import Line_Node
class Line_Linked_list:
    def __init__(self):
        self.first = None
        self.lines_counter=0
        self.linked_line_components = Line_Components_List()

    def insert_line(self,production_line):
        if self.first is None:
            self.first = Line_Node(production_line=production_line)
            self.lines_counter+=1
            return
        current= self.first
        while current.next_one:
            current = current.next_one
        current.next_one = Line_Node(production_line=production_line)
        self.lines_counter+=1

    def travel(self):
        print("Total De Lineas: ",self.lines_counter)
        print("===========================================================================================")
        current = self.first
        while current != None:
            print("Número de linea: ",current.production_line.number," Componentes: ",current.production_line.components," Tiempo de Ensamblaje: ",current.production_line.time)
            current = current.next_one
        print("===========================================================================================")
        
    def time_by_line(self,line_number):
        current = self.first
        while current and current.production_line.number != line_number:
            current = current.next_one
        return current.production_line.time

class Component:
    def __init__(self,line_number,components):
        self.line_number = line_number
        self.component = components
        self.next = None

class Line_Components_List:
    def __init__(self):
        self.first = None

    def insert(self, line_number,component):
        u=Component(line_number,component)
        if self.first is None: 
            self.first = u
        else:
            actual=self.first
        while actual.next != None: 
            actual=actual.next
        actual.next = u
