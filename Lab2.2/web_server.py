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

2.2
Создайте веб-сервер, который делает следующее:
При обращении по “/” — выдаёт краткую справку об использовании
При обращении по “/configs” — выдаёт сведения об именах всех хостов, для которых есть кофигурационные файлы (см. работу 1.6)
При обращении по “/config/hostname” выдает сведения о всех IP-адресах этого хоста
"""

import re
import glob
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def help():
    return "справка"

@app.route('/configs')
def func_host():
    return jsonify(host_list)

@app.route('/config/<hostname>')
def func_ip(hostname):
    for k,v in host_ip.items():
        if k == hostname:
            return jsonify(v)


if __name__ == '__main__':
    host_list = []
    host_ip = {}
    for file in glob.glob('d:\OneDrive\Docs\Python_cource\config_files\*'):
        ip_list = []
        with open(file) as f:
            for line in f:
                host_name = re.match('hostname ([a-zA-Z0-9-]+)', line)
                ip_mask = re.search('(?<=ip address )(([0-9]{1,3}[.]){3}[0-9]{1,3})',line)
                if host_name:
                    host_list.append(host_name.group(1))
                    host_temp = host_name.group(1)
                if ip_mask:
                    ip_list.append(ip_mask.group(0))
        host_ip[host_temp] = ip_list
    app.run(debug=True)





