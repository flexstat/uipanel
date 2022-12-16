#!/usr/bin/python3

import subprocess
import os
dirname, filename = os.path.split(os.path.abspath(__file__))


with open(dirname + '/ddos_confg') as f:
    str = f.read().replace('\n', '')



with open("/vddos/conf.d/website.conf", "a") as myfile:
    myfile.write(str+"\n")


