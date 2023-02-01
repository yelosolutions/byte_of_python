#!/usr/bin/python3
"""
Creates a backup of all of my important files
"""
import os
from datetime import datetime


#a list of the files that I want to backup
source = ['/home/vagrant/movies', '/home/vagrant/notes']

#the main backup directory
target_dir = '/home/vagrant/backup'

#make the backup directory if it is not available
if not os.path.exists(target_dir):
	os.mkdir(target_dir)

#create a zip file to store the backed up files
#use current date and time as the name of the zipfile
name = datetime.now()
target_zip = target_dir + os.sep + name.strftime('%Y%m%d%H%M%S') + '.zip'

#create a zip command that can be executed from the cmd line
#I'll use the zip command from the standard library
#the -r option is  for recursively adding all of the files listed in the source 
zip_command  = 'zip -r {} {}'.format(target_zip, ' '.join(source))

print('This is the zip command:\n', zip_command)

print('Wait a moment as your files backed up...')
#execute the zip command return a success message when the zip command runs
if os.system(zip_command) == 0: #the os.system function returns 0 for success else 1
	print('Successfully backed up in', target_zip)
else:
	print('Backup FAILED')
