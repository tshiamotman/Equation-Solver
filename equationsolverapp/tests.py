from fractions import Fraction
from django.test import TestCase
from equationsolverapp.handlers.calculator import Calculator
from equationsolverapp.handlers.expression import Expression
from equationsolverapp.handlers.variable import Variable

class CalculatorTests(TestCase):

    def test_expression(self):
        expression_string = "2x + 4y - 1"
        exp =  Expression(expression_string)

        self.assertEqual(3, len(exp.variables))
        self.assertEqual(2, len(exp.operators))

        self.assertEqual({'x', 'y'}, exp.get_unknowns())

    def test_variable(self):
        var = Variable("2x")

        self.assertEqual(2, int(var.number))
        self.assertEqual("x", var.unknown)
        
        self.assertTrue(var.has_unknown())

    def test_calculator(self):
        equation_string = "4x + 2 = 3x + 6"
        calculator = Calculator(equation_string)

        calculator.move_unknowns_to_left_expression()

        self.assertEqual("4x+2-3x = 6", calculator.get_equation_string())

        calculator.move_numbers_to_right_expression()

        self.assertEqual("4x-3x = 6-2", calculator.get_equation_string())

        self.assertTrue(Variable("1x").__eq__(calculator.add_unknowns()))
        self.assertEqual("1x = 6-2", calculator.get_equation_string())

        self.assertTrue(Variable("4").__eq__(calculator.add_numbers()))
        self.assertEqual("1x = 4", calculator.get_equation_string())        

        self.assertEqual(4, calculator.solve_value_of_unknown())

    def test_calculator_2(self):
        equation_string = "4x + 2 = 2x + 6"
        calculator = Calculator(equation_string)

        calculator.move_unknowns_to_left_expression()

        self.assertEqual("4x+2-2x = 6", calculator.get_equation_string())

        calculator.move_numbers_to_right_expression()

        self.assertEqual("4x-2x = 6-2", calculator.get_equation_string())

        self.assertTrue(Variable("2x").__eq__(calculator.add_unknowns()))
        self.assertEqual("2x = 6-2", calculator.get_equation_string())

        self.assertTrue(Variable("4").__eq__(calculator.add_numbers()))
        self.assertEqual("2x = 4", calculator.get_equation_string())        

        self.assertEqual(2, calculator.solve_value_of_unknown())

    def test_calculator_3(self):
        equation_string = "4x + 2 = x + 6"
        calculator = Calculator(equation_string)

        calculator.move_unknowns_to_left_expression()

        self.assertEqual("4x+2-1x = 6", calculator.get_equation_string())

        calculator.move_numbers_to_right_expression()

        self.assertEqual("4x-1x = 6-2", calculator.get_equation_string())

        self.assertTrue(Variable("3x").__eq__(calculator.add_unknowns()))
        self.assertEqual("3x = 6-2", calculator.get_equation_string())

        self.assertTrue(Variable("4").__eq__(calculator.add_numbers()))
        self.assertEqual("3x = 4", calculator.get_equation_string())        

        self.assertEqual(Fraction(4,3), calculator.solve_value_of_unknown())