from policyengine_uk.model_api import *


class benunit_equivalisation_ahc(Variable):
    value_type = float
    entity = BenUnit
    label = "Equivalisation factor to account for benunit composition, using AHC factors"
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
            0.58
            + 0.42 * count_other_adults
            + 0.42 * count_older_children
            + 0.2 * count_young_children
        )