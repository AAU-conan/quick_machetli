#! /usr/bin/env python3
from contrastive_regression import *
from environments import *
from properties import *

run_env = LocalRunEnvironment(Path("~/Documents/Phd/conan/conan-dev/builds/release/bin/downward").expanduser())
# run_env = MCCCplexRunEnvironment(Path("~/singularity_images/conan-dev-115d23909.img").expanduser())

CONFIGURATION = "propagation(eval=propagation_evaluator(eval=blind()))"
GT_CONFIGURATION = "astar(blind(), pruning=dominance(database=previous_lower_g()))"


ContrastiveRegressionEvaluator(run_env, CONFIGURATION, GT_CONFIGURATION, [
    RhsCondition(InputReadCompletedProperty()),
    RhsCondition(SolvedProperty()),
    LhsCondition(UnsolvableProperty()),
]).run_evaluator()

