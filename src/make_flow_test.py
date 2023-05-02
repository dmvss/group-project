from CICFlowmeter import make_flow
import os

def main():
    path = os.path.dirname(os.path.realpath(__file__))
    os.chdir(path)
    pcap_dir = f'{path}\\..\\tcpdump\\pcap'
    csv_dir = f'{path}\\..\\tcpdump\\csv'
    _, out = make_flow(pcap_dir, csv_dir)
    print(out)

if __name__ == '__main__':
    main()

