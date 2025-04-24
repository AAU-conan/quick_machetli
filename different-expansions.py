#! /usr/bin/env python3
from contrastive_regression import *
from environments import *
from properties import *

#run_env = LocalRunEnvironment(Path("~/Documents/Phd/conan/conan-dev/builds/release/bin/downward").expanduser())
run_env = MCCCplexRunEnvironment(Path("/nfs/home/cs.aau.dk/ny77nw/singularity_images/conan-dev-8802afe1b.img").expanduser())


BUGGY_CONFIGURATION = "propagation(eval=propagation_evaluator(eval=blind()))"
GT_CONFIGURATION = "astar(blind(), pruning=dominance(database=previous_lower_g()))"


ContrastiveRegressionEvaluator(run_env, GT_CONFIGURATION, BUGGY_CONFIGURATION, [
    BothBiCondition(InputReadCompletedProperty()),
    BothBiCondition(SolvedProperty()),
    NotBiCondition(SupersetCondition(RegexAllProperty(r"Expanding state: (.+)"))),
]).run_evaluator()



