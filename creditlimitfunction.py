def calculate_credit_limit(monthly_income, credit_score):
    """
    Calculate a credit limit based on verified monthly income and Experian credit score.
    Ensures monthly repayments (at 2% monthly interest) never exceed 40% of income.

    Parameters:
    - monthly_income (float): Verified monthly income in USD.
    - credit_score (int): FICO credit score (range: 300–850), based on Experian's scale.

    Returns:
    - credit_limit (float): Final approved credit limit, in USD.

    Logic:
    1. Monthly repayment must not exceed 40% of income.
       So: Max Credit Limit = (0.40 * income) / 0.02
    2. This max limit is adjusted *downward* based on credit score risk:
       (based on Experian FICO score bands)

       - 300–579: Very Poor     → 50% of max limit
       - 580–669: Fair          → 70% of max limit
       - 670–739: Good          → 85% of max limit
       - 740–799: Very Good     → 100% of max limit
       - 800–850: Exceptional   → 100% of max limit

    3. No applicant will receive a credit limit that results in payments exceeding 40% of income.

    Example:
    Income = $5,000 → Max limit = $100,000
    Credit Score = 600 → Adjustment = 70%
    Final limit = $70,000
    """

    # Step 1: Calculate the hard cap on credit limit (based on 40% income and 2% monthly interest)
    monthly_interest_rate = 0.02
    max_credit_limit = (0.40 * monthly_income) / monthly_interest_rate

    # Step 2: Apply adjustment factor based on Experian credit score bands
    if credit_score < 580:
        adjustment_factor = 0.5  # Very Poor
    elif credit_score < 670:
        adjustment_factor = 0.7  # Fair
    elif credit_score < 740:
        adjustment_factor = 0.85  # Good
    else:
        adjustment_factor = 1.0  # Very Good or Exceptional

    # Step 3: Final credit limit is adjusted down but never above the max
    final_credit_limit = max_credit_limit * adjustment_factor

    return round(final_credit_limit, 2)

