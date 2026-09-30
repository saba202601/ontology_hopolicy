"""Transparent demonstration calculations, not a claim adjudicator."""
def hurricane_deductible(dwelling, rate, aop, credit=0, subsequent=False):
    if dwelling <= 0 or not 0 <= rate <= 1 or aop < 0 or credit < 0:
        raise ValueError('Enter positive dwelling and nonnegative deductibles/credit.')
    annual = dwelling * rate
    if credit > annual:
        raise ValueError('Credit cannot exceed the annual hurricane deductible.')
    if credit and not subsequent:
        raise ValueError('Prior credit requires a subsequent hurricane scenario.')
    return max(annual-credit,aop) if subsequent else annual

def letter(data, dwelling, rate, aop):
    return f'''Florida homeowners coverage discussion
Sample correspondence for a fictional policy

Dear {data['homeowner']},

Please review the coverage assumptions for demonstration policy {data['policy_id']}. We should confirm the policy forms, rebuilding cost and flood arrangements before selecting coverage.

The illustrated dwelling limit is ${dwelling:,.0f}. A {rate:.0%} hurricane deductible equals ${dwelling*rate:,.0f}; the illustrated all-other-perils deductible is ${aop:,.0f}. These are demonstration selections, not a quote or confirmation of insurance.

Flood coverage is not included in this demonstration homeowners policy. Please discuss separate flood insurance. Wind damage and flooding require different coverage reviews, even when caused by the same storm.

Please provide the declarations, endorsements, roof information and any recent rebuilding estimate. We also need to confirm personal-property settlement terms and any prior hurricane deductible credit. For subsequent hurricanes in the same calendar year with the same insurer or insurer group, the deductible generally uses the greater of the remaining hurricane deductible and the all-other-perils deductible; insurer verification is needed.

Actual coverage depends on the issued policy, exclusions, conditions and loss facts. This letter does not bind coverage or determine a claim payment.

Sincerely,
Your insurance representative

Reference: Florida Department of Financial Services, Florida's Hurricane Deductible and Homeowners Insurance Overview (accessed September 30, 2026).
'''
