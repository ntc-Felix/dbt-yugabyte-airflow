from faker.providers import BaseProvider


class MarketProvider(BaseProvider):
    def product(self):
        product_list = ["cheese", "bread", "juice", "soda", "apple", "orange"]
        return self.random_element(product_list)
