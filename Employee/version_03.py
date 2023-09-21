class Employee:
    def __init__(self, is_dead, is_separated, is_retired):
        self.state = (
            is_dead * "DEAD"
            or is_separated * "SEPARATED"
            or is_retired * "RETIRED"
            or "NORMAL"
        )
        self.pay_states = {
            "DEAD": self.calculate_dead_amount,
            "SEPARATED": self.calculate_separated_amount,
            "RETIRED": self.calculate_retired_amount,
            "NORMAL": self.calculate_normal_pay_amount,
        }

    def get_pay_amount(self):
        return self.pay_states[self.state]()

    def calculate_dead_amount(self):
        # code to calculate the pay amount for a deceased employee
        return 5

    def calculate_separated_amount(self):
        # code to calculate the pay amount for a separated employee
        return 1

    def calculate_retired_amount(self):
        # code to calculate the pay amount for a retired employee
        return 2

    def calculate_normal_pay_amount(self):
        # code to calculate the normal pay amount for an active employee
        return 3


employee = Employee(is_dead=False, is_separated=False, is_retired=False)
print(employee.get_pay_amount())
