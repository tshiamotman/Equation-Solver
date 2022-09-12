from django.test import TestCase

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

        self.assertEqual(2, var.number)
        self.assertEqual("x", var.unknown)
        
        self.assertTrue(var.has_unknown())
