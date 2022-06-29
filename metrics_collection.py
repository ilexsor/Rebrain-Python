import my_logger
import os
import psutil

host_info = {}
disk_info = []
memory_info = {}
cpu_info = {}
load_avg = {}

logger = my_logger.get_logger('Metrics')
logger.setLevel('INFO')


def get_metrics():
    metrics = {
        "host_info": f"System: {os.uname()[0]}, Host: {os.uname()[1]}, IP: {psutil.net_if_addrs()['enp2s0'][0].address}",
        "disk_info": f"Device: {psutil.disk_partitions()[0].device}, Mount point: {psutil.disk_partitions()[0].mountpoint}, File System: {psutil.disk_partitions()[0].fstype}, Total: {psutil.disk_usage('/').total}, Used: {psutil.disk_usage('/').used}",
        "memory_info": f"Total: {psutil.virtual_memory()[0]}, Used: {psutil.virtual_memory()[3]}, Percent: {psutil.virtual_memory()[2]}",
        "cpu_info": f"Cores: {psutil.cpu_count()}, Freq: {psutil.cpu_freq()[0]}",
        "load_avg": f"Load 1: {os.getloadavg()[0]}, Load 5: {os.getloadavg()[1]}, Load 15: {os.getloadavg()[2]}"
    }

    logger.info("New metrics are collected " + str(metrics))

    return metrics



