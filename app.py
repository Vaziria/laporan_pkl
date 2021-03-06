import argparse
import random
import string

from file_format import FileFormat
from logger import Logger

from envi import _config

logger = Logger(__name__)



_isi = """
;; A Records
{domain}.	1	IN	A	{ip}
"""

_line = "{sub}.{domain}.	1	IN	A	{ip}\n"

_this_config = _config.get('random_sub', {})

# print(_this_config)

# exit()


class RandomNs:

	file = None
	note = []
	limit_file = _this_config.get('limit_file_line', 100)
	limit_huruf = [1, 3]

	def __init__(self, filename, limit_sub = 700):
		self.file = FileFormat(filename, [ 'ip' ], [ 'domain' ])
		self.limit_huruf = _this_config.get('limit_char', [1, 3])

		self.limit_sub = _this_config.get('limit_sub', 700)

	def generate(self):

		for item in self.file.data:
			domain = item['domain']
			ip = item['ip']
			note = []

			first = True

			for c in range(0, self.limit_sub):

				c_file = int((c + 1) / 100)

				if c_file == 0:
					c_file = 1

				fname = "dist/{}_out_{}.txt".format(domain, c_file)

				while True:
					limit = random.randint(*self.limit_huruf)
					sub = self.get_random(limit)
					
					if sub not in note:
						note.append(sub)
						break


				self.save(fname, sub, domain, ip, first)
				
				first = False

				self.add_note(domain, sub)

				logger.info('{}.{} --> save to {}'.format(sub, domain, fname))

	def save(self, fname, sub, domain, ip, first):

		if first:
			payload = _isi.format(domain=domain, ip=ip)
		else:
			payload = _line.format(sub=sub, domain=domain, ip=ip)

		with  open(fname, 'a+') as out:
			out.write(payload)


	def add_note(self, domain, sub):
		with open('note/{}.txt'.format(domain), 'a+') as out:
			out.write('{}.{}\n'.format(sub, domain))



	def get_random(self, limit):
		return ''.join(random.SystemRandom().choice(string.ascii_lowercase) for _ in range(limit))






if __name__ == '__main__':

	parser = argparse.ArgumentParser(description='Random NameServer')
	parser.add_argument('file', type=str, help='file')

	args = parser.parse_args()

	runner = RandomNs(args.file)
	runner.generate()


