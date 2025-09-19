from collections.abc import Callable
from pathlib import Path
from typing import Any

from machetli import sas

from properties import Property, InputReadCompletedProperty
from environments import RunEnvironment
from single_regression import Condition


class BiCondition:
    # A condition is something that can be true or
    def evaluate(self, lhs, rhs) -> (bool, str):
        raise NotImplementedError()

    def __str__(self):
        return f"{self.__class__.__name__}({self.property if hasattr(self, 'property') else ''})"

class EqualityBiCondition(BiCondition):
    def __init__(self, property: Property | Condition, none_is: bool = False):
        self.none_is = none_is
        self.property = property

    def evaluate(self, lhs: str, rhs: str) -> (bool, str):
        l = self.property.evaluate(lhs)
        r = self.property.evaluate(rhs)
        if l is None or r is None:
            return self.none_is, f"l={l}, r={r}, any none is handled as {self.none_is}"
        else:
            return l == r, f"{l} == {r}"

class NotEqualityBiCondition(BiCondition):
    def __init__(self, property: Property | Condition, none_is: bool = False):
        self.eq = EqualityBiCondition(property, not none_is)

    def evaluate(self, lhs: str, rhs: str) -> (bool, str):
        eq, exp = self.eq.evaluate(lhs, rhs)
        return not eq, f"not ({exp})"

    def __str__(self):
        return f"Not{self.eq}"

class NotBiCondition(BiCondition):
    def __init__(self, condition: BiCondition):
        self.condition = condition

    def evaluate(self, lhs: str, rhs: str) -> (bool, str):
        v, exp = self.condition.evaluate(lhs, rhs)
        return not v, f"not ({exp})"

class AndCondition(BiCondition):
    def __init__(self, *conditions: BiCondition):
        self.conditions = conditions

    def evaluate(self, lhs: str, rhs: str) -> (bool, str):
        r = [condition.evaluate(lhs, rhs) for condition in self.conditions]
        return all(v for v, _ in r), " and ".join(f"({exp})" for v, exp in r)

class OrCondition(BiCondition):
    def __init__(self, *conditions: BiCondition):
        self.conditions = conditions

    def evaluate(self, lhs: str, rhs: str) -> (bool, str):
        r = [condition.evaluate(lhs, rhs) for condition in self.conditions]
        return any(v for v, _ in r), " or ".join(f"({exp})" for v, exp in r)

class LessThanOrEqualCondition(BiCondition):
    def __init__(self, property: Property):
        self.property = property

    def evaluate(self, lhs: str, rhs: str) -> (bool, str):
        lhs_value = self.property.evaluate(lhs)
        rhs_value = self.property.evaluate(rhs)
        result = lhs_value <= rhs_value
        return result, f"{lhs_value} <= {rhs_value}"

class LambdaCondition(BiCondition):
    def __init__(self, property: Property, function: Callable[[Any, Any], bool]):
        self.property = property
        self.function = function

    def evaluate(self, lhs: str, rhs: str) -> (bool, str):
        lhs_value = self.property.evaluate(lhs)
        rhs_value = self.property.evaluate(rhs)
        result = self.function(lhs_value, rhs_value)
        return result, f"lambda({lhs_value}, {rhs_value}) = {result}"
    
class RhsCondition(BiCondition):
    def __init__(self, property: Property | Condition):
        self.property = property

    def evaluate(self, lhs: str, rhs: str) -> (bool, str):
        rhs_value = self.property.evaluate(rhs)
        return rhs_value, f"rhs({rhs_value})"

class LhsCondition(BiCondition):
    def __init__(self, property: Property | Condition):
        self.property = property

    def evaluate(self, lhs: str, rhs: str) -> (bool, str):
        lhs_value = self.property.evaluate(lhs)
        return lhs_value, f"lhs({lhs_value})"

class BothBiCondition(BiCondition):
    def __init__(self, property: Property | Condition):
        self.property = property

    def evaluate(self, lhs: str, rhs: str) -> (bool, str):
        lhs_value = self.property.evaluate(lhs)
        rhs_value = self.property.evaluate(rhs)
        result = lhs_value and rhs_value
        return result, f"both({lhs_value} and {rhs_value})"

def InputReadCompletedCondition() -> BiCondition:
    return BothBiCondition(InputReadCompletedProperty())


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
            all_true = True
            for condition in self.conditions:
                v, exp = condition.evaluate(lhs_log.stdout, rhs_log.stdout)
                if not v:
                    all_true = False
                    print(exp)
            return all_true
        sas.run_evaluator(evaluate)


