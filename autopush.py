#!/home/joshua/jwww/bin/python
# -*- coding: utf-8 -*-
import subprocess
import datetime

subprocess.call(["git", "add", "."])
subprocess.call(["git", "commit", "-m", "joshua defined auto push at " + str(datetime.datetime.now())]) # 加上当前系统的时间
subprocess.call(["git", "push"])
