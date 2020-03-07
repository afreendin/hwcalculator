from Calculator import Calculator
import unittest
import csv


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.calc = Calculator()

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.calc, Calculator)

    def test_add(self):
        with open('./src/Unit Test Addition.csv') as f:
            self.reader = csv.DictReader(f)
            for row in self.reader:
                self.assertEqual(self.calc.add(int(row['Value 2']), int(row['Value 1'])), int(row['Result']))

    def test_subtract(self):
        with open('./src/Unit Test Subtraction.csv') as f:
            self.reader = csv.DictReader(f)
            for row in self.reader:
                self.assertEqual(self.calc.subtract(int(row['Value 2']), int(row['Value 1'])), int(row['Result']))

    def test_multiply(self):
        with open('./src/Unit Test Multiplication.csv') as f:
            self.reader = csv.DictReader(f)
            for row in self.reader:
                self.assertEqual(self.calc.multiply(int(row['Value 2']), int(row['Value 1'])), int(row['Result']))

    def test_division(self):
        with open('./src/Unit Test Division.csv') as f:
            self.reader = csv.DictReader(f)
            for row in self.reader:
                self.assertEqual(float(format(self.calc.division(int(row['Value 2']), int(row['Value 1'])), '.9f')), float(row['Result']))

    def test_square(self):
        with open('./src/Unit Test Square.csv') as f:
            self.reader = csv.DictReader(f)
            for row in self.reader:
                self.assertEqual(self.calc.square(int(row['Value 1'])), int(row['Result']))

    def test_square_root(self):
        with open('./src/Unit Test Square Root.csv') as f:
            self.reader = csv.DictReader(f)
            for row in self.reader:
                if isinstance(row['Result'], int):
                    self.assertEqual(int(self.calc.square_root(int(row['Value 1']))), int(row['Result']))
                if isinstance(row['Result'], float):
                    if len(row['Result'].split('.')[1])==8:
                        self.assertEqual(float(round(self.calc.square_root(int(row['Value 1'])), 8)), float(row['Result']))
                    else:
                        self.assertEqual(float(round(self.calc.square_root(int(row['Value 1'])), 9)), float(row['Result']))


if __name__ == '__main__':
    unittest.main()