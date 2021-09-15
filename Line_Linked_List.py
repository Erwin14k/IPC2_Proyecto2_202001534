from Line_Node import Line_Node
class Line_Linked_list:
    def __init__(self):
        self.first = None

    def insert_line(self,production_line):
        if self.first is None:
            self.first = Line_Node(production_line=production_line)
            return
        current= self.first
        while current.next_one:
            current = current.next_one
        current.next_one = Line_Node(production_line=production_line)

    def travel(self):
        current = self.first
        while current != None:
            print("Número de linea: ",current.production_line.number," Componentes: ",current.production_line.components," Tiempo: ",current.production_line.time)
            current = current.next_one
    
    
