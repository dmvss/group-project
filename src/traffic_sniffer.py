from scapy.all import *
import os
from subprocess import check_output

def traffic_sniffer():
    interface = check_output((
    "powershell -NoLogo -NoProfile -NonInteractive -ExecutionPolicy bypass -Command ""& {"
    "Get-NetRoute –DestinationPrefix '0.0.0.0/0' | Select-Object -First 1 | "
    "Get-NetIPConfiguration | Select-Object -ExpandProperty InterfaceAlias"
    "}"""
    )).decode().strip()

    path = os.path.dirname(os.path.realpath(__file__))
    output_pcap_file = f'{path}\\..\\tcpdump\\pcap\\sniffed.pcap'
    writer = PcapWriter(output_pcap_file, append = False)

    def packet_capture(pkt):
        writer.write(pkt)
    
    sniff(iface=interface, prn=packet_capture, timeout=15)



