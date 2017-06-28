import ListComprehension
import unittest

class TestPerfectNumber(unittest.TestCase):
	def test_generate_list_and_sum_1(self):
		start = 1
		end = 11
		expacted_value = -55
		value = ListComprehension.generate_list_and_sum(start, end)
		self.assertEqual(value, expacted_value)
	def test_generate_list_and_sum_2(self):
		start = 10
		end = 11
		expacted_value = -100
		value = ListComprehension.generate_list_and_sum(start, end)
		self.assertEqual(value, expacted_value)

if __name__ == '__main__':
	unittest.main()
