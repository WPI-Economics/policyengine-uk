from policyengine_uk.model_api import *


class benunit_equivalisation_bhc(Variable):
    value_type = float
    entity = BenUnit
    label = "Equivalisation factor to account for benunit composition, using BHC factors"
    definition_period = YEAR

    def formula(benunit, period, parameters):
        count_other_adults = max_(
            benunit.sum(benunit.members("is_adult", period)) - 1, 0
        )
        count_young_children = benunit.sum(
            benunit.members("is_young_child", period)
        )
        count_older_children = benunit.sum(
            benunit.members("is_older_child", period)
        )
        return (
            0.67
            + 0.33 * count_other_adults
            + 0.33 * count_older_children
            + 0.2 * count_young_children
        )


class household_sum_of_benunit_equivalisation_bhc(Variable):
    value_type = float
    entity = Household
    label = "Household sum over BenUnit equivalisation factors, for BHC factors."
    definition_period = YEAR

    adds = ["benunit_equivalisation_bhc"]


class benunit_share_of_household_equiv_bhc(Variable):
    value_type = float
    entity = BenUnit
    label = "BenUnit share of equivalisation, for use in allocating Household-level quantities to BenUnit."
    definition_period = YEAR

    def formula(benunit, period, parameters):
        benunit_equivalisation_factor = benunit("benunit_equivalisation_bhc", period)
        household_sum_of_benunit_equivalisation_bhc = benunit.household("household_sum_of_benunit_equivalisation_bhc", period)
        return benunit_equivalisation_factor / household_sum_of_benunit_equivalisation_bhc
    