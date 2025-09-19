#! /usr/bin/env python3
from contrastive_regression import *
from environments import LocalPyperplanRunEnvironment
from properties import *


# run_env = LocalProbfdRunEnvironment(Path("~/conan/adversarial/probfd_adversarial/bin/default/release/probfd").expanduser())
run_env = LocalPyperplanRunEnvironment(Path("~/conan/pyperplan").expanduser())
# run_env = MCCCplexRunEnvironment(Path("~/singularity_images/conan-dev-115d23909.img").expanduser())

CONFIGURATION = "-s astar -t factored -H saturatedcostpartitioning --qdom"
WORKING_CONFIGURATION = "-s astar -t factored -H blind"


ContrastiveRegressionEvaluator(run_env, CONFIGURATION, WORKING_CONFIGURATION, [
    RhsCondition(InputReadCompletedProperty()),
    RhsCondition(SolvedProperty()),
    LhsCondition(UnsolvableProperty()),
]).run_evaluator()

