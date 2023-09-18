def disabilityAmount(seniority: int, monthsDisabled: int, isPartTime: bool, age: int, disabilityPercentage: int, income: int, insuranceType: str):
    """Calculates the amount of disability benefits that an individual is eligible for.
    Takes into account factors such as seniority, months disabled, whether the individual
    is working part-time, age, disability percentage, income, and insurance type.
    """
    if seniority < 2 or monthsDisabled > 12 or isPartTime or age < 62 or disabilityPercentage < 60 or income > 40000 or insuranceType != "disability":
        return 0
    else:
        # If all conditions are met, calculate the benefit amount based on a formula
        benefitAmount = (income * disabilityPercentage) / 100
        return benefitAmount