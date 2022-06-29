# Entry point
import my_logger
import logs_send
import register_client
from time import sleep

from metrics_collection import get_metrics

logger = my_logger.get_logger("main")
logger.setLevel('INFO')
logger.info("Start program")

register_client.registration()
while True:
    logs_send.send_logs(get_metrics())
    sleep(2)

logger.info("End program")
