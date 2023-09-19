class Employee:
    def __init__(
        self,
        seniority: int,
        months_disabled: int,
        is_part_time: bool,
        age: int,
        disability_percentage: int,
        income: int,
        insurance_type: str,
    ):
        self.seniority = seniority
        self.months_disabled = months_disabled
        self.is_part_time = is_part_time
        self.age = age
        self.disability_percentage = disability_percentage
        self.income = income
        self.insurance_type = insurance_type

    def calculate_benefit_amount(self):
        """using a formula, calculates the benefit amount a person receives, if eligible, otherwise returns -1"""
        if self.decide_disability_benefit_eligibility():
            return (self.income * self.disability_percentage) / 100
        else:
            return -1

    def decide_disability_benefit_eligibility(self):
        """returns true or false whether or not the person is eligible for a disability benefit"""
        min_seniority = 2
        max_months_disabled = 12
        min_age = 62
        min_disability_percentage = 60
        max_income = 40000
        valid_insurance_type = "disability"

        if (
            self.seniority < min_seniority
            or self.months_disabled > max_months_disabled
            or self.is_part_time
            or self.age < min_age
            or self.disability_percentage < min_disability_percentage
            or self.income > max_income
            or self.insurance_type.lower() != valid_insurance_type
        ):
            return False

        return True


employee = Employee(3, 6, False, 65, 70, 35000, "Disability")
benefit_amount = employee.calculate_benefit_amount()
if benefit_amount == -1:
    print("the person is not eligible for a disability benefit")
else:
    print(f"the benefit amount is: {benefit_amount}.")
