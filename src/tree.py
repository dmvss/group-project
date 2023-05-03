import pickle
from utility import get_file_path

def load_model(filepath):
    with open(filepath,'rb') as f:
        return pickle.load(f)

def remove_headers(data):
    data = data.drop('Flow ID',axis=1)
    data = data.drop('Src IP',axis=1)
    data = data.drop('Dst IP',axis=1)
    data = data.drop('Timestamp',axis=1)
    data = data.drop('Label',axis=1)
    data = data.drop('Src Port',axis=1)
    data = data.drop('Dst Port',axis=1)
    data = data.drop('Protocol',axis=1)
    data =  data[data['Flow Duration'] != 0]
    return data

def classify(model, traffic):
    vpn = 0
    nonvpn =  0
    output = model.predict(traffic)
    total = len(output)

    for decision in output:
        if decision == 0:
            nonvpn += 1
        else:
            vpn += 1
    
    print_percentage_info = lambda label : print(f'{round(label/total * 100, 2)} % |', end='')

    if vpn > nonvpn:
        print("VPN ", end="")
        print_percentage_info(vpn)
    else:
        print("NON-VPN ", end="")
        print_percentage_info(nonvpn)

    print(f' TOTAL FLOWS: {total}, VPN: {vpn}, NON-VPN: {nonvpn}')