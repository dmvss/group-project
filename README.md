# VPN Traffic Classifier

This project is a real-time VPN traffic classifier designed to differentiate between VPN and non-VPN traffic using artificial intelligence. It was developed by a group of students as part of a university assignment. The project utilizes the ISCX VPN dataset (ISCXVPN2016) for model training and CICFlowMeter for generating packet flows that are subsequently interpreted by the model.

## Requirements

- WinPcap_4_1_3
- python3
- java

## Installation (Windows)

```
pip install -r requirements.txt
python main.py
```
#### Linux is not currently supported.

## Acknowledgements

Canadian Institute for Cybersecurity

[CicFlowMeter](https://github.com/ISCX/CICFlowMeter)

[VPN-nonVPN dataset (ISCXVPN2016)](https://www.unb.ca/cic/datasets/vpn.html)

Gerard Drapper Gil, Arash Habibi Lashkari, Mohammad Mamun, Ali A. Ghorbani, "Characterization of Encrypted and VPN Traffic Using Time-Related Features", In Proceedings of the 2nd International Conference on Information Systems Security and Privacy(ICISSP 2016) , pages 407-414, Rome , Italy



