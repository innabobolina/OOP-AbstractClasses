"""Classes for melon orders."""

from random import randint
from datetime import datetime

class AbstractMelonOrder():
    """An abstract base class that other Melon Orders inherit from."""

    def __init__(self, species, qty, order_type, tax):
        """Initialize melon order attributes."""

        self.species = species
        self.qty = qty
        self.shipped = False
        self.order_type = order_type
        self.tax = tax

    def mark_shipped(self):
        """Record the fact than an order has been shipped."""

        self.shipped = True

    def get_base_price(self):

        extra_charge = 0

        if datetime.today().weekday() in range(5) and datetime.now().hour in range(8, 12):
            extra_charge = 4

        print(f'Day: {datetime.today().weekday()}  Hour: {datetime.now().hour}')

        return randint(5, 9) + extra_charge


    def get_total(self):
        """Calculate price, including tax."""

        base_price = self.get_base_price()
        flat_fee = 0
        print("Print base price: ", base_price)

        if self.species == "Christmas":
            base_price = base_price * 1.5

        if self.order_type == "international" and self.qty < 10:
            flat_fee = 3
        
        total = (1 + self.tax) * self.qty * base_price 

        return total + flat_fee 


class GovernmentMelonOrder(AbstractMelonOrder):

    def __init__(self, species, qty):
        super().__init__(species, qty, "domestic", 0)

        self.passed_inspection = False 

    def mark_inspection(self, passed):

        self.passed_inspection = passed 


class DomesticMelonOrder(AbstractMelonOrder):
    """A melon order within the USA."""
    
    def __init__(self, species, qty):
        super().__init__(species, qty, "domestic", 0.08)


class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""

    def __init__(self, species, qty, country_code):
        super().__init__(species, qty, "international", 0.17)
        """Initialize melon order attributes."""
        self.country_code = country_code

    def get_country_code(self):
        """Return the country code."""

        return self.country_code


order1 = DomesticMelonOrder("cantaloupe", 2)
print(order1.get_total())
