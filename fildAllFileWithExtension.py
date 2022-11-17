#Using glob
import glob, os

os.chdir("/Users/shasank/PycharmProjects/BasicsToAdvanced/Basics")

for file in glob.glob("*.txt"):
    print(file)

#Using os
import os

for file in os.listdir("/Users/shasank/PycharmProjects/BasicsToAdvanced/Basics"):
    if file.endswith(".txt"):
        print(file)

#Using os.walk
for root, dirs, files in os.walk("/Users/shasank/PycharmProjects/BasicsToAdvanced/Basics"):
    for file in files:
        if file.endswith(".txt"):
            print(file)