#!/usr/bin/env python3

from pathlib import Path
from typing import Callable, Any

from machetli import sas
from properties import Property
from run_planner import run_planner


class Condition:
    def evaluate(self, log: str) -> bool:
        raise NotImplementedError()

class IsTrueCondition(Condition):
    def __init__(self, property: Property):
        self.property = property

    def evaluate(self, log: str) -> bool:
        return self.property.evaluate(log)

class LambdaCondition(Condition):
    def __init__(self, function: Callable[[...], bool], *properties: Property):
        self.function = function
        self.properties = properties

    def evaluate(self, log: str) -> bool:
        return self.function(*[p.evaluate(log) for p in self.properties])

class SingleRegressionEvaluator:
    # Evaluates the buggy configuration against the ground truth configuration
    def __init__(self, planner: Path, configuration: str, conditions: list[Condition]):
        self.planner = planner
        self.configuration = configuration
        self.conditions = conditions

    def run_evaluator(self):
        def evaluate(sas_file: Path):
            log = run_planner(sas_file, self.planner, self.configuration)
            return all(
                condition.evaluate(log.stdout)
                for condition in self.conditions
            )

        sas.run_evaluator(evaluate)
