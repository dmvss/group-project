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

mReplace = {
    'Total Fwd Packet': 'Tot Fwd Pkts',
    'Total Bwd packets': 'Tot Bwd Pkts',
    'Total Length of Fwd Packet': 'TotLen Fwd Pkts',
    'Total Length of Bwd Packet': 'TotLen Bwd Pkts',
    'Fwd Packet Length Max': 'Fwd Pkt Len Max',
    'Fwd Packet Length Min': 'Fwd Pkt Len Min',
    'Fwd Packet Length Mean': 'Fwd Pkt Len Mean',
    'Fwd Packet Length Std': 'Fwd Pkt Len Std',
    'Bwd Packet Length Max': 'Bwd Pkt Len Max',
    'Bwd Packet Length Min': 'Bwd Pkt Len Min',
    'Bwd Packet Length Mean': 'Bwd Pkt Len Mean',
    'Bwd Packet Length Std': 'Bwd Pkt Len Std',
    'Flow Bytes/s': 'Flow Byts/s',
    'Flow Packets/s': 'Flow Pkts/s',
    'Fwd IAT Total': 'Fwd IAT Tot', 
    'Bwd IAT Total': 'Bwd IAT Tot',
    'Fwd Header Length': 'Fwd Header Len',
    'Bwd Header Length': 'Bwd Header Len',
    'Fwd Packets/s': 'Fwd Pkts/s',
    'Bwd Packets/s': 'Bwd Pkts/s',
    'Packet Length Min': 'Pkt Len Min', 
    'Packet Length Max': 'Pkt Len Max',
    'Packet Length Mean': 'Pkt Len Mean',
    'Packet Length Std': 'Pkt Len Std',
    'Packet Length Variance': 'Pkt Len Var',
    'FIN Flag Count': 'FIN Flag Cnt',
    'SYN Flag Count': 'SYN Flag Cnt',
    'RST Flag Count': 'RST Flag Cnt',
    'PSH Flag Count': 'PSH Flag Cnt',
    'ACK Flag Count': 'ACK Flag Cnt',
    'URG Flag Count': 'URG Flag Cnt',
    'CWR Flag Count': 'CWE Flag Count',
    'ECE Flag Count': 'ECE Flag Cnt',
    'Average Packet Size': 'Pkt Size Avg',
    'Fwd Segment Size Avg': 'Fwd Seg Size Avg',
    'Bwd Segment Size Avg': 'Bwd Seg Size Avg',
    'Fwd Bytes/Bulk Avg': 'Fwd Byts/b Avg',
    'Fwd Packet/Bulk Avg': 'Fwd Pkts/b Avg',
    'Fwd Bulk Rate Avg': 'Fwd Blk Rate Avg',
    'Bwd Bytes/Bulk Avg': 'Bwd Byts/b Avg',
    'Bwd Packet/Bulk Avg': 'Bwd Pkts/b Avg',
    'Bwd Bulk Rate Avg': 'Bwd Blk Rate Avg',
    'Subflow Fwd Packets': 'Subflow Fwd Pkts',
    'Subflow Fwd Bytes': 'Subflow Fwd Byts',
    'Subflow Bwd Packets': 'Subflow Bwd Pkts',
    'Subflow Bwd Bytes': 'Subflow Bwd Byts',
    'FWD Init Win Bytes': 'Init Fwd Win Byts',
    'Bwd Init Win Bytes': 'Init Bwd Win Byts'
}

def remove_headers(data):
    data = data.drop('Flow ID',axis=1)
    data = data.drop('Src IP',axis=1)
    data = data.drop('Dst IP',axis=1)
    data = data.drop('Timestamp',axis=1)
    data = data.drop('Label',axis=1)
    #data = data.drop('Src Port',axis=1)
    #data = data.drop('Dst Port',axis=1)
    #data = data.drop('Protocol',axis=1)
    data =  data[data['Flow Duration'] != 0]
    data =  data[data['Protocol'] != 0]
    return data