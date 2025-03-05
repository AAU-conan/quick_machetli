from collections.abc import Callable
from pathlib import Path
from typing import Any

from machetli import sas

from properties import Property, InputReadCompletedProperty
from run_planner import run_planner


class ContrastiveCondition:
    # A condition is something that can be true or
    def evaluate(self, lhs, rhs) -> bool:
        raise NotImplementedError()

class EqualityCondition(ContrastiveCondition):
    def __init__(self, property: Property):
        self.property = property

    def evaluate(self, lhs: str, rhs: str) -> bool:
        return self.property.evaluate(lhs) == self.property.evaluate(rhs)

class NotCondition(ContrastiveCondition):
    def __init__(self, condition: ContrastiveCondition):
        self.condition = condition

    def evaluate(self, lhs: str, rhs: str) -> bool:
        return not self.condition.evaluate(lhs, rhs)

class AndCondition(ContrastiveCondition):
    def __init__(self, *conditions: ContrastiveCondition):
        self.conditions = conditions

    def evaluate(self, lhs: str, rhs: str) -> bool:
        return all(condition.evaluate(lhs, rhs) for condition in self.conditions)

class OrCondition(ContrastiveCondition):
    def __init__(self, *conditions: ContrastiveCondition):
        self.conditions = conditions

    def evaluate(self, lhs: str, rhs: str) -> bool:
        return any(condition.evaluate(lhs, rhs) for condition in self.conditions)

class LessThanOrEqualCondition(ContrastiveCondition):
    def __init__(self, property: Property):
        self.property = property

    def evaluate(self, lhs: str, rhs: str) -> bool:
        return self.property.evaluate(lhs) <= self.property.evaluate(rhs)

class LambdaCondition(ContrastiveCondition):
    def __init__(self, property: Property, function: Callable[[Any, Any], bool]):
        self.property = property
        self.function = function

    def evaluate(self, lhs: str, rhs: str) -> bool:
        return self.function(self.property.evaluate(lhs), self.property.evaluate(rhs))
    
class InputReadCompletedCondition(ContrastiveCondition):
    def __init__(self):
        self.property = InputReadCompletedProperty()

    def evaluate(self, lhs: str, rhs: str) -> bool:
        return self.property.evaluate(lhs) and self.property.evaluate(rhs)



class ContrastiveRegressionEvaluator:
    # Evaluates the buggy configuration against the ground truth configuration
    def __init__(self, planner: Path, lhs_configuration: str, rhs_configuration: str, conditions: list[ContrastiveCondition]):
        self.planner = planner
        self.lhs_configuration = lhs_configuration
        self.rhs_configuration = rhs_configuration
        self.conditions = conditions

    def run_evaluator(self):
        def evaluate(sas_file: Path):
            lhs_log = run_planner(sas_file, self.planner, self.lhs_configuration)
            rhs_log = run_planner(sas_file, self.planner, self.rhs_configuration)
            return all(
                condition.evaluate(lhs_log.stdout, rhs_log.stdout)
                for condition in self.conditions
            )

        sas.run_evaluator(evaluate)


