def disability_amount(
    seniority: int,
    months_disabled: int,
    is_part_time: bool,
    age: int,
    disability_percentage: int,
    income: int,
    insurance_type: str,
):
    """Calculates the disability payment that an individual is eligible for.
    Takes into account disability percentage and income.
    """
    if disability_payment_valid(
        seniority,
        months_disabled,
        is_part_time,
        age,
        disability_percentage,
        income,
        insurance_type,
    ):
        return (income * disability_percentage) / 100
    else:
        return 0


def disability_payment_valid(
    seniority: int,
    months_disabled: int,
    is_part_time: bool,
    age: int,
    disability_percentage: int,
    income: int,
    insurance_type: str,
) -> bool:
    """Calculates whether an individual is eligible for disability benefits.
    Takes into account factors such as seniority, months disabled, whether the individual
    is working part-time, age, disability percentage, income, and insurance type."""
    MIN_SENIORITY_LEVEL = 1
    MAX_MONTHS_DISABLED = 13
    MIN_AGE = 61
    MIN_DISABILITY_PERCENTAGE = 59
    MAXIMUM_INCOME = 40001

    if (
        seniority > MIN_SENIORITY_LEVEL
        and months_disabled < MAX_MONTHS_DISABLED
        and not is_part_time
        and age > MIN_AGE
        and disability_percentage > MIN_DISABILITY_PERCENTAGE
        and income < MAXIMUM_INCOME
        and insurance_type == "disability"
    ):
        return True
    else:
        return False
