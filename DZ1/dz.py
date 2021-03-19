"""
Напишите программу, которая:
- прочитает содержимое всех конфигурационных файлов из каталога (аналогично лабораторной работе 1.5);
- сгенерирует список всех интерфейсов на всех устройствах, с указанием IP-адресов и масок (аналогично лабораторной работе 1.6);
- сгенерирует адресный план — таблицу со столбцами «Сеть», «Маска» (комбинации сети и маски должны быть уникальными);
- выведет адресный план на экран — в виде, пригодном для чтения, формат вывода определите сами.

Дополнительное задание («со звёздочкой»): сгенерируйте адресный план в виде таблицы MS Excel, воспользуйтесь библиотекой openpyxl (см. лабораторную работу 1.2)
"""
import re
import ipaddress
import glob

"""
interface GigabitEthernet7/0/4
!
interface Vlan1
 no ip address
 shutdown
!
interface Vlan18
 ip address 10.12.225.52 255.255.255.192
!
interface Vlan37
 ip address dhcp
 shutdown
!
interface Vlan112
 ip address dhcp
 shutdown
!
"""
need_ip = 0
for file in glob.glob('d:\OneDrive\Docs\Python_cource\config_files\*'):
    with open(file) as f:
        for line in f:
            pass

def find_int(val):
    if need_ip == 1 :  # предыдущий interface без IP
    int = re.match('interface ([a-zA-Z0-9/]+)', val)
    if int: need_ip = 1

def find_ip(val):
    ip_mask = re.search('(?<=ip address )(([0-9]{1,3}[.]){3}[0-9]{1,3}) (([0-9]{1,3}[.]){3}[0-9]{1,3})', val)
    ip = ipaddress.IPv4Interface(ip_mask.group(0).replace(' ', '/'))
    need_ip = 0 # ip для предыдущего интерфейса найден
    pass
