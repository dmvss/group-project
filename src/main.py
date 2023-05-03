import pandas as pd

import tree
from CICFlowmeter import make_flow
from sniff import traffic_sniffer
from utility import *

def main():
    path = get_file_path()

    SNIFF_DURATION = 15
    pcap_dir = f'{path}\\..\\tcpdump\\pcap'
    csv_dir = f'{path}\\..\\tcpdump\\csv'
    model = tree.load_model(f'{path}\\..\\model\\decision_tree.pkl')
    sniffed_csv = f'{csv_dir}\\sniffed.pcap_Flow.csv'

    episodes = 10

    for _ in range(episodes):
        remove_obsolete_files()

        traffic_sniffer(SNIFF_DURATION)
        done, out = make_flow(pcap_dir, csv_dir)

        if not done:
            print("Error parsing pcap files.")
            return
        
        input = pd.read_csv(sniffed_csv)
        input = tree.remove_headers(input)
        tree.classify(model, input)

if __name__ == '__main__':
    main()
