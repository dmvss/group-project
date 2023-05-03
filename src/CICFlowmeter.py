import os
from utility import get_file_path
import subprocess

def make_flow(pcap_dir, csv_dir):
    path = get_file_path()
    exec_path = f'{path}\\..\\CICFlowmeter\\bin'
    os.chdir(exec_path)
    try:
        process = subprocess.Popen(f'cfm.bat {pcap_dir} {csv_dir}', shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, universal_newlines=True)
        stdout = process.communicate()[0]
    except Exception as e:
        print(e)
        return 0, f'Error occured: {stdout}'
    finally:
        os.chdir(path)
    return 1, stdout