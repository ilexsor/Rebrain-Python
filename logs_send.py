# Module for send metrics
import json
import psutil
import requests
import my_logger
from requests.exceptions import ConnectionError

logger = my_logger.get_logger('log_send')


def send_logs(metrics):
    url = 'http://127.0.0.1:8000/metrics/add'
    ip = psutil.net_if_addrs()['enp2s0'][0].address
    headers = {'Content-type': 'application/json'}
    logger.setLevel('INFO')

    try:
        response = requests.post(url, json=metrics, headers=headers)
        if response.status_code != 201:
            logger.setLevel("WARNING")
            logger.warning("Logs not send, reason: " + response.text)
        else:
            logger.setLevel('INFO')
            logger.info(response.status_code, response.text)
            logger.info(f'Logs from ip: {ip} are sent')
    except ConnectionError:
        logger.setLevel('ERROR')
        logger.error('Connection error')
