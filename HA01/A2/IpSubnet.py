import sys
ip1,ip2,nm =sys.argv[1],sys.argv[2],int(sys.argv[3])

binIp1 = [bin(int(ip1))[2:].rjust(8,'0') for ip1 in ip1.split('.')]
ip1 = ''.join(binIp1)

binIp2 = [bin(int(ip2))[2:].rjust(8,'0') for ip2 in ip2.split('.')]
ip2 = ''.join(binIp2)

nid1 = ip1[:nm].ljust(32,'0')
nid2 = ip2[:nm].ljust(32,'0')

if nid1 == nid2:
    print("Same subnet")
else:
    print("Different subnet")
