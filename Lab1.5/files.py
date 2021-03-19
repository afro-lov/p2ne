import glob

ip = []
for file in glob.glob('d:\OneDrive\Docs\Python_cource\config_files\*'):
    with open(file) as f:
        for line in f:
            if line.find('ip address') != -1:
                ip.append(line.replace('ip address','').strip().rstrip('\n'))

uniq_ip = list(set(ip))

for line in uniq_ip:
    print(line)
