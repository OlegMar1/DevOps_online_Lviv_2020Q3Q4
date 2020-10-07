import unittest
from FizzBuzz import FizzBuzz_test

class TestFizzBuzz(unittest.TestCase):

	def test_simple_should_return_the_number(self):
		self.assertEqual(FizzBuzz_test(1), 1)
		self.assertEqual(FizzBuzz_test(2), 2)
		self.assertEqual(FizzBuzz_test(4), 4)

	def test_fizz(self):
		self.assertEqual(FizzBuzz_test(3), str(3) + "\tFizz")
		self.assertEqual(FizzBuzz_test(9), str(9) + "\tFizz")

	def test_buzz(self):
		self.assertEqual(FizzBuzz_test(5), str(5) + "\tBuzz")
		self.assertEqual(FizzBuzz_test(10), str(10) + "\tBuzz")
	
	def test_fizzbuzz(self):
		self.assertEqual(FizzBuzz_test(15), str(15) + "\tFizzBuzz")
		self.assertEqual(FizzBuzz_test(30), str(30) + "\tFizzBuzz")
		

if __name__ == '__main__':
	unittest.main()


