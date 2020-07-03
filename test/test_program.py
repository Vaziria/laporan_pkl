import unittest

from app import RandomNs

runner = RandomNs('note.txt')

class TestRunning(unittest.TestCase):

	def test_variable(self):
		pass

	def test_program_running(self):
		pass

	def test_random_benar(self):
		limit = 10

		hasil = runner.get_random(limit)

		self.assertEqual(limit, len(hasil))


if __name__ == '__main__':

	unittest.main()