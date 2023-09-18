def disabilityAmount(seniority: int, monthsDisabled: int, isPartTime: bool, age: int, disabilityPercentage: int, income: int, insuranceType: str):
    """Calculates the amount of disability benefits that an individual is eligible for.
    Takes into account factors such as seniority, months disabled, whether the individual
    is working part-time, age, disability percentage, income, and insurance type.
    """
    noBenefit = {
      "maxSeniority": 2,
      "maxMonthsDisabled": 12,
      "partTimeJobStatus": True,
      "maxAge": 62,
      "maxDisabilityPercentage": 60,
      "minIncome": 40000,
      "BenefitInsuranceType": "disability"
    }
    
    if seniority < noBenefit["maxSeniority"]:
        return 0
    if monthsDisabled > noBenefit["maxMonthsDisabled"]:
        return 0
    if isPartTime == noBenefit["partTimeJobStatus"]:
        return 0
    if age < noBenefit["maxAge"]:
        return 0
    if disabilityPercentage < noBenefit["maxDisabilityPercentage"]:
        return 0
    if income > noBenefit["minIncome"]:
        return 0
    if insuranceType != noBenefit["BenefitInsuranceType"]:
        return 0
    # If all conditions are met, calculate the benefit amount based on a formula
    benefitAmount = (income * disabilityPercentage) / 100
    return benefitAmount