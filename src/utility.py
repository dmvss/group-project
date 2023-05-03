import os

def get_file_path():
    return os.path.dirname(os.path.realpath(__file__))

def remove_obsolete_files():
    path = get_file_path()
    try:
        os.remove(f'{path}\\..\\tcpdump\\pcap\\sniffed.pcap')
        os.remove(f'{path}\\..\\tcpdump\\csv\\sniffed.pcap_Flow.csv')
    except:
        pass