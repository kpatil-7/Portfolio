class Effect:
    def __init__(self, delta_money, delta_product_quality, delta_employee_happiness, delta_customer_hapiness):
        # How much money the company starts
        self.delta_money = delta_money
        # Product quality index 0-100
        self.delta_product_quality = delta_product_quality
        # Employee Happiness index 0-100
        self.delta_employee_happiness = delta_employee_happiness
        # Customer Happiness index 0-100
        self.delta_customer_hapiness = delta_customer_hapiness

    def __str__(self):
        to_return = "Effect: " + "\n"
        to_return += "Money: " + str(self.delta_money) + "\t"
        to_return += "Product Quality: " + str(self.delta_product_quality) + "\n"
        to_return += "Employee Happiness: " + str(self.delta_employee_happiness) + "\t"
        to_return += "Customer Happiness: " + str(self.delta_customer_hapiness) + "\n"
        return to_return
