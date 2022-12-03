#!/usr/bin/python3
import subprocess
import os
dirname, filename = os.path.split(os.path.abspath(__file__))



with open(dirname + '/add.in.file') as f:
    str = f.read().replace('\n', '')

list_data = str.split(';')

with open("/etc/bind/named.conf.local") as f_old, open(dirname + "/named.conf.local", "w") as f_new:
    for line in f_old:
        f_new.write(line)
        if '#RU' in line:
            f_new.write('include "/etc/bind/' + list_data[0] + '";'  + "\n")
        if '#ANY' in line:
            f_new.write('include "/etc/bind/' + list_data[1] + '";'  + "\n")


subprocess.call(["cp " + dirname + "/named.conf.local /etc/bind/"], shell=True)

