#! /usr/bin/env python3
from properties import *
from single_regression import *

REPO = Path("~/conan/conan-dev").expanduser()
PLANNER = REPO / "builds/release_nogcc14/bin/downward"
CONFIGURATION = "astar(blind())"

SingleRegressionEvaluator(PLANNER, CONFIGURATION, [
    InputReadCompletedProperty(),
    SolvedProperty(),
    LambdaCondition(lambda x: x >= 100, TypedRegexProperty(r"Expanded (\d+) state\(s\).", int)),
]).run_evaluator()

