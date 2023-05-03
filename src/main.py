import pickle
import os
import glob as gl
import pandas as pd
from scapy.all import *
from subprocess import check_output
from traffic_sniffer import traffic_sniffer
from make_flow_test import main
from tree import data_treatment
from tree import traffic_evaluation

path = os.path.dirname(os.path.realpath(__file__))

traffic_sniffer()
main()
csv_folder_path = gl.glob(f"{path}\\..\\tcpdump\\csv\\*.csv")[0]
source = pd.read_csv(csv_folder_path)
traffic_evaluation(data_treatment(source))
