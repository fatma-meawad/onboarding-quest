def disabilityAmount(seniority: int, monthsDisabled: int, isPartTime: bool, age: int, disabilityPercentage: int, income: int, insuranceType: str):
    """Calculates the disability payment that an individual is eligible for.
    Takes into account disability percentage and income.
    """
    if disabilityPaymentValid(seniority, monthsDisabled, isPartTime, age, disabilityPercentage, income, insuranceType):
        return (income * disabilityPercentage) / 100
    else:
        return 0
    
def disabilityPaymentValid(seniority: int, monthsDisabled: int, isPartTime: bool, age: int, disabilityPercentage: int, income: int, insuranceType: str) -> bool:
    """Calculates whether an individual is eligible for disability benefits. 
    Takes into account factors such as seniority, months disabled, whether the individual
    is working part-time, age, disability percentage, income, and insurance type. """
    MIN_SENIORITY_LEVEL = 1 
    MAX_MONTHS_DISABLED = 13
    MIN_AGE = 61
    MIN_DISABILITY_PERCENTAGE = 59
    MAXIMUM_INCOME = 40001

    if (seniority > MIN_SENIORITY_LEVEL
        and monthsDisabled < MAX_MONTHS_DISABLED 
        and not isPartTime 
        and age > MIN_AGE
        and disabilityPercentage > MIN_DISABILITY_PERCENTAGE 
        and income < MAXIMUM_INCOME
        and insuranceType == "disability"):
        return True
    else:
        return False