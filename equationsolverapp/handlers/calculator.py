from fractions import Fraction
from equationsolverapp.handlers.variable import Variable
from .expression import Expression

class Calculator:

    def __init__(self, equation: str) -> None:
        expressions = equation.split("=")

        self.left_expression = Expression(expressions[0])
        self.right_expression = Expression(expressions[1])
        
        self.unkwowns = self.left_expression.get_unknowns().union(self.right_expression.get_unknowns())

    def move_unknowns_to_left_expression(self):
        variables_moved = list()
        for var in self.right_expression.get_variables_with_unknowns():
            var.sign = var.sign * -1
            variables_moved.append(var)
            self.left_expression.variables.append(var)
            self.right_expression.variables.remove(var)

        return variables_moved

    def move_numbers_to_right_expression(self):
        variables_moved = list()
        for number in self.left_expression.get_variables_without_unknowns():
            number.sign = number.sign * -1
            variables_moved.append(number)
            self.right_expression.variables.append(number)
            self.left_expression.variables.remove(number)

        return variables_moved

    def sum_unknowns(self) -> Variable:
        sum = 0
        for var in self.left_expression.get_variables_with_unknowns():
            sum += int(var.get_actual_number())
            self.left_expression.variables.remove(var)
        
        new_variable = Variable(str(sum) + var.unknown)
        self.left_expression.variables.append(new_variable)
        return new_variable

    def add_numbers(self) -> Variable:
        sum = 0
        for number in self.right_expression.get_variables_without_unknowns():
            sum += int(number.get_actual_number())
            self.right_expression.variables.remove(number)

        new_number = Variable(str(sum))
        self.right_expression.variables.append(new_number)
        return new_number

    def get_equation_string(self) -> str:
        self.left_expression.update_string()
        self.right_expression.update_string()
        
        return self.left_expression.string + " = " + self.right_expression.string

    def solve_value_of_unknown(self):
        unknown_variable: Variable = self.left_expression.variables[0] if len(self.left_expression.variables) == 1 else None
        right_variable: Variable = self.right_expression.variables[0] if len(self.right_expression.variables) == 1 else None

        answer = int(right_variable.get_actual_number())/int(unknown_variable.get_actual_number())

        if answer % 1 == 0: return answer
        else:
            return Fraction(int(right_variable.get_actual_number()), int(unknown_variable.get_actual_number()))