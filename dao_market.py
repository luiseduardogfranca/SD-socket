class Market():

    def __init__(self):
        self.products = [
            {"code": "123", "name": "Margarina 200g", "price": 6.2, "quantity": 10},
            {"code": "122", "name": "Margarina 500g", "price": 12.2, "quantity": 30},
            {"code": "127", "name": "Cerveja 500ml", "price": 4, "quantity": 20},
            {"code": "124", "name": "Cerveja 1L", "price": 8, "quantity": 50},
            {"code": "121", "name": "Marcarrão", "price": 2.40, "quantity": 23},
            {"code": "126", "name": "Feijão carioquinha", "price": 6.89, "quantity": 40}]

    def get_product_by_code(self, code):
        query = list(filter(lambda product: product["code"] == code, self.products))

        return query[-1] if len(query) > 0 else None
    
    def add_product(self, product): 
        if ("code" in product and "name" in product and "price" in product and "quantity" in product):
            self.products.append(product)
            return True
        return False

    def remove_product(self, code): 
        new_product_arr = list(filter(lambda product: product["code"] != code, self.products))
        is_removed = True if len(new_product_arr) < len(self.products) else False
        self.products = new_product_arr
        return is_removed