# This class describe the company
import global_vars as G

class Company:
    def __init__(self, money, product_quality, employee_happiness, customer_hapiness):
        # How much money the company starts
        self.money = money
        # Product quality index 0-100
        self.product_quality = product_quality
        # Employee Happiness index 0-100
        self.employee_happiness = employee_happiness
        # Customer Happiness index 0-100
        self.customer_hapiness = customer_hapiness

    def update_status(self, effect):
        self.money += effect.delta_money

        self.product_quality += effect.delta_product_quality
        self.product_quality = max(self.product_quality, 0)
        self.product_quality = min(self.product_quality, 100)

        self.customer_hapiness += effect.delta_customer_hapiness
        self.customer_hapiness = max(self.customer_hapiness, 0)
        self.customer_hapiness = min(self.customer_hapiness, 100)

        self.employee_happiness += effect.delta_customer_hapiness
        self.employee_happiness = max(self.employee_happiness, 0)
        self.employee_happiness = min(self.employee_happiness, 100)

    def status_check(self):
        if self.money <= 0:
            return G.OUT_OF_MONEY
        if self.product_quality == 0:
            return G.PRODUCT_OBSOLETE
        if self.employee_happiness == 0:
            return G.EMPLOYEE_UNHAPPY
        if self.customer_hapiness == 0:
            return G.CUSTOMER_UNHAPPY
        return G.EVERYTHING_OKAY

    def revenue_report(self):
        additional_money = 5000*((self.product_quality/100 + self.customer_hapiness/100 + self.employee_happiness)/3)
        self.money += additional_money
        return additional_money

    def __str__(self):
        to_return = "Company Status: " + "\n"
        to_return += "Money: " + str(self.money) + "\t"
        to_return += "Product Quality: " + str(self.product_quality) + "\n"
        to_return += "Employee Happiness: " + str(self.employee_happiness) + "\t"
        to_return += "Customer Happiness: " + str(self.customer_hapiness) + "\n"
        return to_return
