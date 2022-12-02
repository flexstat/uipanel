#!/usr/bin/python3
import os
import subprocess

working_directory = os.getcwd()
str = ''
str_i  = ''


list_ip = ['77.222.63.155',' 79.133.42.139']
list_country = ['ru','de']

with open('userdata') as f:
    str = f.read().replace('\n', '')

list_data = str.split(';')

for i in range(len(list_ip)):

    with open('conf_default') as file_in:
        text = file_in.read()

    text_ip = text.replace('$ip', list_ip[i])
    text_ip_domain = text_ip.replace('$domain', list_data[0])

    with open(list_data[2] + '.' + list_country[i] + '.' + list_data[0] + '.zone' , 'w') as file_out:
        file_out.write(text_ip_domain)



with open('default_named_conf') as file_in:
    text = file_in.read()

text_domain = text.replace('$domain', list_data[0])
text_domain_ip = text_domain.replace('$country_ru', list_country[0])
text_domain_ip_country = text_domain_ip.replace('$country_de', list_country[1])
text_domain_ip_country_username = text_domain_ip_country.replace('$user', list_data[2])

main_conf_str = 'named.conf.' + list_data[2] + '.' + list_data[0]

with open('named.conf.' + list_data[2] + '.' + list_data[0], 'w') as file_out:
        file_out.write(text_domain_ip_country_username)

with open('add.in.file', 'w') as file_out:
        file_out.write(main_conf_str)



#commands


subprocess.call(["ssh root@77.222.63.249 mkdir /home/"+list_data[2]], shell=True)
subprocess.call(["scp named.conf.* root@77.222.63.249:/etc/bind"], shell=True)
subprocess.call(["scp *.zone root@77.222.63.249:/var/cache/bind/master"], shell=True)
subprocess.call(["scp add.* root@77.222.63.249:/home/"+list_data[2]], shell=True)
subprocess.call(["scp addinbind.py root@77.222.63.249:/home/"+list_data[2]], shell=True)
subprocess.call(["ssh root@77.222.63.249 python3 /home/"+list_data[2]+"/addinbind.py"], shell=True)
