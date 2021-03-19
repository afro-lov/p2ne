"""
Подключить библиотеку ipaddress

Написать функцию-классификатор, которая на вход принимает произвольную строку и возвращает словарь:
- {"ip":IPv4Interface()} — для строк вида " ip address x.x.x.x x.x.x.x"
- {“int”:str} — для строк вида "interface name"
- {"host":str} — для строк вида "hostname xxx"
- пустой словарь — во всех остальных случаях

Аналогично предыдущей работе открыть последовательно каждый конфигурационный файл, прочитать его построчно

Классифицировать каждую прочитанную строку

Создать три списка: все IP-адреса, все имена интерфейсов, все имена хостов, вывести на экран
"""

import re
import ipaddress
import glob

def func(val):
    # ищем строки типа: "ip address 10.12.222.188 255.255.255.192"
    ip_mask = re.search('(?<=ip address )(([0-9]{1,3}[.]){3}[0-9]{1,3}) (([0-9]{1,3}[.]){3}[0-9]{1,3})', val)
    # ищем строки типа: "hostname beeline-catme3400"
    host_name = re.match('hostname ([a-zA-Z0-9-]+)', val)
    # ищем строки типа: "interface Vlan183"
    int = re.match('interface ([a-zA-Z0-9/-]+)', val)
    if ip_mask:
        ip_d = {}
        # генерим словарик типа: {"ip":IPv4Interface()}
        # из ip_mask берем "10.12.222.188 255.255.255.192" меняя пробел на / и пихаем в ipaddress.IPv4Interface
        ip_d['ip'] = ipaddress.IPv4Interface(ip_mask.group(0).replace(' ','/'))
        # пример результата: {'ip': IPv4Interface('10.12.163.124/25')}
        return ip_d , 1
    elif host_name:
        host_d = {}
        host_d['host'] = host_name.group(1)
        return host_d , 2
    elif int:
        int_d = {}
        int_d['int'] = int.group(1)
        return int_d , 3
    else:
        empty_d = {}
        return empty_d , 4

ip_list = []
host_list = []
int_list = []
for file in glob.glob('d:\OneDrive\Docs\Python_cource\config_files\*'):
    with open(file) as f:
        for line in f:
            a = func(line)
            if a[1] == 1:
                ip_list.append(a[0])
            elif a[1] == 2:
                host_list.append(a[0])
            elif a[1] == 3:
                int_list.append(a[0])

# ip_list = list(set(ip_list))
# TypeError: unhashable type: 'dict'

print(ip_list)
# for i in ip_list: print(i['ip'])
print(host_list)
# for i in host_list: print(i['host'])
print(int_list)
# for i in int_list: print(i['int'])

