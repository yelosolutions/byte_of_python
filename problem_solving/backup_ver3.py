#!/usr/bin/python3
"""
Creates a backup of my important files.
Keeps zip files named as current time of the 
day inside directories named as current day
"""
import os
from datetime import datetime


#a list that specifies the directories and files to be backed up
source = ['/home/vagrant/movies','/home/vagrant/notes']

#the main backup directory
target_dir = '/home/vagrant/backup'

#make a backup directory if one isn't available
if not os.path.exists(target_dir):
	os.mkdir(target_dir)

#keep zip files named as current time within directories named as current date
time = datetime.now()
today = target_dir + os.sep + time.strftime('%Y%m%d')
now = time.strftime('%H%M%S')
target = today + os.sep + now + '.zip'

#create directory today if it doesn't exist
if not os.path.exists(today):
	os.mkdir(today)

#prompt the user to enter a comment to be able to know, when they backup
#to remember the changes made
comment = input('Enter a comment: ')

#check if a comment was supplied 
if len(comment) == 0:
	response = input('Are you sure?y/n ')
	if response == 'y':
		target = today + os.sep + now + '.zip'
	else:
		print('Not allowed')
else:
	target = today + os.sep + now + '_' + comment.replace(' ', '_') + '.zip'

#implement a zip command using the standard library's zip command
#the -r option recursively adds all subdirectories and files in a directory
#the join method of strings converts the list into a string 
zip_command = 'zip -r {0} {1}'.format(target, ' '.join(source))


#the command is ran using os.system 
#which returns a 0 for success and an error message for failure
print('This is the zip command:\n', zip_command)
print('Wait a moment...')

if os.system(zip_command) == 0:
	print('Successfully backed up to:\n', target)
else:
	print('FAILED to backup') 
