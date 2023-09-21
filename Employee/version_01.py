class Employee:
    def __init__(self, state):
        self.state = state
        self.pay_calculators = {
            "dead": self.calculate_dead_amount,
            "separated": self.calculate_separated_amount,
            "retired": self.calculate_retired_amount,
            "normal": self.calculate_normal_pay_amount,
        }

    def get_pay_amount(self):
        pay_calculator = self.pay_calculators.get(self.state)
        return pay_calculator()

    def calculate_dead_amount(self):
        # Imagine there is code here for calculating the pay amount for a deceased employee
        return 1

    def calculate_separated_amount(self):
        # Imagine there is code here for calculating the pay amount for a separated employee
        return 0

    def calculate_retired_amount(self):
        # Imagine there is code here for calculating the pay amount for a retired employee
        return 0

    def calculate_normal_pay_amount(self):
        # Imagine there is code here for calculating the normal pay amount for an active employee
        return 0

