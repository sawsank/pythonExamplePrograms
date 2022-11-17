#Using os module
import os.path, time
import pathlib

file = pathlib.Path('/Users/shasank/PycharmProjects/BasicsToAdvanced/Basics/calender.py')
print("last modification time: %s" % time.ctime(os.path.getmtime(file)))
print("last metadata change time or path creation time: %s"% time.ctime(os.path.getctime(file)))


#Using stat() method
import datetime
import pathlib

fname = pathlib.Path('calculator.py')
print("Last modification time: %s" % datetime.datetime.fromtimestamp(fname.stat().st_mtime))
print("Last metadata change time or path creation time: %s" % datetime.datetime.fromtimestamp(fname.stat().st_ctime))