from pysnmp.hlapi import *
# инфа о системе:
snmp_object = ObjectIdentity('SNMPv2-MIB', 'sysDescr', 0)
# интерфейсы тут:
snmp_object2 = ObjectIdentity('1.3.6.1.2.1.2.2.1.2')

result = getCmd(SnmpEngine(),
                CommunityData("public", mpModel=0),
                UdpTransportTarget(("10.31.70.107", 161)),
                ContextData(),
                ObjectType(snmp_object))

for i in result:
    for j in i[3]:
        print(j)

result2 = nextCmd(SnmpEngine(),
                CommunityData("public", mpModel=0),
                UdpTransportTarget(("10.31.70.107", 161)),
                ContextData(),
                ObjectType(snmp_object2),
                lexicographicMode=False)

for i in result2:
    for j in i[3]:
        print(j)