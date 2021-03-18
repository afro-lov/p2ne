from ipaddress import IPv4Network
import random

class IPv4RandomNetwork(IPv4Network):
    def __init__(self, ip_mask):
        IPv4Network.__init__(self, ip_mask, strict=False)
    def check(self):
        # исключаем сети : loopback , multicast, private и т.д
        if self.is_loopback or self.is_multicast or self.is_private or self.is_reserved:
            return 0
        else: return 1
    def key_value(self):
        # задаем правила для сортировки
        return int(self.hostmask)*2**32 + int(self.network_address)

net_list = []
for j in range(1,50):
    # 0x0b000000, 0xdf000000 - сети в диапазоне от 11.0.0.0 до 223.0.0.0
    i = IPv4RandomNetwork((random.randint(0x0d000000, 0xff000000),random.randint(8, 24)))
    if i.check():
        net_list.append(i)
        #print(i)

# сортировка по своим правилам через служебную функцию sortfunc
def sortfunc(x):
    return x.key_value()
#net_list.sort(key=sortfunc)
#print(net_list)

for n in sorted(net_list,key=sortfunc):
    print(n)