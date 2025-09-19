#! /usr/bin/env python3
from contrastive_regression import *
from environments import *
from properties import *

# run_env = LocalRunEnvironment(Path("~/conan/conan-dev/builds/release_nogcc14/bin/downward").expanduser())
run_env = LocalPyperplanRunEnvironment(Path("~/conan/pyperplan").expanduser())
# run_env = MCCCplexRunEnvironment(Path("~/singularity_images/conan-dev-115d23909.img").expanduser())

CONFIGURATION = "-s astar -t factored -H optimalcostpartitioning"
WORKING_CONFIGURATION = "-s astar -t factored -H saturatedcostpartitioning"


ContrastiveRegressionEvaluator(run_env, CONFIGURATION, WORKING_CONFIGURATION, [
    RhsCondition(InputReadCompletedProperty()),
    RhsCondition(SolvedProperty()),
    NotBiCondition(EqualityBiCondition(CostProperty())),
]).run_evaluator()

