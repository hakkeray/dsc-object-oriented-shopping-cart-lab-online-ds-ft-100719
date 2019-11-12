class ShoppingCart:

    def __init__(self, emp_discount=None):
        self.employee_discount = None
        self.items = []
        self.total = 0


    def add_item(self, name, price, quantity=1):
       for i in list(range(quantity)):
           self.items.append({'name': name, 'price':price})
           self.total += price
       return self.total


    def mean_item_price(self):
        num_items = len(self.items)
        total = self.total
        mean = total/num_items
        return mean


    def median_item_price(self):
        prices = [item['price'] for item in self.items]
        length = len(prices)
        if (length%2 == 0):
            med_one = int(length/2)
            med_two = med_one - 1
            median = (prices[med_one] + prices[med_two])/2
            return median
        med = int(length/2)
        return prices[med]



    def apply_discount(self):
        if self.employee_discount:
           discount = self.employee_discount/100
           disc_total = self.total * (1 - discount)
           return disc_total
        else:
            return "Sorry, there is no discount to apply to your cart :("



    def void_last_item(self):
        if self.items:
            removed_item = self.items.pop()
        else:
            return "There are no items in your cart!"
        self.total -= removed_item['price']
