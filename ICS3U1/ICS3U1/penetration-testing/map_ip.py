import nmap
import sys
import time

nm = nmap.PortScanner()
print("\nRunning...\n")
nm_scanner = nm.scan(sys.argv[1], '80',arguments='-O')

host_is_up = "The host is: "+nm_scanner['scan'][sys.argv[1]]['status']['state']+"\n"
port_status = "The port 80 is: "+nm_scanner['scan'][sys.argv[1]]['tcp'][80]['state']+"\n"
method_scan = "The method of scaning is: "+nm_scanner['scan'][sys.argv[1]]['tcp'][80]['reason']+'"\n'
geus_os = "There is a %s chance that the host is running %s"%(nm_scanner['scan'][sys.argv[1]]['osmatch'][0]['accuracy'], nm_scanner['scan'][sys.argv[1]]['osmatch'][0]['name'])+"\n"

with open("%s.txt"%sys.argv[1], 'w') as f:
    f.write(host_is_up+port_status+method_scan+geus_os)
    f.write("\nReport generated "+time.strftime("%Y-%m-%d_%H:%M:%S GMT", time.gmtime()))

print("\nFinished...")