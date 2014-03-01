#!/usr/bin/python

import os
import time

source = '/home/madhura/Downloads/python-progs'
target = '/home/madhura/Downloads/python-backup'
target_zip = target+time.strftime('%Y%m%d%H%M%S')+'.zip'
zip_command = "zip -qr %s %s" % ( target_zip, source)

if os.system(zip_command) == 0 :
        print zip_command
        print 'Successful backup to %s' %target
else :
        print 'backup failed'
