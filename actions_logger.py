import logging


logging.basicConfig(filename='application_log.log', level=logging.INFO, format='%(asctime)s %(message)s')
logging.basicConfig(filename='application_log.log', level=logging.ERROR, format='%(asctime)s %(message)s')
logging.basicConfig(filename='application_log.log', level=logging.WARNING, format='%(asctime)s %(message)s')


class Logger:

    def file_was_found(self):
        logging.info(f"[+] File was read successfully.")
        logging.warning(f"----------------------------------------------------------------------------------")

    def no_file_error(self, e):
        logging.error(f"[-] Excel file with data was not found.. Error:{e}")
        logging.warning(f"----------------------------------------------------------------------------------")

    def access_error(self, e):
        logging.error(f"[-] Access denied. Error:{e}")
        logging.warning(f"----------------------------------------------------------------------------------")

    def server_reachability_error(self, e):
        logging.error(f"[-] Server is unreachable. Error:{e}.")
        logging.warning(f"----------------------------------------------------------------------------------")

    def device_was_added(self, device):
        logging.info(f"[+] {device} was added to Zabbix successfully.")

    def device_was_not_added(self, device):
        logging.error(f"[-] {device} was not added to Zabbix.")