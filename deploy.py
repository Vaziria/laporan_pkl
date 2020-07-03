from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

from envi import _config
from logger import Logger

logger = Logger(__name__)

gauth = GoogleAuth()
gauth.LocalWebserverAuth()

drive = GoogleDrive(gauth)

file1 = drive.CreateFile({'parents': [{'id': _config.get('folderid')}], 'title': _config.get('appname')})
file1.SetContentFile(_config.get('target_upload'))
file1.Upload()

logger.info('uploading file finished')