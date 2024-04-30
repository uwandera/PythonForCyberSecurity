from scapy.all import *
import ipaddress

ports = [25,80,53,443,445,8080,8443]

def SynScan(host):
    ans,unans = sr(
        IP(dst=host)/
        TCP(sport=33333,dport=ports,flags="S")
        ,timeout=2,verbose=0)
    print("open ports at %s:" % host)
    for (s,r,) in ans:
        if s[TCP].dport == r[TCP].sport and r[TCP].flag == "SA":
            print(s[TCP].dport)

def DNSScan(host):
    ans.unans = sr(
        IP(dst=host)/
        UDP(dport=53)/
        DNS(rd=1,qd=DNSQR(qname="google.com"))
        ,timeout=2,verbose=0)
    if ans and ans[UDP]:
        print("DNS Server at %s"%host)

host = input("QUAL ENDEREÇO DE IP DA VÍTIMA: ")
try:
    ipaddress.ip_address(hots)
except:
    print("ENDEREÇO INVALIDO")
    exit(-1)

SynScan(host)
DNSScan(host)