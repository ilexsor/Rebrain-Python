import psutil
import requests
from requests.exceptions import ConnectionError
import logs_send
import my_logger

logger = my_logger.get_logger('get_client')


def check_client():
    ip = psutil.net_if_addrs()['enp2s0'][0].address
    url = 'http://127.0.0.1:8000/clients/'
    try:
        logger.setLevel('INFO')
        logger.info('Connect to server, get clients')
        responce = requests.get(url).json()

        for resp in responce:
            resp_ip = resp['ip_address']
            if ip == resp_ip:
                logger.info(f'Client with ip {ip} already registered')
                return True
        logger.info(f'Client with ip {ip} not registered')
        return False
    except ConnectionError:
        logger.setLevel('ERROR')
        logger.error('Connection error, check server')

