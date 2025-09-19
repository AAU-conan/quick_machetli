import re


class Property:
    # A property is something that can be extracted from a log
    def evaluate(self, input: str):
        raise NotImplementedError()

    def __str__(self):
        return f"{self.__class__.__name__}()"

class RegexProperty(Property):
    # Uses regex to extract a string property from a log
    def __init__(self, regex: str):
        self.regex = regex

    def evaluate(self, input: str) -> str | None:
        match = re.search(self.regex, input)
        if match:
            return match.group(1)
        return None

class TypedRegexProperty(RegexProperty):
    # Uses regex to extract a typed property from a log
    def __init__(self, regex: str, type: type):
        super().__init__(regex)
        self.type = type

    def evaluate(self, input: str) -> str | None:
        match = super().evaluate(input)
        return self.type(match) if match is not None else None

class RegexContainsProperty(RegexProperty):
    def evaluate(self, input: str) -> bool:
        return re.search(self.regex, input) is not None

class InputReadCompletedProperty(Property):
    def evaluate(self, input: str) -> bool:
        return "done reading input!" in input or "Reading input task... Finished" in input

def SolvedProperty() -> RegexContainsProperty:
    return RegexContainsProperty(r"Solution found.|Goal reached. Start extraction of solution.")

def UnsolvableProperty() -> RegexContainsProperty:
    return RegexContainsProperty(r"Completely explored state space -- no solution!|No solution could be found")

def CostProperty() -> TypedRegexProperty:
    return TypedRegexProperty(r"Plan cost: (\d+)", int)

class ObjectiveValueProperty(Property):
    def evaluate(self, input: str) -> float | None:
        match = re.search(r"Objective value for the initial state lies within the interval \[(\d+|inf), (?:\d+\.?\d*|inf)\]", input)
        if match:
            return float(match.group(1))
        else:
            match = re.search(r"No policy found for the initial state.", input)
            if match:
                return float('inf')
        return None

def ExpandedUntilLastJumpProperty() -> TypedRegexProperty:
    return TypedRegexProperty(r"Expanded until last jump: (\d+)", int)
