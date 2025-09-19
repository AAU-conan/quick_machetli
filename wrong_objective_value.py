#! /usr/bin/env python3
from contrastive_regression import ContrastiveRegressionEvaluator, LhsCondition, BothBiCondition, RhsCondition
from environments import *
from properties import *
from single_regression import LambdaCondition

run_env = LocalProbfdRunEnvironment(Path("~/conan/adversarial/probfd_adversarial/bin/default/release/probfd").expanduser())
# run_env = MCCCplexRunEnvironment(Path("~/singularity_images/conan-dev-115d23909.img").expanduser())

CONFIGURATION = "lilao()"
WORKING_CONFIGURATION = "ilao()"


ContrastiveRegressionEvaluator(run_env, CONFIGURATION, WORKING_CONFIGURATION, [
    BothBiCondition(InputReadCompletedProperty()),
    BothBiCondition(RegexContainsProperty(r"Objective value for the initial state lies within the interval")),
    LhsCondition(LambdaCondition(lambda e: e is not None and e <= 2, TypedRegexProperty(r"Expanded state\(s\): (\d+)", int))),
    RhsCondition(LambdaCondition(lambda e: e is not None and e >= 30, TypedRegexProperty(r"Expanded state\(s\): (\d+)", int))),
]).run_evaluator()

