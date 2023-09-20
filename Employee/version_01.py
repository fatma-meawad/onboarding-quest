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
        pay_calculator = self.pay_calculators.get(self.state, self.calculate_normal_pay_amount)
        return pay_calculator()

    def calculate_dead_amount(self):
        return 0

    def calculate_separated_amount(self):
        return 0

    def calculate_retired_amount(self):
        return 0

    def calculate_normal_pay_amount(self):
        return 0
