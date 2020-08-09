import subprocess
import os

from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

from envi import _config
from logger import Logger

logger = Logger(__name__)


def get_version():
	# git describe --tags
	label = subprocess.check_output(["git", "describe", "--tags"]).strip()
	return label

def run():
	version = str(get_version())
	appname = _config.get('appname').format(version=version)
	
	gauth = GoogleAuth()
	gauth.LocalWebserverAuth()

	drive = GoogleDrive(gauth)

	file1 = drive.CreateFile({'parents': [{'id': _config.get('folderid')}], 'title': appname})
	file1.SetContentFile(_config.get('target_upload'))
	file1.Upload()

	logger.info('uploading file finished')

if __name__ == '__main__':

	version = get_version()
	logger.info('uploading {}'.format(str(version)))

	run()