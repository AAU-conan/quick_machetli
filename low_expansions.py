#! /usr/bin/env python3
from contrastive_regression import *
from environments import *
from properties import *
from single_regression import SingleRegressionEvaluator

run_env = LocalRunEnvironment(Path("~/conan/conan-dev/builds/release_nogcc14/bin/downward").expanduser())
# run_env = MCCCplexRunEnvironment(Path("~/singularity_images/conan-dev-115d23909.img").expanduser())

CONFIGURATION = "astar(lmcut())"

SingleRegressionEvaluator(run_env, CONFIGURATION, [
    InputReadCompletedProperty(),
    SolvedProperty(),
]).run_evaluator()

