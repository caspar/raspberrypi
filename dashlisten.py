from scapy.all import *
cmd = "say \"Hello World\""

def arp_display(pkt):
    while True:
        if pkt[ARP].op == 1:
            if pkt[ARP].psrc == '0.0.0.0':
                if pkt[ARP].hwsrc == '74:c2:46:16:8f:86':
                    print "Pushed Button"
                    os.system(cmd)
print sniff(prn=arp_display, filter="arp", store=0, count=10)

#
# def arp_display(pkt):
#     while True:
#         if pkt[ARP].op == 1: #who-has (request)
#             if pkt[ARP].psrc == '0.0.0.0': # ARP Probe
#                 if pkt[ARP].hwsrc == '74:c2:46:16:8f:86':
#                     print "Pushed Button"
#                     os.system(cmd)
#                 # else:
#                 #     print "ARP Probe from unknown device: " + pkt[ARP].hwsrc
#
print sniff(prn=arp_display, filter="arp", store=0, count=10)
