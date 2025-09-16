from policyengine_uk.model_api import *

class benunit_total_extracost_benefits(Variable):
    type = float
    entity = BenUnit
    label = "Benefit Unit total benefit income from extra cost disability benefits: DLA, PIP, AA, and Scottish disability benefits"
    unit = GBP
    definition_period = YEAR

    # TODO - add the other extra-cost disability benefits

    adds = [
        "dla",
        "pip"
    ]