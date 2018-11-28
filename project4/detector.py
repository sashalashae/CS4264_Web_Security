import sys, dpkt, socket

fileName = str(sys.argv[1])
fileDes = open(fileName, 'rb')
pcap = dpkt.pcap.Reader(fileDes)

ip_list = []

for ts, buf in pcap:
    try:        
        eth = dpkt.ethernet.Ethernet(buf)
        if type(eth.data) == dpkt.ip.IP:
            ip = eth.data
            if type(ip.data) == dpkt.tcp.TCP:            
                tcp = ip.data
                found = 0
                for item in ip_list:
                    if ip.src == item["src"]:
                        if (tcp.flags & dpkt.tcp.TH_SYN) > 0 and (tcp.flags & dpkt.tcp.TH_ACK) == 0:
                            item["syn"] = item["syn"] + 1
                            found = 1
                            break
                    if ip.dst == item["src"]:
                        if (tcp.flags & dpkt.tcp.TH_SYN) > 0 and (tcp.flags & dpkt.tcp.TH_ACK) > 0:
                            item["ack"] = item["ack"] + 1
                            found = 1
                            break
                if found == 0:
                    if (tcp.flags & dpkt.tcp.TH_SYN) > 0 and (tcp.flags & dpkt.tcp.TH_ACK) == 0:
                        ip_list.append({"src": ip.src, "syn": 1, "ack": 0})
                    if (tcp.flags & dpkt.tcp.TH_SYN) > 0 and (tcp.flags & dpkt.tcp.TH_ACK) > 0:
                        ip_list.append({"src": ip.dst, "syn": 0, "ack": 1})
    except:
        continue
fileDes.close()
for item in ip_list:
    if item["syn"] >= 3*item["ack"]:
        print socket.inet_ntoa(item["src"])
print "\n"
