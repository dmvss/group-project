import pickle
import os

path = os.path.dirname(os.path.realpath(__file__))

with open(f'{path}\\..\\decision_tree.pkl','rb') as f:
    traffic_classifier = pickle.load(f)

def data_treatment(raw_data):
    raw_data = raw_data.drop('Flow ID',axis=1)
    raw_data = raw_data.drop('Src IP',axis=1)
    raw_data = raw_data.drop('Dst IP',axis=1)
    raw_data = raw_data.drop('Timestamp',axis=1)
    raw_data = raw_data.drop('Label',axis=1)
    return raw_data

def traffic_evaluation(traffic):
    vpn = 0
    nonvpn =  0
    output = traffic_classifier.predict(traffic)
    for decision in output:
        if decision == 0:
            nonvpn += 1
        else:
            vpn += 1
    print(f'classified as vpn: {vpn},\nclassified as non-vpn: {nonvpn},\nDECISION: ')
    if vpn>nonvpn:
        print('Traffic sent through vpn service')
    else:
        print('Traffic sent without vpn service')
