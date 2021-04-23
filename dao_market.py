class Market():

    def __init__(self):
        self.products = [
            {"code": "123", "name": "Margarina 200g", "price": 6.2, "quantity": 10},
            {"code": "123", "name": "Margarina 500g", "price": 12.2, "quantity": 30},
            {"code": "124", "name": "Cerveja 500ml", "price": 4, "quantity": 20},
            {"code": "124", "name": "Cerveja 1L", "price": 8, "quantity": 50},
            {"code": "121", "name": "Marcarrão", "price": 2.40, "quantity": 23},
            {"code": "126", "name": "Feijão carioquinha", "price": 6.89, "quantity": 40}]
    
    def get_product_by_code(self, code):
        return list(filter(lambda product: product["code"] == code, self.products))

    def get_amount_products_by_code(self, code):
        list_product = self.get_product_by_code(code)
        list_quantity = list(map(lambda product: product["quantity"], list_product))

        return sum(list_quantity)