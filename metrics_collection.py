import psutil, os

host_info = {}
disk_info = {}

def get_metrics():
    mertics = {
        host_info: {
            'System': os.uname()[0],
            'Host': os.uname()[1],
            'IP': psutil.net_if_addrs()['enp2s0'][0].address
        },
        disk_info: {

        }
    }


get_metrics()
