import os

import psutil
import requests
import my_logger
import get_Clients
from requests.exceptions import ConnectionError


def registration():
    logger = my_logger.get_logger('reg_client')
    url = 'http://127.0.0.1:8000/api/clients/add'
    ip = psutil.net_if_addrs()['enp2s0'][0].address
    description = os.uname()[0]
    name = os.uname()[1]
    body = {
        'ip_address': ip,
        'description': description,
        'name': name
    }

    try:
        logger.setLevel('INFO')
        if not get_Clients.check_client():
            requests.post(url, body)
            logger.info('New client is registered')
            return True
        else:
            return False
    except ConnectionError:
        logger.setLevel('ERROR')
        logger.error('Connection error, check server')
