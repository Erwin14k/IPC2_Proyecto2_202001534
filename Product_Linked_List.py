from Product_Node import Product_Node
import re
class Product_Linked_List:
    def __init__(self):
        self.first = None
        self.product_names_list=""
        self.collected_names=""

    def insert_product(self,product):
        if self.first is None:
            self.first = Product_Node(product=product)
            return
        current= self.first
        while current.next_one:
            current = current.next_one
        current.next_one = Product_Node(product=product)

    def travel(self):
        current = self.first
        while current != None:
            print("Nombre del producto: ",current.product.name," Elaboración: ",current.product.elaboration)
            current = current.next_one
    
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
