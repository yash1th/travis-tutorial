import unittest
import test_file_1

class TestMethods(unittest.TestCase):
	def test_add(self):
		self.assertEqual(test_file_1.get_status_code('https://google.com'),200)


if __name__ == '__main__':
	unittest.main()
