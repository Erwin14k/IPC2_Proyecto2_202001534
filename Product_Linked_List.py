from Product_Node import Elaboration_Node, Product_Node
import re
class Product_Linked_List:
    def __init__(self):
        self.first = None
        self.product_names_list=""
        self.collected_names=""
        self.products_counter=0

    def insert_product(self,product):
        if self.first is None:
            self.first = Product_Node(product=product)
            self.products_counter+=1
            return
        current= self.first
        while current.next_one:
            current = current.next_one
        current.next_one = Product_Node(product=product)
        self.products_counter+=1

    def travel(self):
        print("Total Productos: ",self.products_counter)
        print("===========================================================================================")
        current = self.first
        while current != None:
            print("Nombre del producto: ",current.product.name," Elaboración: ",current.product.elaboration)
            current = current.next_one
        print("===========================================================================================")
    
    
    def product_name_list_collector(self):
        self.collected_names=""
        temp_buffer=""
        state=0
        self.product_names_list=""
        current = self.first
        while current != None:
            self.product_names_list+=(current.product.name+",")
            current = current.next_one
        self.product_names_list+="$"
        for c in self.product_names_list:
            if state==0:
                if re.search('[a-z]', c) or re.search('[A-Z]', c) or c.isdigit() or c==" ":
                    self.collected_names+=c
                elif c==",":
                    state=1
                elif c=="$":
                    break
                else:
                    temp_buffer=""
            if state==1:
                if c==",":
                    temp_buffer=""
                    temp_buffer+=c
                elif  re.search('[a-z]', c) or re.search('[A-Z]', c) or c.isdigit() or c==" ":
                    self.collected_names+=temp_buffer
                    self.collected_names+=c
                    temp_buffer=""
                else:
                    state=0
        print(self.collected_names)


    def product_elaboration(self,name):
        current = self.first
        while current and current.product.name != name:
            current = current.next_one
        return current.product.elaboration

    def product_component(self,name):
        current = self.first
        while current and current.product.name != name:
            current = current.next_one
        return current.product.elaboration


    def verify_component_line(self,name,component):
        current = self.first
        while current and current.product.name != name:
            current = current.next_one

class Elaboration_Linked_List:
    def __init__(self):
        self.first = None
        

    def insert_elaboration(self,elaboration,product_name):
        if self.first is None:
            self.first = Elaboration_Node(elaboration=elaboration,product_name=product_name)
            return
        current= self.first
        while current.next_one:
            current = current.next_one
        current.next_one = Elaboration_Node(elaboration=elaboration,product_name=product_name)
    def travel(self):
        print("===========================================================================================")
        current = self.first
        while current != None:
            print("Elaboración del producto: ",current.elaboration," Producto: ",current.product_name)
            current = current.next_one
        print("===========================================================================================")

    
    


