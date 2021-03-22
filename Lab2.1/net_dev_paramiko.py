import paramiko, time
import re
# ограничиваем количество байт которые прочитаем с устройства
buf_size = 20000
# указывает через какое время мы будем считывать вывод. без него может получить что никакого вывода не будет
timeout = 1

ssh_con = paramiko.SSHClient()
ssh_con.set_missing_host_key_policy(paramiko.AutoAddPolicy())

host = '10.31.70.209'
login = 'restapi'
password = 'j0sg1280-7@'

ssh_con.connect(host, username=login, password=password, look_for_keys=False, allow_agent=False)
session = ssh_con.invoke_shell()

session.send("\n")
session.recv(buf_size)
session.send("terminal length 0\n")
time.sleep(timeout)

session.send("\n")
session.recv(buf_size)
session.send("show ip int brief\n")
time.sleep(timeout*2)
s = session.recv(buf_size).decode()
print(s)
l = s.split('\n')
for i in l:
    if 3 <= l.index(i) < len(l)-1:
        a = re.search('^([a-zA-Z0-9]+)', i)
        if a:
            str = 'show interfaces ' + a.group(0) + ' | i (packets input)|(packets output)\n'
            session.send("\n")
            session.recv(buf_size)
            session.send(str)
            time.sleep(timeout)
            s_new = session.recv(buf_size).decode()
            print(s_new)
            # print(a.group(0))

session.close()