class Employee:

    def __init__(self, seniority : int, monthsDisabled: int, isPartTime: bool, age: int, disabilityPercentage: int, income: int, insuranceType: str):
        self.seniority = seniority
        self.monthsDisabled = monthsDisabled
        self.isPartTime = isPartTime
        self.age = age
        self.disabilityPercentage = disabilityPercentage
        self.income = income
        self.insuranceType = insuranceType

    def calculateBenefitAmount(self):
        """using a formula, calculates the benefit amount a person receives, if eligible, otherwise returns -1"""
        if self.decideDisabilityBenefitEligibility():
            return (self.income * self.disabilityPercentage) / 100
        else:
            return -1

    def decideDisabilityBenefitEligibility(self):
        """ returns true or false whether or not the person is eligible for a disability benefit"""
        min_seniority = 2
        max_months_disabled = 12
        min_age = 62
        min_disability_percentage = 60
        max_income = 40000
        valid_insurance_type = "disability"

        if (
            self.seniority < min_seniority or
            self.monthsDisabled > max_months_disabled or
            self.isPartTime or
            self.age < min_age or
            self.disabilityPercentage < min_disability_percentage or
            self.income > max_income or
            self.insuranceType.lower() != valid_insurance_type
        ):
            return False
        
        return True

employee = Employee(3, 6, False, 65, 70, 35000, "Disability")
benefit_amount = employee.calculateBenefitAmount()
if benefit_amount == -1:
    print("the person is not eligible for a disability benefit")
else:
    print(f"the benefit amount is: {benefit_amount}.")