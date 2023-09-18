def disabilityAmount(seniority: int, monthsDisabled: int, isPartTime: bool, age: int, disabilityPercentage: int, income: int, insuranceType: str):
    """Calculates the amount of disability benefits that an individual is eligible for.
    Takes into account factors such as seniority, months disabled, whether the individual
    is working part-time, age, disability percentage, income, and insurance type.
    """
    if seniority < 2:
        return 0
    if monthsDisabled > 12:
        return 0
    if isPartTime:
        return 0
    if age < 62:
        return 0
    if disabilityPercentage < 60:
        return 0
    if income > 40000:
        return 0
    if insuranceType != "disability":
        return 0
    # If all conditions are met, calculate the benefit amount based on a formula
    benefitAmount = (income * disabilityPercentage) / 100
    return benefitAmount