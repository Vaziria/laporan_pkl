from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

gauth = GoogleAuth()
gauth.LocalWebserverAuth()

drive = GoogleDrive(gauth)

file1 = drive.CreateFile({'parents': [{'id': '1Vxdx6T9_w4bEtvse8aLDL_FIMhqf6XCV'}], 'title': 'test.zip'})
file1.SetContentFile('dist/test.exe')
file1.Upload()