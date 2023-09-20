class Employee:
    def __init__(self, is_dead, is_separated, is_retired):
        self.isDead = is_dead
        self.isSeparated = is_separated
        self.isRetired = is_retired
        self.pay_calculation_methods = {
            (True, False, False): self.calculate_dead_amount,
            (False, True, False): self.calculate_separated_amount,
            (False, False, True): self.calculate_retired_amount,
            (False, False, False): self.calculate_normal_pay_amount
        }

    def get_pay_amount(self):
        return self.pay_calculation_methods.get(
            (self.isDead, self.isSeparated, self.isRetired),
            self.calculate_normal_pay_amount
        )()

    def calculate_dead_amount(self):
        # Imagine there is code here for calculating the pay amount for a deceased employee
        return 0

    def calculate_separated_amount(self):
        # Imagine there is code here for calculating the pay amount for a separated employee
        return 0

    def calculate_retired_amount(self):
        # Imagine there is code here for calculating the pay amount for a retired employee
        return 0

    def calculate_normal_pay_amount(self):
        # Imagine there is code here for calculating the normal pay amount for an active employee
        return 0
