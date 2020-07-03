import os
import yaml

fname = os.environ.get('env', '')

_file = 'environtment/{}.env'.format(fname)
_config = None


with open(_file, 'r', encoding='utf8') as out:
	_config = yaml.safe_load(out)

if __name__ == '__main__':

	print(_config)