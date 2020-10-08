import unittest
from FizzBuzz import FizzBuzz_test

class TestFizzBuzz(unittest.TestCase):

	def test_number(self):
		self.assertEqual(FizzBuzz_test(1), 1)
		self.assertEqual(FizzBuzz_test(2), 2)
		self.assertEqual(FizzBuzz_test(4), 4)

	def test_fizz(self):
		self.assertEqual(FizzBuzz_test(3), str(3) + "\tFizz")
		self.assertEqual(FizzBuzz_test(21), str(21) + "\tFizz")

	def test_buzz(self):
		self.assertEqual(FizzBuzz_test(5), str(5) + "\tBuzz")
		self.assertEqual(FizzBuzz_test(85), str(85) + "\tBuzz")

	def test_fizzbuzz(self):
		self.assertEqual(FizzBuzz_test(15), str(15) + "\tFizzBuzz")
		self.assertEqual(FizzBuzz_test(75), str(75) + "\tFizzBuzz")


if __name__ == '__main__':
	unittest.main()
