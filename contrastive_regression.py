from collections.abc import Callable
from pathlib import Path
from typing import Any

from machetli import sas

from properties import Property, InputReadCompletedProperty
from environments import RunEnvironment
from single_regression import Condition


class BiCondition:
    # A condition is something that can be true or
    def evaluate(self, lhs, rhs) -> bool:
        raise NotImplementedError()

class EqualityBiCondition(BiCondition):
    def __init__(self, property: Property | Condition):
        self.property = property

    def evaluate(self, lhs: str, rhs: str) -> bool:
        return self.property.evaluate(lhs) == self.property.evaluate(rhs)

class NotBiCondition(BiCondition):
    def __init__(self, condition: BiCondition):
        self.condition = condition

    def evaluate(self, lhs: str, rhs: str) -> bool:
        return not self.condition.evaluate(lhs, rhs)

class AndCondition(BiCondition):
    def __init__(self, *conditions: BiCondition):
        self.conditions = conditions

    def evaluate(self, lhs: str, rhs: str) -> bool:
        return all(condition.evaluate(lhs, rhs) for condition in self.conditions)

class OrCondition(BiCondition):
    def __init__(self, *conditions: BiCondition):
        self.conditions = conditions

    def evaluate(self, lhs: str, rhs: str) -> bool:
        return any(condition.evaluate(lhs, rhs) for condition in self.conditions)

class LessThanOrEqualCondition(BiCondition):
    def __init__(self, property: Property):
        self.property = property

    def evaluate(self, lhs: str, rhs: str) -> bool:
        return self.property.evaluate(lhs) <= self.property.evaluate(rhs)

class LambdaCondition(BiCondition):
    def __init__(self, property: Property, function: Callable[[Any, Any], bool]):
        self.property = property
        self.function = function

    def evaluate(self, lhs: str, rhs: str) -> bool:
        return self.function(self.property.evaluate(lhs), self.property.evaluate(rhs))
    
class RhsCondition(BiCondition):
    def __init__(self, property: Property | Condition):
        self.property = property

    def evaluate(self, lhs: str, rhs: str) -> bool:
        return self.property.evaluate(rhs)

class LhsCondition(BiCondition):
    def __init__(self, property: Property | Condition):
        self.property = property

    def evaluate(self, lhs: str, rhs: str) -> bool:
        return self.property.evaluate(lhs)

class BothBiCondition(BiCondition):
    def __init__(self, property: Property | Condition):
        self.property = property

    def evaluate(self, lhs: str, rhs: str) -> bool:
        return self.property.evaluate(lhs) and self.property.evaluate(rhs)

def InputReadCompletedCondition() -> BiCondition:
    return BothBiCondition(InputReadCompletedProperty())

class SupersetCondition(BiCondition):
    def __init__(self, property: Property | Condition):
        self.property = property

    def evaluate(self, lhs: str, rhs: str) -> bool:
        lhs_set = set(self.property.evaluate(lhs))
        rhs_set = set(self.property.evaluate(rhs))
        print(f"lhs_set: {lhs_set}")
        print(f"rhs_set: {rhs_set}")
        
        return lhs_set.issuperset(rhs_set)


class ContrastiveRegressionEvaluator:
    # Evaluates the buggy configuration against the ground truth configuration
    def __init__(self, run_env: RunEnvironment, lhs_configuration: str, rhs_configuration: str, conditions: list[BiCondition]):
        self.run_env = run_env
        self.lhs_configuration = lhs_configuration
        self.rhs_configuration = rhs_configuration
        self.conditions = conditions

    def run_evaluator(self):
        def evaluate(sas_file: Path):
            lhs_log = self.run_env.run_planner(sas_file, self.lhs_configuration)
            rhs_log = self.run_env.run_planner(sas_file, self.rhs_configuration)
            return all(
                condition.evaluate(lhs_log.stdout, rhs_log.stdout)
                for condition in self.conditions
            )

        sas.run_evaluator(evaluate)


