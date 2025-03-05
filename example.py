#! /usr/bin/env python3
from contrastive_regression import *
from properties import *

REPO = Path("~/conan/conan-dev").expanduser()
PLANNER = REPO / "builds/release_nogcc14/bin/downward"
BUGGY_CONFIGURATION = "astar(goperatorcounting(lpsolver=cplex,constraint_generators=[lmcut_constraints_fts()]))"
GT_CONFIGURATION = "astar(blind())"

ContrastiveRegressionEvaluator(PLANNER, BUGGY_CONFIGURATION, GT_CONFIGURATION, [
    InputReadCompletedCondition(),
    LessThanOrEqualCondition(TypedRegexProperty(r"Expanded (\d+) state\(s\).", int)),
]).run_evaluator()

