
import unittest
import cap 

class TestCap(unittest.TestCase):
	
	def test_one_word(self):
		text = 'python'
		result = cap.cap_text(text)
		self.assertEqual(result,'Python')

	def test_multiple_word(self):
		text = 'Python is fun'
		result = cap.cap_text(text)
		self.assertEqual(result,'Python is fun')

if __name__ == '__main__':
	unittest.main()

