class Product_Node:
    def __init__(self, product=None, next_one=None):
        self.product = product
        self.next_one = next_one 

class Elaboration_Node:
    def __init__(self, elaboration=None,product_name=None,next_one=None):
        self.elaboration = elaboration
        self.product_name=product_name
        self.next_one = next_one 
