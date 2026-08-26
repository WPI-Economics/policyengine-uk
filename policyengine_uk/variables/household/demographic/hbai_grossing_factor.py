from policyengine_uk.model_api import *

class hbai_grossing_factor(Variable):
    value_type = int
    entity = Household
    label = "Household HBAI grossing factor"
    documentation = "HBAI has different grossing factors (weights) to FRS because it is only defined on a sub-sample of the broader FRS sample" \
                    "This variable includes (nonzero) HBAI grossing factors for FRS households that are in HBAI, and zero for those that are not."
    definition_period = YEAR
