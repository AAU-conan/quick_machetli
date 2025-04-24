#! /usr/bin/env python3
from single_regression import *
from environments import *
from properties import *

run_env = LocalRunEnvironment(Path("~/Documents/Phd/conan/conan-dev/builds/release/bin/downward").expanduser())
# run_env = MCCCplexRunEnvironment(Path("~/singularity_images/conan-dev-115d23909.img").expanduser())

CONFIGURATION =  "propagation(eval=propagation_evaluator(eval=blind()))"


SingleRegressionEvaluator(run_env, CONFIGURATION, [
    InputReadCompletedProperty(),
    # SolvedProperty(),
    RegexContainsProperty("Number of iterations: 1000"),
    

    
    
]).run_evaluator()

