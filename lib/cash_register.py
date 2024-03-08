#!/usr/bin/env python3


# Add items of varying quantities and prices
# Calculate discounts
# Keep track of what's been added to it
# Void the last transaction


# def test_void_last_transaction(self):
#       '''subtracts the last item from the total'''
#       self.cash_register.add_item("apple", 0.99)
#       self.cash_register.add_item("tomato", 1.76)
#       self.cash_register.void_last_transaction()
#       assert(self.cash_register.total == 0.99)
#       self.reset_register_totals()

class CashRegister:

    def __init__(self,discount = 0,total = 0):
        self.total = 0
        self.discount = discount
        self.items = []
        self.items_prices = []
    def rest_regiter_totals(self):
        self.total = 0
    def add_item(self,title,price,quantity = 1):
        self.total += price * quantity
        
        self.items_prices.append(price * quantity)
        for i in range(quantity):
            self.items.append(title)
        

    def apply_discount(self):
        if self.discount:
           total = self.total
           self.total = int(self.total * ((100 - self.discount) / 100))
           print(f"After the discount, the total comes to ${self.total}.")
        
        else:
            print("There is no discount to apply.")

    def void_last_transaction(self):
        items_prices = self.items_prices
        last_item_ind = len(items_prices) - 1
        price_to_deduct = items_prices[last_item_ind]
        self.total -= price_to_deduct

    
   
        
   
  




