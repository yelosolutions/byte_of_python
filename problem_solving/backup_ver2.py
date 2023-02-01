#!/usr/bin/python3
""" Creates a backup directory for my important files
Keeps backed up zip files with current time as names
in directories with dates as names
"""
import os
from datetime import datetime


# a list of the directories that I want to backup
source = ['/home/vagrant/movies', '/home/vagrant/notes']

# the main backup directory
target_dir = '/home/vagrant/backup'

# makes a backup directory if one is not present
if not os.path.exists(target_dir):
	os.mkdir(target_dir)

# use datetime time to get the current date
name = datetime.now()

# using the name variable to create the zip directories names
today =  target_dir + os.sep + name.strftime('%Y%m%d')
if not os.path.exists(today):
	os.mkdir(today)

# creates zip file names
now = today + os.sep + name.strftime('%H%M%S') + '.zip'

target_zip = now

# a zip command to create the zip files
# will use the zip standard library command an the -r option 
# that recursively adds all subdirectories and files to be backed up
# use the join method of strings to turn the source list into a string
zip_command = 'zip -r {0} {1}'.format(target_zip, ' '.join(source))

print('This is the zip command:\n', zip_command)

print('Wait a moment...')
# runs as if it was run in the system, returns 0 for success and
# an error number for failure.
if os.system(zip_command) == 0:
	print('Successfully backed up to', target_zip)



print(today)

