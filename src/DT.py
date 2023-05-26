import pickle
from utility import get_file_path

def DT_load_model(filepath):
    with open(filepath,'rb') as f:
        return pickle.load(f)

def DT_predict(model, traffic):
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