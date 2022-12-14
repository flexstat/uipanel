#!/usr/bin/python3
import os
import subprocess
dirname, filename = os.path.split(os.path.abspath(__file__))


working_directory = os.getcwd()
str = ''
str_i  = ''
list_view_country = []

list_ip = ['77.222.54.250','77.222.55.11']
list_country = ['ru','de']

with open(dirname + '/userdata') as f:
    str = f.read().replace('\n', '')

list_data = str.split(';')

for i in range(len(list_ip)):

    with open(dirname + '/conf_default') as file_in:
        text = file_in.read()

    text_ip = text.replace('$ip', list_ip[i])
    text_ip_domain = text_ip.replace('$domain', list_data[0])

    with open(dirname + '/' + list_data[2] + '.' + list_country[i] + '.' + list_data[0] + '.master.zone' , 'w') as file_out:
        file_out.write(text_ip_domain)


#ru
with open(dirname + '/default_named_conf_zone_ru') as file_in:
    text = file_in.read()

text_domain = text.replace('$domain', list_data[0])
text_domain_country = text_domain.replace('$country_ru', list_country[0])
text_domain_country_user = text_domain_country.replace('$user', list_data[2])

main_conf_str_ru ='view' + '.' +  list_country[0] + '.' + list_data[2] + '.' + list_data[0] + '.zone;'

with open(dirname + '/view' + '.' + list_country[0] + '.' + list_data[2] + '.' + list_data[0] + '.zone', 'w') as file_out:
        file_out.write(text_domain_country_user)



#de
with open(dirname + '/default_named_conf_zone_de') as file_in:
    text = file_in.read()

text_domain = text.replace('$domain', list_data[0])
text_domain_country = text_domain.replace('$country_de', list_country[1])
text_domain_country_user = text_domain_country.replace('$user', list_data[2])

main_conf_str_de = 'view' + '.' + list_country[1] + '.' + list_data[2] + '.' + list_data[0] + '.zone'

with open(dirname + '/view' + '.' + list_country[1] + '.' + list_data[2] + '.' + list_data[0] + '.zone', 'w') as file_out:
        file_out.write(text_domain_country_user)



with open(dirname + '/add.in.file', 'w') as file_out:
        file_out.write(main_conf_str_ru)
        file_out.write(main_conf_str_de)



#config ddos worker

with open(dirname + '/ddos_confg') as file_in:
    text = file_in.read()
text_domain = text.replace('$domain', list_data[0])
text_domain_ip = text_domain.replace('$ip', list_data[1])


with open(dirname + '/ddos_confg', 'w') as file_out:
        file_out.write(text_domain_ip)



#commands


#dns
subprocess.call(["ssh root@77.222.63.249 mkdir /home/"+list_data[2]], shell=True)
subprocess.call(["scp " + dirname +"/view.* root@77.222.63.249:/etc/bind"], shell=True)
subprocess.call(["scp " + dirname +"/*master.zone root@77.222.63.249:/var/cache/bind/master"], shell=True)
subprocess.call(["scp " + dirname +"/add.* root@77.222.63.249:/home/"+list_data[2]], shell=True)
subprocess.call(["scp " + dirname +"/addinbind.py root@77.222.63.249:/home/"+list_data[2]], shell=True)
subprocess.call(["ssh root@77.222.63.249 python3 /home/"+list_data[2]+"/addinbind.py"], shell=True)
subprocess.call(["ssh root@77.222.63.249 systemctl restart bind9 && reload rdcl"], shell=True)


#ddov filter
subprocess.call(["ssh root@77.222.54.250 mkdir /home/"+list_data[2]], shell=True)
subprocess.call(["scp " + dirname + "/ddos_confg root@77.222.54.250:/home/"+list_data[2]], shell=True)
subprocess.call(["scp " + dirname +"/addinddos.py root@77.222.54.250:/home/"+list_data[2]], shell=True)
subprocess.call(["ssh root@77.222.54.250 python3 /home/"+list_data[2]+"/addinddos.py"], shell=True)


subprocess.call(["ssh root@77.222.55.11 mkdir /home/"+list_data[2]], shell=True)
subprocess.call(["scp " + dirname +"/ddos_confg root@77.222.55.11:/home/"+list_data[2]], shell=True)
subprocess.call(["scp " + dirname +"/addinddos.py root@77.222.55.11:/home/"+list_data[2]], shell=True)
subprocess.call(["ssh root@77.222.55.11 python3 /home/"+list_data[2]+"/addinddos.py"], shell=True)
