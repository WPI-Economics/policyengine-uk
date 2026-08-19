from policyengine_uk.model_api import *

HBAI_NET_INCOME_ELEMENTS = [
    "employment_income", #Person
    "self_employment_income", #Person
    "savings_interest_income", #Person
    "dividend_income", #Person
    "miscellaneous_income", #Person
    "property_income", #Person
    "private_pension_income", #Person
    "private_transfer_income", #Person
    "maintenance_income", #Person
    "free_school_meals", #Person
    "free_school_fruit_veg", #Person
    "free_school_milk", #Person
    "child_benefit", #BenUnit
    "council_tax_benefit", #BenUnit
    "esa_income", #BenUnit
    "esa_contrib", #Person
    "housing_benefit", #BenUnit
    "income_support", #BenUnit
    "jsa_income", #BenUnit
    "jsa_contrib", #Person
    "pension_credit", #BenUnit
    "universal_credit", #BenUnit
    "working_tax_credit", #BenUnit
    "child_tax_credit", #BenUnit
    "attendance_allowance", #Person
    "afcs", #Person
    "bsp", #Person
    "carers_allowance", #Person
    "dla", #Person
    "iidb", #Person
    "incapacity_benefit", #Person
    "pip", #Person
    "sda", #Person
    "state_pension", #Person
    "maternity_allowance", #Person
    "statutory_sick_pay", #Person
    "statutory_maternity_pay", #Person
    "ssmg", #Person
    "tax_free_childcare", #Person
    "healthy_start_vouchers", #Person
    # Reference for tax-free-childcare: https://assets.publishing.service.gov.uk/media/5e7b191886650c744175d08b/households-below-average-income-1994-1995-2018-2019.pdf
]

HBAI_HOUSEHOLD_ELEMENTS_TO_ALLOCATE = [
    "free_tv_licence_value",
    "cost_of_living_support_payment",
    "winter_fuel_allowance"
]

HBAI_NET_INCOME_DEDUCTIONS = [
    "income_tax", #Person
    "national_insurance", #Person
    "student_loan_repayments", #Person
    "employee_pension_contributions", #Person
    "personal_pension_contributions", #Person
    "maintenance_expenses", #Person
]

HBAI_HOUSEHOLD_DEDUCTIONS_TO_ALLOCATE = [
    "council_tax",
    "domestic_rates",
    "external_child_payments"
]

class hbai_benunit_net_income(Variable):
    value_type = float
    entity = BenUnit
    label = "Benefit Unit net income (HBAI definition)"
    documentation = "Disposable income for the benefit unit, following the definition used for official poverty statistics"
    unit = GBP
    definition_period = YEAR

    def formula(benunit, period, parameters):

        benunit_share_of_household = benunit("benunit_share_of_household_equiv_bhc", period)

        net_household_allocations = sum([benunit.household(v, period) for v in HBAI_HOUSEHOLD_ELEMENTS_TO_ALLOCATE]
                                    ) - sum([benunit.household(v, period) for v in HBAI_HOUSEHOLD_DEDUCTIONS_TO_ALLOCATE])
        
        return benunit_share_of_household * net_household_allocations + add(benunit, period, HBAI_NET_INCOME_ELEMENTS) - add(benunit, period, HBAI_NET_INCOME_DEDUCTIONS)
