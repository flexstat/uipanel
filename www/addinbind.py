#!/usr/bin/python3
import os
dirname, filename = os.path.split(os.path.abspath(__file__))


with open(dirname + '/add.in.file') as f:
    str = f.read().replace('\n', '')

list_data = str.split(';')


with open("/etc/bind/named.conf", "a") as myfile:
    myfile.write('include "/etc/bind/' + list_data[0] + '";' + "\n")


