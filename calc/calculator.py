"""Class for the Calculator object that contains all the methods"""
from calc.operations.addition import Addition
from calc.operations.multiplication import Multiplication
from calc.operations.subtraction import Subtraction
from calc.operations.division import Division
from calc.operations.calculation import Calculation


class Calculator:
    """ This is the Calculator class"""

    history = []
    calc_iterations = 0

    @staticmethod
    def add_number(value_a, value_b):
        """ adds number to result and appends to history list"""
        addition = Addition(value_a, value_b)
        Calculator.add_calculation_history(addition)
        Calculator.calculation_counter()
        return Calculator.get_last_calculator_result

    @staticmethod
    def multiply_number(value_a, value_b):
        """multiply number to result"""
        multiplication = Multiplication(value_a, value_b)
        Calculator.add_calculation_history(multiplication)
        Calculator.calculation_counter()
        return Calculator.get_last_calculator_result

    @staticmethod
    def divide_number(value_a, value_b):
        """divides number to result"""
        division = Division(value_a, value_b)
        Calculator.add_calculation_history(division)
        Calculator.calculation_counter()
        return Calculator.get_last_calculator_result

    @staticmethod
    def subtract_number(value_a, value_b):
        """ subtract number from result"""
        subtraction = Subtraction(value_a, value_b)
        Calculator.add_calculation_history(subtraction)
        Calculator.calculation_counter()
        return Calculator.get_last_calculator_result

    @staticmethod
    def add_calculation_history(calculation):
        """holds calculation history"""
        Calculator.history.append(Calculation)

    @staticmethod
    def get_last_calculator_result():
        """retrieves last calculation result"""
        return Calculator.history[-1]

    @staticmethod
    def get_first_calculator_result():
        """retrieves first calculation result"""
        return Calculator.history[0]

    @staticmethod
    def calculation_counter():
        """counts number of calculations done"""
        Calculator.calc_iterations +=1
        return Calculator.calc_iterations

    @staticmethod
    def remove_history():
        """clears calculator history"""
        Calculator.history.clear()

    @staticmethod
    def remove_one(index):
        """clears a specific item from history"""
        Calculator.history.remove(index)


