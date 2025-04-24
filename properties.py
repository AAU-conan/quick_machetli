import re


class Property:
    # A property is something that can be extracted from a log
    def evaluate(self, input: str):
        raise NotImplementedError()

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

class RegexAllProperty(RegexProperty):
    def evaluate(self, input: str) -> list[str]:
        matches = re.findall(self.regex, input)
        return matches if matches else None 

class InputReadCompletedProperty(Property):
    def evaluate(self, input: str) -> bool:
        return "done reading input!" in input

def SolvedProperty() -> RegexContainsProperty:
    return RegexContainsProperty(r"Solution found.")

def UnsolvableProperty() -> RegexContainsProperty:
    return RegexContainsProperty(r"Completely explored state space -- no solution!")

def CostProperty() -> TypedRegexProperty:
    return TypedRegexProperty(r"Plan cost: (\d+)", int)
