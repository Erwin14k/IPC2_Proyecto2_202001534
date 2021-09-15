from Product_Node import Product_Node
class Product_Linked_List:
    def __init__(self):
        self.first = None

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