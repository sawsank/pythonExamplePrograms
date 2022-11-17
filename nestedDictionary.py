from pathlib import Path
import os
import distutils.dir_util
try:
    Path("/Users/shasankjoshi/PycharmProjects/BasicsToAdvanced/Basics/dirA/dirB").mkdir(parents=True, exist_ok=True)


    os.makedirs("/Users/shasankjoshi/PycharmProjects/BasicsToAdvanced/Basics/dirA/dirC")

    distutils.dir_util.mkpath("/Users/shasankjoshi/PycharmProjects/BasicsToAdvanced/Basics/dirA/dirD")
except FileExistsError:
    print("File already exists")