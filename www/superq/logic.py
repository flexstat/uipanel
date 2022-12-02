#!/usr/bin/python3
import os

working_directory = os.getcwd()
str = ''
str_i  = ''


list_ip = ['11.10.10.1','11.10.10.2']
list_country = ['ru','de']

with open('userdata') as f:
    str = f.read().replace('\n', '')

list_data = str.split(';')

for i in range(len(list_ip)):

    with open('conf_default') as file_in:
        text = file_in.read()

    text_ip = text.replace('$ip', list_ip[i])
    text_ip_domain = text_ip.replace('$domain', list_data[0])

    with open(list_data[2] + '.' + list_country[i] + '.' + list_data[0] + '.zone ' , 'w') as file_out:
        file_out.write(text_ip_domain)
print(working_directory)
