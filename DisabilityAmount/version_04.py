def disability_amount(
    seniority: int,
    months_disabled: int,
    is_part_time: bool,
    age: int,
    disability_percentage: int,
    income: int,
    insurance_type: str,
):
    """Calculates the amount of disability benefits that an individual is eligible for.
    Takes into account factors such as seniority, months disabled, whether the individual
    is working part-time, age, disability percentage, income, and insurance type.
    """
    no_benefit = {
        "maxSeniority": 2,
        "maxMonthsDisabled": 12,
        "partTimeJobStatus": True,
        "maxAge": 62,
        "maxDisabilityPercentage": 60,
        "minIncome": 40000,
        "BenefitInsuranceType": "disability",
    }

    if seniority < no_benefit["maxSeniority"]:
        return 0
    if months_disabled > no_benefit["maxMonthsDisabled"]:
        return 0
    if is_part_time == no_benefit["partTimeJobStatus"]:
        return 0
    if age < no_benefit["maxAge"]:
        return 0
    if disability_percentage < no_benefit["maxDisabilityPercentage"]:
        return 0
    if income > no_benefit["minIncome"]:
        return 0
    if insurance_type != no_benefit["BenefitInsuranceType"]:
        return 0
    # If all conditions are met, calculate the benefit amount based on a formula
    benefit_amount = (income * disability_percentage) / 100
    return benefit_amount
