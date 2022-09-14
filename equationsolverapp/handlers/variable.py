import re

class Variable:

    def __init__(self, string: str) -> None:
        results = re.search("[1-9]", string)
        self.number: int = int(results.group()) if results is not None else 1 

        results = re.search("[a-zA-Z]", string)
        self.unknown: str = results.group() if results is not None else None

        results = re.search("[-+]", string)
        self.sign: int = -1 if results is not None and results.group() == "-" else 1

    def __eq__(self, __o: object) -> bool:
        if not isinstance(__o, Variable.__class__):
            return NotImplemented

        return self.number == __o.number and  self.unknown == __o.unknown and self.sign == __o.sign

    def has_unknown(self) -> bool:
        return self.unknown != None

    def get_actual_number(self) -> str:
        return str(self.sign * self.number)
