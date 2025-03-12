#! /usr/bin/env python3
from contrastive_regression import *
from environments import *
from properties import *

run_env = LocalRunEnvironment(Path("~/conan/conan-dev/builds/release_nogcc14/bin/downward").expanduser())
# run_env = MCCCplexRunEnvironment(Path("~/singularity_images/conan-dev-115d23909.img").expanduser())

CONFIGURATION = "astar(goperatorcounting(cache_estimates=false,lpsolver=cplex,constraint_generators=[qdom_lmcut()]))"
GT_CONFIGURATION = "astar(lmcut())"


ContrastiveRegressionEvaluator(run_env, CONFIGURATION, GT_CONFIGURATION, [
    RhsCondition(InputReadCompletedProperty()),
    RhsCondition(SolvedProperty()),
    NotBiCondition(EqualityBiCondition(CostProperty())),
]).run_evaluator()

