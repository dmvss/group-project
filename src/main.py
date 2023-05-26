import CICFlowmeter
import DT
import NN
import sniff
import utility

import pandas as pd
from datetime import datetime

def main():

    EPISODES = 10
    SNIFF_DURATION = 30
    USE_NN = True
    #if False decision tree is used instead

    #init
    path = utility.get_file_path()
    pcap_dir = f'{path}\\..\\tcpdump\\pcap'
    logs_dir = f'{path}\\..\\logs'
    csv_dir = f'{path}\\..\\tcpdump\\csv'
    sniffed_csv = f'{csv_dir}\\sniffed.pcap_Flow.csv'
    NN_model_path = f'{path}\\..\\model\\NN_FLOW_TIMEOUT_15.h5'
    DT_model_path = f'{path}\\..\\model\\decision_tree_srcPort_dstPort.pkl'
    model = None

    if USE_NN:
        model = NN.NN_load_model(NN_model_path)
    else:
        model = DT.DT_load_model(DT_model_path)

    if model == None:
        print("Loading model failed.")
        return

    timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    log_file = open(f'{logs_dir}\\{timestamp}.txt', "a")

    for ep in range(EPISODES):
        utility.remove_obsolete_files()

        sniff.capture_start(SNIFF_DURATION)
        done, logs = CICFlowmeter.make_flow(pcap_dir, csv_dir)

        if not done:
            print("Error parsing pcap files.")
            return
        
        traffic_data = pd.read_csv(sniffed_csv)
        traffic_data.rename(columns=utility.mReplace, inplace=True)

        # for _, flow in traffic_data.iterrows():
        #     src_ip = flow['Src IP']
        #     dst_ip = flow['Dst IP']
    
        traffic_data = utility.remove_headers(traffic_data)

        if USE_NN:
            prediction_batch = NN.NN_predict(model, traffic_data)

            label, confidence = NN.NN_classify_batch(prediction_batch)
        
            #debug logs
            log_file.write(f'episode: {ep + 1}, label: {label}, confidence: {confidence}\n\n')
            debug_info = NN.NN_classify_batch_debug(prediction_batch)

            print(f'episode: {ep}, label: {label}, confidence: {confidence}')

            for row in debug_info:
                print(row)
                log_file.write(f'{row[0]}, {row[1]}, {row[2]}\n')

        else:
            DT.DT_predict(model, traffic_data) #writing logs to file when using decision tree is not implemented

        log_file.write('\n')

    log_file.close()

if __name__ == '__main__':
    main()
