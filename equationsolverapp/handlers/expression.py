import re

from equationsolverapp.handlers.variable import Variable

class Expression:

    def __init__(self, string: str) -> None:
        self.string = string
        self.operators = re.findall("[-+]", string)
        
        self.variables = []
        string_vars = re.split("\-|\+", string)
        for i in range(0, len(string_vars)):
            if len(self.operators) == len(string_vars):
                var = self.operators[i] + string_vars[i]
            else:
                if i == 0:
                    var = string_vars[i]
                else:
                    var = self.operators[i-1] + string_vars[i]
        
            self.variables.append(Variable(var))

    def get_variables_without_unknowns(self):
        numbers = list()

        for variable in self.variables:
            if not variable.has_unknown():
                numbers.append(variable)

        return numbers

    def get_unknowns(self) -> set:
        unknowns = set()

        for variable in self.variables:
            if variable.has_unknown():
                unknowns.add(variable.unknown)

        return unknowns

    def get_variables_with_unknowns(self) -> list:
        unknowns = list()

        for variable in self.variables:
            if variable.has_unknown():
                unknowns.append(variable)

        return unknowns

    def update_string(self) -> str:
        self.string = ""
        for i in range(0, len(self.variables)):
            var: Variable = self.variables[i]

            if i > 0 and var.sign == 1:
                self.string += "+"

            if var.has_unknown():
                self.string += var.get_actual_number() + var.unknown
                
            else:
                self.string += var.get_actual_number()

        return self.string
